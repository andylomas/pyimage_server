# pyimage_server

Example of a webserver using Python to generate images on a computer connected over a network. Uses the aiohttp and socketio Python modules. This is an adapted version of https://github.com/andylomas/picam_server designed to work on any computer.

A p5.js sketch is used to create a simple web app to send messages to the server to take pictures, request the images from the server, and display them in a browser.

The code is designed to illustrate handling errors and lost connections, including disabling the 'Take Picture' button in the p5.js sketch if the connection is lost, and re-enabling it when the connection is restored.

## Installation

1. Place the files into a suitable project directory such as /home/pi/code/python/pyimage_server.
2. Edit 'server.py' changing the project_root variable to the directory that you used to install the files.
3. Edit 'sketch.js' changing the serverAddress variable to the URL to access the raspberry pi on the network.
4. Install the requirements by cd-ing to the project directory and using 'python3 -m pip install -r requirements.txt'.

To run the server:

1. cd to the project directory.
2. Run the server using 'python3 server.py'.

## Notes

The application saves all the pictures in the images directory of the project_root. These images aren't ever deleted by the server, so it will be necessary to occassionally empty this directory to avoid it filling up and the server running out of disk space.
