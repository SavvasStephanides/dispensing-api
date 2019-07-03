from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import os
import time
from modules.controller.ConvertController import ConvertController

app = Flask(__name__)

@app.route("/convert", methods=['POST'])
def convert():
    file = request.files['file']
    file_name_prefix = str(time.time_ns())
    filename = secure_filename(file_name_prefix + ".xml")
    file.save(os.path.join("/uploads", filename))

    convert_controller = ConvertController()
    convert_controller.convert_xml_to_excel(file_name_prefix)

    output_path = "/exceloutput/" + file_name_prefix + ".xlsx"
    return send_file(output_path, as_attachment=True)