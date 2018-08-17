import rospy
from aruco_detector.srv import *
import cv2
from cv_bridge import CvBridge, CvBridgeError

def main():
    print("start")
    img = cv2.imread('/tmp/right.png',0)
    rospy.wait_for_service('/aruco_detector/get_corners')
    #cv2.imshow('image',img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    try:
        srv = rospy.ServiceProxy('/aruco_detector/get_corners', GetCorners)
        msg_frame = CvBridge().cv2_to_imgmsg(img)
        resp = srv(msg_frame, 0)
        print(resp)
        return resp
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
    main()