import disnake
import datetime


Embed = {
    "error": {
        "title": "**Error**",
        "colour": disnake.Colour.red(),
    },
    "warn": {
        "title": "**Warning**",
        "colour": disnake.Colour.yellow(),
    },
    "success": {
        "title": "**Success**",
        "colour": disnake.Colour.green(),
    },
    "info": {
        "title": "**Info**",
        "colour": disnake.Colour.blurple(),
    },  
}



class Embed():
    def __init__(self, author_name, author_url, author_icon):

        self.author_name = author_name
        self.author_url  = author_url
        self.author_icon = author_icon

    def generate_embed(self, title: str, description: str, color = disnake.Colour.blurple(), thumbnail: str = None, image: str = None,  timestamp = datetime.datetime.now()):

        embed = disnake.Embed(
            title=title,
            description=description,
            colour=color,
            timestamp=timestamp
        )

        if self.author_url and self.author_name and self.author_icon:
            embed.set_author(
                name     = self.author_name,
                icon_url = self.author_icon,
                url      = self.author_url
            )

        if thumbnail:
            embed.set_thumbnail(thumbnail)

        if image:
            embed.set_image(image)

        return embed

    def generate_type_embed(self, type: str, description: str, timestamp = datetime.datetime.now()):
        
        
        embed = disnake.Embed(
        title=Embed[type]["title"],
        description=description,
        colour=Embed[type]["colour"],
        timestamp=timestamp
        )

        return embed
