import discord as d

def runDD():
    client = d.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    
        if message.content.startswith('$Shastabot'):
            await message.channel.send('Hello!')
            
    client.run(str(input()))