from math import pi
import flet
from flet import Container, ElevatedButton, Page, alignment, animation, transform

def main(page: Page):

    c = Container(
        width=100,
        height=70,
        bgcolor="blue",
        border_radius=5,
        rotate=transform.Rotate(0, alignment=alignment.center),
        animate_rotation=animation.Animation(duration=300, curve="bounceOut"),
    )

    def animate(e):
        c.rotate.angle += pi / 2
        page.update()

    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.spacing = 30
    page.add(
        c,
        ElevatedButton("Animate!", on_click=animate),
    )

flet.app(target=main)