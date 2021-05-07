class FileHandler:

    # File Handle Method
    def handlefile(self, myfile, dp, blob):

        if myfile.fileType == '.xls' or myfile.fileType == '.xlsx':
            tempfilepath = dp.xlsxtocsv(blob.download_as_bytes())
            return tempfilepath

        elif myfile.fileType == '.dbf' or myfile.fileType == '.DBF':
            tempfilepath = dp.dbftocsv(blob.download_as_bytes())
            return tempfilepath

        elif myfile.fileType == '.txt' or myfile.fileType == '.TXT':
            tempfilepath = dp.txttocsv(blob.download_as_bytes())
            return tempfilepath
        else:
            return print("Cant Handle File")
