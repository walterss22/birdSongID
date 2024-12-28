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

    # try: 
    #     os.mkdir(os.getcwd()+"/wavData")
    # except:
    #     print("wavData directory already exists")

    # outpath = pjoin(os.getcwd(), 'wavData')
    # print(outpath)
    # print(path)

    if os.getcw

    meta = pd.read_csv(os.getcwd() + "/bird_song/bird_songs_metadata.csv")
    print(meta.shape)
    df = pd.DataFrame()

    for fileName in files:
        # print(fileName[:-4])
        # print(outpath + "/" + fileName[:-4]+".csv")
        try:
            print("trying")
            rate, data = sci.read(pjoin(path, fileName))
            temp = pd.DataFrame(data)
            # print(fileName[:-4])
            temp = temp.T
            csvName = outpath + "/" + fileName[:-4]+".csv"
            
            #match up species name with 
            spec = meta[meta["filename"] == fileName]["name"].values
           
            temp["species"] = spec
            print(temp)

            print("attempt concat")
            df = pd.concat([df, temp], ignore_index=True)
            print(df)

            # df.to_csv(csvName)
            # df.append(temp)
            print(df.shape)
            print("data converted to csv")
        except:
            print(f"file not readable: {fileName}")
            
    df.to_csv("labeledData.csv") 

    # for file in 