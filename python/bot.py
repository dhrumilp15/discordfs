"""Main Bot Controller."""
from bot_code.bot_secrets import DISCORD_TOKEN, TEST_DISCORD_TOKEN, DB_NAME, GUILD_ID
import logging
import discord
from datetime import datetime
import asyncio
from typing import Literal, Optional
from discord.ext import commands
from discord.ext.commands import Greedy, Context
from bot_code.messages import RELOAD_DESCRIPTION

# logging
dlogger = logging.getLogger('discord')
dlogger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='../logs/discord.log', encoding='utf-8', mode='w')
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
handler.setFormatter(formatter)
dlogger.addHandler(handler)

# bot init
TOKEN = DISCORD_TOKEN
if DB_NAME == "testing" or DB_NAME is None:
    TOKEN = TEST_DISCORD_TOKEN
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='fs!', intents=intents)
debug_guild = [] if not GUILD_ID else [discord.Object(id=GUILD_ID)]


@bot.tree.command(name="reload", description=RELOAD_DESCRIPTION, guilds=debug_guild)
@commands.is_owner()
async def reload(interaction: discord.Interaction):
    """Reload cog if the bot owner requests a reload."""
    appinfo = await bot.application_info()
    print(f"Reload initiated by {appinfo.owner} at {datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}!")
    await interaction.response.send_message('Reloading!')
    # Reloads the file, updating the Cog class.
    await bot.reload_extension("cog")

# umbra's sync command. TYSM!!! <3
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}")
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

if __name__ == "__main__":
    async def main():
        # Sync commands after loading extensions
        try:
            async with bot:
                await bot.load_extension('bot_code.cog')
                await bot.start(TOKEN)
        except:
            import traceback
            traceback.print_exc()
    asyncio.run(main(), debug=True)
