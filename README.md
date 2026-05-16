# Claude Code Setup — discontinued

> **This repository is no longer maintained.** All configuration has moved to
> [**MauriceDHanisch/agent-dotfiles**](https://github.com/MauriceDHanisch/agent-dotfiles),
> which manages Claude, plus shared skills, from a single source of truth.

## Why the move

`claude-setup` was Claude-only and copied files into `~/.claude`. The new
[agent-dotfiles](https://github.com/MauriceDHanisch/agent-dotfiles) repo:

- Manages multiple agents from one repo, with shared skills as the single
  source of truth — edit a skill once, every agent that consumes it sees the
  change.
- Uses symlinks instead of copies, so edits in `~/.claude` propagate back to
  the repo automatically.
- Pure-bash installer with no dependencies beyond `git` (no `stow`, no
  package-manager prompts).
- Backs up any conflicting local files to `~/.agent-dotfiles-backup/` before
  linking, and sweeps orphan symlinks on every install.

## Migrating

```bash
curl -fsSL https://raw.githubusercontent.com/MauriceDHanisch/agent-dotfiles/main/setup.sh | bash
```

That's it — re-run the same command on every machine to stay in sync.
