import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from setup import SetupCommands

def main():
    # Create Bot instance
    bot = discord.Client(intents=intents())
    # Create CommandTree instance
    tree = app_commands.CommandTree(bot)

    # Setup slash commands
    SetupCommands(tree)

    @bot.event
    async def on_ready():
        print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")

    # Start discord bot
    bot.run(os.getenv("DISCORD_TOKEN"))

def intents():
    """
    This function sets the intents for the Discord bot.
    It uses the default intents and enables message-related intents.

    Returns:
        discord.Intents: The configured intents object
    """
    intents = discord.Intents.default()
    intents.messages = True
    return intents

if __name__ == "__main__":
    load_dotenv()
    main()
