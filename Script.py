import os
class script(object):
    START_TXT = """<b>ʜᴇʏ {}, {}\n\nɪ ᴀᴍ ᴀ ᴘᴏᴡᴇʀꜰᴜʟ ᴀᴜᴛᴏꜰɪʟᴛᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ɢɪᴠᴇ ᴍᴏᴠɪᴇs ᴏʀ sᴇʀɪᴇs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴘᴍ !! 😍\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/DP_BOTZ">DP Botz</a></blockquote></b>"""
    
    HELP_TXT = """<b>ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ ɢᴇᴛ ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ꜱᴘᴇᴄɪꜰɪᴄ ᴍᴏᴅᴜʟᴇꜱ..</b>"""
    
    TELE_TXT = """<b>/telegraph - sᴇɴᴅ ᴍᴇ ᴘɪᴄᴛᴜʀᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴜɴᴅᴇʀ (5ᴍʙ)

ɴᴏᴛᴇ - ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋ ɪɴ ʙᴏᴛʜ ɢʀᴏᴜᴘs ᴀɴᴅ ʙᴏᴛ ᴘᴍ</b>"""
    FSUB_TXT = """<b>• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ 😗
• ᴍᴀᴋᴇ ᴍᴇ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ Gʀᴏᴜᴘ  😉
• sᴇɴᴅ /fsub ʏᴏᴜʀ_ᴛᴀʀɢᴇᴛ_ᴄʜᴀᴛ_ɪᴅ
ᴇx: <code>/fsub -100xxxxxx</code>

ɴᴏᴡ ɪᴛ's ᴅᴏɴᴇ.ɪ ᴡɪʟʟ ᴄᴏᴍᴘᴇʟ ʏᴏᴜʀ ᴜsᴇʀs ᴛᴏ ᴊᴏɪɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ/ɢʀᴏᴜᴘ, ᴀɴᴅ I ᴡɪʟʟ ɴᴏᴛ ᴘʀᴏᴠɪᴅᴇ ᴀɴʏ ғɪʟᴇs ᴜɴᴛɪʟ ʏᴏᴜʀ ᴜsᴇʀs ᴊᴏɪɴ ʏᴏᴜʀ ᴛᴀʀɢᴇᴛ ᴄʜᴀɴɴᴇʟ.

ᴛᴏ ᴅɪsᴀʙʟᴇ ғsᴜʙ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ, sɪᴍᴘʟʏ sᴇɴᴅ <code>/del_fsub</code>

ᴛᴏ ᴄʜᴇᴄᴋ ɪғ ғsᴜʙ ɪs ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴏʀ ɴᴏᴛ, ᴜsᴇ <code>/show_fsub</code></b>"""

    FORCESUB_TEXT="""<b>
ɪɴ ᴏʀᴅᴇʀ ᴛᴏ ɢᴇᴛ ᴛʜᴇ ᴍᴏᴠɪᴇ ʀᴇᴏ̨ᴜᴇsᴛᴇᴅ ʙʏ ʏᴏᴜ.

ʏᴏᴜ ᴡɪʟʟ ʜᴀᴠᴇ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ.

ғɪʀsᴛ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "Jᴏɪɴ ᴜᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ" ʙᴜᴛᴛᴏɴ, ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ʀᴇᴏ̨ᴜᴇsᴛ ᴛᴏ Jᴏɪɴ" ʙᴜᴛᴛᴏɴ.

ᴀғᴛᴇʀ ᴛʜᴀᴛ, ᴛʀʏ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴀᴛ ᴍᴏᴠɪᴇ ᴛʜᴇɴ, ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ "ᴛʀʏ ᴀɢᴀɪɴ" ʙᴜᴛᴛᴏɴ.
    </b>"""
    
    TTS_TXT="""
<b>• sᴇɴᴅ /tts ᴛᴏ ᴜsᴇ ᴛʜɪs ғᴇᴀᴛᴜʀᴇ</b>"""

    DISCLAIMER_TXT = """
<b>ᴛʜɪꜱ ɪꜱ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ. ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ꜱʜᴀʀᴇ ᴏʀ ᴄᴏɴꜱᴜᴍᴇ ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ. 

<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/JISSHU_BOTS'>JISSHU BOTS</a></b></blockquote>"""
    

    ABOUT_TEXT = """<blockquote><b>‣ ᴍʏ ɴᴀᴍᴇ : Star Movies Bot\n‣ ᴄʀᴇᴀᴛᴏʀ : <a href='https://t.me/U_Karthik'>Karthik</a>\n‣ ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ\n‣ ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ\n‣ ᴅᴀᴛᴀ ʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\n‣ ʜᴏsᴛᴇᴅ ᴏɴ  : ᴀʟʟ ᴡᴇʙ\n‣ ʙᴜɪʟᴅ sᴛᴀᴛᴜs : ᴠ5.2 [sᴛᴀʙʟᴇ]</b></blockquote>"""    
    
    SUPPORT_GRP_MOVIE_TEXT = '''<b>ʜᴇʏ {}

ɪ ғᴏᴜɴᴅ {} ʀᴇsᴜʟᴛs 🎁,
ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ sᴇɴᴅ ʜᴇʀᴇ 🤞🏻
ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ᴛᴏ ɢᴇᴛ ✨</b>'''

    CHANNELS = """
<u>ᴏᴜʀ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ᴄʜᴀɴɴᴇʟꜱ</u> 

▫ ᴀʟʟ ʟᴀᴛᴇꜱᴛ ᴀɴᴅ ᴏʟᴅ ᴍᴏᴠɪᴇꜱ & ꜱᴇʀɪᴇꜱ.
▫ ᴀʟʟ ʟᴀɴɢᴜᴀɢᴇꜱ ᴍᴏᴠɪᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ.
▫ ᴀʟᴡᴀʏꜱ ᴀᴅᴍɪɴ ꜱᴜᴘᴘᴏʀᴛ.
▫ 𝟸𝟺x𝟽 ꜱᴇʀᴠɪᴄᴇꜱ ᴀᴠᴀɪʟᴀʙʟᴇ."""

    LOGO = """

BOT WORKING PROPERLY 🔥"""
    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v4.2 [ Sᴛᴀʙʟᴇ ]</code>

