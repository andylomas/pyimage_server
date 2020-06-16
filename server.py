from aiohttp import web
import socketio
from PIL import Image
import random
import uuid
import os

print("Starting server.py")

# Change the working directory to the project root
# This line should be changed depending on where you place the code
project_root = 'E:/Users/Andy Lomas/Documents/GitHub/pyimage_server'
os.chdir(project_root)

# Create an images directory if it doesn't already exist
if not os.path.exists(project_root + '/images'):
    print(f'creating images directory in {project_root}')
    os.makedirs(project_root + '/images')
    
# Setup the web server application
app = web.Application()

# Serve requests for index.html
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# Serve request for sketch.js
async def sketch(request):
    with open('sketch.js') as f:
        return web.Response(text=f.read(), content_type='text/javascript')

# Specify callbacks to use when get request for specified routes
app.router.add_get('/', index)
app.router.add_get('/sketch.js', sketch)

# Handle any request using /images/ in the path as a request for
# a static file from the images directory
app.router.add_static('/images/',
                      path=f'{project_root}/images',
                      name='images')

# Attach socketio asynchronous server to the web server application
# to handle messages over sockets
sio = socketio.AsyncServer()
sio.attach(app)

# Client connecting to a socket
@sio.event
def connect(sid, environ):    
    print("connect ", sid)

# Function to generate an image of random coloured squares
def randomImage(sizeX, sizeY):
    # Create a low resolution image with random pixel colours
    im = Image.new('RGB', (sizeX // 16, sizeY // 16))
    pixels = im.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            pixels[x, y] = (
                random.randint(0,255),
                random.randint(0,255),
                random.randint(0,255))

    # Resize the image up to full size, turning each original
    # pixel into a square
    im = im.resize((sizeX, sizeY), Image.NEAREST)
    
    # Return the image as the result of the function
    return im
    
# 'takepicture' received on the socket
@sio.on('takepicture')
async def takepicture(sid, data):
    # Generate a unique name for the image
    uniqueImageName = f'image_{uuid.uuid4()}.jpg'

    # Print message to the console
    print(f'takepicture: sid:{sid}, file:{uniqueImageName}')

    # Generate a random image (since we don't have a camera)
    im = randomImage(1280, 720)
    im.save(f'images/{uniqueImageName}')

    # Send a message to the client with the name of the image file
    await sio.emit('picturetaken', f'images/{uniqueImageName}', to=sid)

# Client disconnect from socket
@sio.event
def disconnect(sid):    
    print('disconnect ', sid)

if __name__ == '__main__':
    # If we're running this file directly, start the web application
    web.run_app(app)
