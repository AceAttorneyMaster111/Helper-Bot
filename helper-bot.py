import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
    print("Bot working.")
    print(client.user.name + "#" + client.user.discriminator)
    print(client.user.id)
    print("------")
@client.event
async def on_message(message):
    lowercase = message.content.lower()
    if ("toasty" in lowercase or "bot" in lowercase) and ("down" in lowercase or "not working" in lowercase or "dead" in lowercase or "offline" in lowercase) and message.author != client.user and message.channel.id == "303203727362490368":
        await client.send_message(message.channel, message.author.mention + ", is Toasty down? When a bot admin comes by, they can restart the bot.")
while True:
    try:
        client.loop.run_until_complete(client.start("Bot Token"))
    except Exception as e:
        print("Error: {}. Reconnecting.".format(str(type(e))))
    except BaseException as f:
        print("Exiting: " + str(type(f)))
        client.loop.run_until_complete(client.logout())
        exit()
