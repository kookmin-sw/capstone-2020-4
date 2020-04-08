var io = require('socket.io').listen(4567);
var flag = 0;

io.on('connection', function (socket) {
    console.log('connect');
    var instanceId = socket.id;

    socket.on('msg', function (data) {
        if(data === "complete"){
          console.log(data);
        }
        if(data === "isdone"){
          console.log(data);
          socket.emit('msg','done');
          const { spawn } = require('child_process');
          const ls = spawn('./a.out');
          ls.stdout.on('data', (data) => {
             console.log(`stdout: ${data}`);
          });
        }
    })
});