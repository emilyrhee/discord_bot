import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import os
import nltk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents, help_command=None)

@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if "love you" in message.content:
        await message.channel.send("Love you too")

    if "wyd" in message.content:
        wyd_responses = ["On the toilet.", "Wrapping up some work.", "Watching some YouTube."]
        await message.channel.send(random.choice(wyd_responses) + " Wbu?")



bot.run(os.getenv('TOKEN'))

