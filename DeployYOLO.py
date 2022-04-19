import torch
from time import time
import cv2

def detect(frame, model):
    frame = [frame]
    results = model(frame)
    print(results.xyxyn[0])
    labels, coords = results.xyxyn[0][:,-1], results.xyxyn[0][:,:-1]
    
    return labels, coords

def draw_box(resutls, frame, classes):
    pass