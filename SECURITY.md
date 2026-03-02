
# Security Model
___

This project operates entirely within Python's native security model, which assumes that any
code running in the interpeter is fully trusted. Python does not enforce internal sandboxing, 
privilege seperation, or access to internal state are all first-class features of the language.
This library exposes object structure using those same mechanisms and does not introduce additional
protections or constraints.

---
## What the Library Guarantees
---

- It only inspects objects explicitly provided by the caller, and all of it's children objects. This is all inclusive.
    
- It does not execute arbitrary code during introspection beyond what Python’s attribute access semantics already perform.
    
- It does not read files, environment variables, or external resources unless the user passes objects that reference them.
    
- It does not modify the objects it inspects unless explicitly configured to do so.

---
## What the Library Does Not Guarantee
---

- It does not hide, sanitize, or redact sensitive information contained within objects.
    
- It does not prevent exposure of private attributes, internal state, closures, or implementation details.
    
- It does not enforce security boundaries between components or modules.
    
- It does not detect secrets or classify sensitive fields.
    
- It does not provide sandboxing, isolation, or execution restrictions.
    
- It does not protect users from introspecting objects that contain confidential or high‑risk data.

---
## User Responsibilities
---

- Ensure that objects passed to the introspector do not contain sensitive information that should not be exposed.
    
- Implement redaction, filtering, or access‑control logic at the application level if required.
    
- Avoid using introspection output directly in logs, UIs, or external systems without appropriate review.
    
- Understand that introspection may reveal internal implementation details that were not intended for external visibility.

---
## Known Risks and Limitations
---

- Python’s attribute access may invoke user‑defined code (e.g., properties, descriptors), which can have side effects.
    
- Objects with deep or cyclic references may expose more internal state than expected.
    
- Introspection of third‑party libraries may reveal private or undocumented fields.
    
- Sensitive data stored in closures, defaults, or internal buffers may be surfaced if reachable through Python’s runtime.

---
## Supported Versions
---

BInspected is developed as a rolling, forward-moving project. Only the latest released version recieve security-related fixes.
Older versions may continure to functions, but they are not monitored or patched for security issues.

| Version | Supported          |
| ------- | ------------------ |
| 0.1.0   | :white_check_mark: |
| 0.1.0   | ;white_check_mark: |

Security support will expand once the project reaches a stable boundary. Until then, the expectation is that users upgrade 
to the most recent release to receive fixes.

---
## Reporting a Vulnerability
---

Security issues should be reported privately so they can be evaluated and addressed responsibly.
  - Where to report: Open a private security advisory or email the maintainer at 

