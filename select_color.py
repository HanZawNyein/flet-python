import flet
from flet import Dropdown, ElevatedButton, Page, Text, dropdown


def main(page: Page):
    def button_click(e):
        output_text.value = f"Dropdown value is : {color_dropdown.value}"
        page.update()

    output_text = Text()
    submit_btn = ElevatedButton(text="submit", on_click=button_click)
    color_dropdown = Dropdown(
        width=100,
        options=[
            dropdown.Option("RED"),
            dropdown.Option("GREEN"),
            dropdown.Option("BLUE")
        ]
    )
    page.add(color_dropdown, submit_btn, output_text)


flet.app(target=main)
