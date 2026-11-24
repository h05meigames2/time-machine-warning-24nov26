[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/h05meigames2/time-machine-warning-24nov26/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/h05meigames2/time-machine-warning-24nov26/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

# Funniest Time Machine Warning Label

A single-line warning label for a time machine, written for the [Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151) bounty on make.fun. It keeps a straight official face while turning the classic duplicate-self hazard into the joke — the punchline lands on the last few words: only one of you is insured.

## The program

`main.py` (Python 3.13, standard library only, no network) holds the label as a single string, validates it — exactly one line, between 1 and 120 characters — and writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), exiting 0 on success.

## The label

> WARNING: Never wave at yourself — if you wave back, the timeline now has two of you, and only one is insured.

## Run locally

```bash
MAKEFUN_OUTPUT_DIR=/tmp/tm-out python3 main.py
cat /tmp/tm-out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

---
Built for [make.fun](https://make.fun) — referral: `77v1ce78`
