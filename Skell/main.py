import configparser
import discord as d
from random import randint
import textAdventure
config = configparser.ConfigParser()
config.read("config.ini")

def GetShastaFact():
    out = ""
    shasta_facts = open(config['DEFAULT']['shasta_facts'],"r")
    lines = shasta_facts.readlines()
    out = lines[randint(0,len(lines)-1)]
    shasta_facts.close()
    return out

def AddShastaFact(fact):
    with open(config['DEFAULT']['shasta_facts'],"a") as shasta_facts:
        shasta_facts.write(fact)
    
def runDD():
    client = d.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))
    
    @client.event
    async def on_message(message):
        #ignore messages from myself
        if message.author == client.user:
            return
        
        if message.content == "$Shastabot fact get":
            await message.channel.send("Did you know: "+GetShastaFact())
        elif message.content.startswith("$Shastabot fact add"):
            AddShastaFact(message.content[18:])
            await message.channel.send("Fact added: "+message.content[18:])
        elif message.content == "$Shastabot test":
            await message.channel.send(config["DISCORD"]["test_phrase"])
        elif message.content.startswith("$Shastabot "):
            out = textAdventure.readCommand(message.content[10:])
            for line in out:
                await message.channel.send(line)
    client.run(config["DISCORD"]["discord_token"])
    
if __name__ == "__main__":
    runDD()
