import flet
from flet import Container, ElevatedButton, Page, animation, transform

def main(page: Page):

    c = Container(
        width=150,
        height=150,
        bgcolor="blue",
        border_radius=10,
        offset=transform.Offset(-2, 0),
        animate_offset=animation.Animation(1000),
    )

    def animate(e):
        c.offset = transform.Offset(0,0)
        c.update()

    page.add(
        c,
        ElevatedButton("Reveal!", on_click=animate),
    )

flet.app(target=main)