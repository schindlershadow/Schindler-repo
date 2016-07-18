import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO

try:
    from mcstatus import MinecraftServer
    mcstatusAvailable = True

except:
    mcstatusAvailable = False
    
servername = "schindlershadow.zapto.org"
port = "25565"

class Redminecraft:
    """Gets information from a minecraft server!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/redminecraft/settings.json", 'load')
        self.server_specific_setting_keys = ["SERVER", "PORT"]
        servername = self.settings["SERVER"]
        port = self.settings["PORT"]
    
        if port == "":
            port = "25565"
    
    
    @commands.command()
    async def mycom(self):
        """This does stuff!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

    @commands.command(name = "status")
    async def status(self):
        """Get server status"""

        server = MinecraftServer(servername, int(port))
        status = server.status()
        await self.bot.say("The main Infinix server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

    @commands.command(name = "latency")
    async def latency(self):
        """Get server latency"""

        server = MinecraftServer(servername, int(port))
        latency = server.ping()
        await self.bot.say("The server replied in {0} ms".format(latency))

    @commands.command(name = "players")
    async def players(self):
        """Get server players"""

        server = MinecraftServer(servername, int(port))
        query = server.query()
        await self.bot.say("The server has the following players online: {0}".format(", ".join(query.players.names)))

    @commands.command(pass_context=True, name = "setserver")
    @checks.is_owner()
    async def setserver(self, name: str):
        self.settings["SERVER"] = name
        await self.bot.say("Server set to " + name)
        self.save_settings()

    @commands.command(pass_context=True, name = "setport")
    @checks.is_owner()
    async def setport(self, name: str):
        self.settings["PORT"] = name
        await self.bot.say("Port set to " + name)
        self.save_settings()
    
def save_settings(self):
    fileIO('data/redminecraft/settings.json', 'save', self.settings)

def setup(bot):
    if mcstatusAvailable:
        bot.add_cog(redminecraft(bot))

    else:
        raise RuntimeError("You need to run `pip install mcstatus`")