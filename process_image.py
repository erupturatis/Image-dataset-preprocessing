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
    def reshape_image(img_path, x:int = 128, y:int = 128):
        
        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)

        dim = (x, y)

        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        status = cv2.imwrite(img_path, resized)


    @staticmethod   
    def rescale_image(img_path, scale:float):
        if scale>100:
            scale = scale/100

        img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
        dim = (img.shape[0]*scale, img.shape[1]*scale)

        resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
        status = cv2.imwrite(img_path, resized)




class ProcessDataset(object):

    img_paths = list()

    def __init__(self) -> None:
        pass

    def __call__(self, dataset_name, x:int, y:int) -> None:
        self.resize_dataset(dataset_name,x,y)
        

    def resize_dataset(self, dataset_name:str, x:int, y:int):
        self.clone_dataset(dataset_name)
        self.get_paths(f'{dataset_name}_processed')
        self.resize_path_images(x,y)


    def rescale_dataset(self, dataset_name:str, scale:float):
        self.clone_dataset(dataset_name)
        self.get_paths(f'{dataset_name}_processed')
        self.resize_path_images(scale)


    def rescale_path_images(self, scale):
        
        for image in self.img_paths:
            ProcessImage.rescale_image(image, scale=scale)


    def resize_path_images(self,x,y):
        i = 0
        for image in self.img_paths:
            ProcessImage.reshape_image(image,x,y)
            i+=1
            if i%100 == 0:
                print(i)


    def get_paths(self, name:str):
        for path,dirs,files in os.walk(name):
            for filename in files:
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    fullname = os.path.abspath(os.path.join(path,filename))
                    self.img_paths.append(fullname)
    

    @staticmethod
    def clone_dataset(dataset_name:str):

        from_directory = dataset_name
        to_directory = f"{dataset_name}_processed"
        print("start clone")
        shutil.copytree(from_directory, to_directory)
        print("cloned")