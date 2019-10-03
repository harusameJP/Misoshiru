#参考1:https://qiita.com/1ntegrale9/items/9d570ef8175cf178468f
#参考2:https://discordpy.readthedocs.io/en/stable/api.html


# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'TOKEN'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/cat':
        await message.channel.send('meaw')

# 話しかけられた人に返信
        @client.event
async def on_message(message):
    if client.user in message.mentions: # 話しかけられたかの判定
        reply = f'{message.author.mention} 呼んだ?' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

# BOT起動時に任意のチャンネルにメッセージを送信
        @client.event
async def on_ready():
    CHANNEL_ID = # 任意のチャンネルID(int)
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('BOT起動！！')

# 同一カテゴリ内にnewチャンネルを作成
@client.event
async def on_message(message):
    if message.content.startswith('/createch'):
        category_id = message.channel.category_id
        category = message.guild.get_channel(category_id)
        new_channel = await category.create_text_channel(name='new')
        reply = f'{new_channel.mention} を作成しました。'
        await message.channel.send(reply)

# ログの全削除
@client.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')

#役職の付与
@client.event
async def on_message(message):
    if message.content.startswith('/join'):
        role = discord.utils.get(message.guild.roles, name='member')
        #memberという役職がないと機能しない
await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)

#リアクショントリガー
@client.event
async def on_message(message):
    if message.content.startswith('/thumb'):
        channel = message.channel
        await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            await channel.send('👎')
        else:
            await channel.send('👍')

        
        
        
client.run("NjI4OTY3ODczNjYyMDI1NzYw.XZXzJg.MQD8yK96xr8huposO2JAKyAf3Es")
