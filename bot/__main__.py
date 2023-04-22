# by <@kaif-00z>

import os
import re

from . import *

print("Starting...")

try:
    bot.start(bot_token=BOT_TOKEN)
except Exception as exc:
    print(exc)


@bot.on(events.NewMessage(pattern="/ping"))
async def ping(event):
    t = time.time()
    x = await event.reply("`Pɪɴɢ!!!`")
    tt = time.time() - t
    p = float(str(tt)) * 1000
    await x.edit(f"Pɪɴɢ: {int(p)}ms")


@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\n🛡️𝚃𝙷𝙸𝚂 𝙸𝚜 𝙰 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙴𝙳𝙸𝙾 𝙰𝙽𝙳 𝙰𝚄𝙳𝙸𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁 𝙱𝙾𝚃🛡️.",
        buttons=[
            [Button.inline("𝙷𝙴𝙻𝙿", data="usei")],
            [
                Button.url(
                    "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="Campus_Bot_Updates.t.me"
                ),
                Button.url("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁", url="https://t.me/MH17_KUNAL"),
            ],
        ],
    )


@bot.on(events.NewMessage(pattern="/help"))
async def help(event):
    await event.reply(
        "🔮𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙴𝙳𝙸𝙾 𝙰𝙽𝙳 𝙰𝚄𝙳𝙸𝙾.\n🔮𝙱𝙾𝚃 𝚃𝙰𝙺𝙴 𝚂𝙾𝙼𝙴 𝚃𝙸𝙼𝙴 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙺𝙴𝙴𝙿 𝙿𝙰𝚃𝙸𝙴𝙽𝙲𝙴."
    )


@bot.on(events.NewMessage(pattern="/yt ?(.*)"))
async def yt(event):
    link = event.pattern_match.group(1) or None
    if not link:
        return await event.reply("`𝙿𝙻𝚉 𝙶𝙸𝚅𝙴 𝙰 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙻𝙸𝙽𝙺`")
    await event.reply(
        "𝙲𝙷𝙾𝙾𝚂𝙴 𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙳𝙾",
        buttons=[
            [
                Button.inline("𝙰𝚄𝙳𝙸𝙾", data=f"audio{link}"),
                Button.inline("𝚅𝙴𝙳𝙸𝙾", data=f"vedio{link}"),
            ],
        ],
    )


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"audio(.*)")))
async def audio(event):
    link = event.pattern_match.group(1).decode("UTF-8")
    x = await event.edit("`𝙵𝚎𝚝𝚌𝚑𝚒𝚗𝚐 𝙳𝚊𝚝𝚊 𝙵𝚛𝚘𝚖 𝚈𝚘𝚞𝚝𝚞𝚋𝚎...`")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "%(id)s.mp3",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"{link}"])
        info_dict = ydl.extract_info(link, download=False)
        audio_title = info_dict.get("title", None)
        audio_duration = info_dict.get("duration", None)
        audio_id = info_dict.get("id")
    audio = audio_id + ".mp3"
    os.system(f"wget https://i.ytimg.com/vi/{audio_id}/maxresdefault.jpg")
    os.rename("maxresdefault.jpg", f"{audio_id}.jpg")
    thumb = audio_id + ".jpg"
    await bot.send_file(
        event.chat_id,
        audio,
        supports_streaming=True,
        thumb=thumb,
        attributes=[
            DocumentAttributeAudio(
                title=audio_title,
                duration=audio_duration,
            )
        ],
    )
    await x.delete()


@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"vedio(.*)")))
async def vedio(event):
    link = event.pattern_match.group(1).decode("UTF-8")
    x = await event.edit("`fetching data from youtube...`")
    ydl_opts = {
        "format": "best",
        "outtmpl": "%(id)s.mp4",
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"{link}"])
        info_dict = ydl.extract_info(link, download=False)
        video_duration = info_dict.get("duration", None)
        video_height = info_dict.get("height", None)
        video_width = info_dict.get("width", None)
        video_id = info_dict.get("id")
    video = video_id + ".mp4"
    os.system(f"wget https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg")
    os.rename("maxresdefault.jpg", f"{video_id}.jpg")
    thumb = video_id + ".jpg"
    await bot.send_file(
        event.chat_id,
        video,
        attributes=[
            DocumentAttributeVideo(
                duration=video_duration,
                w=video_width,
                h=video_height,
                supports_streaming=True,
            )
        ],
        thumb=thumb,
    )
    await x.delete()


@bot.on(events.callbackquery.CallbackQuery(data="usei"))
async def usei(event):
    await event.edit(
        "𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 /𝚢𝚝 𝚆𝙸𝚃𝙷 𝙻𝙸𝙽𝙺\nLike 𝙱𝙴𝙻𝙾𝚆:\n\t/yt https://youtube.com/...",
        buttons=[Button.inline("𝙱𝙰𝙲𝙺", data="back")],
    )


@bot.on(events.callbackquery.CallbackQuery(data="back"))
async def reback(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\n🛡️𝚃𝙷𝙸𝚂 𝙸𝚜 𝙰 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙴𝙳𝙸𝙾 𝙰𝙽𝙳 𝙰𝚄𝙳𝙸𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁 𝙱𝙾𝚃🛡️.",
        buttons=[
            [Button.inline("𝙷𝙴𝙻𝙿", data="usei")],
            [
                Button.url(
                    "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url="Campus_Bot_Updates.t.me"
                ),
                Button.url("𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁", url="https://t.me/MH17_KUNAL"),
            ],
        ],
    )


@bot.on(events.NewMessage(pattern="/eval"))
async def eval(event):
    if event.sender_id != OWNER:
        return
    await event.reply("`Processing ...`")
    cmd = event.text.split(" ", maxsplit=1)[1]
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, event)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    final_output = "**EVAL**: `{}` \n\n **OUTPUT**: \n`{}` \n".format(cmd, evaluation)
    if len(final_output) > 4095:
        with io.BytesIO(str.encode(final_output)) as out_file:
            out_file.name = "eval.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
            )
            await event.delete()
    else:
        await event.reply(final_output)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)


@bot.on(events.NewMessage(pattern="/bash"))
async def bash(event):
    if event.sender_id != OWNER:
        return
    cmd = event.text.split(" ", maxsplit=1)[1]
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    e = stderr.decode()
    if not e:
        e = "No Error"
    o = stdout.decode()
    if not o:
        o = "**Tip**: \n`If you want to see the results of your code, I suggest printing them to stdout.`"
    else:
        _o = o.split("\n")
        o = "`\n".join(_o)
    OUTPUT = f"**QUERY:**\n__Command:__\n`{cmd}` \n__PID:__\n`{process.pid}`\n\n**stderr:** \n`{e}`\n**Output:**\n{o}"
    if len(OUTPUT) > 4095:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "exec.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
            )
            await event.delete()
    await event.reply(OUTPUT)


print("Bot has started...")
bot.run_until_disconnected()
