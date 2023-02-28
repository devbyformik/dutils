# developed by formik#0001
import json
import discord, datetime
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

class rpc:
	name = config["rpc"]["name"]
	url = config["rpc"]["url"]


msg = open(msg_path, 'r').read()

client = discord.Client()

dutils_version = "v6.40"

adin_ross = 760305693462626314

def cls():
	cmd = "cls" if os.name=="nt" else "clear"
	os.system(cmd)

@client.event
async def on_ready():
	# for dev: https://discordpy.readthedocs.io/en/stable/api.html#discord.Activity
	await client.change_presence(activity=discord.Streaming(name=rpc.name, url=rpc.url))
	print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
	global log_messages, log_channels, announce, clear, prefix
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
		for i in range(amount):
			try:
				await message.channel.send(msg)
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
					``` ```
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
					Dutils Info:
					``` ```
					Current Version: {dutils_version}
					Developer: formik#0001
					```""")
		return
	elif f"{prefix}patch" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		msg = f"""```
					Dutils Patch Notes:
					``` ```
					Current Version: {dutils_version}
					Developer: formik#0001

					- bug fixes

					- new config options: "announce" , "clear" , "log_messages" , "log_channels" , "prefix"
						- announce: announce program events in text channel
						- clear: clear command calls
						- log_messages: log messages from the specified channels
						- log_channels: channels to log messages from
						- prefix

					- new commands: "announce.false" , "announce.true" , "clear.true", "clear.false", "log.add" , "log.remove" , "console.cls"
						- announce.false: disable announcements for the current session
						- announce.true: enable announcements for the current session
						- clear.false: disable clear option
						- clear.true: enable clear option
						- log.add: add current channel to log target
						- log.remove: remove current channel from log target
						- prefix.set: set prefix
						- console.cls: clear the console
					
					- new experimental feature: Custom Streaming RPC
					```"""
		print(msg)
		await message.channel.send(msg)
		return
	elif f"{prefix}version" in message.content.lower() and "available commands:" not in message.content.lower():
		if clear:
			await message.delete()
		await message.channel.send(f"""```
					Current Dutils Version: {dutils_version}```""")
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
		if clear:
			await message.delete()
		cls()
		print(f"\nConsole has been cleared.\n")
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

cls()

print(f"""

		Dutils {dutils_version}
		developed by formik#0001

> Type {prefix}help in a text channel to get started.

""")


client.run(token)









