# Copyright (c) 2019, NVIDIA CORPORATION. All rights reserved.
#
# This work is licensed under the Creative Commons Attribution-NonCommercial
# 4.0 International License. To view a copy of this license, visit
# http://creativecommons.org/licenses/by-nc/4.0/ or send a letter to
# Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

"""Global configuration."""

#----------------------------------------------------------------------------
# Paths.

result_dir = 'results'
data_dir = 'datasets'
cache_dir = 'cache'
run_dir_ignore = ['results', 'datasets', 'cache']

#----------------------------------------------------------------------------

RESOLUTION = 128
DESC = ""
DATA_DIR = "/content/gdrive/My Drive/Kopie von ffhq-r07.tfrecords"
PICKLE_DIR = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Decoder_TF/00000-sgan-ffhq128-1gpu/network-snapshot-011489.pkl"

ENCODER_PICKLE_DIR = None
# Encoder
GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Encoder_TF/128x128_RecW" # 128X128 Weighted Rec Loss
#GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Encoder_TF/128x128_All_Losses" # 128X128 ALL!
#GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Encoder_TF/128x128_Only_Rec"   # 128x128 Only Rec!
#GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Encoder_TF/128x128_Weighted"   # 128x128 Weighted!

# Decoder
#GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Decoder_TF/128x128_StyleGAN"
#GDRIVE_PATH = "/content/gdrive/My Drive/Public/tensorboards_shared/Training_Decoder_TF/64X64_StyleGAN"

# only for decoer
TIME = 0
KIMG = 0

'''

ToDo:
* copy data
* connect GDrive
* make sure the sub-directories 'images' and 'snapshots' exist





Later:
* automatically create sub-dirs
'''
