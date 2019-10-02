import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import threading
import time
import csv

#----------- Funcs

#----------- Main

class Rec:
	def __init__(self, data, NumbOnScreen, frameNumb ):
		self.data = data
		self.NumbOnScreen = NumbOnScreen
		self.frameNumb = frameNumb

qrArray = set()
cam = cv2.VideoCapture(0)	#cam handle
font = cv2.FONT_HERSHEY_DUPLEX
i = 0
frameCount = 0

with open('list.csv', 'a', newline='') as f:
	fieldWriter = csv.writer(f)
	fieldWriter.writerow(['data', 'codes shown', 'frame number'])

	while True:
		_, frame = cam.read()

		decodedObjects = pyzbar.decode(frame)
		i = 0
		for obj in decodedObjects:
			
			cv2.putText(frame, str(obj.data), 
						(50,(50 + 30*i)), font, 0.4, (200, 200, 100), 1 )
			i = i + 1

			if str(obj.data) not in qrArray:
				fieldWriter.writerow([str(obj.data), str(i), str(frameCount)])
				qrArray.add(str(obj.data))
		
		cv2.putText(frame, "Esc to exit", 
						(50,470), font, 1, (200, 200, 100), 1 )

		frameCount = frameCount + 1

		cv2.imshow("Frame", frame)

		key = cv2.waitKey(1)
		if key == 27:
			break
	f.close()

cam.release()
cv2.destroyAllWindows() 