from FileConfig import FileDtl
from DataPort import DataPort
from BucketHandler import BucketCon
from FileHandler import FileHandler
import argparse


def myargs(argu, filedtl):
    if argu.t:
        filedtl.filetype = str(argu.t)
    else:
        filedtl.filetype = str(argu.type)
    if argu.p:
        filedtl.filepath = str(argu.p)
    else:
        filedtl.filepath = str(argu.path)
    if argu.b:
        filedtl.uploadbucket = str(argu.b)
    else:
        filedtl.uploadbucket = str(argu.bucket)
    return


if __name__ == '__main__':
    # Objects
    myfile = FileDtl.FileDtl()
    dp = DataPort.DataPort()
    fh = FileHandler.FileHandler()
    bconfig = BucketCon.BucketConfig

    # Default Argument
    parser = argparse.ArgumentParser(description='File Porting Arguments.')
    # Adding Arguments with flags
    # Type of File
    parser.add_argument('--type', type=str, default=None,
                        help='for file type')
    parser.add_argument('-t', type=str, default=None,
                        help='for file type')
    # Path of File
    parser.add_argument('--path', type=str, default=None,
                        help='for file type')
    parser.add_argument('-p', type=str, default=None,
                        help='for file type')
    # Destination Bucket of File
    parser.add_argument('--bucket', type=str, default=None,
                        help='for file type')
    parser.add_argument('-b', type=str, default=None,
                        help='for file type')

    args = parser.parse_args()
    myargs(args, myfile)

    # Bucket Connection
    bucket = bconfig.getbucketconn()

    # TestExcel.xls Sale_Dtl.txt SALE_DTL.DBF
    blob = bucket.get_blob(myfile.filePath + '/' + myfile.fileName + myfile.fileType)

    # Handling Files
    tempfilepath = fh.handlefile(myfile, dp, blob)

    # Upload to Bucket
    print(bconfig.uploadtobucket(tempfilepath, myfile, myfile.uploadBucket))

    # Temp Files CLean Up Function
    dp.cleanup()

    # # Get list of files from bucket
    # print(bconfig.getbuckectfilelist(bucket))
