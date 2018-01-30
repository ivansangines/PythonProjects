#!C:\Users\ivans_000\AppData\Local\Programs\Python\Python35-32\python

import cgi
import HostScannerDAL as HSD
import threading
import GUI_Display as GD


print("Content-type:text/html\r\n\r\n")
print("<html><body>")

class Switch_Result ():
    def __init__(self, hst_id, hst_name):
        self.PPSD=HSD.HostScannerDAL()
        self.ip_add=hst_id
        self.h_nam=hst_name
        self.Switch_Results()

    def Switch_Results(self):
        #obtaining the data using the querry in the readportstatus method
        dat=self.PPSD.read_port_status(self.ip_add, self.h_nam)
        #printing the information as a table
        for d in dat:
            print('<tr align="center"><td border: none>'+str(d['scanId'])+'</td>'+
                   '<td>'+str(d['PortNumber'])+'</td>'+
                  '<td>' + str(d['IsPortOpen']) + '</td>' +
                  '<td>' + str(d['ScanStartTime']) + '</td></tr>')

        #thr2 = threading.Thread(target=self.CGUI())
        #thr2.start()
        #thr2.join()
    #CREATING THE GUI TABLE
    #def CGUI(self):
        #self.GDD = GD.ResultsDialog(self.ip_add, self.h_nam)


form = cgi.FieldStorage()
name=form.getvalue("host_name")
ip=form.getvalue("host_ip")
#name='Usuario.ad.bridgeport.edu'
#ip='10.12.55.82'
#PPSD=HSD.HostScannerDAL()
#dat=PPSD.read_port_status('10.12.55.82','Usuario.ad.bridgeport.edu')

#checking if we are receiving name and ip address
if ip and name is not None:
    print("<h1 align='center'> RESULTS PAGE </h1>")
    print("<table border=1 border-collapse= collapse  > ")
    print("<th> SCAN_ID</th>")
    print("<th> PORT_NUMBER</th>")
    print("<th> IS_OPEN</th>")
    print("<th> SCAN_TIME</th>")
    Switch_Result(ip,name)
    print("</table>")
    print("</body></html>")

#not received proper information
else:
    print("<h3 align='center'> SCANNING PAGE </h>")
    print("<p align = 'left'> Received host = Host ID not received  </p>")
    print("</body></html>")
