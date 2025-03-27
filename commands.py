from utils import verify_user, check_token

#Code 1 By Tech Shreyansh
#@Client.on_message..........
#async def start(...........

    data = message.command[1]
    if data.split("-", 1)[0] == "verify": # set if or elif it depend on your code
        userid = data.split("-", 2)[1]
        token = data.split("-", 3)[2]
        if str(message.from_user.id) != str(userid):
            return await message.reply_text(
                text="<b>⚠️ Invalid verification link format!</b>",
                protect_content=True
            )
        is_valid = await check_token(client, userid, token)
        if is_valid == True:
            await message.reply_text(
                text=f"<b>✅ Verification Successful!\n👋 Hello {message.from_user.mention},You now have full access until midnight.📂 You can now access all files.</b>",
                protect_content=True
            )
            await verify_user(client, userid, token)
        else:
            return await message.reply_text(
                text="<b>⌛ Verification link expired!\n\nPlease generate a new verification link !</b>",
                protect_content=True
            )

#Code 2 By Tech Shreyansh
# new code from here :- 
# where you want to add your verification 
# this is the code where user get shortlink and verification message 

from utils import check_verification, get_token
from info import VERIFY, VERIFY_TUTORIAL, BOT_USERNAME


#Code 2 By Tech Shreyansh
#@Client.on_message..........
#async def...........

    if not await check_verification(client, message.from_user.id) and VERIFY == True:
        btn = [[
            InlineKeyboardButton("Verify", url=await get_token(client, message.from_user.id, f"https://telegram.me/{BOT_USERNAME}?start="))
        ],[
            InlineKeyboardButton("How To Open Link & Verify", url=VERIFY_TUTORIAL)
        ]]
        await message.reply_text(
            text="<b>🔒 Verification Required\n\nYou need to verify before accessing files!\nClick below to verify:</b>",
            protect_content=True,
            reply_markup=InlineKeyboardMarkup(btn)
        )
        return
