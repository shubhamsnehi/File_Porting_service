import os
import pandas as pd
from simpledbf import Dbf5


class DataPort:

    # For '.xls' and '.xlsx' files
    @staticmethod
    def xlsxtocsv(file_bytes):
        try:
            tempfilepath = './TempFiles/TempExcelCsv.csv'
            df = pd.DataFrame(pd.read_excel(file_bytes))
            df.to_csv(tempfilepath, '|')
            print("Data ported form '.xls' to '.csv")
            return tempfilepath
        except:
            print("Unable to port from '.xls' to '.csv")
            return

    # For '.dbf' files
    @staticmethod
    def dbftocsv(blob):
        tempfilepath = './TempFiles/SALE_DTL_DBF.csv'
        try:
            blob.download_to_filename('./TempFiles/Tempdbf.DBF')
            dbf = Dbf5('./TempFiles/Tempdbf.DBF', codec='utf-8')
            dbf.to_dataframe().to_csv(tempfilepath, '|')
            print("Data ported from '.dbf' to '.csv")
            return tempfilepath
        except:
            return print("Unable to port from '.dbf' to '.csv")

    # For '.txt'
    @staticmethod
    def txttocsv(blob):
        try:
            blob.download_to_filename('./TempFiles/Temptxt.txt')
            df = pd.DataFrame(pd.read_csv('./TempFiles/Temptxt.txt', delimiter=';'))
            df.to_csv('./TempFiles/TempTxTCsv.csv', '|')
            print("Data ported from '.dbf' to '.csv'")
        except:
            print("Unable to port '.dbf' to '.csv'")

    # Clean Up code
    @staticmethod
    def cleanup():
        folder = './TempFiles'
        if len(os.listdir(folder)) > 0:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.exists(file_path):
                    os.remove(file_path)
        print("Clean Up Done!")
