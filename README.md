# pyimage_server

Example of a webserver using Python to generate images on a computer connected over a network. Uses the aiohttp and socketio Python modules. This is an adapted version of https://github.com/andylomas/picam_server designed to work on any computer and generating images made of random coloured squares instead of using the Raspberry Pi camera.

A p5.js sketch is used to create a simple web app to send messages to the server to take pictures, request the images from the server, and display them in a browser.

The code is designed to illustrate handling errors and lost connections, including disabling the 'Take Picture' button in the p5.js sketch if the connection is lost, and re-enabling it when the connection is restored.

The instructions were originally written for use with a Raspberry Pi, which uses the command 'python3' to run Python 3.x. Depending on how you have Python installed on your computer you might need to use a different command to run Python, such as 'py -3' is typically used on Windows.

## Installation

1. Place the files into a suitable project directory.
2. Edit 'server.py' changing the project_root variable to the directory that you used to install the files.
3. Edit 'sketch.js' changing the serverAddress variable to the URL to access the server on the network. If you just want to run this locally rather than over a network you should be able to use 'http://localhost:8080'
4. Install the requirements by changing to the project directory and using 'python3 -m pip install -r requirements.txt'.

### To run the server:

1. cd to the project directory.
2. Run the server using 'python3 server.py'.

### To run the web application:

1. Open a browser on the client computer.
2. Enter the URL to the server such as 'http://localhost:8080', 'http://raspberrypi.local:8080' or 'http://192.168.0.18:8080'.

## Notes

The application saves all the pictures in the images directory of the project directory. These images aren't ever deleted by the server, so it will be necessary to occassionally empty this directory to avoid it filling up and the server running out of disk space.
