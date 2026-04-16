# Git Ignore

Certain files should never be committed to version control.

Example `.gitignore` entries:

node_modules  
.env  
.env.local  
.next  
dist  
coverage

---

## Environment Files

Environment files often contain secrets and must always be ignored.

---

## Build Artifacts

Directories like `.next` are generated during build and should not be committed.
