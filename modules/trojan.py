from geovpn import *

#MEMBER TROJAN
@bot.on(events.NewMessage(pattern=r"(?:.memtr|memtr|/memtr|/memtr@geo_vpn_bot|.memtr@geo_vpn_bot|memtr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'mem-trojan'))
async def memtr(event):
	async def memtr_(event):
		cmd = 'bot-mem-tr'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""
{z}
**Shows Users Trojan**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await memtr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)
		
#CREATE TROJAN
@bot.on(events.NewMessage(pattern=r"(?:.addtr|/addtr|addtr|/addtr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'create-trojan'))
async def addtr(event):
	async def addtr_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Quota:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**» Expired (Hari) :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		async with bot.conversation(chat) as pw2:
			await event.respond("**» Limit User (IP) :**")
			pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw2 = (await pw2).raw_text
		async with bot.conversation(chat) as bug:
			await event.respond("**» INPUT BUG HOST :**")
			bug = bug.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			bug = (await bug).raw_text
		cmd = f'printf "%s\n" "{user}" "{exp}" "{pw}" "{pw2}" "{bug}" | bot-addtr'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(exp))
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
•━━━━━━━━━━━━•
**• Xray/Trojan Account •**
•━━━━━━━━━━━━•
**» `Remarks      :`** {user}
**» `User Quota   :`** {pw} GB
**» `User IP      :`** {pw2} IP
**» `port TLS     :`** 443
**» `Port NTLS    :`** 80
**» `Port GRPC    :`** 443
**» `User ID      :`** {uuid}
**» `AlterId      :`** 0
**» `Security     :`** auto
**» `NetWork      :`** (WS) or (gRPC)
**» `Path TLS     :`** Bebas/trojan
**» `Path NLS     :`** Bebas/trojan
**» `Path Dynamic :`** http://BUG.COM
**» `ServiceName  :`** trojan-grpc
•━━━━━━━━━━━━•
**» Link WS TLS   : ** `{b[0]}`
•━━━━━━━━━━━━•
**» Link WS None TLS   :** `{b[1].replace(" ","")}`
•━━━━━━━━━━━━•
**» Link GRPC  :** `{b[2].replace(" ","")}`
•━━━━━━━━━━━━•
**» Format Openclash  :** https://{DOMAIN}:81/trojan-{user}.html
•━━━━━━━━━━━━•
**🗓️ Expired Until:** `{later}`
**🤖@sampiiiiu**
•━━━━━━━━━━━━•
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await addtr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)

#CEK TROJAN
@bot.on(events.NewMessage(pattern=r"(?:.cektr|/cektr|cektr|/cektr@geo_vpn_bot)$"))
async def cektr(event):
	async def cektr_(event):
		cmd = 'bot-cektr'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.respond(f"""
```{z}```
**Shows Logged Trojan**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cektr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)
		
#TRIAL TROJAN
@bot.on(events.NewMessage(pattern=r"(?:.trialtr|/trialtr|trialtr|/trialtr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'trial-trojan'))
async def trialtr(event):
	async def trialtr_(event):


		cmd = f'printf "%s\n" "trial`</dev/urandom tr -dc X-Z0-9 | head -c4`" "1" "2" | bot-trialtr'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**User Already Exist**")
		else:
			today = DT.date.today()
			later = today + DT.timedelta(days=int(1))
			b = [x.group() for x in re.finditer("trojan://(.*)",a)]
			print(b)
			remarks = re.search("#(.*)",b[0]).group(1)
			domain = re.search("@(.*?):",b[0]).group(1)
			uuid = re.search("trojan://(.*?)@",b[0]).group(1)
			msg = f"""
•━━━━━━━━━━━━•
**• Xray/Trojan Account •**
•━━━━━━━━━━━━•
**» `Remarks      :`** `{remarks}`
**» `User Quota   :`** `1 GB`
**» `port TLS     :`** `443`
**» `Port NTLS    :`** `80`
**» `Port GRPC    :`** `443`
**» `User ID      :`** `{uuid}`
**» `AlterId      :`** `0`
**» `Security     :`** `auto`
**» `NetWork      :`** `(WS) or (gRPC)`
**» `Path TLS     :`** `Bebas/trojan`
**» `Path NLS     :`** `Bebas/trojan`
**» `Path Dynamic :`** `http://BUG.COM`
**» `ServiceName  :`** `trojan-grpc`
•━━━━━━━━━━━━•
**» Link TLS   : **
`{b[0]}`
•━━━━━━━━━━━━•
**» Link GRPC  :** 
`{b[1].replace(" ","")}`
•━━━━━━━━━━━━•
**🗓️ Expired Until:** `{later}`
**🤖 @sampiiiiu**
•━━━━━━━━━━━━•
"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trialtr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)

#RENEW
@bot.on(events.NewMessage(pattern=r"(?:.renewtr|/renewtr|renewtr|/renewtr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'renew-trojan'))
async def renewtr(event):
	async def renewtr_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/.trojan.db | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.respond(f"""
**⚡ LIST RENEW USER**
{z}
**👉 Select Your Number :**
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**» Expired (Hari) :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		async with bot.conversation(chat) as pw2:
			await event.respond("**» Limit User (GB) :**")
			pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw2 = (await pw2).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**» Limit User (IP) :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		cmd = f'printf "%s\n" "3" "{user}" "{exp}" "{pw2}" "{pw}" | m-trojan | sleep 3 | exit'
		subprocess.check_output(cmd, shell=True)
		await event.respond(f"""
**» Successfully Renewed ✅**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renewtr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)

#LIMIT
@bot.on(events.NewMessage(pattern=r"(?:.limittr|/limittr|limittr|/limittr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'limit-trojan'))
async def limittr(event):
	async def limittr_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/.trojan.db | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.respond(f"""
**⚡ CHANGE LIMIT USER**
{z}
**👉 Select Your Number :**
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**» Limit User (IP) or 0 Unlimited :**")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**» Limit User (GB) or 0 Unlimited :**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		cmd = f'printf "%s\n" "6" "{user}" "{exp}" "{pw}" | m-trojan | sleep 3 | exit'
		subprocess.check_output(cmd, shell=True)
		await event.respond(f"""
**» Successfully Change ✅**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limittr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)

#delete
@bot.on(events.NewMessage(pattern=r"(?:.deltr|/deltr|deltr|/deltr@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'delete-trojan'))
async def deltr(event):
	async def deltr_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/.trojan.db | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.respond(f"""
**⚡ LIST DELETE USER**
{z}
**👉 Select Your Number :**
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		cmd = f'printf "%s\n" "2" "{user}" | m-trojan | sleep 3 | exit'
		subprocess.check_output(cmd, shell=True)
		await event.respond(f"""
**» Successfully Deleted ✅**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await deltr_(event)
	else:
		await event.answer("Pinjem Dulu Seratus",alert=True)

@bot.on(events.NewMessage(pattern=r"(?:.trojan|/trojan|trojan|/trojan@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'trojan'))
async def start(event):
	inline = [
[Button.inline(" ᴛʀɪᴀʟ ","trial-trojan")],
[Button.inline(" ᴄʀᴇᴀᴛᴇ ","create-trojan"),
Button.inline(" ᴄʜᴇᴄᴋ ","cek-tr"),
Button.inline(" ᴅᴇʟᴇᴛᴇ ","delete-trojan")],
[Button.inline(" ʀᴇɴᴇᴡ ","renew-trojan"),
Button.inline(" ᴍᴇᴍʙᴇʀ ","mem-trojan"),
Button.inline(" ʟɪᴍɪᴛ ","limit-trojan")],
[Button.inline("🔙ᴍᴀɪɴ ᴍᴇɴᴜ","menu")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Pinjem Dulu Seratus", alert=True)
		except:
			await event.reply("Pinjem Dulu Seratus")
	elif val == "true":
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		sh = f' cat /etc/ssh/.ssh.db | grep "###" | wc -l'
		ssh = subprocess.check_output(sh, shell=True).decode("ascii")
		vm = f' cat /etc/vmess/.vmess.db | grep "###" | wc -l'
		vms = subprocess.check_output(vm, shell=True).decode("ascii")
		vl = f' cat /etc/vless/.vless.db | grep "###" | wc -l'
		vls = subprocess.check_output(vl, shell=True).decode("ascii")
		tr = f' cat /etc/trojan/.trojan.db | grep "###" | wc -l'
		trj = subprocess.check_output(tr, shell=True).decode("ascii")
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -s ipv4.icanhazip.com"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")
		iisp = f" cat /etc/xray/isp"
		iisp = subprocess.check_output(citsy, shell=True).decode("ascii")

		msg = f"""
•━━━━━━━━━━━━•
**❖ ᴛʀᴏᴊᴀɴ ᴍᴀɴᴀɢᴇʀ ❖**
•━━━━━━━━━━━━•
**🔹 ꜱᴇʀᴠɪᴄᴇ:** `ᴛʀᴏᴊᴀɴ`
**🔹 ʜᴏꜱᴛɴᴀᴍᴇ/ɪᴘ :** `{DOMAIN}`
**🔹 ɪꜱᴘ:** `{z["isp"]}`
**🔹 ᴄᴏᴜɴᴛʀʏ :** `{city.strip()}`
**🔹 ᴛʀᴏᴊᴀɴ ᴀᴄᴄᴏᴜɴᴛ :** `{trj.strip()}`
•━━━━━━━━━━━━•
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)
