from app import app
from flask import jsonify, make_response, request
from detector import performDetect
import numpy as np
from cv2 import *

@app.route('/yolov4')
def index():
    return "Hello, YOLO!"


@app.route('/yolov4/detections',  methods=['POST'])
def detecting():
    user_name = request.form.get('user-name')
    image_name = request.form.get('image-name')
    image = request.files.get('image').read()

    # convert string data to numpy array
    npimg = np.fromstring(image, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    # get bounding box
    boudingbox = performDetect(imageContent=img)

    response_body = {
        "user-name": user_name,
        "image-name": image_name,
        "boudingbox": boudingbox
    }

    res = make_response(jsonify(response_body), 201)

    return res
