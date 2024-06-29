from wedding.util.template_util import get_template
from wedding.util.photos_util import all_photos


if __name__ == "__main__":
    template = get_template(file_name="index.html.j2")

    with open(f"./app/index.html", "w", encoding="UTF-8") as file:
        file.write(
            template.render(photos=all_photos(path="app/assets/"))
        )
