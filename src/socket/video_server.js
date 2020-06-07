var io = require('socket.io').listen(4567);
var flag = new Array();
var idx = 0;
var clients = new Array();
var check1 = 0;
var check2 = 0;
io.on('connection', function (socket) {
    console.log(socket.id);
    socket.on('ready', function (data) {
         clients[idx] = socket.id;
         console.log(socket.id);
         console.log(data);
         flag[idx] = data;
         var tmp = data.split('.');
         io.to(socket.id).emit('number',{value: String(idx)});
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
            var id = data.split('.');
            id = id[0];
            var spawn = require('child_process').spawn;
            var top = spawn('python3.6', ["./down.py", data]);
            top.stdout.on('data', (data) => {
//	      console.log(`stdout: ${data}`);
	    });

	    top.stderr.on('data', (data) => {
 	      console.log(`stderr: ${data}`);
	    });

	    top.on('close', (code) => {
  	      console.log(`child process exited with code ${code}`);
	    });
            io.to(clients[id]).emit("video_result", "complete"); 
           /*var exec = require('child_process').exec,
              ls;
            ls = exec("python3.6 down.py " + data, function (error, stdout, stderr) {
                console.log('stderr: ' + stderr);
                if (error !== null) {
                        console.log('exec error: ' + error);
                }
            });
	    console.log("download done")*/
   });
   socket.on('voice', function (data) {
         console.log(data);
         var id = data.split('.');
         id = id[0];
         var exec = require('child_process').exec,
              ls;
         ls = exec("python3.6 subtitle.py --video " + data, function (error, stdout, stderr){
                console.log('stderr: ' + stderr);
                io.to(clients[id]).emit("voice_result", "complete");
                if (error !== null) {
                        console.log('exec error: ' + error);
                }
         });
    })
});
