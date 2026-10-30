"""Plan log rotation: days until a disk fills, given growth and free space.

Usage: python3 main.py --growth-mb-per-day 120 --free-mb 1200 --keep-days 7
"""
import argparse
import sys


def days_until_full(free_mb, growth_per_day):
    if growth_per_day <= 0:
        return None
    return free_mb / growth_per_day


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--growth-mb-per-day", type=float, required=True)
    parser.add_argument("--free-mb", type=float, required=True)
    parser.add_argument("--keep-days", type=int, default=7)
    args = parser.parse_args(argv)
    days = days_until_full(args.free_mb, args.growth_mb_per_day)
    needed = args.growth_mb_per_day * args.keep_days
    print(f"Growth {args.growth_mb_per_day:g} MB/day, free {args.free_mb:g} MB -> disk full in {days:.1f} days.")
    print(f"Keeping {args.keep_days} days needs {needed:g} MB (fits: {'yes' if needed <= args.free_mb else 'no'}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