Bʏ @Star_Moviess_Bot</b>"""
        
    
    STATUS_TXT = """<b><u>🗃 ᴅᴀᴛᴀʙᴀsᴇ 1 🗃</u>

» ᴛᴏᴛᴀʟ ᴜsᴇʀs - <code>{}</code>
» ᴛᴏᴛᴀʟ ɢʀᴏᴜᴘs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🗳 ᴅᴀᴛᴀʙᴀsᴇ 2 🗳</u></b>

» ᴛᴏᴛᴀʟ ꜰɪʟᴇs - <code>{}</code>
» ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ - <code>{} / {}</code>

<u>🤖 ʙᴏᴛ ᴅᴇᴛᴀɪʟs 🤖</u>

» ᴜᴘᴛɪᴍᴇ - <code>{}</code>
» ʀᴀᴍ - <code>{}%</code>
» ᴄᴘᴜ - <code>{}%</code></b>"""

    NEW_USER_TXT = """<b>#New_User {}

≈ ɪᴅ:- <code>{}</code>
≈ ɴᴀᴍᴇ:- {}</b>"""

    NEW_GROUP_TXT = """#New_Group {}

Group name - {}
Id - <code>{}</code>
Group username - @{}
Group link - {}
Total members - <code>{}</code>
User - {}"""

    REQUEST_TXT = """<b>📜 ᴜꜱᴇʀ - {}
📇 ɪᴅ - <code>{}</code>

🎁 ʀᴇǫᴜᴇꜱᴛ ᴍꜱɢ - <code>{}</code></b>"""  
   
    IMDB_TEMPLATE_TXT = """
<b>ʜᴇʏ {message.from_user.mention}, ʜᴇʀᴇ ɪꜱ ᴛʜᴇ ʀᴇꜱᴜʟᴛꜱ ꜰᴏʀ ʏᴏᴜʀ ǫᴜᴇʀʏ {search}.

