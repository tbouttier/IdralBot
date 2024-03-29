# main.py
import os
import files
import time

from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='/')


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.command()
async def donner(ctx):
    user = ctx.message.author.name
    channel_id = ctx.message.channel.id
    channel = ctx.message.channel

    if channel_id == 645731571055198259 or user == 'SlyDower':
        files.write_gold(user)
        await ctx.send(f'{user} a donné 1 <:or:645726669977681920> !')
        await ctx.send(f'Il/Elle a donné  {files.get_user_gold(user)} <:or:645726669977681920> en tout.')

        new_name = f'Or récolté : {files.total_gold()}/250'
        await channel.edit(topic=new_name)

        if files.total_gold() == 250:
            time.sleep(3)
            await ctx.send(f'\nMerci à tous pour vos dons!\nJ\'ai atteint mon objectif, vous me reverrez bientôt :wink:')
            await score(ctx)
            raise SystemExit(0)

    else:
        await ctx.send(f'Je n\'accepte pas les messages privés désolé ...')

    return


async def score(ctx):
    place = 0
    for scoreline in files.get_score():
        place += 1
        await ctx.send(f'#{place} - {scoreline[0]} - {scoreline[1]} <:or:645726669977681920>')
    return


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Arrête de faire n\'importe quoi')
        return
    raise error


client.run(TOKEN)
