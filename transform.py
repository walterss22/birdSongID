"""
Author: Scott Walters

This file stores the code taht is necassary to conver the .wav files to a format usable by the scikit-learn model
"""

from dask.distributed import LocalCluster
import scipy.io.wavfile as sci
import os
from os.path import dirname, join as pjoin
import pandas as pd


def transform():

    files = []
    path = os.getcwd() + "/bird_song/wavfiles"
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)

    path += "/"

    try: 
        os.mkdir(os.getcwd()+"/wavData")
    except:
        print("wavData directory already exists")

    outpath = pjoin(os.getcwd(), 'wavData')
    # print(outpath)
    # print(path)


    for fileName in files:
        # print(fileName[:-4])
        # print(outpath + "/" + fileName[:-4]+".csv")
        try:
            print("trying")
            rate, data = sci.read(pjoin(path, fileName))
            # print("file read")
            df = pd.DataFrame(data)
            # print(fileName[:-4])
            # print("data in df")
            csvName = outpath + "/" + fileName[:-4]+".csv"
            # print(csvName)
            df.to_csv(csvName)
            print(df.shape)
            print("data converted to csv")
        except:
            print(f"file not readable: {fileName}")

    # for file in 