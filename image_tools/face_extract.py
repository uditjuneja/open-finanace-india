import cv2
import sys
import os
import traceback
import urllib.request
import numpy as np

from .config import FACE_BUFFER, SCALE_FACTOR, MIN_NEIGHBORS, MIN_SIZE


class FaceExtract:
    __instance = None

    def __init__(self):
        if self.__instance:
            return self.__instance

        self.face_cascade = cv2.CascadeClassifier(HAAR_CASCADE_PATH)
        self.__instance = self

    def extract_face(self):
        image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        face_coordinates = self.face_cascade.detectMultiScale(
            image_grey,
            scaleFactor=SCALE_FACTOR,
            minNeighbors=MIN_NEIGHBORS,
            minSize=MIN_SIZE,
            flags=0,
        )

        faces = []
        for x, y, w, h in face_coordinates:
            sub_img = image[
                y - FACE_BUFFER : y + h + FACE_BUFFER,
                x - FACE_BUFFER : x + w + FACE_BUFFER,
            ]
            faces.append(sub_img)

        return faces
