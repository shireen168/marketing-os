# Marketing-OS Lessons Learned

Append-only. Record insights, mistakes, and decisions as they happen.

Format: `[YYYY-MM-DD] LESSON: ... | INSIGHT: ... | APPLY TO: ...`

---

[2026-05-06] LESSON: File structure and naming discipline is foundational to repo usability | INSIGHT: Having files duplicated in both EA root and GitHub folder creates confusion about which is source-of-truth. Single structure location (setup/) = cleaner mental model for cloners. | APPLY TO: All future portfolio projects — establish clear separation between EA local-only files (tasks, decisions, internal docs) and public GitHub files (code, guides, examples). No duplicates.

[2026-05-06] LESSON: Markdown formatting with content breaks after colons/dashes dramatically improves scannability | INSIGHT: "**Goal:** text on same line" requires eye to parse two concepts in parallel. Breaking to "**Goal:**\ntext" separates metadata from content, reduces cognitive load. Small change, major UX impact. | APPLY TO: All future project READMEs — always break content after bold labels/colons for professional readability.

[2026-05-06] LESSON: Submodule detection and conversion is critical in multi-folder monorepos | INSIGHT: A cloned folder can retain its own .git directory, which Git interprets as a submodule. This breaks relative path navigation and confuses cloners. Always check for and remove .git from nested folders. | APPLY TO: Before pushing any folder to GitHub that originated elsewhere, run: `rm -rf folder/.git && git rm --cached folder` to convert to regular files.
