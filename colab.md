# Instructions to run this on Google Colab

### Preparation (only once)
1. Create new Folder on Google Drive for Outputs + Subfolders `images` and `snapshots`
2. Create new Git-Branch and Set up Configuration
    * `config.py` (e.g. specify Google-Drive Path, Generator-Pickle, maybe Encoder-Pickle, Resolution, Data-Dir (can be in gDrive, too!))
    * do further adjustments, if needed 
    
### Start Job
Open a notebook and execute the following:

1. Clone this repo and check out correct branch

```python
!git clone https://github.com/pascalherrmann/idinvert
%cd /content/idinvert
!git checkout <name of correct branch>
````

2. (Import TF and) Mount GDrive to access Encoder-Checkpoint, Fixed Generator, Data, Log-Folder

```python
%tensorflow_version 1.x
import tensorflow as tf
print(tf.__version__)

from google.colab import drive
drive.mount('/content/gdrive')
!cd /content/gdrive/My\ Drive/Public/ && ls
```

3. Run Job

```python
!python train_encoder.py
````

### ToDo:
* automatically create drive folders