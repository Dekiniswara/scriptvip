from geovpn import *
#CEK VMESS
@bot.on(events.NewMessage(pattern=r"(?:info|/info|/info@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'info'))
async def info_vps(event):
	async def info_vps_(event):
		cmd = 'bot-vps-info'.strip()
		await event.edit("Processing.")
		await event.edit("Processing..")
		await event.edit("Processing...")
		await event.edit("Processing....")
		time.sleep(0)
		await event.edit("**😁**")
		
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""```{z}```
""",buttons=[[Button.inline("‹ 🔙ᴍᴀɪɴ ᴍᴇɴᴜ ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await info_vps_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)
