from geovpn import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|menu|/menu|/menu@geo_vpn_bot|.menu@geo_vpn_bot|menu@geo_vpn_bot)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline("ꜱꜱʜ ᴍᴇɴᴜ","ssh")],
[Button.inline("ᴠᴍᴇꜱꜱ ᴍᴇɴᴜ","vmess"),
Button.inline("ᴠʟᴇꜱꜱ ᴍᴇɴᴜ","vless")],
[Button.inline("ᴛʀᴏᴊᴀɴ ᴍᴇɴᴜ","trojan")],
[Button.inline("ᴠᴘꜱ ɪɴꜰᴏ","info"),
Button.inline("ꜱᴇᴛᴛɪɴɢ","setting")],
[Button.url("ᴛᴇꜱᴛɪ","https://t.me/testikuy_mang"),
Button.url("ᴏʀᴅᴇʀ","https://t.me/sampiiiiu")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Pinjem Dulu Seratus", alert=True)
		except:
			await event.reply("Pinjem Dulu Seratus")
	elif val == "true":
		sh = f' cat /etc/ssh/.ssh.db | grep "#ssh#" | wc -l'
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

		msg = f"""
•━━━━━━━━━━━━•
**❖ ᴀᴅᴍɪɴ ᴘᴀɴᴇʟ ᴍᴇɴᴜ ❖**
•━━━━━━━━━━━━•
**🔹ᴏꜱ           :** `{namaos.strip().replace('"','')}`
**🔹ᴄɪᴛʏ         :** `{city.strip()}`
**🔹ᴅᴏᴍᴀɪɴ  :** `{DOMAIN}`
**🔹ɪᴘ ᴠᴘꜱ     :** `{ipsaya.strip()}`
**🔹ᴠᴇʀꜱɪᴏɴ  :** `v3.1`
**🔹ᴀᴅᴍɪɴ    :** @sampiiiiu
**🔹ʙᴏᴛ ʙʏ ɢᴇᴏ ᴘʀᴏᴊᴇᴄᴛ **
•━━━━━━━━━━━━•
•━━━━━━━━━━━━•
**❖ ᴀᴄᴄᴏᴜɴᴛ ᴄʀᴇᴀᴛᴇᴅ ❖** 
•━━━━━━━━━━━━•
**🔹ꜱꜱʜ ᴏᴠᴘɴ       `:**{ssh.strip()}` __account__
**🔹xʀᴀʏ ᴠᴍᴇꜱꜱ  `:**{vms.strip()}` __account__
**🔹xʀᴀʏ ᴠʟᴇꜱꜱ    `:**{vls.strip()}` __account__
**🔹xʀᴀʏ ᴛʀᴏᴊᴀɴ `:**{trj.strip()}` __account__
•━━━━━━━━━━━━•
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)
