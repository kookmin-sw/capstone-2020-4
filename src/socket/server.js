var io = require('socket.io').listen(4567);
var flag = new Array();
var idx = 0;
var clients = new Array();

io.on('connection', function (socket) {
    console.log(socket.id);
    socket.on('ready', function (data) {
         clients[idx] = socket.id;
         console.log(socket.id);
         console.log(data);
         flag[idx] = data;
         var tmp = data.split('.');
         io.to(socket.id).emit('number',{value: String(idx) + '.' +  tmp[1]});
         idx ++;
    })
    socket.on('complete', function (data) {
         var id = data.split('.');
         id = id[0];
         console.log(data);
         var a = "";
         a = String(data);
         io.to(clients[id]).emit("upload", "complete");
    })
    socket.on('filter', function (data) {
            console.log(data)
            var exec = require('child_process').exec,
              ls;
            ls = exec("python3.6 down.py " + data, function (error, stdout, stderr) {
                console.log('stderr: ' + stderr);
                if (error !== null) {
                        console.log('exec error: ' + error);
                }
            });
            console.log("download done")
   });
});