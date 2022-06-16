import cv2

import os
import fnmatch
import shutil

class ProcessImage(object):

    def __init__(self) -> None:
        pass
    
    def test(self):
        pass
    
    @staticmethod
    def get_image(image_path, image_name):
        pass

    @staticmethod
    def reshape_image(img, x:int = 128, y:int = 128):
        print("reshaped")

    @staticmethod   
    def rescale_image(img, scale:int):
        print("rescaled")


class ProcessDataset(object):

    img_paths = list()

    def __init__(self) -> None:
        pass

    def __call__(self, dataset_name) -> None:
        print("called")
        self.clone_dataset(dataset_name)


    def get_paths(self):
        for path,dirs,files in os.walk('Dataset'):
            for filename in files:
                if filename.endswith(('.jpg', '.jpeg', '.gif', '.png')):
                    fullname = os.path.abspath(os.path.join(path,filename))
                    print(fullname)
                    self.img_paths.append(fullname)
    

    @staticmethod
    def clone_dataset(dataset_name:str):

        from_directory = dataset_name
        to_directory = f"{dataset_name}_processed"

        shutil.copytree(from_directory, to_directory)