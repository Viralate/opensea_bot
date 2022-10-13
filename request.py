from email.mime import image
from operator import floordiv
import os
import base64
from tokenize import Name
from unicodedata import name
from aiohttp import JsonPayload
import discord
import requests
import json
import discord
from discord import Webhook, RequestsWebhookAdapter

# logs into the discord bot

token = 'OTk5ODM2MjM5NjQ3NzQ4MjM3.GIsq3s._d3bjv1fjYbkwsIr7XRH-Wx2r90LOxmhJpTytU'

client = discord.Client()

@client.event
async def on_ready():
    print(f"Bot Logged in as {client.user}")



client.run(token)


webhook_url = 'https://discord.com/api/webhooks/1026805730742902845/1'

token = 'OTk5ODM2MjM5NjQ3NzQ4MjM3.GIsq3s._d3bjv1fjYbkwsIr7XRH-Wx2r90LOxmhJpTytU'

client = discord.Client()


#get users input

headers = {
    "accept": "application/json",
    "X-API-KEY": "d0b6281e87d84702b020419fdf58ea81"
}

c = input()
r = requests.get("https://api.opensea.io/api/v1/collection/" + c)
 

#all data on the colleciton
floor = r.json()["collection"]["stats"]["floor_price"]
n = r.json()["collection"]["name"]
one_hour = r.json()["collection"]["stats"]["one_hour_volume"]
image_url = r.json()["collection"]["image_url"]





webhook = Webhook.from_url('https://discord.com/api/webhooks/1026805730742902845/H6uYgG5lxW2JFkfdDscZS2dNZIHc3PBuqqVAGkHrcvPgHkzytqeN4mZeb9u6C-HKDEzi' , adapter=RequestsWebhookAdapter())
e = discord.Embed(title= "OpenSea Collection Link", url = "https://opensea.io/collection/" + c, description=f"Current floor for {str(n)} is {str(floor)}Ξ \n Past one hour volume: {str(one_hour)}\n")
e.set_image(url = image_url)
e.set_footer(text = "Made by Viralate", icon_url = image_url)

webhook.send(embed=e)









