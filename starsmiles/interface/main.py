import numpy as np
import pandas as pd

from starsmiles.ml_logic.proc_pred import load_image, preproc_image, predict

def make_prediction()-> None:

    image_to_load = input('Enter the path to your image: ')

    image = load_image(image_to_load)

    proc_image = preproc_image(image)

    predict(proc_image)



if __name__ == '__main__':
    try:
        make_prediction()
    except:
        import sys
        import traceback

        import ipdb
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        ipdb.post_mortem(tb)
