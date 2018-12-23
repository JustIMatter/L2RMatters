import os
import os.path

import mss


def on_exists(fname):

    if os.path.isfile(fname):
        newfile = fname + ".old"
        print("{0} -> {1} ".format(fname, newfile))
        os.rname(fname, newfile)


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 160, "left": 160, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)
