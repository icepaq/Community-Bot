#
# Author: Anton#2908 on Discord
# Contributors: N_One_Kid#4040 Anton#2908
# To contribute please read the README file.
#


import discord
import sqlActions
import random
import cmath

curve = 0.1  # Horizontal stretch of radical function

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        sqlActions.dbSetup()

    async def on_message(self, message):
        #################
        # Levels System #
        #################
        xp = sqlActions.selectLevels(str(message.author.id))
        if message.author.bot:
            pass
        else:
            if xp is None:
                sqlActions.userInsert(str(message.author), str(message.author.id), 0)
            else:
                new_xp = xp[0] + random.randrange(10)
                sqlActions.updateLevel(new_xp, str(message.author.id))

                # Levels are not stored in the database. Instead, xp is. The level is calculated by
                # retrieving xp and calculating the square root and removing the decimals.
                new_level = int(cmath.sqrt(new_xp * curve).real)
                old_level = int(cmath.sqrt(xp[0] * curve).real)

                if new_level > old_level:
                    m = '<@' + str(message.author.id) + "> is now level " + str(new_level)
                    await message.channel.send(m)
        #######################
        # End of Level System #
        #######################

        print('Message from {0.author}: {0.content}'.format(message))

        if message.content.startswith('ping'):
            channel = message.channel
            await channel.send('pong')

        if message.content.startswith('!level'):
            try:
                level_result = sqlActions.selectLevels(str(message.mentions[0].id))
                print(message.mentions[0])
                print(message.mentions[0].id)
                rs = int(cmath.sqrt(level_result[0] * curve).real)

                await message.channel.send('<@' + str(message.mentions[0].id) + "> is level " + str(rs))
            except:
                level_result = sqlActions.selectLevels(str(message.author.id))
                rs = int(cmath.sqrt(level_result[0] * curve).real)

                await message.channel.send('<@' + str(message.author.id) + "> you are level " + str(rs))

        if message.content.startswith('!xp'):
            xp_result = sqlActions.selectXP(str(message.author.id))
            await message.channel.send(xp_result)

        if message.content.startswith('!leaderboard'):
            leaderboard = sqlActions.leaderboard()
            await message.channel.send(leaderboard)

client = MyClient()

secret = ""
with open("creds", "r") as s:
    secret = s.read()

client.run(secret)