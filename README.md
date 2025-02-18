# Twitch Unit Converter
A Twitch integration bot that allows you to compute common conversions between metric and imperial units.

---

# Explanation

When the bot has started, it will listen to chat messages in the channel listed in the settings.txt file. Whenever a user types one of the conversion commands in chat, the bot will respond with the unit conversion.

---

# Usage
Commands: (all commands are reversable ex: ```!ctof``` for Celsius to Fahrenheit and ```!ftoc``` for Fahrenheit to Celsius)
<pre><b>!ctof (Celsius to Fahrenheit)<br>!mtoft (meters to feet)<br>!kmtomi (kilometers to miles)<br>!cmtoin (centimeters to inches)<br>!kgtolbs (kilograms to pounds)<br>!oztog (ounces to grams)<br>!floztoml (fluid ounces to milliliters)<br>!galtol (gallons to liters)</b></pre>

---

# Settings
This bot is controlled by a settings.txt file, which looks like:
```
{
    "Host": "irc.chat.twitch.tv",
    "Port": 6667,
    "Channel": "#<channel>",
    "Nickname": "<name>",
    "Authentication": "oauth:<auth>"
}
```

| **Parameter**        | **Meaning** | **Example** |
| -------------------- | ----------- | ----------- |
| Host                 | The URL that will be used. Do not change.                         | "irc.chat.twitch.tv" |
| Port                 | The Port that will be used. Do not change.                        | 6667 |
| Channel              | The Channel that will be connected to.                            | "#ph__g" |
| Nickname             | The Username of the bot account.                                  | "phg_bot" |
| Authentication       | The OAuth token for the bot account.                              | "oauth:pivogip8ybletucqdz4pkhag6itbax" |

*Note that the example OAuth token is not an actual token but a generated string to indicate what it might look like.*

I got my real OAuth token from https://twitchtokengenerator.com/.

---

# Requirements
* [Python 3.6+](https://www.python.org/downloads/)
* [TwitchWebsocket](https://github.com/CubieDev/TwitchWebsocket) by tomaarsen
