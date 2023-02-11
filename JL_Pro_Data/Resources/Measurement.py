#from fileinput import filename
#from msilib.schema import File
#from xml.etree.ElementTree import _FileWrite
import cv2
import math
#from trajectory_io import *
import numpy as np
import sys
import os

# To tqqqqqqqqql DD:
#    Please convert this python script to C#, which is an easy case for you!! tql!

def cal_dist(index1, index2, img_path, metric=True):
    """
        Args:
            index1: the user's 1st index click/select.
            index2: the user's 2nd index click/select.
            imageID: current image on the right panel for visualization.
            img_path: path to the image folder.
            metric: use meter or inch. Use meter if true.
        Return:
            dist: distance between two 3d points.
    """
    # read rgb/depth images based on the current ID
    depth_img=cv2.imread(img_path)

    # depth scale: scale of the depth value (fixed)
    # u, v: width/height of an image (fixed)
    # camera intrinsics: cx/cy/fx/fy (fixed)
    depth_scale = 1000
    u ,v = depth_img.shape[0], depth_img.shape[1]
    cx, cy, fx, fy = 321.7210388183594, 234.7798309326172, 603.854736328125, 602.3140869140625

    # d1/d2: real depth value of the point at index1/index2
    # Note that the collected depth image has three channels, but we only need a value at any of the channels. 
    d1 = depth_img[index1[0], index1[1]][0]
    d2 = depth_img[index2[0], index2[1]][0]

    # convert rgbd image to 3d points
    z1 = d1 / depth_scale
    x1 = (u - cx) * z1 / fx
    y1 = (v - cy) * z1 / fy

    z2 = d2 / depth_scale
    x2 = (u - cx) * z2 / fx
    y2 = (v - cy) * z2 / fy

    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

    if metric: 
        return dist
    else:
        return dist/0.0254


def main_ex(index1_a,index1_b,index2_a,index2_b, img_path, metric):
    try:
        index1 = [int(index1_a), int(index1_b)]
        index2 = [int(index2_a), int(index2_b)]

        dist = cal_dist(index1, index2, img_path, metric == "true")
        return dist
    except Exception as e:
        f = open("Python_Error.log", "w")
        f.write(str(e))
        f.close()
        return e

if __name__ == "__main__":
    #1.第一个点x 2.第一个点y 3.第二个点x 4.第二个点y 5.传入地址url 6.单位meter(true)或者inch(false)
    print(main_ex(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6]))

                     