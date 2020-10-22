import discord
import threading
from discord.ext import commands
from main import InstaBot

TOKEN = "NzY4NzM0NTM1MjAxNTg3MjIx.X5Ex0w.wwd5IauiyJQ8k4YQMlTQSAtggm8"

bot = commands.Bot(command_prefix="$")


# =============== NORMAL FUNCS ====================
def start_insta_bot():
		try: 
			insta_bot.start()
		except:
			if runBot:
				insta_bot.stop()
				start_insta_bot()
			else: return

@bot.event
async def on_ready():
	print(f"{bot.user.name} connected to discord!")


# =============== BOT COMMANDS ====================

@bot.command(name="insta_config")
async def insta_config(ctx, user, pasw, tag):
	global acc_info
	acc_info = (user,pasw,tag)
	await ctx.send(f"Bot configured on {user} with #{tag}.")

@bot.command(name="start")
async def start(ctx):
	global insta_bot
	global runBot
	global selenium_thread
	runBot = True
	insta_bot = InstaBot("chromedriver.exe", acc_info[0], acc_info[1], acc_info[2])
	selenium_thread = threading.Thread(target=start_insta_bot)
	await ctx.send(f"Bot started on {acc_info[0]}")
	selenium_thread.start()


@bot.command(name="stop")
async def stop(ctx):
	global runBot
	insta_bot.stop()
	runBot = False
	await ctx.send(f"Bot stopped")


bot.run(TOKEN)