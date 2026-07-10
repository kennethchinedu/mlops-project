# Lesson 0.1 — Your Python installation & this project's home

**Phase 0 · assigned 2026-07-10**

## Concept

Before writing any Python, you must know *which* Python you're running. A Mac usually has several: one that came with the OS, ones installed by tools, maybe one from python.org or Homebrew. When your terminal runs `python3`, it searches a list of folders called the **PATH**, in order, and uses the first match. Most "it works on my machine" problems in DevOps trace back to exactly this: two environments resolving the same command to different programs. So lesson one of MLOps/DevOps is: never assume — verify what will actually run.

The second habit starting today: everything lives in **git**. Git is a time machine for your project — every "commit" is a snapshot you can return to, compare against, and (later) trigger automation from. Your future CI/CD pipelines (Phase 5) will react to commits, so your git habits start before your Python habits.

## Reading

1. https://docs.python.org/3/using/mac.html — how Python works on macOS; focus on the difference between the system Python and one you install.
2. https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F — just this chapter; focus on the "three states" (modified, staged, committed).

## Exercise — no Python code yet, only terminal

Work inside `project1/`. Do each step yourself and **write down what you observe** in a file called `notes.md` (create it yourself — this file is yours, not mine):

1. Find out which Python runs and from where: use `which python3` and `python3 --version`. Record both outputs in your notes. Is it 3.12 or newer? If not, install a current one from python.org or Homebrew and verify the version changes.
2. Ask Python itself where it lives: run `python3` to open the interactive prompt (the REPL), and in it, import the `sys` module and print `sys.executable`. (How to import and print: that's in the first pages of the Python tutorial — find it yourself.) Exit the REPL. Record the path.
3. Initialize git in this folder with `git init`. Run `git status` and read every line of the output — write in your notes what "untracked files" means in your own words.
4. Tell git who you are (`git config` — look up the two settings for name and email in the git book chapter).
5. Stage and commit `notes.md` with a message that describes *why* the commit exists, not just "add file".
6. Run `git log` and record what a commit is identified by.

## Done when

- [ ] `notes.md` exists, with your observations from steps 1–6 in your own words
- [ ] `python3 --version` shows 3.12+
- [ ] `git log` shows at least one commit with a meaningful message
- [ ] You can answer the check questions below without looking

## Check yourself

1. What does the PATH have to do with which Python runs? /usr/local/bin/python3
2. What's the difference between a *modified* file, a *staged* file, and a *committed* file? modified files are files that was changed
 stageed files are files that are being tracked, committed are files that have been saved and ready to push

3. Why did we NOT commit before configuring `git config`?
To keep track of the files we want to commit

When done, tell me "review" and I'll check your work.
