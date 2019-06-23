from flask import render_template
from app import app

import cv2
import numpy as np
import os

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    create_image()
    return render_template('index.html', title='Home', user=user)

ROWS=512
COLS=512
SQUARE=10
def create_image():
    img = np.zeros([ROWS, COLS])
    for i in range(min(ROWS-SQUARE, COLS-SQUARE)):
        for j in range(i-SQUARE, i+SQUARE):
            if j < 0:
                continue
            for k in range(i-SQUARE, i+SQUARE):
                if k < 0:
                    continue 
                img[j, k] = 255
    dir_path = os.path.dirname(os.path.realpath(__file__))
    cv2.imwrite(os.path.join(dir_path, "static/img-gen.jpg"), img)

    
    

