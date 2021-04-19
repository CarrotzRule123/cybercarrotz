from classroom import Classroom
from timetable import Timetable
from discord.ext import commands

newClass = Classroom()
table = Timetable()

def read_file():
    with open('../secrets.json') as f:
        return json.load(f)

secrets = read_file()
bot = commands.Bot(command_prefix='>')

@bot.command(name='say', help='says something')
async def say(ctx, *args):
    for role in ctx.author.roles:
        if role.name == "Casted out meme king":
            await ctx.send("Nope you suck")
            return
    txt = ""
    for x in args:
        txt = txt + " " + x
    response = txt
    await ctx.send(response)

@bot.command(name='hw', help='reports homework')
async def hw(ctx):
    data = newClass.main()
    await ctx.send(data)

@bot.command(name='tt', help="updates timetable")
async def tt(ctx, command, *args):
    verified = False
    for role in ctx.author.roles:
        if role.name == "Monitor" or role.name == "Helper":
            verified = True
    if not verified:
        await ctx.send("Nope you suck")
        return
    #Add CHANNEL_ID
    channel = bot.get_channel("CHANNEL_ID")
    data = ""
    if command == "update":
        data = table.update()
    elif command == "add":
        table.add(args[0], args[1], args[2], args[3])
        data = table.update()
    elif command == "parse":
        text = args[0].replace("'", '"')
        table.parse(text)
        data = table.update()
    elif command == "edit":
        table.edit(args[0], int(args[1]), args[2], args[3], args[4])
        data = table.update()
    elif command == "remove":
        table.edit(args[0], int(args[1]), args[2])
        data = table.update()
    if 'oldMsg' not in globals():
        global oldMsg
        oldMsg = await channel.send(data)
    else:
        await oldMsg.edit(content=data)
    ctx.send("Done!")

bot.run(secrets["token"])
