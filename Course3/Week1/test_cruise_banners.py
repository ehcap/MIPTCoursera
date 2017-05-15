import pandas as pd
import os.path as path


def convert_file():

    with open('Week3/umn_foursquare_datasets/checkins.dat') as fRead, \
            open('Week3/umn_foursquare_datasets/checkins.cvs','w') as fWrite:
        i=0
        for line in fRead:
            rowItems = map(lambda x:x.strip(), line.split('|'))
            if len(rowItems)>1 and ( rowItems[3]=='' or rowItems[4]==''):
                fWrite.write(','.join(rowItems))
            #line = ','.join(map(lambda x:x.strip(), fRead.readline().split('|')))

def main():
    if not path.isfile('Week3/umn_foursquare_datasets/checkins.cvs'):
        convert_file()
    dt=pd.read_csv('Week3/umn_foursquare_datasets/checkins.cvs')
    #print dt.length()

if __name__ == '__main__':
    main()