🍿 Title: {title}
🎃 Genres: {genres}
📆 Year: {release_date}
⭐ Rating: {rating} / 10</b>
"""

    FILE_CAPTION = """<b>@Movies_Dayz - {file_name}\n\nJoin ➥ <a href="https://t.me/Movies_Dayz">Movies Dayz</a></b>"""
    

    ALRT_TXT = """ᴊᴀʟᴅɪ ʏᴇʜᴀ sᴇ ʜᴀᴛᴏ !"""

    OLD_ALRT_TXT = """ʏᴏᴜ ᴀʀᴇ ᴜsɪɴɢ ᴍʏ ᴏʟᴅ ᴍᴇssᴀɢᴇs..sᴇɴᴅ ᴀ ɴᴇᴡ ʀᴇǫᴜᴇsᴛ.."""

    NO_RESULT_TXT = """<b>ᴛʜɪs ᴍᴇssᴀɢᴇ ɪs ɴᴏᴛ ʀᴇʟᴇᴀsᴇᴅ ᴏʀ ᴀᴅᴅᴇᴅ ɪɴ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ 🙄</b>"""
    
    I_CUDNT = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆 𝗺𝗼𝘃𝗶𝗲 𝗼𝗿 𝘀𝗲𝗿𝗶𝗲𝘀 𝗶𝗻 𝘁𝗵𝗮𝘁 𝗻𝗮𝗺𝗲.. 😐"""

    I_CUD_NT = """😑 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 😞... 𝗰𝗵𝗲𝗰𝗸 𝘆𝗼𝘂𝗿 𝘀𝗽𝗲𝗹𝗹𝗶𝗻𝗴."""
    
    CUDNT_FND = """🤧 𝗛𝗲𝗹𝗹𝗼 {}

𝗜 𝗰𝗼𝘂𝗹𝗱𝗻'𝘁 𝗳𝗶𝗻𝗱 𝗮𝗻𝘆𝘁𝗵𝗶𝗻𝗴 𝗿𝗲𝗹𝗮𝘁𝗲𝗱 𝘁𝗼 𝘁𝗵𝗮𝘁 𝗱𝗶𝗱 𝘆𝗼𝘂 𝗺𝗲𝗮𝗻 𝗮𝗻𝘆 𝗼𝗻𝗲 𝗼𝗳 𝘁𝗵𝗲𝘀𝗲 ?? 👇"""
    
    FONT_TXT= """<b>ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ᴍᴏᴅᴇ ᴛᴏ ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜰᴏɴᴛs sᴛʏʟᴇ, ᴊᴜsᴛ sᴇɴᴅ ᴍᴇ ʟɪᴋᴇ ᴛʜɪs ꜰᴏʀᴍᴀᴛ

<code>/font hi how are you</code></b>"""
    
    PLAN_TEXT = """<b>ᴡᴇ ᴀʀᴇ ᴘʀᴏᴠɪᴅɪɴɢ ᴘʀᴇᴍɪᴜᴍ ᴀᴛ ᴛʜᴇ ʟᴏᴡᴇsᴛ ᴘʀɪᴄᴇs:
    
1 ʀᴜᴘᴇᴇ ᴘᴇʀ ᴅᴀʏ 👻
29 ʀᴜᴘᴇᴇs ғᴏʀ ᴏɴᴇ ᴍᴏɴᴛʜ 😚
55 ʀᴜᴘᴇᴇs ғᴏʀ ᴛᴡᴏ ᴍᴏɴᴛʜs 😗

ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ ʙᴜʏɪɴɢ ↡↡↡
</b>"""
    
    VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪғɪᴇᴅ ᴛᴏᴅᴀʏ, ᴘʟᴇᴀꜱᴇ ᴄʟɪᴄᴋ ᴏɴ ᴠᴇʀɪғʏ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇꜱꜱ ғᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    SECOND_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {} {},

📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ ᴀɴᴅ ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ᴛɪʟʟ ɴᴇxᴛ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 2/3

ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇꜱ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴꜱ ᴛʜᴇɴ ʙᴜʏ ʙᴏᴛ ꜱᴜʙꜱᴄʀɪᴘᴛɪᴏɴ 😊

💶 sᴇɴᴅ /plan ᴛᴏ ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ</b>"""

    SECOND_VERIFY_COMPLETE_TEXT = """<b>👋 ʜᴇʏ {},

ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 2nd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ <code>{}</code></b>"""

    THIRDT_VERIFICATION_TEXT = """<b>👋 ʜᴇʏ {},
    
📌 <u>ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ, ᴛᴀᴘ ᴏɴ ᴛʜᴇ ᴠᴇʀɪꜰʏ ʟɪɴᴋ & ɢᴇᴛ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ.</u>

#ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ:- 3/3

ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴅɪʀᴇᴄᴛ ꜰɪʟᴇs ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀᴋᴇ ᴘʀᴇᴍɪᴜᴍ sᴇʀᴠɪᴄᴇ (ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴠᴇʀɪꜰʏ)</b>"""

    THIRDT_VERIFY_COMPLETE_TEXT= """<b>👋 ʜᴇʏ {},
    
ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ᴛʜᴇ 3rd ᴠᴇʀɪꜰɪᴄᴀᴛɪᴏɴ ✓

