import os
import subprocess as sb
from subprocess import call,Popen, PIPE


path = "images"
output_path="results"
f = open('data/inputs.names', 'w')
for file in os.listdir(path):
	f.write(path+"/"+file+"\n")
f.close()
command = "./darknet detect cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights "+output_path
os.system(command)
