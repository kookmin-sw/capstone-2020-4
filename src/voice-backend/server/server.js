var io = require('socket.io').listen(1234);
var flag = new Array();
var idx = 0;
var clients = new Array();


io.on('connection', function (socket) {
    socket.on('complete', function (data) {
         var id = data.split('.');
         id = id[0];
         console.log(data);
         var a = "";
         a = String(data);
         io.to(clients[id]).emit("abc", "complete");
         console.log("complete");
         var exec = require('child_process').exec,
              ls;
          ls = exec("python3.6 down.py " + data + " & python ../main.py  --dir " + data, function (error, stdout, stderr) {
                console.log('stderr: ' + stderr);
                if (error !== null) {
                        console.log('exec error: ' + error);
                }
                var exec2 = require('child_process').exec,
                     done;
                done = exec2("python /home/ubuntu/voice_classification/server/done.py --dir " + id, function (error, stdout, stderr) {
                     console.log('stderr: ' + stderr);
                     if (error !== null) {
                        console.log('exec error: ' + error);
                      }
                   console.log("voice done")
                 });
//          console.log("done");
               })
          });
        
//           var exec = require('child_process').exec,
//               ls;
//           ls = exec("python ../main.py  --dir " + data, function (error, stdout, stderr) {
//                 console.log('stderr: ' + stderr);
//                 if (error !== null) {
//                         console.log('exec error: ' + error);
//                 }
//           console.log("voice done")
//         });
// //          console.log("done");
//        })

    
   
});
