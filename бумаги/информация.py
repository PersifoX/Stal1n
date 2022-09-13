import datetime
import disnake
import pymongo

#from бумаги.Завод.документ import Документ
from disnake.ext import commands, tasks

embed = disnake.Embed(
    colour=disnake.Colour.gold(),
    timestamp=datetime.datetime.now()
)

class Информация(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name="республика", description="документ о республике")
    async def республика(self, ctx):
        embed = disnake.Embed(title=f'🔨 | Информация о республике **{ctx.guild.name}**', color=disnake.Colour.gold())
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon)

        vlevels = {
        'none':':white_circle: Отсутствует',
        'low':':green_circle: Низкий',
        'medium':':yellow_circle: Средний',
        'high':':orange_circle: Высокий',
        'extreme':':red_circle: Самый высокий'
        }
        embed.add_field(name='Чины республики', value=f'''
        > Всего: **{len(ctx.guild.roles)}**
        > С правами администратора: **{len([r for r in ctx.guild.roles if r.permissions.administrator])}**
        > С правами модератора: **{len([r for r in ctx.guild.roles if r.permissions.kick_members])}**
        > Интеграций: **{len([r for r in ctx.guild.roles if r.managed])}**
        ''')
        embed.add_field(name='Каналы', value=f'''
        > Всего: **{len([c for c in ctx.guild.channels if not isinstance(c, disnake.CategoryChannel)])}**
        > Текстовых: **{len(ctx.guild.text_channels)}**
        > Голосовых: **{len(ctx.guild.voice_channels)}**
        > Категорий: **{len(ctx.guild.categories)}**
        ''')
        embed.add_field(name='Участники', inline=False, value=f'''
        > Всего: **{len(ctx.guild.members)}**
        > Людей: **{len([m for m in ctx.guild.members if not m.bot])}**
        > Машин: **{len([m for m in ctx.guild.members if m.bot])}**
        > Администраторов: **{len([m for m in ctx.guild.members if m.guild_permissions.administrator])}**
        > Модераторов: **{len([m for m in ctx.guild.members if m.guild_permissions.kick_members])}**
        ''')
        dt = ctx.guild.created_at.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)
        if not ctx.guild.owner:
            oww = "**Не имеет владельца**"
        else:
            oww = f"**{ctx.guild.owner}** ({ctx.guild.owner.mention})"
        embed.add_field(name='Прочее', value=f'''
        > Владелец: {oww}
        > Уровень проверки: **{vlevels[str(ctx.guild.verification_level)]}**
        > Дата основания республики: <t:{int(dt.timestamp())}> (<t:{int(dt.timestamp())}:R>)
        ''')

        await ctx.send(embed=embed)



    @commands.slash_command(name="гражданин", description="информация о гражданине")
    async def гражданинinfo(ctx, *, гражданин: disnake.User = None): # b'\xfc'
        if гражданин is None:
            гражданин = ctx.author      
        date_format = "%d %b %Y %I:%M"
        embed = disnake.Embed(color=0xdfa3ff, description=гражданин.mention)
        if гражданин.avatar:
            embed.set_author(name=str(гражданин), icon_url=гражданин.avatar)
            embed.set_thumbnail(url=гражданин.avatar)
        embed.add_field(name="Вступил в республику:", value=f"**{гражданин.joined_at.strftime(date_format)}**")
        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
        embed.add_field(name="Позиция гражданства:", value=str(members.index(гражданин)+1))
        embed.add_field(name="Получил гражданство:", value=f"**{гражданин.created_at.strftime(date_format)}**")

        if len(гражданин.roles) > 1:
            role_string = ' '.join([r.mention for r in гражданин.roles][1:])
            embed.add_field(name="Чины ({}):".format(len(гражданин.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in гражданин.guild_permissions if p[1]])
        embed.add_field(name="Разрешения в этой республике:", value=f"||{perm_string}||", inline=False)
        embed.set_footer(text='ID: ' + str(гражданин.id))

        return await ctx.send(embed=embed)




    @commands.slash_command(name="чин", description="информация о чине (локальном)")
    async def чин(ctx, чин: disnake.Role):
        embed = disnake.Embed(title=f'**🔨 | Информация о чине (локальном) **', color=disnake.Colour.gold(), description=f'{чин.mention}\n')
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in чин.permissions if p[1]])

        embed.add_field(name='Создан:', value=f'**<t:{int(чин.created_at.timestamp())}>**', inline=True)
        embed.add_field(name='Позиция:', value=f'**{чин.position}**', inline=True)
        embed.add_field(name='Цвет:', value=f'**{чин.color}**', inline=True)
        embed.add_field(name='Управляется машиной:', value=f'||**{чин.managed}**||', inline=True)
        embed.add_field(name='Разрешения:', value=f'||{perm_string}||', inline=False)

        await ctx.send(embed=embed)



def setup(bot: commands.Bot):
    bot.add_cog(Информация(bot))