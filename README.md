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

<p>All commands are prefaced with `$shastabot`. Known commands can be listed with `$shastabot help`</p>


####FAQ

<p>Q: Why does `generate` only ever show one mountain<p>
<p>A: Other mountains were not in the scope of this project.</p>
<p>Q: Why are there so few facts?</p>
<p>A: You can add additional facts yourself! I encourage you to get out there and discover something about the mountain.</p>