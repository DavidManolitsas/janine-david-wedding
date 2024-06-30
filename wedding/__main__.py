from wedding.util.template_util import get_template
from wedding.util.photos_util import all_photos
from wedding.model.album import Album


if __name__ == "__main__":
    template = get_template(file_name="index.html.j2")

    albums = [
        Album("index.html.j2", "./app/index.html", "app/assets/images/getting-ready"),
        Album("bridal-party.html.j2", "./app/bridal-party.html", "app/assets/images/bridal-party"),
        Album("ceremony.html.j2", "./app/ceremony.html", "app/assets/images/ceremony"),
        Album("couple.html.j2", "./app/couple.html", "app/assets/images/couple"),
        Album("first-look.html.j2", "./app/first-look.html", "app/assets/images/first-look"),
        Album("group-photos.html.j2", "./app/group-photos.html", "app/assets/images/group-photos"),
        Album("reception.html.j2", "./app/reception.html","app/assets/images/reception")
    ]

    for album in albums:
        template = get_template(file_name=album.template)

        with open(album.target, "w", encoding="UTF-8") as file:
            file.write(
                template.render(photos=all_photos(path=album.source))
            )
