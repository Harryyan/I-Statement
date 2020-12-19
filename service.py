from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from upload import UPLOAD_FOLDER, DataApi

app = Flask(__name__)
api = Api(app)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

##
## Actually setup the Api resource routing here
##
api.add_resource(DataApi, "/upload")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
