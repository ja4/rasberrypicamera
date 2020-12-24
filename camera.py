import datetime
import time
from picamera import PiCamera


for count in range(60*24):
	date_time = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
	camera = PiCamera()
	camera.resolution = (1024,768)

	#camera.start_preview()
	camera.start_recording("/home/pi/video/"+date_time+"video.h264")
	camera.wait_recording(60)
	camera.stop_recording()
#camera.stop_preview()
	camera.close()   

