#!/bin/bash
set -e

echo "Claude Code setup starting..."
echo ""

echo "→ Cloning claude-setup to temp dir..."
TMPDIR=$(mktemp -d)
git clone https://github.com/MauriceDHanisch/claude-setup.git "$TMPDIR" --quiet
echo "✓ Repo cloned"

echo "→ Copying config files into ~/.claude..."
mkdir -p ~/.claude/commands
cp "$TMPDIR/CLAUDE.md" ~/.claude/CLAUDE.md
cp "$TMPDIR/settings.json" ~/.claude/settings.json
cp "$TMPDIR/setup.sh" ~/.claude/setup.sh
cp "$TMPDIR/statusline.sh" ~/.claude/statusline.sh
cp "$TMPDIR/README.md" ~/.claude/README.md
cp "$TMPDIR/.gitignore" ~/.claude/.gitignore
cp "$TMPDIR/commands/commit.md" ~/.claude/commands/commit.md
cp "$TMPDIR/commands/check.md" ~/.claude/commands/check.md
echo "✓ Files updated"

echo "→ Deleting temp clone..."
rm -rf "$TMPDIR"
echo "✓ Temp clone deleted"

echo "→ Making statusline executable..."
chmod +x ~/.claude/statusline.sh
echo "✓ statusline.sh ready"

echo ""
echo "✅ Claude Code setup complete!"
echo ""
echo "Installed:"
echo "  ✓ Global guidelines       (CLAUDE.md)"
echo "  ✓ Settings & permissions  (settings.json)"
echo "  ✓ Custom commands         (commands/commit, commands/check)"
echo "  ✓ Statusline              (statusline.sh)"
echo ""
echo "To update from remote:"
echo "  curl -fsSL https://raw.githubusercontent.com/MauriceDHanisch/claude-setup/main/setup.sh | bash"
