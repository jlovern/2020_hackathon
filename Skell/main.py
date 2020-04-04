import configparser
import discord as d
from random import choice
import noise
import pillow
from scipy.misc import toimage
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
        

def generate():
    """Generate a side-view of mountains from perlin noise."""
    shape = (1024,1024)
    scale = 100.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0
    
    world = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=1024, 
                                        repeaty=1024, 
                                        base=0)
    toimage(world).save("img1.png","PNG")

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
            if message.content == "$shastabot fact get":
                await message.channel.send("Did you know: "+GetShastaFact())
            elif message.content.startswith("$shastabot fact add"):
                AddShastaFact(message.content[18:])
                await message.channel.send("Fact added: "+message.content[18:])
            elif message.content == "$shastabot test":
                await message.channel.send(config["DISCORD"]["test_phrase"])
            elif message.content == "$shastabot generate":
                generate()
                await message.channel.send(file=d.File("img1.PNG"))
            else:
                out = textAdventure.readCommand(message.content[10:])
                for line in out:
                    await message.channel.send(line)
    client.run(config["DISCORD"]["discord_token"])

if __name__=="__main__":
    runDD()
