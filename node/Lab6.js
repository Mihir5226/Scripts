var http =require("http");
var fs = require("fs");
var os =require("os");
var ip =require("ip");


http.createServer(function(req,res)
{  if(req.url ==="/"){
    fs.readFile("./public/index.html", "UTF-8",function(err,body){
    res.writeHead(200,{"Content-Type":"text/html"});
    res.end(body);
    });
}



else if(req.url.match("/sysinfo"))
{ 
    myHostName =os.hostname();
    myIp = ip.address();
   var myServerUptime = os.uptime();

   var totalSeconds =(os.uptime());
   var days = Math.floor(totalSeconds/86400);
   totalSeconds %=86400;
   var hours = Math.floor(totalSeconds/3600);
   totalSeconds %=3600;
   var minutes =Math.floor(totalSeconds/60);
   var seconds = totalSeconds % 60;
   

    myTotalMemory =(os.totalmem()/1000000).toFixed(2) + " MB";
    myFreeMemory =(os.freemem()/1000000).toFixed(2) + " MB";
    numberOfCpu = os.cpus().length;

    var uptime = `${days} days, ${hours} hours, ${minutes} minutes and ${seconds} seconds`;

    html = `<!DOCTYPE html>
 <html>
     <head>
         <title> Node JS Response</title>
     </head>
     <body>
         <p>Hostname:${myHostName}</p>
         <p>IP:${myIp}</p>
         <p> Server Uptime:${uptime}</p>
         <p>Total Memory:${myTotalMemory}</p>
         <p> Free Memory:${myFreeMemory}</p>
         <p>Number of CPUs:${numberOfCpu}</p>
     </body>
 </html>`
 res.writeHead(200,{"Content-Type":"text/html"});
 res.end(html)
}

else
{
    res.writeHead(404,{"content-Type":"text/html"});
    res.end(`404 File Not Found at ${req.url}`);
}
}).listen(3000);

console.log("Server listening on port 3000")
