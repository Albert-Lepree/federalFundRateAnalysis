import pandas as pd
import requests
import matplotlib.pyplot as plt

def main():
    pd.set_option("display.max_rows", 202, "display.max_columns", None)  # shows all columns in the dataframes

    FFR = pd.read_csv('data/FEDFUNDSRATE.csv') # Extract and transform csv to dataframe
    FFRPC = pd.read_csv('data/FFRPCHNG.csv')
    SPXPC = pd.read_csv('data/SP500.csv')

    result = pd.merge(FFR, FFRPC, on='DATE')
    result = pd.merge(result, SPXPC, on='DATE')

    # prints whole DF
    print(result)

    # average SP500 return methods
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], .1)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], .3)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], .5)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], 1)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], -0.1)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], -0.3)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], -0.5)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], -1)
    analysis1(result['FEDFUNDS'], result['FEDFUNDS_CH1'], result['SP500_PCH'], -3)

    # graph data
    graphData(result)

######################################
# calculates the average return of the
# SP500 when federal funds rate are
# above a certain range
######################################
def analysis1(FFR, FFRPC, SPXPC, rateToCompare):
    FFRsum = 0                          # calculates average federal fund rate during rate hikes
    SPXsum = 0                          # sum of specified data set
    n = 0                               # number of entries in set

    for i in range(len(FFRPC)):
        if FFRPC[i] > rateToCompare:    # if the percent change is higher then save
            SPXsum += SPXPC[i]
            FFRsum += FFR[i]
            n += 1                      # increment to calculate average

    SPXmean = (SPXsum/n)
    FFRmean = (FFRsum/n)

    print(f'{SPXmean} is the average return of the SP500 when the Federal Fund rate changes {rateToCompare} in a month')
    print(f'The average effective fund rate after this increase is {FFRmean}\n')


def graphData(df):
    df.plot(x = 'DATE', y=['FEDFUNDS', 'FEDFUNDS_CH1', 'SP500_PCH'], kind='line')
    plt.show()


main()




