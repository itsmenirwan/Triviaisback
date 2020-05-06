import discord
import asyncio
from discord import Game


bot_channel_id = discord.Object(id='557440175731507200')
oot_channel_id_list = ["557440175731507200","513818250652680213","557439769106448406","557439871447203857","557439829218951168","557439964179333121","525131707410677761","535628205139296256","459842150323060736"
]

sent_new_message = False
answer_scores = {
    "1": 0,
    "2": 0,
    "3": 0
}
answer_scores_last = {
    "1": 0,
    "2": 0,
    "3": 0
}

apgscore = 150
nomarkscore = 80
markscore = 40

bot = discord.Client()
selfbot = discord.Client()

@bot.event
async def on_ready():
    print("")
    print("Connected to discord.")
    print("User: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.send_message(bot_channel_id, "**Bot is Ready!** ``Connected with Peoples``")

@bot.event
async def on_ready():
    await bot.change_presence(game=Game(name='hqnow!'))
    print("Logged in as " + bot.user.name)
    print("hqnow!")
					
@bot.event
async def on_message(message):
    global sent_new_message
    global answer
    global answer_scores
    global answer_scores_last

    if message.server == None:
        return

    if message.content.lower() == "-hq":
        if "565445948973514762" in [role.id for role in message.author.roles]:
            
            sent_new_message = False
            answer_scores = {
                "1": 0,
                "2": 0,
                "3": 0
            }
            answer = ""
               
       
    

@selfbot.event
async def on_ready():
    print("Self Bot")
    print("======================")
    print("Connected to discord.")
    print("User: " + selfbot.user.name)
    print("ID: " + selfbot.user.id)

@selfbot.event
async def on_message(message):
    global answer_scores
    
    global answer

    if message.server == None:
        return

   
    if message.channel.id in oot_channel_id_list:
        content = message.content.lower().replace(' ', '').replace("'", "")
        if content == "1":
            answer_scores["1"] += nomarkscore
        elif content == "2":
            answer_scores["2"] += nomarkscore
        elif content == "3":
            answer_scores["3"] += nomarkscore
        elif content.startswith("1?") or content.startswith("1apg?"):
            answer_scores["1"] += markscore
        elif content.startswith("2?") or content.startswith("2apg?"):
            answer_scores["2"] += markscore
        elif content.startswith("3?") or content.startswith("3apg?"):
            answer_scores["3"] += markscore
        elif content == "1apg":
            answer_scores["1"] += apgscore
        elif content == "2apg":
            answer_scores["2"] += apgscore
        elif content == "3apg":
            answer_scores["3"] += apgscore
        elif content == "4apg":
            answer_scores["4"] += apgscore
        elif content in ["not1", "n1"]:
            answer_scores["1"] -= nomarkscore
        elif content in ["not2", "n2"]:
            answer_scores["2"] -= nomarkscore
        elif content in ["not3", "n3"]:
            answer_scores["3"] -= nomarkscore
        elif content.startswith("not1?") or content.startswith("n1?"):
            answer_scores["1"] -= markscore
        elif content.startswith("not2?") or content.startswith("n2?"):
            answer_scores["2"] -= markscore
        elif content.startswith("not3?") or content.startswith("n3?"):
            answer_scores["3"] -= markscore
        else:
            return

        allanswers = answer_scores.values()
        highest = max(allanswers)
        answer = list(allanswers).index(highest)+1

async def send_embed(client, embed):
    return await client.send_message(bot_channel_id, embed=embed)

async def edit_embed(client, old_embed, new_embed):
    return await client.edit_message(old_embed, embed=new_embed)

async def discord_send():
    global sent_new_message
    global answer
    global answer_scores_last

    await bot.wait_until_ready()
    await asyncio.sleep(0)

    answer_scores_last = {
        "1": 0,
        "2": 0,
        "3": 0
    }

    answer_message = []
    
    while not bot.is_closed:
	    
        if answer_scores != answer_scores_last:
            if answer:
                one_check = ""
                two_check = ""
                three_check = ""
                if answer == 1:
                    one_check = " :white_check_mark:"
                if answer == 2:
                    two_check = " :white_check_mark:"
                if answer == 3:
                    three_check = " :white_check_mark:"
                if not sent_new_message:
                    embed=discord.Embed(title="HQ Assist", description="SEARCH RESULTS FOR HQ TRIVIA", color=0xadd8e6 )
                    embed.add_field(name="A", value=f"{answer_scores['1']}.0{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}.0{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}.0{three_check}", inline=False)
                    embed.set_footer(text=f"Made by nirwan", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQFYhQ52HnQv9fbZbyBcPJOn5q6rYGfqS26EaBMLMBp8LsAZX8U")
                    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQFYhQ52HnQv9fbZbyBcPJOn5q6rYGfqS26EaBMLMBp8LsAZX8U")
				    
                    answer_message = await send_embed(bot, embed)
                    sent_new_message = True
                else:
                    embed=discord.Embed(title="HQ Assist", description="SEARCH RESULTS FOR HQ TRIVIA", color=0xadd8e6 )
                    embed.add_field(name="A", value=f"{answer_scores['1']}.0{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}.0{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}.0{three_check}", inline=False)
                    embed.set_footer(text=f"Made by nirwan", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQFYhQ52HnQv9fbZbyBcPJOn5q6rYGfqS26EaBMLMBp8LsAZX8U")
                    embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQFYhQ52HnQv9fbZbyBcPJOn5q6rYGfqS26EaBMLMBp8LsAZX8U")
				    
                    await edit_embed(bot, answer_message, embed)
                answer_scores_last = answer_scores.copy()
                await asyncio.sleep(0.0)
                continue

        answer_scores_last = answer_scores.copy()
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.create_task(bot.start("NzA2ODI0MDU4ODAwNTcwNDI5.XrIZ6g.Pz1kDKpESzPHN0IsfEtZ5pB2KfU"))
loop.create_task(selfbot.start("NDczODIwNzcyMzczMzY0NzM3.XL0xrg.SNIyzmaOKfS04qZnI2f23no0ZSA", bot=False))

loop.create_task(discord_send())
loop.run_forever()
