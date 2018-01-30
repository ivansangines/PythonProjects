#!C:\Users\ivans_000\AppData\Local\Programs\Python\Python35-32\python

import cgi
import socket
import HostScannerDAL as HSD
import threading


class Helper_Python_Host_Scanner():
    def __init__(self, host_id):
        # store value of ip address from user

        # store value from user hostname

        pass

    def update_host_name(self):
        pass

    def start_scan(self):
        # gets the host number from Hosts table in DAL

        # calls the create scan table method in DAL

        pass

    def scan_port(self, min_port, max_port):
        # Updates which port number is being scanned to the HTML page

        # Update the scan table for scan completion time

        pass


if host_id is not None:
    Helper_Python_Host_Scanner(host_id)

else:
    print('''

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
            </html>
            '''
          )
