from flask import Flask, request, send_file
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
import time
from modules.controller.ConvertController import ConvertController
import boto3

app = Flask(__name__)
CORS(app)

@app.route("/convert", methods=['POST'])
def convert():
    file = request.files['file']
    file_name_prefix = str(time.time_ns())
    filename = secure_filename(file_name_prefix + ".xml")
    file.save(os.path.join("/uploads", filename))

    convert_controller = ConvertController()
    convert_controller.convert_xml_to_excel(file_name_prefix)

    output_path = "/exceloutput/" + file_name_prefix + ".xlsx"

    file = open(output_path, "rb")

    s3 = boto3.client('s3')
    s3.upload_fileobj(file, "dispensing-output", file.name.split('/')[2], ExtraArgs={'ACL': 'public-read'})

    return file_name_prefix + ".xlsx"