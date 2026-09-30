// Two-Tone Balls: ten balls on the Customize page, through Cosmetic Kit (a dependency: see info.toml). Each is a clear
// glass ball (no image) whose lower half is tinted glass of one colour (a model), rolling with the ball.

import bool AddBall(const string &in, const string &in, const string &in, const string &in, const string &in) from "cosmetic-kit";

const array<string> KEYS = {"red", "orange", "yellow", "lime", "green", "teal", "blue", "purple", "pink", "black"};
const array<string> NAMES = {"Red", "Orange", "Yellow", "Lime", "Green", "Teal", "Blue", "Purple", "Pink", "Black"};

void Main()
{
    string f = Plugins::Folder();
    for (uint i = 0; i < KEYS.length(); i++)
        AddBall("two-tone-balls." + KEYS[i], NAMES[i] + " Two-Tone", "", f + "previews/" + KEYS[i] + ".png",
                f + "models/" + KEYS[i] + ".txt");
}
