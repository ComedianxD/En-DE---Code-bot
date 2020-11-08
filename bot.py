import hashlib
from discord.ext import commands
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad


bot = commands.Bot(command_prefix="+")


def iv_16(txt):
	if len(txt) > 16:
		txt = txt[:16]
	elif len(txt) < 16:
		while len(txt) != 16:
			txt += " "
	return txt


@bot.command()
async def encode(ctx, *, message):
	key = str(ctx.message.author).encode()
	key_256 = hashlib.sha256(key).digest()
	iv = bytes(iv_16(key))

	cipher = AES.new(key_256, AES.MODE_CBC, iv)

	padded_message = pad(message.encode(), AES.block_size)

	encrypted_message = cipher.encrypt(padded_message)

	await ctx.channel.send(encrypted_message)


@bot.command()
async def decode(ctx, message, key):
	try:
		key_ = key.encode()
		key_256 = hashlib.sha256(key_).digest()
		iv = bytes(iv_16(key_))

		message = eval(message)

		cipher = AES.new(key_256, AES.MODE_CBC, iv)

		decrypted_message = unpad(cipher.decrypt(message), AES.block_size).decode()
	except ValueError:
		decrypted_message = "Wrong Key!"

	await ctx.channel.send(decrypted_message)


'''@bot.command()
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)'''

bot.run('Nzc0OTYzMzA2NDE3ODgxMTE4.X6fa0g.XaSM1HmCW6N50AeykxxkEelWu6Q')
# bot.run('NzczMTM3MDU3Mjg3MzcyODEw.X6E1_g.ruYswAyswmTn9a2XgXtyCPIbOWk')
