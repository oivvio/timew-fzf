# timew-fzf

A [timewarrior](https://timewarrior.net/) extension to list and restart recently tracked intervals with the help of `fzf`.

The extension works with tags and will find uniquely tagged intervals and list them by recency, with the most recent one closest to the prompt. The user can then filter them with the help of `fzf` and start a new interval based on the tags of an old interval.

## Screencast

![](https://raw.githubusercontent.com/oivvio/timew-fzf/main/docs/timew-fzf.gif)

## Installation

**Requirements**

For timew-fzf to work you need [`fzf`](https://github.com/junegunn/fzf#installation) to be on PATH. You will also need python3 and you will need to `pip install timew-report` and `pip install pyfzf`.

1. Clone the repo to a location of your liking

   git clone git@github.com:oivvio/timew-fzf.git

2. Add a symlink from ~/.timewarrior/extensions

   `cd ~/.timewarrior/extensions`

   `ln -s /path_to_where_you_cloned_the_repo/timew-fzf/twfzf.py`

3. Optionally add a symlink to the utility script

   `cd ~/.local/bin`

   `ln -s /path_to_where_you_cloned_the_repo/timew-fzf/rr`

## Usage

Start a selection based on intervals from the last 6 months.

    timew twfzf 6m

But why do all that typing, like an animal, when you can just type...

    rr

to launch a utility script that will stop any currently running interval and then run `timew twfzf 6m` whith an option to override the 6 months, so...

    rr 2y

will let you select among intervals from the last two years, and so on.
