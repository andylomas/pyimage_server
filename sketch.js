// Global variables
let socket;
let button;
let currentImage;

function setup() {
  // Create a canvas to fill the window
  createCanvas(windowWidth, windowHeight);
  background(20, 40, 80);

  // Take Picture button
  button = createButton('Take Picture');
  button.position(50, 50);
  button.mousePressed(sendTakePicture);

  // Address of the web server. Change this address to the
  // server you're running on
  const serverAddress = 'http://localhost:8080';

  // Connect to the server using a socket
  socket = io.connect(serverAddress);
  
  // Specify a function to call every time a 'picturetaken' message
  // is received
  socket.on('picturetaken',
    function(data) {
      // The data received is the name of the image we want to load
      // from the server
      const imageName = data;
      console.log('Picture taken: ' + imageName);

      // Load the image asynchronously with a callback to
      // run when the image has been received from the server
      loadImage(serverAddress + '/' + imageName, 
        function(img) {
          console.log('loadImage: image received');
          // Display the picture in the canvas
          currentImage = img;
          image(currentImage, 0, 0);
        },
        function(err) {
          console.log('loadImage error: ' + err);
        }
      );
    }
  );

  // Callback if the connection has an error
  socket.on('error',
    function(err) {
      console.log('socket error: ' + err);
    }
  )

  // Callback if connection is lost
  socket.on('disconnect',
    function() {
      console.log('disconnected from the server');
      alert('Disconnected from the server');
      // Disable the Take Picture button
      button.attribute('disabled', '');
    }
  );

  // Callback if reconnected
  socket.on('reconnect',
    function() {
      console.log('reconnected to the server');
      alert('Reconnected to the server');
      // Enable the Take Picture button
      button.removeAttribute('disabled');
    }
  );
}

function draw() {
}

// Function that p5.js calls if the window is resized
function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
  
  if (currentImage) {
    // If we've got a current image re-draw it
    image(currentImage, 0, 0);
  } else {
    // Other wise just draw a coloured ba
    background(20, 40, 80);
  }
}

// Function to send a 'takepicture' message to the server
function sendTakePicture() {
  console.log('sendTakePicture: emitting takepicture');
  socket.emit('takepicture', '');
}
