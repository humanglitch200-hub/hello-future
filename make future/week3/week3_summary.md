# 📋 Week 3 Summary — Prem's Python Journey

## ✅ What Prem Accomplished in Week 3

| Day | What Was Done |
| **Day 15** | `for` loops + `range()` — 5 exercises + star pyramid (written 100% solo, no AI). |
| **Day 16** | `while` loops, `break`, `continue`, FizzBuzz rewritten with `for`, "Guess the Number" game. |
| **Day 17** | Lists — indexing, slicing, methods + permanent List Cheat Sheet. |
| **Day 18** | Looping lists — max, min, count, search + 6-function List Toolkit (7–8 hrs, hard-won). |
| **Day 19** | Combine loops + lists — dedupe, filter, transform + Word Analyzer. |
| **Day 20** | **To-Do List CLI capstone** — 6 functions + menu loop, 13 tests passed ✅ |
| **Day 21** | This summary + Week 3 review. |

---

## 📚 What Prem Learned in Week 3

**Python Concepts:**

- **`for` loops** — looping over ranges, strings, lists. Loop variable, indentation, colon.
- **`range()`** — `range(5)` gives 0–4 (not 1–5). Three-argument form for step. Reverse with negative step.
- **`while` loops** — loop *until* something changes. Condition checked before each iteration.
- **`while True` + `break`** — the "loop forever until told to stop" pattern. Used in Guess the Number and the CLI menu.
- **`break` vs `continue`** — `break` leaves the whole loop; `continue` skips one iteration.
- **Infinite loop safety** — must update the loop variable OR use `break`. `Ctrl+C` to escape.
- **`enumerate()`** — get both index and item. `start=1` for 1-based numbering.
- **List methods** (full set learned):
  - `.append(x)` — add to end
  - `.insert(i, x)` — insert at index
  - `.remove(x)` — remove first occurrence by **value**
  - `.pop()` / `.pop(i)` — remove and return by **index**
  - `.sort()` / `.sort(reverse=True)` — in-place sort (returns `None`!)
  - `.reverse()` — in-place reverse
  - `.index(x)` — find position of value
  - `.count(x)` — how many times value appears
  - `.clear()` — empty the list
- **Indexing and slicing** — 0-based, negative indices, slice end is exclusive, `[::-1]` to reverse.
- **Lists vs strings** — lists are **mutable**, strings are **immutable**.
- **The filter pattern** — empty list → loop → `if` condition → `.append()`
- **The transform pattern** — empty list → loop → `.append(modified_item)`
- **Dedupe** — two ways: loop with `if x not in unique`, or `list(set(x))` (order not guaranteed).
- **Frequency counter** — empty dict → loop → `if key in dict: += 1 / else: = 1`
- **Nested loops** — outer loop for rows, inner loop for columns.
- **Empty-list guards** — `if not items: return` at the top of every "show / remove / search" function.
- **`try/except ValueError` for `int(input())`** — only the conversion can fail, not `input()` itself.
- **`except IndexError`** — catches "user typed 99 but there are only 3 items".
- **File order rule** — define all functions first, call them from the menu at the bottom.
- **`if __name__ == "__main__":`** — wrap the menu so imports don't auto-run.

**Tools & Workflow:**
- Git: `add`, `commit -m`, `push`, `status`, `log --oneline`
- **Never `git add .` from `~`** — always use specific paths like `git add week3/` because the repo lives in the home folder (needs migration).
- The `week3/` folder pattern on GitHub keeps things organized.
- **Time-boxing lesson:** 7–8 hour sessions = diminishing returns. Cap at 2 hours for better retention.

**Projects Completed:**
1. Star pyramid (Day 15) — **written 100% by Prem, first solo code ever**
2. FizzBuzz rewritten with `for` (Day 16)
3. "Guess the Number" game (Day 16)
4. List Cheat Sheet (Day 17 — permanent reference)
5. List Toolkit — 6 functions: `find_max`, `find_min`, `total`, `average`, `count_item`, `find_all_positions` (Day 18)
6. Word Analyzer (Day 19)
7. **To-Do List CLI** (Day 20) — capstone, 13 tests passed ✅

---

## 🔗 Prem's GitHub Repository

**URL:** `https://github.com/humanglitch200-hub/hello-future`

**Week 3 files added:** `week3/day15_*.py` → `week3/day20_todo_list.py`, `week3/week3_summary.md`, etc.

---

## ⚠️ Mistakes Made & Lessons Learned

**Specific bugs hit in Week 3 (each one taught a rule):**

