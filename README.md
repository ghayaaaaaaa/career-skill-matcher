# Career Skill Matcher

A deterministic Python CLI that compares a user-supplied skills list with a small synthetic role catalog. Each result shows matching and missing skills so the rule can be inspected.

## Run

Use Python 3.11 or newer from this directory:

```bash
python -m career_matcher --skill python --skill sql --skill fastapi
```

## How the score works

For each role, the demo counts exact normalized skill matches and divides by the number of listed role skills. Results are sorted by score and then role title. It does not infer skills from a resume, use a learned model, or send data to a service.

## Scope and provenance

All role definitions are synthetic. This AI-assisted portfolio demo is inspired by the career and skill-matching theme in a folder supplied by Ghaya. It is not a release of resumes, candidate records, original model assets, or private data. The score is transparent text overlap, not a qualification assessment, hiring recommendation, or employment decision. No open-source license is included.
