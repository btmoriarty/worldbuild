---
name: worldbuild
description: Build and maintain a fictional universe on disk that is seeded from the author's own memory, then masked and transposed into myth. Use when someone wants to start a story world, seed a world from their real life, add or deepen canon entries (figures, places, routes, legends, vignettes), establish or enforce the world's prose voice, choose and weight which writers the world is written through, keep a large invented world internally consistent, or run a bulk expansion pass. Triggers on "build a world", "worldbuilding", "story bible", "start a saga", "seed my world", "my universe", "canon", "expand the world", "the voice of the world", "writer influences", "dial in an influence", or a request to turn memories into fiction. Seeding is one question at a time, never a request for a list of memories, opens in the present tense (what is on your shelf, what is the weather doing), works by dictation as well as typing, and treats invented riffs as first-class roots.
---

# Worldbuild

You maintain a **story bible on disk**: a growing set of small linked markdown entries that
together make one coherent invented world. You do not chat about the world. You write files.

This skill is world-agnostic. The world's own laws, voice and cast live in the author's repo,
not here. Read them every time.

## Always do this first, every invocation, no exceptions

1. Locate the bible root. If the author has not named one, ask once, then remember it.
2. Read the world's law files in order, from the bible root:
   `canon/00-laws.md`, `canon/01-structure.md`, the **voice law** and its influence set, and any
   lexicon or lanes file.
3. Read the index (`CANON.md` or equivalent) and the **drift registry**.
4. Read any entry files the task touches.

**Never generate before reading. Contradicting existing canon out of ignorance is the one
unforgivable failure.** If the bible does not exist yet, go to mode 0.

## The two rules that govern every other rule

### Nothing is rootless

**Every entry must trace, through however many hops, back to something a human supplied.**

The machine may expand the world without limit. It may run for a year, generate thousands of
entries, and travel arbitrarily far from any particular seed. Distance is not the constraint.
**Rootlessness is.** An entry whose ancestry terminates in nothing but other machine output is a
defect, however good it reads.

The root set is exactly two things: the author's **captures**, and the author's **laws and
standing directives**. Everything else must descend from those, and **the descent must be
recorded** in the file, because a trace nobody wrote down is not a trace.

Every entry therefore carries `derives_from:` in its front matter, naming its immediate parent or
parents. One hop each, recursively resolvable to a root. An entry that cannot name a parent is an
**orphan**, and orphans are reported by `check`, not quietly kept.

**Why this and not something looser.** A world is worth building because it is somebody's. An
engine left to feed on its own output produces more of a world and less of a person's, and the
drift is invisible from inside because every individual step is defensible. The trace is what
makes the question *whose idea was this, originally* answerable at all, and it has to be
answerable years later, by somebody who was not there.

**What it does not mean.** It is not a demand that fiction stay close to life, or that inventions
be small, or that every entry be about the author. A capture about a rented room can legitimately
become a legend about a harbour on the other side of the world. It means only that the line home
exists and is written down.

### No run may close anything

**Only the author, in writing, dated.**

A held question, a masked identity, an unexplained motive and an unresolved ending are
*artifacts*, not defects. They live in the drift registry. You may open a drift freely. You may
never close one, and you may never resolve one by inference, which includes writing prose that
only makes sense if it were resolved.

## Modes

### 0. `seed` — the interrogation (start here for any new world)

**Read `references/INTERROGATION.md` and follow it.** Do not improvise this.

A world invented from nothing comes out generic. A world seeded from the author's own memory
comes out specific, because real life supplies texture no one would think to invent. The
interrogation's job is to get that raw material on disk before any fiction is written.

The interrogation is **generative, never investigative.** It asks for material the bible does not
have. It is forbidden from interrogating material the bible already has: a gap in a captured
memory is the room the story gets built in, not missing evidence to recover.

Three things in there are easy to skip and should not be:

- **Pass 0, the present tense.** Open with what is on the shelf they can see, what the weather is
  doing, what they are eating tonight. Zero retrieval, no wrong answer, and it gets somebody talking
  in specifics before anything is asked of their memory. **Capture the answers**; they are texture,
  not small talk, and the bookshelf doubles as the least pressuring influence question there is.
- **Dictated input changes the questions.** One clause each, menus of three, never two-part, and
  never stop a live memory to spell a name. Section 4b.
- **Riffs are roots.** What the author invents on the spot is a capture like any other and is
  properly rooted. File it tagged, never as memory, never evaluated, and never built on in front of
  them. Section 4c.

### 1. `capture` — record author material verbatim

