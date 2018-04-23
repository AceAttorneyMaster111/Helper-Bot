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
main_message = DEFAULT_MESSAGE
@client.event
async def on_message(message):
    global enabled
    global main_message
    lowercase = message.content.lower()
    if discord.utils.find(lambda r: r.name == "Helpers", message.server.roles) in message.author.roles or message.author.server_permissions.administrator or message.channel.id == "208674478773895168":
        if lowercase == "%help":
            return await client.send_message(message.channel, """When I think a user is saying that Toasty is down, I respond with a message letting them know that an admin can fix the problem when one arrives.

My other commands (only accessible to helpers and admins):
%help: Print this help message
%message: Change my message to users
%disable: Disable my main function
%enable: Enable my main function

Also, after my message is sent, I am by default disabled for five minutes.""")
        if lowercase == "%message":
            await client.send_message(message.channel, message.author.mention + ", what should I change my message to? (type `cancel` to cancel or `reset` to reset to the standard message.")
            m = await client.wait_for_message(channel=message.channel, author=message.author)
            if m is None:
                return await client.send_message(message.channel, "Something went wrong. Canceling.")
            if m.content == "cancel":
                return await client.send_message(message.channel, "Canceling.")
            if m.content == "reset":
                main_message = DEFAULT_MESSAGE
                return await client.send_message(message.channel, "Message reset to `{}`".format(DEFAULT_MESSAGE))
            main_message = m.content
        if lowercase == "%enable":
            enabled = True
            return await client.send_message(message.channel, "Message enabled.")
        if lowercase == "%disabled":
            enabled = False
            return await client.send_message(message.channel, "Message disabled.")
    if enabled and ("toasty" in lowercase or "bot" in lowercase) and ("down" in lowercase or "not working" in lowercase or "dead" in lowercase or "offline" in lowercase) and message.author != client.user and message.channel.id == "303203727362490368":
        await client.send_message(message.channel, message.author.mention + ", " + main_message)
        return await throttle()
async def throttle(time=300):
    global enabled
    enabled = False
    await asyncio.sleep(time)
    enabled = True
while True:
    try:
        client.loop.run_until_complete(client.start("Bot Token"))
    except Exception as e:
        print("Error: {}. Reconnecting.".format(str(type(e))))
    except BaseException as f:
        print("Exiting: " + str(type(f)))
        client.loop.run_until_complete(client.logout())
        exit()
