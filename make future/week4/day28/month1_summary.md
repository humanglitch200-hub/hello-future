# 📋 Month 1 Summary — Prem's Python Journey

**Copy this entire message into your next chat to start Month 2 (Week 5).**

---

## ✅ What Prem Accomplished in Month 1

| Week | What Was Done |
|:---|:---|
| **Week 1** | Variables, types, operators, string methods, `input()`/`print()`, typecasting. First small scripts. |
| **Week 2** | `if/elif/else`, `and/or/not`, nested conditionals. Budget planner + "What Should I Do" tool. |
| **Week 3** | `for`/`while` loops, `range()`, `break`, `continue`, list methods, filter pattern, transform pattern, frequency counter. **To-Do List CLI capstone** (6 functions, 13 tests passed). First fully solo code: star pyramid. |
| **Week 4** | Dicts deep (keys, values, methods, looping, nested), tuples (immutability, unpacking, `zip(*...)`), sets (union/intersection/difference), functions with default args, `*args`, `**kwargs`. **Contact Book CLI capstone** — full CRUD. |

**Total: 28 days. 2 capstone projects. ~50 exercise files. One git corruption survived (Day 24).**

---

## 📚 Concepts Mastered

**Core Python:**
- Variables, types, operators, typecasting (`int()`, `str()`, `float()`)
- `input()` always returns a string — must typecast
- f-strings, string methods (`.split()`, `.strip()`, `.lower()`, `.upper()`, `.replace()`, `.find()`)
- Conditionals: `if / elif / else`, `and / or / not`
- Loops: `for`, `while`, `range()`, `enumerate()`, `break`, `continue`
- **Function rule learned:** functions return, menus print (Day 27 — big upgrade)

**Data structures:**
- **Lists** — mutable, indexed, `.append()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`, slicing, `[::-1]`
- **Tuples** — immutable, unpacking, `zip(*entries)`, can be dict keys
- **Sets** — unique, unordered, `|`, `&`, `-`, `^`, `.add()`, `.discard()`
- **Dicts** — key-value, `.keys()`, `.values()`, `.items()`, `.get()`, `.setdefault()`, `.update()`, `.pop()`, nested dicts, `.items()` loop unpacking
- **Frequency counter pattern** — empty dict → loop → `if key in dict: += 1 else: = 1`

**Functions:**
- `def`, parameters, `return`
- Default arguments — **must come last**
- `*args` (tuple inside) — any count of positional
- `**kwargs` (dict inside) — any named args
- Mutable default gotcha — `def f(x, bag=[])` is a trap; use `None`
- Unpacking on call side: `f(*mylist)`, `f(**mydict)`

**Errors & safety:**
- `try/except ValueError` — always around `int(input())`, never around `input()`
- `try/except IndexError`
- Empty-input guards: `if not items: return None` at top of every read/remove function
- `continue` after failed `try/except` — otherwise the loop falls through with an unassigned variable

**Git:**
- `git add`, `git commit -m`, `git push`, `git status`, `git log --oneline`
- **Never `git add .` from `~`** — always specific paths
- **Always diff before `rm -rf`** (learned after near-loss of Week 1 on Day 24)
- **Always `git status` before commit** — verify files are actually staged, not just claimed in the message
- Recovered from a corrupted `.git` folder by re-cloning from GitHub

---

## 🔗 Projects Completed

| Day | File | What It Does |
|:---|:---|:---|
| 20 | `day20_todo_list.py` |
 **Week 3 capstone.** Add, view, mark done, remove tasks. 6 functions + menu, 13 tests passed. |
| 22 | `day22_grades.py` |
 Student grades tracker — add students, add grades, compute averages, show all. |
| 23 | `day23_word_count.py` | 
Takes a sentence, counts word frequency, prints unique/common/count. |
| 24 | `day24_scores.py` |
 High score tracker using tuples — add, top scorer, sorted list, average. |
| 25 | `day25_common_friends.py` | 
Common interest finder with sets — intersection, symmetric diff, union. |
| 26 | `day26_flexible_stats.py` |
 Flexible stats with `*args`/`**kwargs` — sum, average, max, min, toggleable. |
| 27 | `day27_contact_book_CLI.py` |
 **Month 1 capstone.** Contact Book with dict-of-dicts. Add/find/delete/list/search. Silent functions, menu prints. |

---

## ⚠️ Mistakes Made & Lessons Learned

**Hard-won rules from Month 1 — each one earned with a real bug:**

1. **`task` vs `tasks`** — one name, used everywhere. Never mix singular/plural.
2. **`try/except` around the wrong line** — wrap the `int(input())`, never the `input()`.
3. **`.split()` on a number** — split is for sentences, not numbers.
4. **`.lower` without `()`** — `builtin_function_or_method` in an error = missing `()`.
5. **`if not found:` inside the loop** — "did anything match?" is only known **after** the loop.
6. **List vs dict** — lists use numbers, dicts use keys. Don't mix.
7. **`int(input())` without `try/except`** — crashes on `"abc"`. Every one needs a guard.
8. **Double `-1` in `mark_done`** — subtract once, at the point of use.
9. **`"Done"` vs `"done"`** — dict keys are case-sensitive. Be consistent.
10. **`.pop()` vs `.remove()`** — pop takes an index, remove takes a value.
11. **`if task or position == search`** — `or` doesn't mean "either matches"; write two explicit conditions.
12. **`grade` vs `grades`** — same name trap again in `add_grade`. Cost time.
13. **`sum(grades)` vs `sum(grades[name])`** — sum over a dict sums the *keys*. Use the list.
14. **`find_contact` printing inside itself** — functions return, menus print. Learned Day 27. **Big one.**
15. **Never assume a git commit contains files** — `git log` message lies. `git status` before commit, always.
16. **Never `rm -rf` without `diff -rq` first** — Day 24 nearly deleted all of Week 1.
17. **A `git commit` message doesn't guarantee success** — check `git status` and `git log` after.

