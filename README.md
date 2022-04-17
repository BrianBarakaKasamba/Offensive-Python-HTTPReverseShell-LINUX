# Offensive-Python-HTTPReverseShell
Write up for Black-hat python from lessons at PactpPub networking_and_servers books.
Date :/13/04/2022 
Author: Brian Baraka Kasamba

Python reverse shell via HTTP protocol.

REASON FOR HTTP ?? That the HTTP protocol is highly likely to be opened on the outbound firewall rules,
since it's used for web surfing.

Also, a lot of HTTP traffic is required in every network, which makes monitoring much harder and the chances of  slipping up are high.

TODO

Configure a simple HTTP server and a simple HTTP client.Use the GET and POST methods to send data.

1.Initiate a reverse HTTP session back to server using a GET method.

2.Upon receiving a GET request,take commands using raw input, and send command back to the target.

3.Once command given to the target, it'll initiate a subprocess: (a cmd.exe subprocess).

4.Pass the command to that subprocess and it will post the result back to us using the POST method.

(perform sleep for 3 seconds to ensure continuty)

5.Repeat the whole process all over again using the while True: infinite loop.

HOW TO USE


![proofofpythonversion](https://user-images.githubusercontent.com/98221277/163725729-be3b8139-58d5-4e30-a050-944648c65889.gif)






VIRUS TOTAL RESULTS
python script.
![ClientPythonScript](https://user-images.githubusercontent.com/98221277/163320935-1539c5f2-e218-4712-95ae-37bc85c19308.png)



Compiled Linux Binary
![CompiledBinaryLinux](https://user-images.githubusercontent.com/98221277/163321156-636fcca6-107a-4870-b4dd-6c7c7ab6486f.png)






Confirmed File Type is ELF

![ConfirmFileType](https://user-images.githubusercontent.com/98221277/163321254-77072969-0475-419a-8b44-b44a213f602b.png)








