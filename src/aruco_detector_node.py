#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from aruco_detector.srv import *
from geometry_msgs.msg import Point

import numpy as np
import cv2
import cv2.aruco as aruco
from cv_bridge import CvBridge, CvBridgeError

bridge = CvBridge()

def findArucoMarkers(image, dictionary, debug):
    parameters =  aruco.DetectorParameters_create()
    aruco_dict = aruco.Dictionary_get(dictionary)
    corners, ids, rejectedImgPoints = aruco.detectMarkers(image, aruco_dict, parameters=parameters)
    if debug:
        debugImage = aruco.drawDetectedMarkers(image, corners)
        cv2.namedWindow('debug')
        cv2.imshow('debug', debugImage)
        cv2.waitKey(0)
        cv2.destroyWindow('debug')
        print(corners)

    return corners, ids

def handleGetCorners(req):
    response = GetCornersResponse()

    if req.dictionary != 0:
        dictionary = req.dictionary - 1
    else:
        dictionary = aruco.DICT_ARUCO_ORIGINAL

    print("handle", req.image.height, req.image.width)
    image = bridge.imgmsg_to_cv2(req.image)
    corners, ids = findArucoMarkers(image, dictionary, False)

    if corners is None or ids is None:
        print("Did not find any markers.")
        return response

    for i in xrange(0, len(ids)):
        response.ids.append(ids[i][0])

    for i in xrange(0, len(corners)):
        points = corners[i][0]
        p = Point(points[0][0], points[0][1], 0)
        response.upper_left.append(p)
        p = Point(points[1][0], points[1][1], 0)
        response.upper_right.append(p)
        p = Point(points[2][0], points[2][1], 0)
        response.lower_right.append(p)
        p = Point(points[3][0], points[3][1], 0)
        response.lower_left.append(p)

    print(response)
    return response

def main():
    rospy.init_node('aruco_detector')
    s = rospy.Service('/aruco_detector/get_corners', GetCorners, handleGetCorners)
    print("Ready")
    rospy.spin()

if __name__ == "__main__":
    main()