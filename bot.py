from discord.ext import commands
import requests
import xml.etree.ElementTree as ET
import json

bot = commands.Bot(command_prefix='>')

def read_file():
    with open('./secrets.json') as f:
        return json.load(f)

secrets = read_file()

@bot.command(name='say', help="Repeats whatever it's told")
async def say(ctx, *args):
    response = ""
    for arg in args:
        response = response + " " + arg
    await ctx.send(response)

@bot.command(name='chat', help='Converse with the bot')
async def say(ctx, *args):
    string = ""
    for arg in args:
        string = string + " " + arg
    xml = """<chat application='%s' instance='165'>
    <message>%s</message></chat>""" % (secrets["api_token"], string)
    url = 'https://www.botlibre.com/rest/api/chat'
    headers = {'Content-Type': 'application/xml'}
    result = requests.post(url, data=xml, headers=headers).text
    response = ET.fromstring(result)[0].text
    await ctx.send(response)

@bot.command(name='massping', help='Mass ping someone')
async def massping(ctx, count, *args):
    valid = False
    for role in ctx.author.roles:
        if role.name == "moto moto":
            valid = True
    if not valid:
        await ctx.send("Nope")
        return
    txt = ""
    for x in args:
        txt = txt + " " + x
    response = txt
    for x in range(0, int(count)):
        await ctx.send(response)

@bot.command(pass_context = True)
async def clear(ctx, number):
    mgs = []
    number = int(number) + 1
    async for message in ctx.message.channel.history(limit=number):
        mgs.append(message)
    await ctx.message.channel.delete_messages(mgs)
    
bot.run(secrets["token"])
