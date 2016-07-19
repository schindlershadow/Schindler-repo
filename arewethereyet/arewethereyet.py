import discord
import os
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO

class AreWeThereYet:
    """My custom cog checks stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = isfinalmapup)
    async def isfinalmapup(self):
        """Is the final map up?"""

        isup = getSetting("FINALMAP")
        
        if isup == "YES":
            await self.bot.say("FINAL MAP IS UP WOOT")
            
        else:
           await self.bot.say("Final map is not up ;-;")
        
    @commands.command(pass_context=True, name = "setfinalmapup")
    @checks.is_owner()
    async def setfinalmapup(self, ctx, *, name):
        """Set the state of final map YES/NO"""
        self.settings["FINALMAP"] = name
        await self.bot.say("setfinalmapup set to " + name)
        self.save_settings()
        
    @commands.command(name = isspongeworking)
    async def isspongeworking(self):
        """Is the sponge working?"""

        isup = getSetting("SPONGE")
        
        if isup == "YES":
            await self.bot.say("SPONGE IS WORKING WOOT")
            
        else:
           await self.bot.say("Sponge is not working ;-;")
        
    @commands.command(pass_context=True, name = "setspongeworking")
    @checks.is_owner()
    async def setspongeworking(self, ctx, *, name):
        """Set the state of Sponge YES/NO"""
        self.settings["SPONGE"] = name
        await self.bot.say("setspongeworking set to " + name)
        self.save_settings()

        
def getSetting(self, name):
    self.settings = fileIO("data/arewethereyet/settings.json", 'load')
    self.server_specific_setting_keys = ["FINALMAP", "SPONGE"]
        
    return self.settings[name]
        
def check_folders():
    folder = "data/arewethereyet"
    if not os.path.exists(folder):
        print("Creating " + folder + " folder...")
        os.makedirs(folder)
    
def check_files():
    default = {"FINALMAP": "NO", "SPONGE": "NO"}
    settings_path = "data/arewethereyet/settings.json"
    if not os.path.isfile(settings_path):
        print("Creating default redminecraft settings.json...")
        fileIO(settings_path, "save", default)
        
def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(AreWeThereYet(bot))