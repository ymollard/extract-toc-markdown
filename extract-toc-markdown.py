#!/usr/bin/env python

from argparse import ArgumentParser

parser = ArgumentParser(description="Extract ToC from a mardown doc")
parser.add_argument("path", help="Path to the amrdown file to extract ToC from")
parser.add_argument("--spacedtitles",
                    choices=["ignore", "nocount", "count"],
                    default="count",
                    help="How to treat titles with >= 2 initial spaces after #")
parser.add_argument("--max-depth", type=int, default=10, help="Ignore titles behind this depth")
parser.add_argument("--link-slides-level", type=int, default=-1, help="Generate Mardown links to slides for each title of this level or below.")
parser.add_argument("--slides-separator", type=str, default="---", help="String that separates slides from each other")

args = parser.parse_args()

hold_verbatim = False
levels = [0]
previous_section_line_num = 1
slide_num = 0

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
                    title_str = line.strip().replace("#", "")

                    if args.link_slides_level >= level:
                        title_str = "[" + title_str + "](#" + str(slide_num-1) + ")"

                    print(level_string + ". " + title_str)
                    previous_section_line_num = 0

            elif line.startswith(args.slides_separator):
                slide_num += 1
            else:
                previous_section_line_num += 1
