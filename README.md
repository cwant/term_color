# `term_color`

Colorful/Colourful terminals

I like terminals to have light text on a dark background.
Since I usually have a lot of them open, I like them the backgrounds of
my terminals to have random colors for visual texture
(the main requirement is that the background must be dark).
This software provides wrappers for `xterm` and `xfce4-terminal`
that generate each new terminal with a different random color
(random, but the overall hue of the terminal can be gamed).

## Installation

You will want to have `python` installed, and also `xterm` or
`xfce4-terminal`. This program assumes the terminals are installed
in `/usr/bin`.

Create symbolic links for either `xterm` or `xfce4-terminal` in this
repository, and place them in your path in a place that has higher
priority than the location of your system terminal programs.
Alternatively, put this repository in your path.

## Usage

Call `xterm` or `xfce4-terminal`, e.g., `xterm &`.
You now have an `xterm` with a random background color.

Want your background hue to be weighted towards being bluish?
Try: `xfce4-terminal blue &`

Want another blue xterm, but with a different color than the last one?
Just run the above command again.

Try the above replacing `blue` with `red`, `green`, `grey`,
`cyan` or `magenta`.
