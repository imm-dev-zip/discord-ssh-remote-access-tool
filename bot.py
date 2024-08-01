import discord
from discord import app_commands

import subprocess

# replace with your bot token
BOT_TOKEN = ""

# replace with your guild id
GUILD_ID = 1234567890

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"Logged in as {bot.user.display_name} (ID: {bot.user.id})")

@tree.command(
    name="shell_run",
    description="run shell command",
    guild=discord.Object(id=GUILD_ID)
)
async def shell_run(interaction, command: str):
    await interaction.response.defer()

    result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
    response = f"```stdout: {result.stdout}\nstderr: {result.stderr}```"

    await interaction.followup.send(response)

if __name__ == "__main__":
    bot.run(BOT_TOKEN)
