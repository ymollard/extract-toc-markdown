# extract-toc-markdown
Extract Table Of Content (ToC) from Markdown files

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

In order to ignore or not count some titles, a special meaning is given to titles with more than 2 spaces between `#` and the title such as `#  Introduction`, you can output them normally (`count`, default), output them but not count them (`nocount`), or ignore them (`ignore`)  

```bash
python extract-toc-markdown.py my-markdown-file.md --spacedtitles=nocount
```
