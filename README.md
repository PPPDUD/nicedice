# nicedice
`nicedice` is a program for Debian-based systems that lets you simulate dice and other simple, probabilistic mechanisms, like magic 8-balls.

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

## A note about manmade code
The owner of this project believes in good faith that it complies with [The Manmade Software Declaration 1.0](https://mojavesoft.net/ai-policy/1.0).
Contributors are encouraged to follow the guidelines described at the aforementioned link when proposing any code changes, and patches that appear to violate those rules may be rejected at any time.
