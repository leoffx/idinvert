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
data_dir = 'datasets/bonsai'
cache_dir = 'cache'
run_dir_ignore = ['results', 'datasets', 'cache']

#----------------------------------------------------------------------------
DESC = ""
GDRIVE_PATH = "/content/drive/MyDrive/results"

RESOLUTION = 512
DATA_DIR = "/content/idinvert/datasets/bonsai"
PICKLE_DIR = "/content/drive/MyDrive/results/network-snapshot-002364.pkl"
ENCODER_PICKLE_DIR = None

# only for generator training
TIME = 0
KIMG = 2364

INCEPTION_PATH = '/content/inception_v3_features.pkl'