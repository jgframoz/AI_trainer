import cv2
import numpy as np
import time
import PoseDetector as pm

cap = cv2.VideoCapture("new_vids/pexels-tima-miroshnichenko-5319753.mp4")

dic = {'right arm': [12,14,16], 'left arm': [11,13,15], 'right back': [12,24,26], 'left back': [25,23,11], 'right leg': [30,26,24], 'left leg': [23,25,29], 'right arm back': [14,12,24], 'left arm back': [13,11,23]}

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0
while True:
	success, img = cap.read()
	#img = cv2.resize(img, (1280, 720))
	# img = cv2.imread("AiTrainer/test.jpg")
	img = detector.findPose(img, False)
	lmList = detector.findPosition(img, False)
	# print(lmList)
	if len(lmList) != 0:
		# Right Arm
		#angle = detector.findAngle(img, 12, 14, 16)

		#p1, p2, p3 = dic['right leg']
		#angle = detector.findAngle(img, p1, p2, p3)



		p1, p2, p3 = dic['right leg']
		angle = detector.findAngle(img, p3, p2, p1)
		p1, p2, p3 = dic['left leg']
		angle = detector.findAngle(img, p3, p2, p1)


		# # Left Arm
		#angle = detector.findAngle(img, 11, 13, 15,False)
		#per = np.interp(angle, (210, 310), (0, 100))
		#bar = np.interp(angle, (220, 310), (650, 100))
		# print(angle, per)

		
	cTime = time.time()
	fps = 1 / (cTime - pTime)
	pTime = cTime
	#cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

	cv2.imshow("Image", img)
	cv2.waitKey(1)


