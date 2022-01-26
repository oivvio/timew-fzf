# timew-fzf

A timewarrior extension to list and restart recently tracked intervals with the help of `fzf`.

The extension works with tags and the list will find uniquely tagged intervals and list them by recency, with the most recent one closest to the prompt.

## Installation

**Requirements**

For timew-fzf to work you need `fzf` to be on PATH.

1. Clone the repo

2. Symlink from ~/.timewarrior/extension

## Usage

Start a selection based on intervals from the last 6 months.

    timew twfzf 6m
