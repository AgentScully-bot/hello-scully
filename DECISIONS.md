# Decisions: hello-scully

## 2026-03-01 — Project structure: src layout
**Context:** Choosing between flat layout and src layout
**Decision:** Use src layout (`src/hello_scully/`)
**Alternatives considered:** Flat layout (module at root)
**Rationale:** src layout is modern Python best practice, prevents accidental imports from project root
