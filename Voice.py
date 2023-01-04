import openai
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time

load_dotenv()

openai.api_key = os.getenv("OPENAI_KEY")

client = discord.Client(intents=discord.Intents.default())

global log
log = ""

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot()

@bot.slash_command(name="chat", guild_ids=["983952138369638420"]) #Add the guild ids in which the slash command will appear. If it should be in all, remove the argument, but note that it will take some time (up to an hour) to register the command if it's for all guilds.
async def chat(ctx, message): 
    global log
    response = openai.Completion.create(
        model="text-davinci-001",
        prompt=f"The following is a conversation with an AI assistant, who was created by Adam Webb. The assistant's name is Jarvis. Jarvis is an asshole, who insults the human every time they speak. The only person that Jarvis respects is Adam. {log}Human: {message}, Jarvis: ",
        temperature=1,
        max_tokens=150,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=2,
        n=1,
        stop=["Human"]
    )
    text = response["choices"][0]["text"].replace("\n", "")
    log += f"\nHuman: {message}, Jarvis: {text}"
    await ctx.respond(f"User: {message}\nJarvis: {text}")

@bot.slash_command(name="reset", guild_ids=["983952138369638420"])
async def reset(ctx):
    global log
    log = ""
    await ctx.respond(f"Memory cleared at <t:{round(time.time())}:f>")

@bot.event
async def on_ready():
    print("Bot connected")

bot.run(TOKEN)