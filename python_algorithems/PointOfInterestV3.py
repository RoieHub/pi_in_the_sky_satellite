import os

import cv2
import numpy as np
import sys

filename = sys.argv[1]
filewithoutjpeg=filename[ 0 :len(filename)-5]
img = cv2.imread(filename)
img2 = cv2.imread(filename)
# Image meta Data
height, width, channels = img.shape

print(height, width, channels)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 7, 0.04)
dst[dst < 0.01 * dst.max()] = 202  # This is lazy threshold
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('dst', img)  # Remove from final sunmission.

# Write dest as txt to make it binary "edge" or "not"
k = 4
string = ""


if( not (os.path.isdir(filewithoutjpeg))):
            os.mkdir(filewithoutjpeg)

curretpath=os.path.abspath(os.getcwd())+"/"+filewithoutjpeg+"/"
os.chdir(curretpath)


extension = ".txt"

file_name =  filewithoutjpeg + extension
f= open(file_name, "w+")
f.write(str(height)+","+str(width)+","+str(k*k)+",")

new_height = int(height / k)
new_width = int(width / k)
part = 0
startIndexW = 0
startIndexH = 0
flag = 0
threshold = (new_height*new_width)*0.01
thresh_passed_count = 0
while part < k * k:
    # Each part processed , define start Indexes.
    startIndexW = (part % k) * new_width
    startIndexH = (int(part / k)) * new_height
    # Set count for every part.
    count = 0
    for i in range(startIndexH, startIndexH + new_height - 1):
        for j in range(startIndexW, startIndexW + new_width - 1):
            if dst[i, j] != 202:
                # print(count)
                count += 1
    # Edge point statistics
    # print ("part ",part," : has ",count," Dots")
    if count > threshold:
        print(" good part is ", part)
        thresh_passed_count += 1
        crop_img = img2[startIndexH:startIndexH + new_height - 1, startIndexW:startIndexW + new_width - 1]
        string = str(k) + '-' + str(part)


        f.write(str(part)+",")
        cv2.imwrite(curretpath+string+'-crop_img.jpeg', crop_img)

    part += 1


f.write(str(thresh_passed_count)+"/"+str(part))
f.close()