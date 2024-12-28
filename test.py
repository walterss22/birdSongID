"""
Author: Scott Walters

This is the main file for the project, this file is used to call all necessary funcitons to utilize the application
"""

import scipy
import sklearn 
import pandas as pd
from transform import transform    

def main():
    # make sure that the data has been labelled properly
    transform()

    df = pd.read_csv("labeledData.csv")
    # data = 
    
    return False

if __name__ == "__main__":
    main()