1. **`task` vs `tasks`** — mixed singular/plural names in `add_task`. Rule: **one name, used everywhere.**
2. **`try/except` around `input()`** — put it around the wrong line. `input()` never fails; only `int(input())` does. Rule: **wrap the conversion, not the input.**
3. **`.split()` when asking for a number** — turned `"2"` into `["2"]`, then `int(["2"])` crashed. Rule: **split is for sentences, not numbers.**
4. **`.lower` without `()`** — same trap as Week 2's `sum(dict.values)`. Rule: **`builtin_function_or_method` in an error = missing `()`.** (Happened twice now — watch for it.)
5. **`if not found:` inside the loop** — printed "no matches" once per iteration. Rule: **"did anything match?" is only knowable *after* the loop ends.**
6. **`tasks['t']` — indexing a list with a string** — `TypeError`. Rule: **lists use numbers, dicts use keys. Don't mix.**
7. **Triple-quoted f-string with baked-in indentation** — output looked broken. Rule: **use `\n` or separate prints for clean formatting.**
8. **`int(input())` in the menu without try/except** — crashed on `"abc"`. Rule: **every `int(input())` needs a `ValueError` guard.**
9. **Double `-1` in `mark_done`** — subtracted twice, marked the wrong task. Rule: **subtract 1 once, at the point of use.**
10. **`"Done"` vs `"done"`** — capital D created a new dict key, broke `view`. Rule: **dict keys are case-sensitive. Be consistent.**
11. **`.pop()` vs `.remove()` confusion** — pop takes an index, remove takes a value. Rule: **numbered list → pop. Named search → remove.**
12. **`if task or position == search`** — two broken comparisons, always True. Rule: **`or` doesn't mean "either matches"; write two explicit conditions.**

**Learning-style progress:**
- Wrote the star pyramid **100% solo** — first time doing that.
- Caught and fixed the missing-`()` bug on my own (the Week 2 lesson carried over).
- Time-per-day dropped from 7–8 hrs (Day 18) — need to time-box to **2 hrs max** going forward.

---

## 🎯 Prem's Self-Identified Weaknesses (Carry to Week 4)

1. **Building logic from scratch** — can read logic but struggles to *initiate* without a skeleton. (Improving — star pyramid proved it's possible.)
2. **Writing code without a skeleton** — needs to practice the "close it, rewrite from scratch next day" habit.
3. **Debugging independently** — reads tracebacks but doesn't always know *where* to look first.
4. **Resisting AI assistance** — reaches for help too quickly. **The coaching rule (below) exists for this.**
5. **Time-boxing** — 4–8 hr sessions. Need to cap at 2 hrs for retention.

---

## 🤝 COACHING RULE (Locked In — Must Be Honored)

> **When Prem asks for help, do NOT give full code or complete skeletons. Instead:**
> 1. Ask what he's tried so far
> 2. Point out *where* his thinking is stuck, not *what* to type
> 3. Give hints, pseudocode, or structure — never the finished answer
> 4. If he asks for the answer directly, remind him: *"Try for 15 minutes first, then show me what you have"*
> 5. Only give full code if he has genuinely tried and is stuck on **syntax**, not **logic**
> 6. Encourage the "write it, close it, rewrite from scratch next day" habit
> 7. **Fix one function at a time** — do not dump all bugs at once. Verify each before moving on.

**Reason:** Prem identified that using AI as a crutch is slowing his real learning. He asked for this rule. Hold the line even when he pushes.

---

## 📅 Week 4 Preview — Dictionaries, Tuples, Sets, Functions

**Focus:** dicts in depth, tuples, sets, cleaning up functions

**Schedule:**
- **Day 22:** Dictionaries — keys, values, methods
- **Day 23:** Loop through dicts
- **Day 24:** Tuples
- **Day 25:** Sets
- **Day 26:** More functions — default args, `*args`
- **Day 27:** Build a Contact Book (in-memory, dicts + functions)
- **Day 28:** Review + summary + push

**Goal by end of Week 4:** Build a small in-memory tool with dicts + functions. **This is Prem's Month 1 graduation project.**

---

## 💬 Message to Future Assistant

Prem is now at end of Week 3 of a 12-week Python plan. He:

- Knows variables, types, operators, strings, `input()`, typecasting, conditionals, functions, `try/except`, Git basics
- **Completed Week 3:** `for` loops, `while` loops, `range()`, `break`, `continue`, `enumerate`, list indexing/slicing, list methods, filter pattern, transform pattern, frequency counter
- **Built and pushed a To-Do List CLI capstone** with 6 functions and a menu loop (Day 20) — 13 tests passed
- **Wrote his first fully solo code** (star pyramid, Day 15)
- **Struggles with:** initiating logic from scratch, debugging independently, resisting AI assistance
- **Is self-aware** that he leans on AI too much — **honor the coaching rule above**
- Uses a **low-power Linux Mint laptop** — runs scripts directly from terminal (`python3 file.py`)
- Uses **multiple small files per day** (one exercise = one file) — this is fine
- Gets frustrated when instructions are unclear — be patient and explicit
- Prefers free resources only
- Wants 7-day breakdowns with daily time allocations
- **Time-boxing is a weakness** — encourage 2-hr sessions max, not 7-hr grinds
- **Rule he asked me to enforce:** fix ONE function/bug at a time, verify, then move on. Don't dump all errors at once.
- **Repo issue:** Git initialized in `/home/prem` (home folder). Needs migration to `~/python/hello-future` before Week 5. Until then, never `git add .` from `~`.

**When starting Week 4:**
- Begin with **Day 22: Dictionaries — keys, values, methods**
- Provide reading links, exercises, and a mini-project
- Apply the coaching rule strictly — hints, not answers
- Remind him: he already used dicts in Week 3 (`frequency_map`, the task shape in his CLI). Week 4 is where he goes deep.

---
