from mss import mss, tools


def screenshot(
    quantity: int = 1,
    name: str = 'configs/images/screenshot.png',
    top: int = 0,
    left: int = 0,
    width: int = 1920,
    height: int = 1080
):

    with mss() as sct:
        monitor = {
            "top": top,
            "left": left,
            "width": (quantity * width),
            "height": (quantity * height)
        }
        sct_img = sct.grab(monitor)
        tools.to_png(sct_img.rgb, sct_img.size, output=name)
