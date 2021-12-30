import os
import cv2

# input_dir = './Original/'
# output_dir = './Original_PNG/'
# os.makedirs(output_dir, exist_ok = True)

# for imgfile in os.listdir(input_dir):
#     print ("file : " + imgfile)
#     img = cv2.imread(input_dir + imgfile)
#     outfile = imgfile.split('.')[0] + '.png'
#     cv2.imwrite(output_dir+outfile, img)
    
    
input_dir = 'images/'
output_dir = './Original_PNG/'
os.makedirs(output_dir, exist_ok = True)

for imgfile in os.listdir(input_dir):
    print ("file : " + imgfile)
    img = cv2.imread(input_dir + imgfile)
    outfile = imgfile.split('.')[0] + '.png'
    cv2.imwrite(outfile, img)    