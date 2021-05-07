import os.path
from datetime import datetime


class FileDtl:

    def __init__(self):
        self.filePath = None
        self.fileName = None
        self.fileDate = datetime.now()
        self.fileType = None
        self.uploadBucket = None

    # Properties, Getters and Setters
    # File Arguments
    # @property
    # def fileargs(self, args):

    # File Path
    @property
    def filepath(self):
        return self.filePath

    @filepath.setter
    def filepath(self, path):
        pathstr = path.split('/')
        self.filename = pathstr[len(pathstr) - 1]
        self.filePath = '/'.join(pathstr[0:len(pathstr) - 1])

    # File Name
    @property
    def filename(self):
        return self.fileName

    @filename.setter
    def filename(self, file):
        self.fileName = os.path.splitext(file)[0]
        self.filetype = os.path.splitext(file)[1]

    # File Type
    @property
    def filetype(self):
        # self.fileType = os.path.splitext(self.fileName)[1]
        return self.fileType

    @filetype.setter
    def filetype(self, file):
        self.fileType = file

    # File Date
    @property
    def filedate(self):
        self.fileDate = datetime.now()
        return self.fileDate

    @filedate.setter
    def filedate(self, val):
        self.fileDate = val

    # Upload Bucket Name
    @property
    def uploadbucket(self):
        return self.uploadBucket

    @uploadbucket.setter
    def uploadbucket(self, bucketname):
        self.uploadBucket = bucketname
