import discord
from discord.ext import commands

from PIL import Image
from io import BytesIO

token = "ODM3OTYwNDczMzU2Nzk1OTA0.YI0JgQ.vQjqzwJtB-4GNQY38iC6TR9AxRw"



intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)






@client.event
async def on_ready():
    print("Bot is ready")




#main function
@client.event
async def on_member_join(member):
    
    #IDs
    #server = client.get_guild(433618651074134028)                          #server id
    welcome_channel = member.guild.get_channel(837777546643898399)          #channel id
    
    #embed
    myEmbed = discord.Embed(title="This is the title", description="This is the description", color=0x00ff00)
    myEmbed.add_field(name="This is filed1", value="This is value1", inline=False)
    myEmbed.add_field(name="This is field2", value="This is value2", inline=True)
    myEmbed.set_footer(text="This is a sample footer")
    myEmbed.set_author(name="Author Name")

    await welcome_channel.send(embed=myEmbed)



    #test image
    await welcome_channel.send(file=discord.File('image.jpg'))


    #image manipulation
    img = Image.open("image.jpg")       #background image

    asset = member.avatar_url_as(size = 128)  #asset is member pfp
    data = BytesIO(await asset.read())

    pfp= Image.open(data)
    pfp = pfp.resize((250,250))        #resize pfp           

    img.paste(pfp, (350,150))          #paste pfp on background

    img.save("profile.jpg")            #save combined image

    await welcome_channel.send(file=discord.File('profile.jpg'))  #send combined image
    
    



    

client.run(token)
