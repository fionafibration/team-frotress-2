import dxcam
from PIL import Image
import time

x = 2560 // 2 - 70
y = 1440 // 2 + 350

xoff, yoff = 140, 55


def uber_percentage_tester(dxc):
    frame = None
    while frame is None:
        frame = dxc.grab(region=(x, y, x + xoff, y + yoff))

    img = Image.fromarray(frame)

    img.save("screencap.png")


if __name__ == "__main__":
    camera = dxcam.create()
    input("Ready")
    time.sleep(3)
    uber_percentage_tester(camera)
    print("Done!")
