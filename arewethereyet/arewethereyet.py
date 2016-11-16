import discord
import os
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import fileIO

class AreWeThereYet:
    """My custom cog checks stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/arewethereyet/settings.json", 'load')
        
    def save_settings(self):
        fileIO('data/arewethereyet/settings.json', 'save', self.settings)
        
    @commands.command(name = "nano")
    async def nano(self):
        """This does stuff!"""
        await self.bot.say("もえです！ https://media.giphy.com/media/XP6YS7xG77CI8/giphy.gif")
    
    @commands.command(name = "xile")
    async def xile(self):
        """This does stuff!"""
        await self.bot.say("Xile sucks! PYON http://i.imgur.com/BfQtBXj.jpg")
        
    @commands.command(name = "xiletsuntsun")
    async def xiletsuntsun(self):
        """This does stuff!"""
        await self.bot.say("http://i.imgur.com/B3x6n2p.png")
        
    @commands.command(name = "banjosmad")
    async def banjosmad(self):
        """This does stuff!"""
        await self.bot.say("http://i.imgur.com/jUM6wH4.png")
        
    @commands.command(name = "banjo")
    async def banjosmad(self):
        """This does stuff!"""
        await self.bot.say("http://giphy.com/gifs/deliverance-YkhcPoRjSNisU")
        
    @commands.command(name = "schindler")
    async def schindler(self):
        """This does stuff!"""
        await self.bot.say("http://schindlershadow.com/avatar.png")
        
    @commands.command(name = "dafor")
    async def dafor(self):
        """This does stuff!"""
        await self.bot.say("http://images6.fanpop.com/image/answers/3486000/3486533_1395102856319.13res_392_474.jpg")
        
    @commands.command(name = "dreyel")
    async def trump(self):
        """This does stuff!"""
        await self.bot.say("http://i.imgur.com/77rV2Bn.gif")
        
    @commands.command(name = "thutmose")
    async def thutmose(self):
        """This does stuff!"""
        await self.bot.say("http://img00.deviantart.net/295b/i/2010/169/f/3/commission___shiny_mew_by_senaydragon.png")
        
    @commands.command(name = "dubbbz")
    async def dubbbz(self):
        """This does stuff!"""
        await self.bot.say("http://i.imgur.com/IcTWt4T.png")
        
    @commands.command(name = "zasshu")
    async def zasshu(self):
        """This does stuff!"""
        await self.bot.say("https://uploads.disquscdn.com/images/8fdf314a1692f107639b972e24c789d8ff0674a8b3ee6f77313b1d79b4fdcb84.jpg")
        
    @commands.command(name = "fair")
    async def fair(self):
        """This does stuff!"""
        await self.bot.say("http://pm1.narvii.com/5778/9cebf242160e7f6a8def15184205f2545dc98aeb_hq.jpg")
        
    @commands.command(name = "politics")
    async def politics(self):
        """This does stuff!"""
        await self.bot.say("`Everybody complains about politicians. Everybody says they suck. Well, where do people think these politicians come from? They don't fall out of the sky. They don't pass through a membrane from another reality. They come from American parents and American families, American homes, American schools, American churches, American businesses and American universities, and they are elected by American citizens. This is the best we can do folks. This is what we have to offer. It's what our system produces: Garbage in, garbage out. If you have selfish, ignorant citizens, you're going to get selfish, ignorant leaders. Term limits ain't going to do any good; you're just going to end up with a brand new bunch of selfish, ignorant Americans. So, maybe, maybe, maybe, it's not the politicians who suck. Maybe something else sucks around here... like, the public. Yeah, the public sucks. There's a nice campaign slogan for somebody: 'The Public Sucks. Fuck Hope’`")

    @commands.command(name = "isfinalmapup")
    async def isfinalmapup(self):
        """Is the final map up?"""

        isup = getSetting(self, "FINALMAP")
        
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
        
    @commands.command(name = "isspongeworking")
    async def isspongeworking(self):
        """Is the sponge working?"""

        isup = getSetting(self, "SPONGE")
        
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