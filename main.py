import asyncio
import json
import random
import time

import discord
import openai
import requests
from discord.ext import commands
from dpyConsole import Console
from googleapiclient.discovery import build

from config import contents, messages
from database import insert

# Beispiel: insert( interaction.user.name, interaction.user.id, "<command name>", prompt, response )

with open('keys.json') as f:
    keys = json.load(f)
discord_token = keys['discord_key']
openai.api_key = keys['openai_key']
tenor_key = keys['tenor_key']
service = build('customsearch', 'v1', developerKey=keys['google_key'])

bot = commands.Bot(command_prefix='>', intents=discord.Intents.all())
console = Console(bot)


@bot.tree.command(name='google', description='Search Google')
async def google_respond(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    tick = time.time()
    query = prompt
    result = service.cse().list(q=query, cx='b6f0d8c69f4b54e04', num=3).execute()

    response = ''
    for item in result['items']:
        response += f"{item['title']} - {item['link']}\n"

    await interaction.followup.send(f'{interaction.user.mention} used: `/google {prompt}`')
    await interaction.channel.send(response)
    insert(interaction.user.name, interaction.user.id, "google", prompt, response)

    print(f'Response took {time.time() - tick} seconds')


@bot.tree.command(name='chat', description='Generate a response using Chat-GPT3')
async def openai_respond(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()

    tick = time.time()
    unfiltered_response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f'{prompt}',
        temperature=0.7,
        max_tokens=1024,
    )
    response = unfiltered_response['choices'][0]['text']
    await interaction.followup.send(f'{interaction.user.mention} used: `/chat {prompt}`')
    await interaction.channel.send(f"```\n{response}\n```")
    insert(interaction.user.name, interaction.user.id, "chat", prompt, response)

    print(f'Response took {time.time() - tick} seconds')


@bot.tree.command(name='image', description='Generate image using Dall-E')
async def openai_image(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    tick = time.time()
    unfiltered_response = openai.Image.create(
        prompt=f'{prompt}',
        size='1024x1024',
        n=1,
    )

    response = unfiltered_response['data'][0]['url']
    await interaction.followup.send(f'{interaction.user.mention} used: `/image {prompt}`')
    await interaction.channel.send(response)
    insert(interaction.user.name, interaction.user.id, "image", prompt, response)
    print(f'Response took {time.time() - tick} seconds')


@bot.tree.command(name='gif', description='Search Tenor')
async def tenor_gif(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    tick = time.time()
    n_of_gifs = 20
    unfiltered_response = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&bot_key=%s&limit=%s" % (
            prompt, tenor_key, interaction.user, n_of_gifs)
    )
    tenor_gifs = unfiltered_response.json()
    response = tenor_gifs['results'][random.randint(0, n_of_gifs)]['media_formats']['gif']['url']
    await interaction.followup.send(f"{interaction.user.mention} used: `/gif {prompt}`")
    await interaction.channel.send(response)
    await interaction.channel.send("Via Tenor")
    insert(interaction.user.name, interaction.user.id, "gif", prompt, response)
    print(f'Response took {time.time() - tick} seconds')


private_channels = set()


@bot.tree.command(name='private', description='Create private channel')
async def create_private_channel(interaction: discord.Interaction):
    if interaction.user.name.lower() in private_channels:
        await interaction.response.send_message('You already have a private channel')
        return

    guild = interaction.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        interaction.user: discord.PermissionOverwrite(read_messages=True),
        bot.user: discord.PermissionOverwrite(read_messages=True),
        interaction: discord.PermissionOverwrite(read_messages=True)
    }

    category = discord.utils.get(guild.categories, name='Private Channels')
    if not category:
        category = await guild.create_category('Private Channels')

    await guild.create_text_channel(
        f'{interaction.user.name}',
        category=category,
        overwrites=overwrites
    )
    private_channels.add(interaction.user.name.lower())
    insert(interaction.user.name, interaction.user.id, "create_channel", "", "")


@bot.tree.command(name='close', description='Close private channel')
async def close_channel(interaction: discord.Interaction):
    if interaction.channel.name.startswith(f'{interaction.user.name.lower()}'):
        private_channels.discard(interaction.user.name.lower())
        await interaction.channel.delete()
        insert(interaction.user.name, interaction.user.id, "delete_channel", "", "")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user} \nBot latency: {round(bot.latency * 1000)}ms')
    try:
        synced = await bot.tree.sync()
        print(len(synced))
    except Exception as e:
        print(e)

    guild = bot.guilds[0]
    category = discord.utils.get(guild.categories, name='Private Channels')
    if category:
        for channel in category.text_channels:
            private_channels.add(channel.name.lower())

    while True:
        await bot.change_presence(activity=discord.Game(name=random.choice(contents['games'])))
        await asyncio.sleep(random.randrange(69, 187))


@bot.event
async def on_message(message: discord.Message):
    if message.author == bot.user:
        return
    tick = time.time()

    for m in messages:
        if m in message.content.lower():
            response = messages[m]
            if callable(response):
                response = response()
            await message.channel.send(response)

    print(f'Response took {time.time() - tick} seconds')
    print(message.author)
    print(message.content)


@console.command()
async def shutdown():
    await bot.close()


@console.command()
async def latency():
    print(f'Bot latency: {round(bot.latency * 1000)}ms')


console.start()
bot.run(discord_token)
