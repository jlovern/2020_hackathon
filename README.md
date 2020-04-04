<!doctype html>
<p>If you'd simply like to check out the features of the code, the bot will be 
live at <a href="https://discord.gg/dxBYxtp">this discord server</a> until 4/15/2020.</p>
<p>If you'd like to run it yourself, you'll need access to a discord bot account and a discord server.</p>

<h6>Instructions for running it yourself:</h6>
<p> run `pip install -r requirements.txt` to get all the requirements for this file.</p>
<p> Edit `Skell/config.ini` to include your own discord bot token. If you don't have one of those, 
you'll need to generate one via the <a href="https://discordapp.com/developers/docs/intro">discord developer portal.</a></p>
<p> Connect the bot to a server or your account.</p>
<p>Run the bot from the `Skell` directory with `python main.py`.</p>

<p> At the moment, the only commands that are runnable are `$shastabot test`, `$shastabot fact get`, `$shastabot fact add {fact}`, and `$shastabot generate`.</p>


<p>Thanks for taking a look at this file. Here's how to run it:</p>
<p>First, make sure you have a <a href="https://discordpy.readthedocs.io/en/latest/discord.html">discord bot account</a>. 
   In order to interact with this program, it must be added to a discord server.
   There is an implementation currently running on <a href="https://discord.gg/dxBYxtp">this discord server</a>. 
   It is running on my home linux server, and both the server and the bot will be deleted on 4/15/2020, unless someone asks for an extension.</p>

####Configuration
<p>Do `pip -r Skell/requirements.txt` before anything else
<p>Configuration settings are in `Skell/config.ini`. As of yet, here are such settings:</p>
<ul>
    <li>Default:
        <ul>
            <li>`shasta_facts`: The location of the file containing facts about Mt. Shasta.</li>
        </ul></li>
    <li>Discord:
        <ul>
            <li>`discord_token`: The unique identifier for your discord bot.</li>
            <li>`test_phrase`: The response sent when the command `$Shastabot test` is issued.</li>
        </ul></li>
</ul>
<p>

####Discord commands



####FAQ

<p>Q: Why does `generate` only ever show one mountain<p>
<p>A: Other mountains were not in the scope of this project.</p>
<p>Q: Why are there so few facts?</p>
<p>A: You can add additional facts yourself! I encourage you to get out there and discover something about the mountain.</p>