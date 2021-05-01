import discord
from discord.ext import commands

from PIL import Image, ImageOps, ImageDraw, ImageFilter   #Pillow Library for image manipulations
from io import BytesIO

token = "ODM3OTYwNDczMzU2Nzk1OTA0.YI0JgQ.vQjqzwJtB-4GNQY38iC6TR9AxRw"



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)



@client.event
async def on_ready():
    print("Bot is ready")       #Prints "Bot is ready" in the console when it is deployed 



#main function
@client.event
async def on_member_join(member):
    
    #IDs
    #server = client.get_guild(433618651074134028)                          #server id
    welcome_channel = member.guild.get_channel(837777546643898399)          #channel id - edit this to the ID of the welcome channel
    
    #embed
    myEmbed = discord.Embed(title="This is the title", description="This is the description", color=0x00ff00)
    myEmbed.add_field(name="This is filed1", value="This is value1", inline=False)
    myEmbed.add_field(name="This is field2", value="This is value2", inline=True)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Author Name")

    await welcome_channel.send(embed=myEmbed)



    #test image
    #await welcome_channel.send(file=discord.File('image.png'))


    #image manipulation
    
    img = Image.open("image.png")       #background image

    asset = member.avatar_url_as(size = 128)  #asset is member pfp
    data = BytesIO(await asset.read())

    pfp= Image.open(data)
               

#----------------------------------------------------------
    blur_radius = 0
    offset = 0
    offset = blur_radius * 2 + offset
    mask = Image.new("L", pfp.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pfp.size[0] - offset, pfp.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    result = pfp.copy()
    result.putalpha(mask)
    result.save('pfp_round.png')            #save round image
    await welcome_channel.send(file=discord.File('pfp_round.png'))  #send round pfp image
    
#-----------------------------------------------------------
    rndpfp = Image.open('pfp_round.png')
    rndpfp = rndpfp.resize((250,250))

    img.paste(rndpfp, (350,150))          #paste pfp on background
    img.save('combined.png')

    

    await welcome_channel.send(file=discord.File('combined.png'))  #send round pfp image
    
    



    

client.run(token)
