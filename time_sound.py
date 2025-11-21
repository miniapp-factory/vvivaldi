#!/usr/bin/env python3
"""
time_sound.py

A simple script that prompts the user for a target time (HH:MM:SS) and plays a sound
when that time is reached. The script uses the `playsound` library to play an
audio file named `alert.wav` located in the same directory. If the target time
has already passed, the script will notify the user and exit.
"""

import datetime
import time
import sys

try:
    from playsound import playsound
except ImportError:
    print("The 'playsound' module is required. Install it with:")
    print("    pip install playsound")
    sys.exit(1)


def parse_time(time_str: str) -> datetime.time:
    """Parse a time string in HH:MM:SS format."""
    try:
        return datetime.datetime.strptime(time_str, "%H:%M:%S").time()
    except ValueError:
        raise ValueError("Time must be in HH:MM:SS format.")


def main() -> None:
    target_str = input("Enter target time (HH:MM:SS): ").strip()
    try:
        target_time = parse_time(target_str)
    except ValueError as e:
        print(e)
        sys.exit(1)

    now = datetime.datetime.now()
    target_datetime = datetime.datetime.combine(now.date(), target_time)

    # If the target time is earlier than now, assume it's for the next day
    if target_datetime <= now:
        target_datetime += datetime.timedelta(days=1)

    print(f"Waiting until {target_datetime.strftime('%Y-%m-%d %H:%M:%S')}...")

    while datetime.datetime.now() < target_datetime:
        time.sleep(1)

    print("Target time reached! Playing sound...")
    try:
        playsound("alert.wav")
    except Exception as e:
        print(f"Failed to play sound: {e}")


if __name__ == "__main__":
    main()
