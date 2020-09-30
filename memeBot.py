import random
import praw
import discord
from discord.ext import commands
import os



reddit = praw.Reddit(client_id=os.environ.get("client_id"),
                     client_secret=os.environ.get("client_secret"),
                     username=os.environ.get("user"),
                     password=os.environ.get("pass"),
                     user_agent='redditApi')


colors = [
    0x7F0000,
    0x535900,
    0x40D9FF,
    0x8C7399,
    0xD97B6C,
    0xF2FF40,
    0x8FB6BF,
    0x502D59,
    0x66504D,
    0x89B359,
    0x00AAFF,
    0xD600E6,
    0x401100,
    0x44FF00,
    0x1A2B33,
    0xFF00AA,
    0xFF8C40,
    0x17330D,
    0x0066BF,
    0x33001B,
    0xB39886,
    0xBFFFD0,
    0x163A59,
    0x8C235B,
    0x8C5E00,
    0x00733D,
    0x000C59,
    0xFFBFD9,
    0x4C3300,
    0x36D98D,
    0x3D3DF2,
    0x590018,
    0xF2C200,
    0x264D40,
    0xC8BFFF,
    0xF23D6D,
    0xD9C36C,
    0x2DB3AA,
    0xB380FF,
    0xFF0022,
    0x333226,
    0x005C73,
    0x7C29A6
]

info_bot='created by <@562541986595340289>\nlanguage: python\napi: <https://www.reddit.com/dev/api/>\nsource code: <https://github.com/iamabdh/memeBot>'

def meme_selector():

        meme_sub,memes_sub, ProgrammerHumor_sub, Memes_Of_The_Dank_sub, dankmemes_sub, CollegeMemes_sub, programmingmemes_sub, codinghumor_sub, ProgrammingJokes_sub, MemeEconomy_sub   =  reddit.subreddit("meme").random(), reddit.subreddit("memes").random(), \
                                                                                                                                                                              reddit.subreddit("ProgrammerHumor").random(), reddit.subreddit("Memes_Of_The_Dank").random(), \
                                                                                                                                                                              reddit.subreddit("dankmemes").random(), reddit.subreddit("CollegeMemes").random(),\
                                                                                                                                                                              reddit.subreddit("programmingmemes").random(), reddit.subreddit("codinghumor").random(), \
                                                                                                                                                                              reddit.subreddit("ProgrammingJokes").random(), reddit.subreddit("MemeEconomy").random()



        subreddit_meme = {f'{meme_sub.title}': meme_sub.url, f'{memes_sub.title}': memes_sub.url,
                          f'{ProgrammerHumor_sub.title}': ProgrammerHumor_sub.url, f'{Memes_Of_The_Dank_sub.title}': Memes_Of_The_Dank_sub.url,
                          f'{dankmemes_sub.title}':dankmemes_sub.url, f'{CollegeMemes_sub.title}':CollegeMemes_sub.url,
                          f'{programmingmemes_sub.title}':programmingmemes_sub.url, f'{codinghumor_sub.title}': codinghumor_sub.url,
                          f'{ProgrammingJokes_sub.title}':ProgrammingJokes_sub.url, f'{MemeEconomy_sub.title}':MemeEconomy_sub.url}

        memesmix={}
        for title, url in subreddit_meme.items():
            ext = url.split('.')[-1]
            if ext == 'jpg':
                    memesmix[f'{title}'] = url
            elif ext == 'png':
                    memesmix[f'{title}'] = url
            elif ext == 'gif':
                    memesmix[f'{title}'] = url
            else:
                    continue


        title, url = random.choice(list(memesmix.items()))

        return title, url


bot = commands.Bot(command_prefix='')

@bot.command()
async def memebro(ctx):
        title_sub, url =meme_selector()
        embed= discord.Embed(title = title_sub, color=random.choice(colors))
        embed.set_image(url = url)
        await ctx.send(embed=embed)

@bot.command()
async def meme_bot(ctx):
    embed = discord.Embed(description= info_bot, color=random.choice(colors))
    await ctx.send(embed=embed)

bot.run(os.environ.get("token"))



