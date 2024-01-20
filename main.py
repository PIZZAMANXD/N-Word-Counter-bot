import discord
import json
import os

intents = discord.Intents.default()
intents.message_content = True
ap = os.path.dirname(__file__)
nlist = ['nigger','nigga']

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'ONLINE')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    number = 1

    for i in range(len(nlist)):
        if nlist[i] in str.lower(message.content):
            id = message.author.id
            json_file = open(ap+r'\data.json','r')
            dict_data = json.load(json_file)
            json_file.close()
            for key in dict_data:
                if int(key)==id: number = dict_data[key]
            if number == 1:
                await message.channel.send(f'<@{id}> said the N-Word! This is their first time saying it!')
                number=2
            else:
                await message.channel.send(f'<@{id}> said the N-Word! They have said the N-Word {number} times!')
                number+=1
            dict_data[str(id)] = number
            json_data = json.dumps(dict_data)
            json_file = open(ap+r'\data.json','w')
            json_file.write(json_data)
            json_file.close()

client.run('BOT_TOKEN')
