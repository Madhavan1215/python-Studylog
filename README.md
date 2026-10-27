# studylog

A small command-line tool for tracking your study sessions. Built with Python and the standard library only.

## What it does

- Log a study session with a topic and the hours spent
- List all sessions, numbered
- Show total hours per topic, highest first
- Delete a session by its number

Sessions are saved in `~/.studylog.json`.

## How to run

You need [uv](https://docs.astral.sh/uv/) and Python 3.14 or newer.

```bash
git clone https://github.com/Madhavan1215/python-Studylog.git
cd python-Studylog
uv run studylog --help
```

## Examples

```bash
uv run studylog add python 1.5
uv run studylog add git 2
uv run studylog list
uv run studylog stats
uv run studylog delete 1
```

Hours must be more than 0 and at most 16.

## Next idea

Filter `list` by date, for example `studylog list --since 2026-10-01`.