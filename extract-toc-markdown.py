#!/usr/bin/env python

from argparse import ArgumentParser

parser = ArgumentParser(description="Extract ToC from a mardown doc")
parser.add_argument("path", help="Path to the amrdown file to extract ToC from")
parser.add_argument("--spacedtitles",
                    choices=["ignore", "nocount", "count"],
                    default="count",
                    help="How to treat titles with >= 2 initial spaces after #")
parser.add_argument("--max-depth", type=int, default=10, help="Ignore titles behind this depth")
args = parser.parse_args()

hold_verbatim = False
levels = [0]
previous_section_line_num = 1

def _count_trailing_spaces(string: str) -> int:
    i = 0
    while string[i] == " ":
        i += 1
    return i

with open(args.path) as f:
    for line in f:
        if line.lstrip().startswith("```"):
            hold_verbatim = not hold_verbatim
        if not hold_verbatim:
            if line.lstrip().startswith("#"):
                initial_spaces = _count_trailing_spaces(line.lstrip().replace("#",""))
                level = line.count("#")                  
                if level > len(levels):
                    while level > len(levels):
                        levels.append(0)
                elif level < len(levels):
                    while level < len(levels):
                        del levels[-1]

                if initial_spaces < 2 or args.spacedtitles == "count":
                    levels[level-1] += 1

                level_string = level*"    "
                if initial_spaces < 2 or args.spacedtitles == "count":
                    level_string += ".".join(map(str, levels))

                must_print_spacedtitles = initial_spaces < 2 or args.spacedtitles != "ignore"
                must_print_depth = level <= args.max_depth
                if must_print_spacedtitles and must_print_depth:
                    print(level_string + ". " + line.strip().replace("#", ""))
                    previous_section_line_num = 0
            else:
                previous_section_line_num += 1
