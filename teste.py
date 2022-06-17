from process_image import ProcessDataset 
import os
import fnmatch
import shutil
import cv2

img = cv2.imread("im am.gif", cv2.IMREAD_UNCHANGED)
dim = (128, 128)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
status = cv2.imwrite("im am1.gif", resized)