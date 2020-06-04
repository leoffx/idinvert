````python
#
# Clone Git
#
!git clone https://github.com/pascalherrmann/idinvert
!git checkout 128x128_RecW
%cd /content/idinvert

#
# Imports
#
%tensorflow_version 1.x
import tensorflow as tf
print(tf.__version__)

import numpy as np
import PIL
import pickle

import imageio

from google.colab import files

# source code
import dnnlib
import dnnlib.tflib as tflib


#
# Mount G-Drive
#
from google.colab import drive
drive.mount('/content/gdrive')
!cd /content/gdrive/My\ Drive/Public/ && ls

#
# copy data over
#
!mkdir datasets
!mkdir datasets/ffhq_training
!cp /content/gdrive/My\ Drive/Public/ffhq/ffhq-r0[2,3,4,5,6].tfrecords ./datasets/ffhq_training/
!cp "/content/gdrive/My Drive/Kopie von ffhq-r07.tfrecords" ./datasets/
!cd ./datasets/ffhq_training && ls -sh
```