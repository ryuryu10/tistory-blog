from json import load
import nextcord
from nextcord.ext import commands
import asyncio
import os

client = commands.Bot(command_prefix='$')

class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @nextcord.ui.button(label="Confirm", style=nextcord.ButtonStyle.danger)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Confirming", ephemeral=True)
        self.value = True
        self.stop()

    @nextcord.ui.button(label="Cancel", style=nextcord.ButtonStyle.blurple)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message("Cancelling", ephemeral=True)
        self.value = False
        self.stop()

@client.event
async def on_ready():
    pass

@commands.command(name="button")
async def button(self, ctx):
    view = Confirm()
    await ctx.send("Do you want to confirm somthing.", view=view)

    await view.wait()

    if not view.value == None:
        print("Timed Out")
    if view.value == True:
        print("Comfirmed")
    if view.value == False:
        print("Cancelled")

client.run('12')