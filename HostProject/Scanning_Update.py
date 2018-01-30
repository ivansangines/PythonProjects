#!C:\Users\ivans_000\AppData\Local\Programs\Python\Python35-32\python

import cgi
import html
import socket as sk
import HostScannerDAL as HSD
import threading

print("Content-type:text/html\r\n\r\n")
print("<html><body>")


class Helper_Python_Host_Scanner():
    def __init__(self, host_id):
        self.host = HSD.HostScannerDAL()
        # store value of ip address from user
        self.host_IP = host_id
        # store value from user hostname
        self.name = sk.gethostbyaddr(self.host_IP)

        self.update_host_name()

    def update_host_name(self):
        print("<p> Start Scanning: " + self.name[0] + " </p>")
        self.start_scan()

    def start_scan(self):

        self.host.create_host(self.host_IP, self.name[0])

        self.host.create_scan(self.host.hostid)

        # scanning ports from 130 to 139
        self.scan_port(130,140)


    def scan_port(self, min_port, max_port):
        #scanning each port number one by one
        for i in range(min_port, max_port):
            s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
            status=s.connect_ex((self.host_IP,i))
            isOpen = 0 if status==0 else 1
            s.close()
            self.host.create_port_status(self.host.scanid,i,isOpen)
            #printing each port scanned
            print("<p> Scanning por number " + str(i) + ", for given Host -->" + self.host_IP + " </p>")

        #GETTING THE TIME ONCE WE CHECK FOR THE SATUS
        self.host.update_scan_end_time(self.host.scanid)
        # Update the scan table for scan completion time
        print("<p> Finished Scanning </p>")
        print("<input type='hidden' name='host_name' value="+self.name[0]+" />")
        print("<input type='hidden' name='host_ip' value="+self.host_IP+" />")





form = cgi.FieldStorage()
#getting the IP provided in the input
host_id = form.getvalue("number")
#checking if ip address has been privided
if host_id is not None:
    print("<h1 align='center'> SCANNING PAGE </h1>")
    print("<p> The ip is: " + host_id + " </p>")
    print("<form method='post' action='Switch_Result.py'>")
    Helper_Python_Host_Scanner(host_id)
    print("<input type='submit' value='View Results' />")
    print("</form>")
    print("</body></html>")

#case where ip is not provided
else:
    print("<h3 align='center'> SCANNING PAGE </h>")
    print("<p align = 'left'> Received host = Host ID not received  </p>")
    print("</body></html>")


'''
            <html> 
                <head>
                <style>
                </style>
                <center> 
                        <h3> SCANNING PAGE </h3>
                </center> 
            </head>
            <body>
                          
                    Received host = Host ID not received
              
            </body>
            </html>"
            
          )'''
