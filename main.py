import discord
from discord.ext import commands
from discord import app_commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix=".", intents=discord.Intents.all())

FILES = [
    "03137d3096875861.txt",
    "129521809f206cc2.txt",
    "21c8125db11e7793.txt",
    "25ec9ff80ff99697.txt",
    "2898c681c6151598.txt",
    "29de2c9bb0d1aa39.txt",
    "2c1421e20f401388.txt",
    "4356d8426dd214b2.txt",
    "5c5d695a0d4c0436.txt",
    "63b2443f78cc5744.txt",
    "683cb837769fbf9d.txt",
    "69d3de3f3ce1f1fc.txt",
    "6d53bc6fd4248fc1.txt",
    "6d53ef61eb1e673f.txt",
    "83dff351c98d4a69.txt",
    "85c614a316b076d1.txt",
    "8aaa09faab1dac12.txt",
    "9864766a09ac7b3f.txt",
    "a0fa0680478e86ae.txt",
    "a4b32c9a3f0f489d.txt",
    "a6aae849b155b4d6.txt",
    "afce701f8b690bec.txt",
    "b654ad00ccb3ff08.txt",
    "bac8ff328543f18b.txt",
    "bdb627dd786814e5.txt",
    "c41277f57a66a917.txt",
    "c8a710654700e75c.txt",
    "cf003e75da5d2d90.txt",
    "d2a081b32720146c.txt",
    "ec3f20794c42d556.txt",
    "f0b2d8a7d9c6a2ab.txt"
]

@client.event
async def on_ready():
    await client.tree.sync()
    print("raedy") # ok bro

@client.tree.command(name="iqsm", description="sends a iqsm")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.user_install()
async def iqsm(interaction: discord.Interaction):
    file = random.choice(FILES)
    url = f"https://raw.githubusercontent.com/hiperdex/boykisser/main/ascii/sfw/{file}"
    response = requests.get(url)

    if response.status_code == 200:
        ascii_art = response.text
        if len(ascii_art) > 1900:
            ascii_art = ascii_art[:1900] + "\n... (truncated)"
        await interaction.response.send_message(ascii_art)
    else:
        await interaction.response.send_message("failed to fetch a file", ephemeral=True)

@client.tree.command(name="test", description="np")
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
@app_commands.user_install()
async def ok(interaction: discord.Interaction):
    await interaction.response.send_message('ok')

client.run(os.getenv("TOKEN"))
