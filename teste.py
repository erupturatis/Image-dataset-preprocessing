from process_image import ProcessDataset 
import os
import fnmatch
import shutil
import cv2

DatasetProcessor = ProcessDataset()
DatasetProcessor('DBZ',128,128)