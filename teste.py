from process_image import ProcessImage as P

import os
import fnmatch
import shutil

from_directory = "Dataset"
to_directory = "Dataset_processed"

shutil.copytree(from_directory, to_directory)