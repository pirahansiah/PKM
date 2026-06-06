# General Coding Task

/no_think
Update all .md files in given folder.
Add front matter headers.

Rules:

* layout is always: default
* generate title from file content or filename
* generate tags from content, folder, and context
* keep metadata consistent and relevant
* no manual placeholders
* no explanations
* no extra text

Output:

* return all updated files in one code block only
* format:
    — file: path/filename.md —

⸻

layout: default
title: …
tags: …

(content)
— file: next.md —
…

* stop after closing fence

i need like PKM methods to need to have link,refrenceline,doubledlink connetion, forward and backward links, ... releven tags,... find other relevent suported headers that can work in github page jukill build of .md files without build or add packages










---

/no_think
Return the complete updated files.
Do not explain changes.
Do not add comments.
Output one code block only.
Stop immediately after the closing fence.

Requirements:
- Provide clean, production-ready, and minimal code.
- Adhere to the language-specific best practices and naming conventions.
- Keep the implementation self-contained unless external dependencies are specified.
- Ensure the code is responsive (if UI) and handles edge cases appropriately.
- No comments inside the files.

Output Format:
- Return the complete contents of all requested files in one response.
- Present only a single fenced code block containing all files concatenated, with a clear separator line between files exactly like:
  --- file: filename.ext ---
  (contents)
  --- file: filename2.ext ---
  (contents)
- Do not add any extra text before or after the code fence.
- Do not explain anything, do not add comments, and stop immediately after the closing fence.

---
Current Code/Context:
<code here or paste context>

---
Rules:
- Return the complete updated file.
- Do not explain changes.
- Do not add comments.
- Output one code block only.
- Stop immediately after the closing fence.
