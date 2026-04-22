# Claude Code Setup

Personal Claude Code config as a single source of truth across machines.

## Install / Update

```bash
curl -fsSL https://raw.githubusercontent.com/MauriceDHanisch/claude-setup/main/setup.sh | bash
```

Clones the repo to a temp dir, copies config files into `~/.claude`, and deletes the temp clone. Safe to re-run at any time — credentials, sessions, and runtime data are never touched.

## What's Included

- Global coding guidelines (`CLAUDE.md`)
- Settings & permissions (`settings.json`)
- Custom commands (`/commit`, `/check`)
- Statusline (`statusline.sh`)

## Making Changes

Edit files directly in `~/.claude` on your primary machine (it's a git repo), then:

```bash
cd ~/.claude
git add -p
git commit -m "your message"
git push
```

Pull to other machines by re-running the install command above.
