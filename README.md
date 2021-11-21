# extract-toc-markdown
Extract Table Of Content (ToC) from any Markdown file, including features for [Marp slides](https://marp.app/).

## Usage
```bash
./extract-toc-markdown.py my-markdown-file.md
```
will output the Table Of Content in the terminal:
```
1. Introduction
  1.1. Part A
  1.2. Part B
2. Conclusion
  2.1. Part A
  2.2. Part B
```

### Filter some titles
In order to ignore or not count some titles, a special meaning is given to titles with more than 2 spaces between `#` and the title such as `#  Introduction`, you can output them normally (`count`, default), output them but not count them (`nocount`), or ignore them (`ignore`)  

```bash
python extract-toc-markdown.py my-markdown-file.md --spacedtitles=nocount
```

### Limit depth
```bash
./extract-toc-markdown.py my-markdown-file.md --max-depth=2
```
will limit output to titles and subtitles (depth=2).

### Generate slide links
This is made for Marp slides with "---" slide delimiters.
```bash
./extract-toc-markdown.py my-markdown-file.md --link-slides-level=2 --max-depth=3
```
Here we generate a ToC for 3 levels but only 2 have links to the right slide page:
```
1. [Introduction](#2)
    1.1. [A](#2)
       1.1.1. level 3 is not linked
    1.2. [B](#5)
    1.3. [C](#9)
```
