"""Compare a skill list with fictional role requirements."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Role:
    title: str
    required_skills: frozenset[str]


ROLE_CATALOG = (
    Role("Python API Developer", frozenset({"python", "rest api", "sql", "git"})),
    Role("Flutter App Developer", frozenset({"flutter", "dart", "rest api", "git"})),
    Role("Data Automation Developer", frozenset({"python", "sql", "automation", "csv"})),
)


def match_roles(skills: set[str]) -> list[dict[str, object]]:
    normalized = {skill.strip().casefold() for skill in skills if skill.strip()}
    if not normalized:
        raise ValueError("Provide at least one non-empty skill.")
    results = []
    for role in ROLE_CATALOG:
        matches = role.required_skills & normalized
        missing = role.required_skills - normalized
        results.append(
            {
                "title": role.title,
                "score": len(matches) / len(role.required_skills),
                "matched": sorted(matches),
                "missing": sorted(missing),
            }
        )
    return sorted(results, key=lambda row: (-row["score"], row["title"].casefold()))


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare skills to fictional role requirements.")
    parser.add_argument("--skill", action="append", default=[], help="Repeat for each skill")
    args = parser.parse_args()
    try:
        rows = match_roles(set(args.skill))
    except ValueError as exc:
        parser.error(str(exc))
    for row in rows:
        print(f"{row['title']}: {row['score']:.0%}")
        print("  matched: " + (", ".join(row["matched"]) or "none"))
        print("  gaps:    " + (", ".join(row["missing"]) or "none"))
    print("Demo only: scores are not hiring or qualification decisions.")


if __name__ == "__main__":
    main()
