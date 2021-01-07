import socket
import time
import picamera
# Connect a client socket to my_server:8000
# (change my_server to the hostname of your server)
client_socket = socket.socket()
client_socket.connect(('169.254.187.242', 8000)) # Pi3 169.254.251.72 (hostname -I)
# Make a file-like object out of the connection 
connection = client_socket.makefile('wb')
try:
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 16
    camera.iso = 800
    camera.brightness = 55
    # Start a preview and let the camera warm up
    camera.start_preview()
    time.sleep(2)
    # Start recording, sending the output to the connection for 60
    # seconds, then stop
    camera.start_recording(connection, format='h264')
    camera.wait_recording(20)
    camera.stop_recording()
finally:
    connection.close()
    client_socket.close()
