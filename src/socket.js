
var io = require('socket.io').listen(4567);
var roomName;
var flag = 0;
io.on('connection', function (socket) {
    console.log('connect');
    var instanceId = socket.id;

    socket.on('msg', function (data) {
        if(data === "complete"){
          flag = 1;
        }
        if(flag == 1){
          console.log(data);
          io.sockets.emit('msg', "jot");
          flag = 0;
        }
    })
});
