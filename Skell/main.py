import configparser
import discord as d
from random import choice

config = configparser.ConfigParser()
config.read("config.ini")

def GetShastaFact():
    out = ""
    shasta_facts = open(config['DEFAULT']['shasta_facts'],"r")
    lines = shasta_facts.readlines()
    out = choice(lines)
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
        if message.content.startswith("$shastabot "):
            print("Received message! Message is: ",message.content)
            if message.content == "$shastabot fact get":
                await message.channel.send("Did you know: "+GetShastaFact())
            elif message.content.startswith("$shastabot fact add"):
                AddShastaFact(message.content[18:])
                await message.channel.send("Fact added: "+message.content[18:])
            elif message.content == "$shastabot test":
                await message.channel.send(config["DISCORD"]["test_phrase"])
            elif message.content == "$shastabot generate":
                await message.channel.send(file=d.File("MtShasta_aerial1.png"))
            else:
               await message.channel.send("Error: Command unknown")
    client.run(config["DISCORD"]["discord_token"])

if __name__=="__main__":
    runDD()
