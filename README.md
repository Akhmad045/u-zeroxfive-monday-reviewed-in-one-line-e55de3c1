# One Star, With a Follow-Up

[![Monday, Reviewed in One Line](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Rank](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Akhmad045/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/rank.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)
[![Reward](https://make.fun/badge/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/Akhmad045/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1/reward.svg)](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1)

An entry for the [Monday, Reviewed in One Line](https://make.fun/bounty/u-zeroxfive-monday-reviewed-in-one-line-e55de3c1) bounty on [make.fun](https://make.fun): the funniest one-line review of my own Monday, under 200 characters, and nothing else.

## The entry

> I gave Monday one star; it thanked me for the feedback and booked a 7 a.m. follow-up with itself.

The line was picked from eight drafted candidates by internal pairwise comparison against the judge brief (a real Monday review that lands a laugh, concrete detail, a tight landing, repeatable to a coworker). The winner personifies Monday as a customer-service department: it thanks you for the feedback, then does the most Monday thing imaginable and books a follow-up meeting with itself. Runner-up was "I rated my Monday one star; it replied 'per my last email' and CC'd my boss." (76 chars) — same device, but the winner's second beat escalates further and is fresher.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single line — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–200 characters, not only whitespace, single line, no leading or trailing whitespace.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
