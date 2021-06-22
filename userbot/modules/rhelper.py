""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.dhelp$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.helpmek` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[AZEL](t.me/kicuh)"
        "\n\n[SUPPORT](https://t.me/bibitunggulnexus)"
        "\n\n[JOIN](https://t.me/Deadendzs)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/azelfirdaus/DIABLO-USERBOT/DIABLO-USERBOT/varshelper.txt)")


CMD_HELP.update({
    "Heleppp":
    "`.dhelp`\
\nPenjelasan: Bantuan Untuk DIABLO-USERBOT.\
\n`.mekvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
