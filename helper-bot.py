import discord
import asyncio
client = discord.Client()
DEFAULT_MESSAGE = "is Toasty down? When a bot admin comes by, they can restart the bot."
@client.event
async def on_ready():
    print("Bot working.")
    print(client.user.name + "#" + client.user.discriminator)
    print(client.user.id)
    print("------")
enabled = True
message = DEFAULT_MESSAGE
@client.event
async def on_message(message):
    global enabled
    global message
    lowercase = message.content.lower()
    if discord.utils.find(lambda r: r.name == "Helpers", message.server.roles) in message.author.roles or message.author.server_permissions.administrator or message.channel.id == "208674478773895168":
    	if lowercase == "%message":
            await client.send_message(message.channel, message.author.mention + ", what should I change my message to? (type `cancel` to cancel or `reset` to reset to the standard message.")
            m = await client.wait_for_message(channel=message.channel, author=message.author)
            if m is None:
                return await client.send_message(message.channel, "Something went wrong. Canceling.")
            if m.content == "cancel":
                return await client.send_message(message.channel, "Canceling.")
            if m.content == "reset":
                message = DEFAULT_MESSAGE
                return await client.send_message(message.channel, "Message reset to `{}`".format(DEFAULT_MESSAGE))
            message = m.content
	    if lowercase == "%enable":
	        enabled = True
	        return await client.send_message(message.channel, "Message enabled.")
	    if lowercase == "%disabled":
	        enabled = False
	        return await client.send_message(message.channel, "Message disabled.")
    if enabled and ("toasty" in lowercase or "bot" in lowercase) and ("down" in lowercase or "not working" in lowercase or "dead" in lowercase or "offline" in lowercase) and message.author != client.user and message.channel.id == "303203727362490368":
        await client.send_message(message.channel, message.author.mention + ", " + message)
while True:
    try:
        client.loop.run_until_complete(client.start("Bot Token"))
    except Exception as e:
        print("Error: {}. Reconnecting.".format(str(type(e))))
    except BaseException as f:
        print("Exiting: " + str(type(f)))
        client.loop.run_until_complete(client.logout())
        exit()
