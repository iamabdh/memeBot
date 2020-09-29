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



def meme_selector():
    subreddit_meme = [reddit.subreddit("meme").random().url, reddit.subreddit("memes").random().url,
                      reddit.subreddit("Memes_Of_The_Dank").random().url,
                      reddit.subreddit("ProgrammerHumor").random().url,
                      reddit.subreddit("MemeEconomy").random().url, reddit.subreddit("programmingmemes").random().url,
                      reddit.subreddit("ProgrammingJokes").random().url, reddit.subreddit("codinghumor").random().url,
                      reddit.subreddit("dankmemes").random().url, reddit.subreddit("CollegeMemes").random().url,
                      reddit.subreddit("bestmemes").random().url, reddit.subreddit("KnowYourMeme").random().url]

    memesmix = []
    for sub in subreddit_meme:
        ext = sub.split('.')[-1]
        if ext == 'jpg':
            memesmix.append(sub)
        elif ext == 'png':
            memesmix.append(sub)
        elif ext == 'gif':
            memesmix.append(sub)
        else:
            continue
    meme=random.choice(memesmix)
    return meme

bot = commands.Bot(command_prefix='meme')

@bot.command()
async def bro(ctx):
        await ctx.send(f'{meme_selector()}')


bot.run(os.environ.get("token"))



