from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from flask_restful.reqparse import Argument
from flask_restful import abort
from pdfAnalyzer import PDFAnalyzer
import os

UPLOAD_FOLDER = "./uploads"
ALLOWED_EXTENSIONS = {"pdf"}
app = Flask(__name__)


class FileStorageArgument(Argument):
    def convert(self, value, op):
        if self.type is FileStorage:
            return value
        super(FileStorageArgument, self).convert(**args, **kwargs)


#
# DataApi
#
class DataApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser(argument_class=FileStorageArgument)
        self.parser.add_argument(
            "file", required=True, type=FileStorage, help="pdf file", location="files"
        )
        super(DataApi, self).__init__()

    def allowed_file(self, filename):
        return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS

    def post(self):
        args = self.parser.parse_args()
        pdfFile = args["file"]
        fileName = pdfFile.filename
        if pdfFile and allowed_file(fileName):
            filename = secure_filename(pdfFile.filename)
            pdfFile.save(os.path.join(app.root_path, UPLOAD_FOLDER, filename))
            return ". success"
        else:
            return "failed"


#
# PDFScanner
#

parser = reqparse.RequestParser()
parser.add_argument("filename")


class PDFScanner(Resource):
    def get(self, filename):
        args = parser.parse_args()
        filename = args["filename"]
