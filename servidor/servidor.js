const net = require('net');
const mqtt = require("mqtt");
var time = require("timers")

const port = 15240; // Port to listen on

const topico = "monitoriaifpe2"

const server = net.createServer((socket) => {
  console.log('Client connected!');

  // Handle incoming data from the client
  socket.on('data', (data) => {
    console.log(`Received topic from client: ${data.toString()}`);

    // Send a response back to the client
    socket.write(topico);
  });

  // Handle client disconnection
  socket.on('end', () => {
    console.log('Client disconnected!');
  });
});

server.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});


const url = 'mqtt://127.0.0.1:1883'



const client = mqtt.connect(url)

function publish(){
    client.publish(topico,"ping")
}

function sleep(ms){
    return new Promise(resolve => setTimeout(resolve, ms))
}
client.on('connect', function () {
    console.log('Connected')
    // Subscribe to a topic
    client.subscribe("teste", function (err) {
      if (!err) {
        // Publish a message to a topic
        for(let i=0;i<10000;i++){
            client.publish(topico, "ping")
            
        }
        
      }
    })
  })