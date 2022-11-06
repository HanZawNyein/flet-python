import flet
from flet import ListView,Page,Text

def main(page:Page):
    lv = ListView(expand=1,spacing=10,item_extent=50)
    page.add(lv)
    for i in range(5000):
        lv.controls.append(Text(f"line {i}"))

        if i % 500 == 0:
            page.update()
    page.update()

flet.app(target=main)