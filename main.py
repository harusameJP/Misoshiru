import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    # Botがログインしたら
@client.event
async def on_ready():
    msg = "こんにちは！です．よろしくね！"
    await client.send_message(text_chat,msg)
    
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

client.run("NjI4OTY3ODczNjYyMDI1NzYw.XZS7aQ.btGunikGY1IMVXblBgu-DSa41X0")
