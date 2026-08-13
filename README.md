# worldbuild

Build a fictional universe on disk that is **seeded from your own memory**, then masked and
transposed into myth.

A world invented from nothing comes out generic, because invention defaults to the average of
everything you have read. Real life has no average. This skill starts by sending you back through
your own memory, records what comes out, and builds the fiction on top of it.

## What it does

- **Interrogates.** A memory-retrieval protocol that gets at material you cannot produce on
  demand: places before events, the periphery instead of the protagonist, procedure over summary,
  and a pass on the things you still do not know.
- **Keeps the world honest.** Two governing rules. *Nothing is rootless*: every entry traces, in
  however many hops, back to something a human supplied. *No run may close anything*: questions the
  author holds open stay open, and only the author can settle one, in writing, dated.
- **Measures.** A dependency-free script reports distribution across the world's axes, plus
  orphaned entries and dangling links.

## Install

**As a plugin, from a marketplace** (once you have published one):

```bash
claude plugin marketplace add <your-github-user>/<your-repo>
```

Then `/plugin install worldbuild` inside Claude Code.

**By hand**, which is the whole of it: copy the `worldbuild/` directory into `~/.claude/skills/`.
It loads on the next session.

**To try it without installing:**

```bash
claude --plugin-dir ./worldbuild
```

That flag also accepts a `.zip` of the directory.

## Use

Say *seed my world* or *let's build a world* and it will start the interrogation. Point it at a
directory to keep the bible in; it will create the structure from `starter-kit/`.

If you already have a bible, name the root and it will read the laws before writing anything.

## What is in here

| Path | What it is |
|---|---|
| `SKILL.md` | The skill. Modes, governing rules, craft rules. |
| `references/INTERROGATION.md` | The seeding protocol. Read before running mode 0. |
| `references/METHOD.md` | The six mechanisms, and why each one exists. |
| `starter-kit/` | Templates for a new bible, plus `baseline.py`. |

## A note on the material

The interrogation asks for real memory, and it works better the more specific you are. Everything
you give it stays upstream in a captures file and is never published as canon: people are masked
when an entry is written, and redactions are permanent. That separation is not decoration. It is
what makes candour safe, and candour is what makes the fiction specific.

## Licence

MIT.
