#!/usr/bin/env python3
#
# timew-fzf
#
# A timewarrior extension to list and restart
# recently tracked intervals with the help of fzf
#
# The extension works with tags and the list will find uniquelly
# tagged intervals and list them by recency, with the most recent one
# closest to the prompt.
#
# Needs fzf to be on PATH
# Needs timew-report and pyzfz from pypi

import os
import sys

from pyfzf.pyfzf import FzfPrompt
from timewreport.parser import TimeWarriorParser


def tags2key(tags):
    """A hashable string from a list of tags"""
    return "|".join(sorted(tags))


def get_recent_uniquelly_tagged_intervals():
    # Get all intervals in range
    parser = TimeWarriorParser(sys.stdin)
    intervals = parser.get_intervals()

    # Filter out open intervals
    intervals = [i for i in intervals if not i.is_open()]

    tags2interval = dict()
    for interval in intervals:
        key = tags2key(interval.get_tags())
        tags2interval[key] = interval

    intervals = list(tags2interval.values())
    intervals.sort(key=lambda i: i.get_start(), reverse=True)

    return intervals


def get_lines_for_fzf():
    """
    Get lines to feed to fzf. We used | to delimit fields in the output
    which means you can not use | within your timewarrior tags if you want this to work
    """
    lines = []
    for interval in get_recent_uniquelly_tagged_intervals():
        start = interval.get_start()
        end = interval.get_end()
        minutes = int((end - start).seconds / 60)
        tags = interval.get_tags()

        # Build the tags string
        tags_str = ""

        for tag in tags:
            # tags with spaces needs to be in quotation marks
            if " " in tag:
                tags_str += f'"{tag}" '
            else:
                tags_str += f"{tag} "
        lines.append(f"{start} |{minutes:4}| {tags_str}")
    return lines


# Launch fzf and get a selection
lines = get_lines_for_fzf()
# print(lines)
# exit()
selection = FzfPrompt().prompt(lines, "--no-sort")[0]
tags_selection = selection.split("|")[-1].strip()

# Put the cmd together
cmd = f"timew start {tags_selection}"

print(cmd)
# run it
os.system(cmd)