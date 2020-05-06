import discord
# import sys
# import os
import random
import asyncio

bot_channel_id = discord.Object(id='557440175731507200')
oot_channel_id_list = ["557440175731507200","513818250652680213","557439769106448406","557439871447203857","557439829218951168","557439964179333121","525131707410677761","535628205139296256","459842150323060736"]

sent_new_message = False
answer_scores = {
    "1": 0,
    "2": 0,
    "3": 0,
   
}
answer_scores_last = {
    "1": 0,
    "2": 0,
    "3": 0,

}
# def restart_program():
#     """Restarts the current program.
#     Note: this function does not return. Any cleanup action (like
#     saving data) must be done before calling this function."""
#     python = sys.executable
#     os.execl(python, python, * sys.argv)
apgscore = 150
nomarkscore = 80
markscore = 40
erase = "``Erased`` ***❌***"

bot = discord.Client()
selfbot = discord.Client()

@bot.event
async def on_ready():
    print("LOCO")
    print("Connected to discord.")
    print("User: " + bot.user.name)
    print("ID: " + bot.user.id)
    await bot.send_message(bot_channel_id, "**READY```LITE ANSWERS```** ")

   

@bot.event
async def on_message(message):
    global sent_new_message
    global answer
    global wrong
    global answer_scores
    global answer_scores_last

    if message.server == None:
        return
    if message.content.lower() == "-r":
       if "553981870933540866" in [role.id for role in message.author.roles]:
           sent_new_message =False
           answer_scores = {
                "1": 0, 
                "2": 0,
                "3": 0,
           }
           wrong = " "
           answer = " "    
          
    
    
    
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
    global wrong

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
              
        elif content in ["not1", "n1", "erased: 1", "erase:1", "erased:1", "erase: 1"]:
            answer_scores["1"] = erase
        elif content in ["not2", "n2", "erased: 2", "erase:2", "erased:3", "erase: 3"]:
            answer_scores["2"] = erase
        elif content in ["not3", "n3", "erased: 3", "erase:3", "erased:3", "erase: 3"]:
            answer_scores["3"] = erase
        
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
        lowest = min(allanswers)
        answer = list(allanswers).index(highest)+1
        wrong = list(allanswers).index(lowest)+1

async def send_embed(client, embed):
    return await client.send_message(bot_channel_id, embed=embed)

async def edit_embed(client, old_embed, new_embed):
    return await client.edit_message(old_embed, embed=new_embed)

async def discord_send():
    global sent_new_message
    global answer
    global wrong
    global answer_scores_last

    await bot.wait_until_ready()
    await asyncio.sleep(0)

    answer_scores_last = {
        "1": 0,
        "2": 0,
        "3": 0,
        
    }

    answer_message = []
    
    while not bot.is_closed:
	    
        if answer_scores != answer_scores_last:
            
            if wrong and answer :
                one_cross = ""
                two_cross = ""
                three_cross = ""
                one_check = ""
                two_check = ""
                three_check = ""
                
                if wrong == 1:
                    one_cross = " "
                if wrong == 2:
                    two_cross = " "
                if wrong == 3:
                    three_cross = " "
                if answer == 1:
                    one_check = " :white_check_mark: "
                if answer == 2:
                    two_check = " :white_check_mark: "
                if answer == 3:
                    three_check = " :white_check_mark: "
                
                if not sent_new_message:
                    value=random.randint(0,0xffffff)
                    embed=discord.Embed(title="LITE ANSWERS", description="", color=value)
                    embed.add_field(name="A", value=f"{answer_scores['1']}{one_cross}{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}{two_cross}{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}{three_cross}{three_check}", inline=False)
                    embed.set_image(url="https://cdn.discordapp.com/attachments/459865236393164810/493986426745126932/multicolours_1.gif")
                    embed.set_footer(text=f"Made by niloj", icon_url="")

                    answer_message = await send_embed(bot, embed)
                    sent_new_message = True
                else:
                    value=random.randint(0,0xffffff)
                    embed=discord.Embed(title="LITE ANSWERS", description="", color=value)
                    embed.add_field(name="A", value=f"{answer_scores['1']}{one_cross}{one_check}", inline=False)
                    embed.add_field(name="B", value=f"{answer_scores['2']}{two_cross}{two_check}", inline=False)
                    embed.add_field(name="C", value=f"{answer_scores['3']}{three_cross}{three_check}", inline=False)
                    embed.set_image(url="https://cdn.discordapp.com/attachments/459865236393164810/493986426745126932/multicolours_1.gif")   
                    embed.set_footer(text=f"Made by niloj", icon_url="")
                    x = await edit_embed(bot, answer_message, embed)
                    await bot.add_reaction(x,emoji="✅")
                    await bot.add_reaction(x,emoji="❌")
                answer_scores_last = answer_scores.copy()
                await asyncio.sleep(0)
                continue

        answer_scores_last = answer_scores.copy()
        await asyncio.sleep(0)

loop = asyncio.get_event_loop()
loop.create_task(bot.start("NTY1NTQ2OTM0MDAyMjUzODI5.XLU0wg.05zgG6mdgJ_1SZd1goXDP24yW_s"))
loop.create_task(selfbot.start("NTQ2OTkzNTE2NDg4Njg3NjE3.XKbk1Q.84g871FgpLiyV33CbTteO2bxp9g", bot=False))

loop.create_task(discord_send())
loop.run_forever()


