"""
SEO autofix — radianceresidency.com (static HTML).

SAFE operations only:
  1. Truncate meta descriptions >155 chars at last sentence/word boundary.
  2. Log every change to SEO_CHANGES.md in the repo.

Does NOT touch: titles, H1, schema, content. Those need per-page judgment.
Idempotent: re-running is a no-op if all metas are already ≤155.
"""
import re
from pathlib import Path
from datetime import date

REPO = Path(r"C:\Users\aagos\assets\residency-website")
LOG = REPO / "SEO_CHANGES.md"
MAX = 155


def smart_trim(text: str, limit: int = MAX) -> str:
    if len(text) <= limit:
        return text
    head = text[:limit]
    # Prefer a clean sentence boundary (".") only
    idx = head.rfind(". ")
    if idx >= limit * 0.55:
        return text[:idx + 1].rstrip()
    # Otherwise word-boundary truncate and append a period
    idx = head.rfind(" ")
    trimmed = text[:idx].rstrip(" ,;:—-")
    if not trimmed.endswith("."):
        trimmed += "."
    return trimmed


META_RE = re.compile(
    r'(<meta\s+name=["\']description["\']\s+content=["\'])(.*?)(["\'][^>]*/?>)',
    re.IGNORECASE | re.DOTALL,
)


def process_file(p: Path) -> tuple[str, str] | None:
    html = p.read_text(encoding="utf-8", errors="replace")
    m = META_RE.search(html)
    if not m:
        return None
    old = m.group(2)
    if len(old) <= MAX:
        return None
    new = smart_trim(old, MAX)
    if new == old:
        return None
    html2 = html[:m.start(2)] + new + html[m.end(2):]
    p.write_text(html2, encoding="utf-8")
    return (old, new)


def main():
    changes: list[tuple[str, str, str]] = []
    for p in sorted(REPO.rglob("*.html")):
        res = process_file(p)
        if res:
            changes.append((str(p.relative_to(REPO)), res[0], res[1]))
    # Append log
    entry = [f"\n## {date.today().isoformat()} — meta description autofix (TradeForge)\n"]
    if not changes:
        entry.append("No changes — all meta descriptions already ≤155 chars.\n")
    else:
        entry.append(f"Trimmed {len(changes)} meta descriptions to ≤{MAX} chars:\n\n")
        for path, old, new in changes:
            entry.append(f"- **{path}** ({len(old)}→{len(new)} chars)\n")
            entry.append(f"  - before: `{old[:120]}...`\n")
            entry.append(f"  - after:  `{new}`\n")
    with LOG.open("a", encoding="utf-8") as f:
        if not LOG.exists() or LOG.stat().st_size == 0:
            f.write("# SEO_CHANGES — radianceresidency.com\n\nAutomated edits from TradeForge. Each entry is a dated, reversible, mechanical fix.\n")
        f.writelines(entry)
    print(f"Updated {len(changes)} files. Log: {LOG}")


if __name__ == "__main__":
    main()
