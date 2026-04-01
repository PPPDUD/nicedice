# nicedice
`nicedice` is a program for Debian-based systems that lets you simulate dice and other simple, probabilistic mechanisms, like 8-balls.

## Presets
`nicedice` comes with multiple premade dice, installed at `/usr/share/nicedice/`:
- `d6die`: standard, six-sided die
- `d20die`: twenty-sided die, most commonly used in RPGs
- `8ball`: magic 8-ball, used for answering simple yes/no questions

## Examples
Roll a standard (six-sided) die: `nicedice /usr/share/nicedice/d6die`

Interactively define a die named `dreidel`: `nicedice-create dreidel`
