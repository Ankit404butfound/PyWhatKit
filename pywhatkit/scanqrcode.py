import cv2
import webbrowser

def scan():
	cap = cv2.VideoCapture(0)
	detector = cv2.QRCodeDetector()
	while True:
		 _, img = cap.read()
		 data, bbox, _ = detector.detectAndDecode(img)
		 if data:
		 	 a=data
		 	 break
		 cv2.imshow("Pywhatkit QRCODE scanner", img)  
		 if cv2.waitKey(1) == ord("q"):
		 	break
	b=webbrowser.open(str(a))
	cap.release()
	cv2.destroyAllWindows()

scan()
