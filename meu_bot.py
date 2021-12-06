import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}'
            await guild;system_channel.send(mensagem)


intents = discord.Intents.default()
intents.members = True

client = MyClient()
client.run('OTE3MjM2OTEzNTc5MTMwOTEx.Ya1xcQ.lUpycMDmoY1DcbOBq_F4Nrag3jI')