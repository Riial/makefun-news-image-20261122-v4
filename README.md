# The World in One Day — Sunday 22 November 2026 (v4)

[![news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/Riial/makefun-news-image-20261122-v4/rank.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/Riial/makefun-news-image-20261122-v4/reward.svg)](https://make.fun/bounty/news-image-20261122)

One image that sums up Sunday 22 November 2026: 35 stories, 9 regions,
15 fields, 13 pictured — every one dated that Sunday.

## What it is

A broadsheet front page. Three heroes lead: COP31 ends with no deal
(the longest summit yet), Russia fires 186 drones at Ukraine overnight
(161 downed), and Democrats clinch 258 House seats — their biggest
majority since 1992. Ten more stories fill the grid, a world map pins
all 35, and 22 more stories run in the "Also on Sunday" column. A
DATE CHECK box lists the near-misses that belong to another day
(including the fabricated "Anthropic shares $87.80" line, flagged as
fabricated because Anthropic is private).

## How it was built

v4 is a legibility rebuild of v3. The judge liked v3's breadth but
found its dense small type illegible at thumbnail size, so v4 subtracts:
the big-number banners are gone from the grid cells, the field tags are
gone from the "Also" items, the hero headlines are bigger (22px serif,
900 weight), the H3 seat chart is a clean open arc with a giant "258",
and the COP31 visual is a single bold idea — the draft pact stamped
"NO DEAL". All 35 stories, numbers, framings, the stats strip, the
8-item timeline, the region bar, the map, the outlet sources, the
certainty badges and the DATE CHECK are unchanged.

The page is typeset in HTML/CSS and rendered to a 1024×1024 PNG with
headless Chromium. The illustrations are AI-painted; the seat chart
and the map pins are hand-built SVG diagrams.

## Running it

```sh
python3 main.py
```

Writes `entry.png` (1024×1024, ≤1 MiB) to the output directory:
`MAKEFUN_OUTPUT_DIR` if set, `/output` if it exists, otherwise `out`.
Standard library only, no network. Running it twice produces
byte-identical output.

## Bounty

[news-image-20261122 on make.fun](https://make.fun/bounty/news-image-20261122)
