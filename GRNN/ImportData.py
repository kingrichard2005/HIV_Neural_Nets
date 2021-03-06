import csv
import numpy as np

def placeDataIntoArray(fileName):
    try:
        with open(fileName, mode='rbU') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',', quotechar=' ')
            dataArray = np.array([row for row in datareader], dtype=float, order='C')

        if (min(dataArray.shape) == 1): # flatten arrays of one row or column
            return dataArray.flatten(order='C')
        else:
            return dataArray

    except:
        print "error placing data into array for {}.".format(fileName)
        
#------------------------------------------------------------------------------
def getAllOfTheData():
    try:
        try:
            data    = placeDataIntoArray('data.csv')
            #data    = placeDataIntoArray(os.path.join(os.getcwd(), 'data.csv'))
        except:
            print("data error")
        try:
            targets = placeDataIntoArray('targets.csv')
            #targets = placeDataIntoArray(os.path.join(os.getcwd(), 'targets.csv'))
        except:
            print("targets error")
    except:
        print "error getting all of data"
    return data, targets

def rescaleTheData(data):
    try:
        # 1 degree of freedom means (ddof) N-1 unbiased estimation
        dataVar = data.var(axis = 0, ddof=1)
        dataMean = data.mean(axis = 0)

        for i in range(data.shape[0]):
            data[i,:] = (data[i,:] - dataMean)/np.sqrt(dataVar)

        return data
    except:
        print "error rescaling the data"
