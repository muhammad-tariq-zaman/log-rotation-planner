# log-rotation-planner

Estimate how many days until a disk fills from log growth, and whether a chosen retention period fits in the free space.

## How to run

```sh
python3 main.py --growth-mb-per-day 120 --free-mb 1200 --keep-days 7
```

## Example output

```
Growth 120 MB/day, free 1200 MB -> disk full in 10.0 days.
Keeping 7 days needs 840 MB (fits: yes).
```

Standard library only. Run the tests with `python3 -m unittest discover`.
