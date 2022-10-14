from email.mime import image
from operator import floordiv
import os
import base64
from tokenize import Name, Token
from unicodedata import name
import discord
import json
import requests
from discord import Webhook
from dotenv import load_dotenv
load_dotenv()

# logs into the discord bot

token = "OTk5ODM2MjM5NjQ3NzQ4MjM3.GreR7Y._CGu4SzKudf0yaa8BJrc-9VuKUo9gusx0uDomI"
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if not message.content.startswith("/"):
        return

    parts = message.content.split(' ')
    if len(parts) != 2:
        await message.channel.send("USAGE: /floor <collection>")
        return

    if parts[0] != '/floor':
        await message.channel.send("Unknown command. Available commands are: /floor")
        return

    collection = parts[1]
    r = requests.get("https://api.opensea.io/api/v1/collection/" + collection)
 
    if r.status_code != 200:
        await message.channel.send("Something went wrong")
        return

    #all data on the colleciton
    floor = r.json()["collection"]["stats"]["floor_price"]
    n = r.json()["collection"]["name"]
    one_hour_volume = r.json()["collection"]["stats"]["one_hour_volume"]
    one_hour_sales =  r.json()["collection"]["stats"]["one_hour_sales"]
    six_hour_volume = r.json()["collection"]["stats"]["six_hour_volume"]
    six_hour_sales = r.json()["collection"]["stats"]["six_hour_sales"]
    one_day_volume = r.json()["collection"]["stats"]["one_day_volume"]
    one_day_sales = r.json()["collection"]["stats"]["one_day_sales"]
    image_url = r.json()["collection"]["image_url"]
    icon_url = "https://pbs.twimg.com/profile_images/1484322477358534658/qhzNEION_400x400.jpg"
    address = r.json()["collection"]["primary_asset_contracts"][0]["address"] #contract address for minting
  

    e = discord.Embed(title="OpenSea Collection Link", url="https://opensea.io/collection/" + collection, description=f"Current floor for {str(n)} is {str(floor)}Ξ\n")
    e.set_thumbnail(url = icon_url)
    e.set_image(url = image_url)
    e.set_footer(text = "you're welcome you filthy investor", icon_url = image_url)
    e.add_field(name = "nerd stats" , value = (f"__One hour volume:__ {int(one_hour_volume)}Ξ\n__One hour sales:__ {int(one_hour_sales)}Ξ\n__Six hour volume:__ {int(six_hour_volume)}Ξ\n__Six hour sales:__ {int((six_hour_sales))}Ξ\n__One day volume:__ {int(one_day_volume)}Ξ\n__One day sales:__ {int(one_day_sales)}Ξ"))
    e.add_field(name = "Contract address:" , value = address)
    await message.delete()
    await message.channel.send(embed=e)


client.run(token)