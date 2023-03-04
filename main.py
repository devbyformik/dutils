# developed by formik#0001
import json
import discord, datetime, asyncio
import re
import time, os
import random



wall = """_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
_
"""

# developed by formik#0001

configf = open('./config.json', 'r+', encoding='utf-8')
config = json.load(configf)
token = config["token"]
amount = config["amount"]
msg_path = config["message_path"]
log_messages = config["log_messages"]
log_channels = config["log_channels"]
announce = config["announce"]
clear = config["clear"]
prefix = config["prefix"]


blackcheat = False
bleed_id = 593921296224747521
blackcheat_config = config["blackcheat"]
blackcheat_words = open(blackcheat_config['words_file'], 'r') # Make sure the word list in in the same directory as the py file
blackcheat_lines = blackcheat_words.readlines()
blackcheat_version = 1.21
used = []

def blackcheat_title():
	print(f"\n\n\t\tBLACKCHEAT BY FORMIK & BENITAS\n\t\t\tVERSION\t{blackcheat_version}\n\n")


class rpc:
	name = config["rpc"]["name"]
	url = config["rpc"]["url"]




client = discord.Client()

dutils_version = "v7.13"

adin_ross = 760305693462626314

def cls():
	cmd = "cls" if os.name == "nt" else "clear"
	os.system(cmd)

