from flet import *

def main(page:Page):
    page.window.height=720
    page.window.width=338
    page.theme_mode = "dark"
    page.theme = Theme(colors.CYAN_700)
    page.horizontal_alignment = 'center'
    
    h_alignment='center'
    app_bar = AppBar()
    

    page.update()
app(target=main,assets_dir='assets')