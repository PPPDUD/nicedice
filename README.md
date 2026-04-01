# nicedice
`nicedice` is a program for Debian-based systems that lets you simulate dice and other simple, probabilistic mechanisms, like 8-balls.

## Presets
`nicedice` comes with multiple premade dice, installed at `/usr/share/nicedice/`:
- `d6die.json`: standard, six-sided die
- `d20die.json`: twenty-sided die, most commonly used in RPGs
- `percentile.json`: 100-sided die with "%" suffix, used for generating percentages
- `8ball.json`: magic 8-ball, used for answering simple yes/no questions

## Creating your own dice
`nicedice-create` is a simple, interactive wizard that generates die definition files for usage with `nicedice`.

In order to use it, you need to have `python3-questionary` installed on your system.

## Examples
Roll a standard (six-sided) die: `nicedice /usr/share/nicedice/d6die`

Interactively define a die named `dreidel.json`: `nicedice-create dreidel.json`