@client.event
async def on_ready():
	# for dev: https://discordpy.readthedocs.io/en/stable/api.html#discord.Activity
	await client.change_presence(activity=discord.Streaming(name=rpc.name, url=rpc.url))
	print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	global log_messages, log_channels, announce, clear, prefix, blackcheat, used, blackcheat_config, blackcheat_lines, blackcheat_words, wall

	# blackcheat (start)
	if blackcheat:
		if f"{prefix}blackcheat.false" in message.content.lower() and "available commands:" not in message.content.lower():
			if clear:
				await message.delete()
			blackcheat = False		
			if announce:
				print(f"\nBlackcheat has been disabled for this session.\n")
				await message.channel.send(f"```Blackcheat has been disabled for this session.```")
		
		if blackcheat == False:
			return
		if message.author.id != bleed_id: # Check if the message is from bleed and in the current server
			return
		if len(message.embeds) == 0: # Check if the message is an embed message
			return
		if client.user.mentioned_in(message) == False: # Only try to answer if bleed actually mentions you
			return
		
		# auto join blacktea (work in progress)
		""" if len(message.embeds) != 0 and ("The game will begin in" in message.embeds[0].description or "The game will begin in" in message.embeds[0].title):	# react with :white_check_mark: 
			print(f"Found game in server\t:\t{message.channel.guild.name}")
			await message.add_reaction(discord.Emoji("white_check_mark"))
			return """

		cls()
		embedText = message.embeds[0].description
		regexSearch = re.search("Type a \*\*word\*\* containing the letters: \*\*(.{3})\*\*.", embedText) # Fetch the letters that need to be contained in the word
		if bool(regexSearch) == False or blackcheat == False:
			return
		startingLetters = regexSearch[1]
		blackcheat_title()
		print("\n\tStarting Letters Found\t:\t" + startingLetters)
		answerText = "null"
		for line in blackcheat_lines:
			if (startingLetters.lower() in line) and (line not in used) and (len(line) <= blackcheat_config["wlencap"]): # Find a word that contains the starting letters
				answerText = line
				used.append(line)
				break
		print("\tAnswer Found\t\t:\t" + answerText)
		pause = random.choice(blackcheat_config["pauses"])
		print(f"\tSleeping for realism\t:\t{pause}\tseconds")
		time.sleep(pause)
		await message.channel.send(answerText) # Send the answer in chat
	# blackcheat (end)


	if message.author != client.user:
		return
	#cls()


	
	if f"{prefix}term" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		exit()
		return
	elif f"{prefix}wall" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		for i in range(amount):
			try:
				await message.channel.send(wall)
			except:
				exit()
		return
	elif f"{prefix}spam" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		spam_msg = open(msg_path, 'r').read()
		for i in range(amount):
			try:
				await message.channel.send(spam_msg)
			except:
				exit()
		return
	elif f"{prefix}cls" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.purge(limit=200, check=lambda msg: msg.author == message.author)
		if message.guild.id == adin_ross:
			await message.channel.send("scam")
		return
	elif f"{prefix}help" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		msg = f"""```
					Available Commands:
					``````
					{prefix}help -> Prints this menu

					{prefix}wall -> Spams walls to the text channel

					{prefix}spam -> Spams the provided message to the text channel

					{prefix}term -> Terminate the current process

					{prefix}cls -> Purges user messages (Only works in Regular Text Channels)

					{prefix}log.start -> Enable the message logger

					{prefix}log.stop -> Disable the message logger

					{prefix}log.add -> Add the current channel to the message logger target list 

					{prefix}log.remove -> Remove the current channel from the message logger target list

					{prefix}clear.true -> Enable Clear setting
					
					{prefix}clear.false -> Disable Clear setting

					{prefix}announce.true -> Enable Announce setting
					
					{prefix}announce.false -> Disable Announce setting

					{prefix}prefix.set -> Set new prefix

					{prefix}console.cls -> Clear the console

					{prefix}blackcheat.true -> Enable blackcheat (Blacktea Cheat)

					{prefix}blackcheat.false -> Disable blackcheat (Blacktea Cheat)

					{prefix}credit -> Display credit
					
					{prefix}verion -> Display version
					
					{prefix}info -> Display all information about dutils
					
					{prefix}patch -> Patch notes
					```"""
		print(msg)
		await message.channel.send(msg)
		return
	elif f"{prefix}info" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.send(f"""```
					dutils Info:
					``` ```
					Current Version: {dutils_version}
					Developer: formik#0001
					```""")
		return
	elif f"{prefix}patch" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		msg = f"""```
					dutils Patch Notes:
					``````
					Current Version: {dutils_version}
					Developer: formik#0001

					- bug fixes
					
					- new experimental feature: Custom Streaming RPC

					- integrated blackcheat (Blacktea Cheat) by formik
						- blackcheat.true
						- blackcheat.false

					- fixed spam command
					```"""
		print(msg)
		await message.channel.send(msg)
		return
	elif f"{prefix}version" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.send(f"""```
					Current dutils Version: {dutils_version}```""")
		return
	elif f"{prefix}credit" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.send("""```
					dutils (Discord Utilities)
					developed by formik#0001
		```""")
		return
	elif f"{prefix}log.start" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print("\nMessage Logger has been enabled for this session.\n")
		log_messages = True
		log_channels.append(message.channel.id)
		if announce:
			await message.channel.send("```Message Logger has been enabled for this session.```")
		return
	elif f"{prefix}log.stop" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print("\nMessage Logger has been disabled for this session.\n")
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		if announce:
			await message.channel.send("```Message Logger has been disabled for this session.```")
		return
	elif f"{prefix}log.add" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(f"\nMessage Logger has been enabled for channel '{message.channel.name}' ({message.channel.id}) in guild '{message.guild.name}' ({message.guild.id}) for this session.\n")
		log_messages = True
		log_channels.append(message.channel.id)
		if announce:
			await message.channel.send("```Message Logger has been enabled for this channel for this session.```")
		return
	elif f"{prefix}log.remove" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		print(f"\nMessage Logger has been disabled for channel '{message.channel.name}' ({message.channel.id}) in guild '{message.guild.name}' ({message.guild.id}) for this session.\n")
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		
		if announce:
			await message.channel.send("```Message Logger has been disabled for this channel for this session.```")
		return
	elif f"{prefix}clear.true" in message.content.lower() and "available commands:" not in message.content.lower():
		clear = True
		if clear:
			await message.delete()
		print("\nClear has been enabled for this session.\n")
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		if announce:
			await message.channel.send("```Clear has been enabled for this session.```")
		return
	elif f"{prefix}clear.false" in message.content.lower() and "available commands:" not in message.content.lower():
		clear = False
		if clear:
			await message.delete()
		print("\nClear has been disabled for this session.\n")
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		if announce:
			await message.channel.send("```Clear has been disabled for this session.```")
		return
	elif f"{prefix}announce.true" in message.content.lower() and "available commands:" not in message.content.lower():
		announce = True
		if clear:
			await message.delete()
		print("\nAnnounce has been enabled for this session.\n")
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		if announce:
			await message.channel.send("```Announce has been enabled for this session.```")
		return
	elif f"{prefix}announce.false" in message.content.lower() and "available commands:" not in message.content.lower():
		announce = False
		if clear:
			await message.delete()
		print("\nAnnounce has been disabled for this session.\n")
		log_messages = False
		log_channels_new = []
		for channel in log_channels:
			if channel != message.channel.id:
				log_channels_new.append(channel)
		
		log_channels = log_channels_new
		if announce:
			await message.channel.send("```Announce has been disabled for this session.```")
		return
	elif f"{prefix}prefix.set" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		argv = message.content.lower().split(" ")
		if len(argv) == 1:
			pass
		else:
			new = argv[1]
			prefix = new
			print(f"\nPrefix has been set to '{new}' for this session.\n")
			if announce:
				await message.channel.send(f"```Prefix has been set to '{prefix}' for this session.```")
	elif f"{prefix}console.cls" in message.content.lower() and "available commands:" not in message.content.lower():
		cls()
		if clear:
			await message.delete()
		print(f"\nConsole has been cleared.\n")
	elif f"{prefix}blackcheat.true" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		blackcheat = True
		if announce:
			print(f"\nBlackcheat has been enabled for this session.\n")
			await message.channel.send(f"```Blackcheat has been enabled for this session.```")
		
	elif f"{prefix}blackcheat.false" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		blackcheat = False		
		if announce:
			print(f"\nBlackcheat has been disabled for this session.\n")
			await message.channel.send(f"```Blackcheat has been disabled for this session.```")
	else:
		return

@client.event
async def on_message_delete(message):
	if (log_messages == True) and (message.channel.id in log_channels):
		print(f"""

		============================================================================================================================================
		
		Deleted message by {message.author.name}#{message.author.discriminator} at {datetime.datetime.now()}
		Server  :  {message.guild.name}\t\t\t({message.guild.id})
		Channel :  {message.channel.name}\t\t\t({message.channel.id})
		Message :  {message.content}

		============================================================================================================================================
		
		""")

if config["looped_client"]:
	while True:
		try:
			cls()

			print(f"""

					dutils {dutils_version}
					developed by formik#0001

			> Type {prefix}help in a text channel to get started.

			""")


			client.run(token)
		except Exception as e:
			continue
		else:
			continue
else:
	cls()

	print(f"""

			dutils {dutils_version}
			developed by formik#0001

	> Type {prefix}help in a text channel to get started.

	""")


	client.run(token)








