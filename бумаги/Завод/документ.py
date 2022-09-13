import disnake

class ОшибкиДокумента:

    неизвестная_ошибка = "неизвестная ошибка документа. Попробуйте обратиться в Ресрублику поддержки"

class Документ:

    def вложение(title: str, description: str, error=None):
        документ = disnake.Embed(
            title=f'**{title}**', description=description, color=disnake.Colour.gold()
        )
        документ.set_thumbnail(url="https://cdn.discordapp.com/avatars/1014576806730408098/f67e71364fdfa1da4695d3d1a6d79092.webp")
        if error:
            readableErr = type(error).__name__
            документ.set_footer(text=f'Самоподписанный документ - {readableErr}')
        else:
            документ.set_footer(text='Самоподписанный документ')

        return документ