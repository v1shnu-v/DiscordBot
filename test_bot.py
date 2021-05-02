import discord
from discord.ext import commands

from PIL import Image, ImageOps, ImageDraw, ImageFont   #Pillow Library for image manipulations
from io import BytesIO


def read_token():
    with open("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()    


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '!',intents = intents)



@client.event
async def on_ready():
    print("Bot is ready for action")       #Prints "Bot is ready" in the console when it is deployed 



#welcome function
@client.event
async def on_member_join(member):
    
    #IDs
    server = client.get_guild(433618651074134028)                           #server id
    welcome_channel = member.guild.get_channel(837777546643898399)          #channel id - edit this to the ID of the welcome channel


    print(f'{member} has joined the server')    #for logs
    
    await welcome_channel.send(f'Keri vaada {member.mention}! Welcome to **Gamers Hub**!')
    
    
    print(f'Members = {server.member_count}')

    

    #image manipulation

    bg = Image.open("bg.png").convert("RGBA")
    avatar = Image.open(BytesIO(await member.avatar_url_as(size=256).read())).convert("RGBA")
    overlay = Image.new('RGBA', bg.size, (255,255,255,0))
    masksize = (avatar.size[0] * 3, avatar.size[1] * 3)
    mask = Image.new('L', masksize, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + masksize, fill=255)
    mask = mask.resize(avatar.size, Image.ANTIALIAS)
    avatar.putalpha(mask)
    overlay.paste(avatar, (422, 61))
    compose = Image.alpha_composite(bg, overlay)

    
    #font for welcome banner
    font = ImageFont.truetype('arial.ttf', size=38)
    draw = ImageDraw.Draw(compose)
    
    #message on welcome banner
    message = f'{member} has joined the server \nGamer #{server.member_count}'

    #box to bound welcome banner text
    bounding_box = [53, 333, 1048, 420]
    x1, y1, x2, y2 = bounding_box  # For easy reading

   

    # Calculate the width and height of the text to be drawn, given font size
    w, h = draw.textsize(message, font=font)

    # Calculate the mid points and offset by the upper left corner of the bounding box
    x = (x2 - x1 - w)/2 + x1
    y = (y2 - y1 - h)/2 + y1

    # Write the text to the image, where (x,y) is the top left corner of the text
    draw.text((x, y), message, align='center', font=font)

    #Draw the bounding box which bounds the text
    #draw.rectangle([x1, y1, x2, y2])

   
    arr = BytesIO()
    compose.save(arr, format='png')
    arr.seek(0)
    await welcome_channel.send(file = discord.File(arr, 'profile.png'))

    
    



    

client.run(token)




#------------------------------------------------------------------------------------------------------------------------    
    #embed
    #myEmbed = discord.Embed(title="This is the title", description="This is the description", color=0x00ff00)
    #myEmbed.add_field(name="This is filed1", value="This is value1", inline=False)
    #myEmbed.add_field(name="This is field2", value="This is value2", inline=True)
    #myEmbed.set_footer(text="This is a sample footer")
    #myEmbed.set_author(name="Author Name")

    #await welcome_channel.send(embed=myEmbed)

#-------------------------------------------------------------------------------------------------------------------------