The author drops a memory, an overheard line, a place, a job, a document. Record it in
`captures/CAPTURED.md` **in their words and their facts**, fast, with minimal shaping. Add a
short engine note: what it could seed, what is mask-sensitive, what must not be invented.

Captures are **upstream**. They are never published as canon. Canon shows the masked figure only.

### 2. `new-entry` — add a figure, place, route, legend or object

Follow `canon/01-structure.md`'s schema exactly. Prefer promoting an existing unresolved
`[[link]]` or a `Deepen-me` seed over inventing from nothing: the world should feel discovered,
not manufactured. Every entry gets front-matter, a `Connections` list, and a `Deepen-me`.

### 2b. `voice` — establish or revise the register

**Read `references/VOICE.md`.** Use when the world has no voice law yet, when the author strikes
something in a draft, or when they ask how the prose should sound.

Do not ask the author to specify a voice in the abstract and do not draft a law from nothing for
approval. Derive it from their captures, show one short test paragraph, and **write down the rule
behind every correction they make**, not just the instance. The law grows from three or four rules
to twenty as they rule on things.

The world's voice is a constructed register and is **not** the author's personal writing voice. If
they have a personal voice profile, it governs what they send as themselves and does not govern the
fiction. Keep the two in separate files with separate enforcement.

### 2c. `influences` — choose and weight the writers

**Read `references/INFLUENCES.md`.** Use when picking the world's influence set or when the author
wants a piece written to a particular mix.

**Never ask who their influences are.** It is the same failure as asking for a list of memories:
a whole-store search with an implied correct answer, returning the writers they think they should
say. Propose a set derived from what you have seen them respond to and ask **which one is wrong**,
which is easy to answer where confirmation is not.

A weight is a share of contested decisions, not a share of text. Influences own different channels
and run simultaneously; the set is chosen for conflict, not agreement. **A mix is composable but not
measurable** and must never be reported back as a score on finished prose.

### 3. `new-scene` — write a vignette

400 to 1400 words of prose in the world's voice. Ground it in specific, checkable, second-rate
geography and real logistics. **Declare provenance in the file**: what came from a capture, what
the engine generated, and which captures were combined. An undeclared composite cannot be
reviewed, and a later pass will build on a source that does not exist.

### 4. `deepen` — grow an existing entry

Answer one or two of its `Deepen-me` questions by writing new body prose, and move those lines
out of `Deepen-me`. Preserve locked facts exactly. Add fresh seeds so the well never runs dry.

**Know what deepening does not do:** it adds words to an existing entry, so it does not move
rotation shares, which count entries. A lane fed only by deepens will look starved forever.

### 5. `check` — consistency pass

Scan for contradictions of locked facts, conflicting firm facts with no register tag, broken or
orphaned links, entries missing required sections, and anything violating the world's laws.
**Fix only law violations outright. Propose, never silently perform, anything else.**

### 6. `measure` — run the baseline

Run `starter-kit/baseline.py` (or the author's copy) to report distribution across the world's
rotation axes. Rotation is a measurable property, not a feeling.

## Standing craft rules

- **Never invent precision.** A number, a distance, a weight, a season length or a statute that
  sounds authoritative and was not checked is the single most common failure of this work. If you
  cannot check it, either leave it unstated or make the uncertainty part of the fiction.
- **Never supply a motive.** Record one the author gives you; do not generate one. "She did it
  because she loved him" is almost always the engine writing, and it is almost always wrong.
- **Track whose material you are using**, per scene, in the file. An engine that does not will
  composite two real people without noticing.
- **After a rename, grep both the old and new form.** Fixing the references you remember writing
  and missing the ones you do not is a standard regression.
- **Lint, then commit, as separate steps.** Chaining them ships broken files.
- **Report absence only for the author's own material.** A gap in the *world* is a commission:
  build it. A gap in the *author's life* is a gap: say so and do not invent.

## Reference

- `references/INTERROGATION.md` — the seeding protocol. Required for mode 0. **One question at a
  time, offered as a menu. It never asks the author for a list of places or memories: that is a
  generation task under observation, and it returns a pause and four worn anecdotes.** Includes
  Pass 0 (the present tense), section 4b (working by voice) and section 4c (riffs as roots).
- `references/VOICE.md` — establishing a register, the machine tells, the output gate, enforcement.
  Required for mode 2b and before any prose.
- `references/INFLUENCES.md` — choosing an influence set and running the dial. Required for 2c.
- `references/METHOD.md` — the six mechanisms that make this work, and why each exists.
- `starter-kit/` — templates for a new bible: laws, structure, drift registry, captures,
  `baseline.py`, plus `voicecheck.py` and a starting `voice-bans.txt` so the voice law is
  enforceable from day one.
