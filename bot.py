from discord.ext import commands

bot = commands.Bot(command_prefix="+")

file = open("file.txt","r")
f = file.readlines()
dic = {} 
dicc = {}
for line in f:
	dicc[line[2]] = line[0]
	dic[line[0]] = line[2]

@bot.command(name="encode")
async def fun(ctx,*args):
	output = ""
	for arg in args:
		for char in arg:
			output = output + dic[char]
		output = output + " "
	await ctx.channel.send(output)



@bot.command(name="decode")
async def fun(ctx,*args):
	output = ""
	for arg in args:
		for char in arg:
			output = output + dicc[char]
		output = output + " "
	await ctx.channel.send(output)


#print(dic) 
@bot.command()
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg

	await ctx.channel.send(response)


#bot.run('NzczMTM3MDU3Mjg3MzcyODEw.X6E1_g.ruYswAyswmTn9a2XgXtyCPIbOWk')