import picamera
from datetime import datetime
import os

def files_to_delete(rootfolder):
	return sorted((os.path.join(dirname,filename) 
        for dirname,dirnames, filenames in os.walk(rootfolder)
	for filename in filenames),key=lambda fn: os.stat(fn).st_mtime),reversed==True

def free_space_up_to(free_bytes_required,rootfolder):
	file_list=files_to_delete(rootfolder)
	delete_file_list=file_list[0]
	
	while delete_file_list:
		
		statv=os.statvfs(rootfolder)
		free=(statv.f_frsize*statv.f_bavail)/1024
		if free >= free_bytes_required:
			break
		os.remove(delete_file_list.pop())  
#4 gigabytes of free space
free_space_up_to(4190045,"/home/pi/video")
with picamera.PiCamera() as camera:
	for filename in camera.record_sequence(
		'/home/pi/video/trip_'+datetime.now().strftime("%m_%d_%Y_%H_%M_%S_seq_")+'%02d.h264' %i for i in range(1440)):
		camera.wait_recording(60)
