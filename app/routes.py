from app import app
from flask import jsonify, make_response, request, render_template
from detector import performDetect
import numpy as np
from cv2 import *
import os

@app.route('/yolov4')
def index():
    return render_template('homepage.html')

@app.route('/traffic_sign')
def index2():
    return render_template('homepage.html')

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
    boundingbox = performDetect(imageContent=img)

    response_body = {
        "user-name": user_name,
        "image-name": image_name,
        "boundingbox": boundingbox
    }

    res = make_response(jsonify(response_body), 201)

    return res


@app.route('/traffic_sign/detection',  methods=['POST'])
def detecting2():
    user_name = request.form.get('user-name')
    image_name = request.form.get('image-name')
    image = request.files.get('image').read()

    # convert string data to numpy array
    npimg = np.fromstring(image, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    # get bounding box
    boundingbox = performDetect(imageContent=img,
        thresh = 0.4,
        configPath="./cfg/yolov4_custom_test.cfg", 
        weightPath="./yolov4_custom_train_final.weights",
        metaPath="./cfg/yolov4-custom.data")

    response_body = {
        "user-name": user_name,
        "image-name": image_name,
        "boundingbox": boundingbox
    }

    res = make_response(jsonify(response_body), 201)

    return res