ɴᴏᴡ ʏᴏᴜ ʜᴀᴠᴇ ᴜɴʟɪᴍɪᴛᴇᴅ ᴀᴄᴄᴇss ꜰᴏʀ ɴᴇxᴛ ꜰᴜʟʟ ᴅᴀʏ </b>"""

    VERIFIED_LOG_TEXT = """<b><u>☄ ᴜsᴇʀ ᴠᴇʀɪꜰɪᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ ☄</u>

⚡️ ɴᴀᴍᴇ:- {} [ <code>{}</code> ] 
📆 ᴅᴀᴛᴇ:- <code>{} </code></b>

#verified_{}_completed"""


    MOVIES_UPDATE_TXT = """<b>#𝑵𝒆𝒘_𝑭𝒊𝒍𝒆_𝑨𝒅𝒅𝒆𝒅 ✅
**🍿 Title:** {title}
**🎃 Genres:** {genres}
**📆 Year:** {year}
**⭐ Rating:** {rating} / 10
</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},

<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""    

    PREPLANSS_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎁 ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇ ʙᴇɴɪꜰɪᴛꜱ:</blockquote>

❏ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
❏ ɢᴇᴛ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
❏ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
❏ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
❏ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
❏ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs ᴀɴᴅ sᴇʀɪᴇs                                                                        
❏ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
❏ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 𝟷ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan
</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/IM_JISSHU'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {}
    
<blockquote>🎖️ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴꜱ :</blockquote>

 ❏ 𝟶𝟷𝟻₹    ➠    𝟶𝟷 ᴡᴇᴇᴋꜱ
 ❏ 𝟶𝟹𝟿₹    ➠    𝟶𝟷 ᴍᴏɴᴛʜ
 ❏ 𝟶𝟽𝟻₹    ➠    𝟶𝟸 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟷𝟶₹    ➠    𝟶𝟹 ᴍᴏɴᴛʜ
 ❏ 𝟷𝟿𝟿₹    ➠    𝟶𝟼 ᴍᴏɴᴛʜ
 ❏ 𝟹𝟼𝟶₹    ➠    𝟷𝟸 ᴍᴏɴᴛʜ

🆔 ᴜᴘɪ ɪᴅ ➩ <code>starbotstamil@oksbi</code> [ᴛᴀᴘ ᴛᴏ ᴄᴏᴘʏ]
 
⛽️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ: /myplan

🏷️ <a href='https://t.me/Karthik_Proofs'>ᴘʀᴇᴍɪᴜᴍ ᴘʀᴏᴏꜰ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.
‼️ ɢɪᴠᴇ ᴜꜱ ꜱᴏᴍᴇᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴘʀᴇᴍɪᴜᴍ ʟɪꜱᴛ.
</b>"""

    ADMIN_CMD_TXT = """<b>
-------------User Premium------------
➩ /add_premium {user ID} {Times} - Add a premium user
➩ /remove_premium {user ID} - Remove a premium user
➩ /add_redeem - Generate a redeem code
➩ /premium_users - List all premium users
➩ /refresh - Refresh free trial for users

-------------Update Channel----------
➩ /set_muc {channel ID} - Set the movies update channel

--------------PM Search--------------
➩ /pm_search_on - Enable PM search
➩ /pm_search_off - Disable PM search

--------------Verify ID--------------
➩ /verify_id - Generate a verification ID for group use only

--------------Set Ads----------------
➩ /set_ads {ads name}}#{Times}#{photo URL} - <a href="https://t.me/Jisshu_developer/11">Explain</a>
➩ /del_ads - Delete ads

-------------Movie Management--------
➩ /link - Fetch movie using a provided link
➩ /most - Display the most viewed movies
➩ /add_redeem - Add a new redeem code
➩ /redeem - Redeem a code for a reward
➩ /streams - View active movie streams</b>"""

    ADMIN_CMD_TXT2 = """<b>
----------Subscription Management-----
➩ /fsub - Add a new subscription
➩ /show_fsub - Display all subscriptions
➩ /del_fsub - Delete a subscription
➩ /myplan - View your subscription plan
➩ /plan - View or modify subscription plan

-------------User Management----------
➩ /ban - Ban a user
➩ /unban - Unban a user
➩ /font - Change font settings
➩ /stats - View statistics or analytics
➩ /details - View detailed information

-------------Group Management---------
➩ /leave {group ID} - Leave the specified group
➩ /groups - Manage groups
➩ /reset_group - Reset group settings

-------------Send Message-------------
➩ /send {user-name} - Use this command as a reply to any message

-------------Settings-----------------
➩ /settings - View or change settings
➩ /set_template - Set a template for messages
➩ /deletefiles - Delete files from storage
➩ /del_file - Delete a specific file</b>"""


    ADMIN_CMD_TXT3 = """<b>
-------------Broadcasting------------
➩ /broadcast - Send a broadcast message
➩ /grp_broadcast - Send broadcast to groups
➩ /invite - Send an invite link

-------------Group Management---------
➩ /leave - Exit from the group or service
➩ /groups - Manage groups
➩ /reset_group - Reset group settings

-------------File Management----------
➩ /delete - Delete a specific item
➩ /deleteall - Delete all items

-------------Logging------------------
➩ /set_log - Set logging preferences

-------------Time Settings------------
➩ /set_time_2 - Set a second time parameter
➩ /set_time_3 - Set a third time parameter</b>"""


    ADMIN_CMD_TXT4 = """<b>
-------------Referral System----------
➩ /refer - Handle referral system

-------------Verification-------------
➩ /set_verify - Set verification settings
➩ /set_verify_2 - Set second-level verification
➩ /set_verify_3 - Set third-level verification
➩ /verifyon - Enable verification
➩ /verifyoff - Disable verification

-------------Channel Management-------
➩ /id - View or set the ID
➩ /channel - Manage channel settings

-------------Skip Options-------------
➩ /setskip - Set skip options

-------------Request Management-------
➩ /delreq - Delete a request</b>"""
    
    GROUP_TEXT = """<b>
 --------------Set Verify-------------
/set_verify {{website link}} {{website api}}
/set_verify_2 {{website link}} {{website api}}
/set_verify_3 {{website link}} {{website api}}
-------------Set Verify Time-----------
/set_time_2 {{seconds}} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {{seconds}} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {{verify.off code}} - off verification <a href="https://t.me/U_Karthik">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/Jisshu_developer/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial - set verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {{log channel id}}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ ᴜsᴇ ᴀʟʟ ғᴇᴀᴛᴜʀᴇs😇</b>"""

    SOURCE_TXT = """<b>
NOTE:
- ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ʜᴇʀᴇ ◉› :<blockquote><a href="https://t.me/DP_BOTZ">𝗦𝘁𝗮𝗿-𝗙𝗶𝗹𝘁𝗲𝗿-𝗕𝗼𝘁</a></blockquote>

developer : Karthik 
</b>""" 
    GROUP_C_TEXT = """<b>
 --------------Set Verify-------------
/set_verify {website link} {website api}
/set_verify_2 {website link} {website api}
/set_verify_3 {website link} {website api}
-------------Set Verify Time-----------
/set_time_2 {seconds} Sᴇᴛ ᴛʜᴇ sᴇᴄᴏɴᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
/set_time_3 {seconds} Sᴇᴛ ᴛʜᴇ ᴛʜɪʀᴅ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴛɪᴍᴇ
--------------Verify On Off------------
/verifyoff {verify.off code} - off verification <a href="https://t.me/IM_JISSHU">Cᴏɴᴛᴀᴄᴛ</a> ᴛʜᴇ ʙᴏᴛ ᴀᴅᴍɪɴ ғᴏʀ ᴀ ᴠᴇʀɪғʏ.ᴏғғ ᴄᴏᴅᴇ
/verifyon - on verification 
------------Set File Caption-----------
/set_caption - set coustom file caption 
-----------Set Imdb Template-----------
/set_template - set IMDb template <a href="https://t.me/Jisshu_developer/8">Example</a>
--------------Set Tutorial-------------
/set_tutorial {tutorial link} - set 1 verification tutorial 
/set_tutorial_2 {tutorial link} - set 2 verification tutorial 
/set_tutorial_3 {tutorial link} - set 3 verification tutorial 
-------------Set Log Channel-----------
--> ᴀᴅᴅ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ʙʏ ᴛʜɪs ꜰᴏʀᴍᴀᴛ & ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ 👇

/set_log {log channel id}
---------------------------------------
ʏᴏᴜ ᴄᴀɴ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀʟʟ ᴅᴇᴛᴀɪʟs 
ʙʏ /details ᴄᴏᴍᴍᴀɴᴅ
Iғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ᴅᴏᴜʙᴛs ᴘʟᴇᴀsᴇ <a href="https://t.me/IM_JISSHU">ᴄᴏɴᴛᴀᴄᴛ</a> ᴍʏ <a href="https://t.me/U_Karthik">ᴀᴅᴍɪɴ</a></b>"""
