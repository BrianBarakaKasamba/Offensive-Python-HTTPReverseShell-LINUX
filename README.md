# Offensive-Python-HTTPReverseShell
Write up for Black-hat python from lessons at PactpPub networking_and_servers books.
Date :/13/04/2022 
Author: Brian Baraka Kasamba

Python reverse shell via HTTP protocol.
REASON FOR HTTP ?? That the HTTP protocol is highly likely to be opened on the outbound firewall rules,
since it's used for web surfing.
Also, a lot of HTTP traffic is required in every network, which makes monitoring much harder and the chances of  slipping up are high.

**TODO
**
Configure a simple HTTP server and a simple HTTP client.Use the GET and POST methods to send data.
Initiate a reverse HTTP session back to server using a GET method.
Upon receiving a GET request,take commands using raw input, and send command back to the target.
Once command given to the target, it'll initiate a subprocess: (a cmd.exe subprocess).
Pass the command to that subprocess and it will post the result back to us using the POST method.
(perform sleep for 3 seconds to ensure continuty)
Repeat the whole process all over again using the while True: infinite loop.

