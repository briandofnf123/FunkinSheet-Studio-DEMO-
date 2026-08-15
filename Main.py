import sys
import os
import webview

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main():
    html_file = resource_path("assets/index.html")
    icon_app = resource_path("assets/icon.ico")

    width, height = 1100, 800

    try:
        screen = webview.screens[0]
        x = (screen.width - width) // 2
        y = (screen.height - height) // 2
    except Exception:
        x, y = None, None

    window = webview.create_window("FunkinSheet Studio", html_file, width=width, height=height, x=x, y=y)
    webview.start(http_server=True, icon=icon_app)

if __name__ == "__main__":
    main()