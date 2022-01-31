import pandas as pd
import requests
import matplotlib.pyplot as plt
import numpy as np

def main():
    #set max rows and columns
    pd.set_option("display.max_rows", 202, "display.max_columns", None)  # shows all columns in the dataframes

    #read data into dataframe
    FFR = pd.read_csv('data/FEDFUNDSRATE.csv') # Extract and transform csv to dataframe
    FFRPC = pd.read_csv('data/FFRPCHNG.csv')
    SPXPC = pd.read_csv('data/SP500.csv')
    NDXPC = pd.read_csv('data/NASDAQCOM.csv')

    # merge data frames
    result = pd.merge(FFR, FFRPC, on='DATE')
    result = pd.merge(result, SPXPC, on='DATE')
    result = pd.merge(result, NDXPC, on='DATE')

    # prints whole DF
    print(result)

    # average SP500 return methods
    # average NDX return methods
    for i in np.arange(-2, 2, 0.25):
        analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['NASDAQCOM_PCH'], i, 'Nasdaq')
        analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], i, 'SP500')

    # graph data
    graphData(result, 'NASDAQCOM_PCH', 'SP500_PCH')

######################################
# calculates the average return of the
# SP500 when federal funds rate are
# above a certain range
######################################
def analysis1(FFR, FFRPC, asset, rateToCompare, assetName):
    FFRsum = 0                          # calculates average federal fund rate during rate hikes
    assetSum = 0                          # sum of specified data set
    n = 0                               # number of entries in set

    for i in range(len(FFRPC)):
        if FFRPC[i] > rateToCompare:    # if the percent change is higher then save
            assetSum += asset[i]
            FFRsum += FFR[i]
            n += 1                      # increment to calculate average

    try:
        assetMean = (assetSum/n)
        FFRmean = (FFRsum/n)
    except:
        pass
    else:
        print(f'{assetMean}% is the average return of the {assetName} when the Federal Fund rate changes {rateToCompare} in a month')
        print(f'The average effective fund rate after this increase is {FFRmean}\n')


def graphData(df, *columnName):
    df.plot(x = 'DATE', y=['FEDFUNDS', 'FEDFUNDS_CH1', *columnName], kind='line')
    plt.show()


main()




