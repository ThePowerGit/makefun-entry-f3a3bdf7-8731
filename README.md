# The Long Roast: Lawmakers and the File They Cannot Convert

Competition entry for make.fun bounty `u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7`.

## The text

> The lawmakers who wrote the AI Act can mandate human oversight for a chatbot, but still convert a Word doc to PDF by screenshotting each page into PowerPoint.

- Character count: 158
- Cap: 320 characters
- Condition: at least one non-whitespace character

`entry.txt` holds exactly this text and nothing else, with no trailing newline.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The program copies `entry.txt` byte-for-byte to `$MAKEFUN_OUTPUT_DIR/entry.txt`, which defaults to `/output/entry.txt` when the variable is unset.

## License

MIT, see `LICENSE`.
