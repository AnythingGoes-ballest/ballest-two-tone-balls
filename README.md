# Two-Tone Balls

A plugin for the [Ballest plugin manager](https://github.com/AnythingGoes-ballest/ballest-plugin-manager): ten
two-tone balls, each clear glass with its lower half in colour. They're added to the **balls** tab of the
**Customize** page through [Cosmetic Kit](https://github.com/AnythingGoes-ballest/ballest-cosmetic-kit). The coloured
half rolls with the ball.

Colours: red, orange, yellow, lime, green, teal, blue, purple, pink and black.

## Install

In the game: footer **plugins** > **browse** > Two-Tone Balls > **install** (Cosmetic Kit comes with it).
Needs the plugin manager host 0.14.0 or newer.

## Files

- `main.as`: adds the balls.
- `models/`: one model per colour (a bowl of tinted glass), written by `make_models.py`. The format is in the plugin
  manager's [custom cosmetics guide](https://anythinggoes-ballest.github.io/ballest-plugin-manager/guides/cosmetics/).
- `previews/`: the tile pictures, drawn from the models by `make_previews.py` (Python with NumPy and Pillow).

## License

MIT
