import nextcord
from nextcord.ext import commands

client = commands.Bot(command_prefix='$')

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="빨간약", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("빨간약을 선택하셨군요")
        self.value = "RED"
        self.stop()

    @nextcord.ui.button(label="파란약", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("파란약을 선택하셨어요")
        self.value = "BLUE"
        self.stop()

@client.event
async def on_ready():
    print('봇이 켜짐')

@client.command(name="button")
async def button(ctx):
    view = Confirm()
    await ctx.send("빨간약과 파란약이 있어요", view=view)

    await view.wait()

    if view.value == "RED":
        print("Comfirmed")
    if view.value == "BLUE":
        print("Cancelled")

client.run('OTE0MzI1NDM4OTgwMDQ2ODQ5.YaLZ6w.wA03HrvTtbVIr5-6sELcUNzRQNg')