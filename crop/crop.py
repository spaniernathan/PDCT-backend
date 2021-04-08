import numpy as np
import cv2 as cv
import glob

source_path = '../ISICArchive/'

## Get files from source folder
files = glob.glob(source_path + '*.jpg')

## Populate handlers with images
for f in files:
    name = f[15:-4]
    img = cv.imread(f)
    h, w = img.shape[:2]
    margin = min(w, h)
    crop_img = img[0:margin, 0:margin]
    cv.imwrite('./output/crop_'+name+'.jpg', crop_img)
    res = cv.resize(crop_img, (224, 224), interpolation = cv.INTER_CUBIC)
    cv.imwrite('./output/'+name+'.jpg', res)
