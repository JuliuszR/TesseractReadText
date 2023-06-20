from PIL import Image, ImageDraw
import pytesseract
import argparse
import cv2
import os
import ipywidgets as widgets
import numpy as np
from ipywidgets import Checkbox

#image_path = "time.jpg"
#img = cv2.imread(image_path, 1)
video_path = "time10.mp4"
video = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
_, img = video.read()
video.release()

move_x = widgets.IntRangeSlider(
    value=[0, img.shape[1]],
    min=0,
    max=img.shape[1],
    step=1,
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=False,
    readout_format='d',
    layout=widgets.Layout(width='600px'),
)

options = []
for i in range(0, img.shape[0]):
    options += [i]
options.reverse()
    
move_y = widgets.SelectionRangeSlider(
    options = options,
    min=0,
    max=img.shape[0]-1,
    index=(0, img.shape[0]-1),
    orientation= 'vertical',
    layout=widgets.Layout(height='400px'),
    continuous_update=False,
    readout=True,
    readoutFormat='d',
    description='Vertical Crop',
)
angle = widgets.FloatSlider(
    value=0,
    min=-90,
    max=90,
    step=1,
    description='Angle:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
    layout=widgets.Layout(width='100%'),
)
move_alpha = widgets.FloatSlider(
    value=1.0,
    min=0.0,
    max=3.0,
    step=0.1,
    description='Alpha:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)
move_beta = widgets.FloatSlider(
    value=30,
    min=-100,
    max=200,
    step=1,
    description='Beta:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='.1f',
)
checkbox = widgets.Checkbox(
    value=False,
    description='Invert',
    disabled=False,
    indent=False,
    onvalue=1,
    offvalue=0,
)