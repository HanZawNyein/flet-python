import os
import flet
from flet import Container, Page, Row, Text, alignment, border, border_radius, colors

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"


def main(page: Page):
    r = Row(wrap=True, scroll="always", expand=True)
    page.add(r)
    for i in range(500):
        r.controls.append(
            Container(
                Text(f"Item {i}",color=colors.PURPLE_300),
                width=100,
                height=100,
                alignment=alignment.center,
                bgcolor=colors.AMBER_100,
                border=border.all(1, colors.AMBER_400),
                border_radius=border_radius.all(5)
            )
        )
    page.update()
flet.app(target=main)
