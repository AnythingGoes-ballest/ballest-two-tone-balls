"""Writes one model per colour into models/: the ball is clear glass (AddBall with no image) and a bowl of tinted glass
makes its lower half coloured; the bowl rolls with the ball.
  python make_models.py"""
COLOURS = [
    ("red", "Red", "ff2418"),
    ("orange", "Orange", "ff7a10"),
    ("yellow", "Yellow", "ffd21a"),
    ("lime", "Lime", "8aff1a"),
    ("green", "Green", "16c83a"),
    ("teal", "Teal", "10c8b4"),
    ("blue", "Blue", "1e5aff"),
    ("purple", "Purple", "8a2cff"),
    ("pink", "Pink", "ff3ca8"),
    ("black", "Black", "101014"),
]

# How strongly the lower half is tinted: 0.45 reads as the colour in game (0.28, as Monkey Balls, looked faint);
# dark glass needs more to show as black.
OPACITY = {"black": 0.85}

for key, name, hexcol in COLOURS:
    opacity = OPACITY.get(key, 0.45)
    with open(f"models/{key}.txt", "w", newline="\n") as f:
        f.write(f"# {name}: a clear ball with its lower half {name.lower()} glass, rolling with the ball.\n")
        f.write(f"material tint glass #{hexcol} opacity={opacity}\n\n")
        f.write("group shell\n")
        f.write("bowl tint r=49.5 wall=0.8\n")
