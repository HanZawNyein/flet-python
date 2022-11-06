import flet
from flet import Checkbox, Text


def main(page):
    def checkbox_changed(e):
        output_text.value = (
            f"You have learned how to ski : {todo_check.value}"
        )
        page.update()
    output_text = Text()
    todo_check = Checkbox(label="ToDo: Learn how to use ski", value=False, on_change=checkbox_changed)
    page.add(todo_check, output_text)
flet.app(target=main)