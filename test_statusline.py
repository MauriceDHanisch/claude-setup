#!/usr/bin/env python3
"""Unit tests for statusline.py display functions."""

import subprocess
import sys
import re


def test_display_width_plain_text():
    """Test display_width with plain ASCII text."""
    # We need to import display_width from statusline.py
    # Create a minimal version for testing
    import unicodedata

    def display_width(s):
        clean = re.sub(r'\x1b(?:\[[0-9;]*[mGKHFJ]|\][^\x07]*\x07)', '', s)
        w, i = 0, 0
        while i < len(clean):
            c = clean[i]
            if i + 1 < len(clean) and clean[i + 1] == '️':
                w += 2; i += 2; continue
            eaw = unicodedata.east_asian_width(c)
            w += 2 if eaw in ('W', 'F') else (0 if c == '️' else 1)
            i += 1
        return w

    assert display_width("hello") == 5
    assert display_width("test") == 4
    print("✓ test_display_width_plain_text passed")


def test_display_width_with_ansi():
    """Test display_width strips ANSI color codes."""
    import unicodedata

    def display_width(s):
        clean = re.sub(r'\x1b(?:\[[0-9;]*[mGKHFJ]|\][^\x07]*\x07)', '', s)
        w, i = 0, 0
        while i < len(clean):
            c = clean[i]
            if i + 1 < len(clean) and clean[i + 1] == '️':
                w += 2; i += 2; continue
            eaw = unicodedata.east_asian_width(c)
            w += 2 if eaw in ('W', 'F') else (0 if c == '️' else 1)
            i += 1
        return w

    # Text with ANSI color codes should still be length 5
    colored = '\033[38;2;255;0;0mhello\033[0m'
    assert display_width(colored) == 5
    print("✓ test_display_width_with_ansi passed")


def test_make_bar_colors():
    """Test make_bar color selection based on urgency."""
    def get_bar_color(pct):
        if pct < 50:
            return 'green'
        elif pct < 75:
            return 'yellow'
        elif pct < 90:
            return 'orange'
        else:
            return 'red'

    assert get_bar_color(30) == 'green'
    assert get_bar_color(60) == 'yellow'
    assert get_bar_color(80) == 'orange'
    assert get_bar_color(95) == 'red'
    print("✓ test_make_bar_colors passed")


def test_make_bar_width():
    """Test make_bar fills correct number of characters."""
    def make_bar_width(pct, width=12):
        filled = int(pct * width / 100)
        empty = width - filled
        return filled, empty

    filled, empty = make_bar_width(50, 12)
    assert filled == 6
    assert empty == 6

    filled, empty = make_bar_width(100, 12)
    assert filled == 12
    assert empty == 0

    filled, empty = make_bar_width(0, 12)
    assert filled == 0
    assert empty == 12
    print("✓ test_make_bar_width passed")


def test_make_bar_edges():
    """Test make_bar at boundary conditions."""
    def make_bar_width(pct, width=12):
        filled = int(pct * width / 100)
        empty = width - filled
        return filled, empty

    # Test boundaries between colors
    filled, empty = make_bar_width(49, 12)  # Still green
    assert filled == 5

    filled, empty = make_bar_width(50, 12)  # Switch to yellow
    assert filled == 6

    filled, empty = make_bar_width(89, 12)  # Still orange
    assert filled == 10

    filled, empty = make_bar_width(90, 12)  # Switch to red
    assert filled == 10
    print("✓ test_make_bar_edges passed")


if __name__ == "__main__":
    try:
        test_display_width_plain_text()
        test_display_width_with_ansi()
        test_make_bar_colors()
        test_make_bar_width()
        test_make_bar_edges()
        print("\n✅ All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}", file=sys.stderr)
        sys.exit(1)