**Learning-style progress:**
- Wrote the star pyramid **100% solo** (Day 15) — first fully independent code.
- Caught the missing-`()` bug on his own (Day 18) — Week 2 lesson carried over.
- Survived a corrupted `.git` and re-cloned cleanly (Day 24) — real-world recovery skill.
- Understood the print-vs-return distinction with a full explanation, on request (Day 27) — asked the right question at the right time.

---

## 🎯 Self-Identified Weaknesses (Carry to Month 2)
- Am week on math type logic.
- can stuck over small stuff
- a bit hard to play with variables
- A bit hard to use functions without print.

1. **Building logic from scratch** — can read logic and understand it, but struggles to *initiate* without a skeleton. (Improving — Contact Book plan + build proved the loop works when done properly.)
2. **AI as crutch** — reaches for help too quickly. This is why the coaching rule exists.
3. **[Your own honest weakness — write it here.]**
4. **[Another one.]**
5. **Time-boxing** — hard 2-hour caps work better than 6-hour grinds (learned Day 18).

---

## 🤝 COACHING RULE (Locked In — Must Be Honored)

> **When Prem asks for help, do NOT give full code or complete skeletons. Instead:**
> 1. Ask what he's tried so far.
> 2. Point out *where* his thinking is stuck, not *what* to type.
> 3. Give hints, pseudocode, or structure — never the finished answer.
> 4. If he asks for the answer directly, remind him: *"Try 15 minutes first, then show me what you have."*
> 5. Only give full code if he has genuinely tried and is stuck on **syntax**, not **logic**.
> 6. Encourage the "write it, close it, rewrite from scratch next day" habit.
> 7. **Fix one function/bug at a time** — verify each before moving on.

**Reason:** Prem identified that using AI as a crutch is slowing his real learning. He asked for this rule. **Hold the line even when he pushes.**

---

## 📅 Month 2 Preview — Weeks 5–8

- **Week 5:** Text files — `open()`, `with`, `read()`, `write()`, `encoding='utf-8'`. Save and reload data so it survives restarting the script.
- **Week 6:** CSV module. `newline=''` + `encoding='utf-8'` on Windows. Save list of dicts → CSV → load back.
- **Week 7:** JSON + basic classes (`__init__`, methods, `self`). Refactor a tool into a class that loads/modifies/saves JSON.
- **Week 8:** Proper `try/except` for `KeyError`, `FileNotFoundError`. Clean code. One finished project with class + save/load + no crash on bad input. Push to GitHub.

**End of Month 2 goal:** a persistent Contact Book (or similar) that saves to disk and loads on startup.

---

## 💬 Message to Future Assistant

Prem is at **end of Month 1** of a 12-week Python plan. He:

- **Knows:** variables, types, operators, strings, `input()`, typecasting, conditionals, functions (basics + defaults + `*args`/`**kwargs`), `try/except`, `for`/`while` loops, `range()`, `break`/`continue`, `enumerate()`, list methods + indexing/slicing, filter/transform patterns, frequency counter, dicts (deep), tuples (unpacking, `zip(*...)`), sets (`|& -^`), Git basics.
- **Built:** To-Do List CLI (Week 3 capstone, 13 tests), Contact Book CLI (Month 1 capstone, CRUD, silent functions), plus 5 smaller projects.
- **Learned the print-vs-return distinction** on Day 27 — a key jump in code quality. **Enforce it from Day 29 onward** — logic functions return, menus print.
- **Survived a git corruption** on Day 24 by re-cloning from GitHub and rescuing 24 files that were never pushed. **Real-world recovery.**
- **Struggles with:** initiating logic from scratch, debugging independently, resisting AI assistance, time-boxing.
- **Is self-aware** that he leans on AI too much — **honor the coaching rule above.**
- Uses a **low-power Linux Mint laptop** — runs scripts with `python3 file.py`.
- Uses **multiple small files per day** (one exercise = one file) — this is fine.
- **Gets frustrated when instructions are unclear** — be patient, be explicit.
- Prefers **free resources only.**
- Wants **7-day breakdowns** with daily time allocations.
- **Time-boxing is a weakness** — encourage 2-hr sessions max, not 6-hr grinds.
- **Rule he asked me to enforce:** fix ONE function/bug at a time, verify, then move on. Don't dump all errors at once.
- **Every day must include:** 🔁 Review Block (5 min, no looking), 📖 Reading with **external links** (never skip), **🔒 MUST REMEMBER** lines, explanations of **why** not just **what**, ✍️ exercises + 🛠️ mini-project, 🚀 git commands with commit message, 2-hour time-box.

**Repo:** `~/python/hello-future` — **never `~` again.**

**When starting Month 2 (Week 5):**
- Begin with **Day 29: Text files — `open()`, `with`, `read()`, `write()`, `encoding='utf-8'`**
- Provide reading links, exercises, a mini-project
- Apply the coaching rule strictly — hints, not answers
- Remind him: **his Contact Book is the perfect candidate** — Week 5's job is to save it to disk and reload on startup. The first time data survives closing the program.

---

**You finished Month 1, Prem. Four weeks. Two capstones. One git corruption survived. That's real. Rest up. 💪**