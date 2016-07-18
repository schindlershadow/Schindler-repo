import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO

try:
    from mcstatus import MinecraftServer
    mcstatusAvailable = True

except:
    mcstatusAvailable = False

class Redminecraft:
    """Gets information from a minecraft server!"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def xile(self):
        """This does stuff!"""
        await self.bot.say("Xile sucks!")

    @commands.command(name = "status")
    async def status(self):
        """Get server status"""

        server = getServer()
        status = server.status()
        await self.bot.say("The main Infinix server has {0} players and replied in {1} ms".format(status.players.online, status.latency))

    @commands.command(name = "latency")
    async def latency(self):
        """Get server latency"""

        server = getServer()
        latency = server.ping()
        await self.bot.say("The server replied in {0} ms".format(latency))

    @commands.command(name = "players")
    async def players(self):
        """Get server players"""

        server = getServer()
        query = server.query()
        await self.bot.say("The server has the following players online: {0}".format(", ".join(query.players.names)))

    @commands.command(pass_context=True, name = "setserver")
    @checks.is_owner()
    async def setserver(self, name: str):
        """Set the server IP/Domain"""
        self.settings["SERVER"] = name
        await self.bot.say("Server set to " + name)
        self.save_settings()

    @commands.command(pass_context=True, name = "setport")
    @checks.is_owner()
    async def setport(self, name: str):
        """Set server port if not default"""
        self.settings["PORT"] = name
        await self.bot.say("Port set to " + name)
        self.save_settings()
    
def getServer():
    self.settings = fileIO("data/redminecraft/settings.json", 'load')
    self.server_specific_setting_keys = ["SERVER", "PORT"]
    servername = self.settings["SERVER"]
    port = self.settings["PORT"]
    
    if port == 0:
        port = 25565
        
    return MinecraftServer(servername, int(port))
    
def save_settings(self):
    fileIO('data/redminecraft/settings.json', 'save', self.settings)
    
def check_folders():
    folders = ("data/redminecraft")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)
    
def check_files():
    default = {"SERVER": "8.8.8.8", "PORT": 25565}
    settings_path = "data/redminecraft/settings.json"
    if not os.path.isfile(settings_path):
        print("Creating default audio settings.json...")
        fileIO(settings_path, "save", default)

def setup(bot):
    check_folders()
    check_files()
    if mcstatusAvailable:
        bot.add_cog(Redminecraft(bot))

    else:
        raise RuntimeError("You need to run `pip install mcstatus`")