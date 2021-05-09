# discordfs

Just a better file manager for discord :)
Implemented as a discord bot

Commands

I really like Discord's Slash Commands, so the bot supports older commands (Ex. `!all`) and slash commands (Ex. `/all`)

- `/search [filename]` : Search for a file by its filename. More search capabilities coming soon! (Also supports: `!fsearch`, `!s`, `!search`, `!fs`)
- `/all` : Display all files that the bot can access (Also supports: `!all`, `!a`)
- `/clear` : Clear all files from the index (This doesn't delete any files/messages in the actual server) (Also supports: `!clear`, `!c`)
- `/remove [filename]` : Remove the bot's access to files named `filename` (Also supports: `!remove`, `!rm`)
- `/delete [filename]` : Remove the bot's access to files named `filename` AND delete their respective messages (Also supports: `!delete`, `!del`)

Add the bot to your server with this link:

https://discord.com/api/oauth2/authorize?client_id=837345172105723985&permissions=2147593280&scope=bot%20applications.commands

Plz let me know if you encounter bugs! Feel free to create an issue on this repo or message me at `dhrumilp15#4369`!
