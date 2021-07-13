import copy
import cv2
import numpy as np

# filename = 'cloud.jpg'
filename = 'cloud1.jpeg'

img = cv2.imread(filename)

# Image meta Data
height, width, channels = img.shape
print(height, width, channels)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 7, 0.04)
print(dst)

# result is dilated for marking the corners, not important
# dst = cv2.dilate(dst, None)

# cv2.imshow("dst1",dst)
# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]


superDst = copy.deepcopy(dst)

superDst[dst < 0.01 * dst.max()] = 202

cv2.imshow("dstAfterFilltration", superDst)
cv2.imshow('dst', img)

# Roies addition.
# Write dest as txt to make it binary "edge" or "not"
k = 9
new_height = int(height / k)
new_width = int(width / k)


print(type(dst))
a_file = open("ndArrayMan4.txt", "w")
a_file.close()


part = 0
startIndexW = 0
startIndexH = 0
flag =0
Threshold = (new_height*new_width)*0.01
while part<k*k:
    # Each part processed , define start Indexes.
    startIndexW = (part % k) * new_width
    startIndexH = (int( part / k )) * new_height
    # Set count for every part.
    count = 0;
    for i in range(startIndexH,startIndexH+new_height-1):
        for j in range(startIndexW,startIndexW+new_width-1):
            if superDst[i, j] != 202:
               # print(count)
                count += 1
    # Edge point statistics
    print ("part ",part," : has ",count," Dots")
    part += 1

#Print grid line
#1) print column lines

#2) print row lines
for i in range(0 , height-1):
    for j in range(0 , width-1):
        if i%new_height == 0 or j%new_width == 0:
            img[i,j] = [0, 255, 255]





cv2.imshow("superDst", img)


feat = cv2.goodFeaturesToTrack(gray, 7, 0.05, 25)

if cv2.waitKey(0) & 0xff == 27:
   cv2.destroyAllWindows()
