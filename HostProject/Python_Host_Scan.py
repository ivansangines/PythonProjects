#!C:\Users\ivans_000\AppData\Local\Programs\Python\Python35-32\python

import cgi

class Python_Host_Scanner:
    def __init__(self):
        self.form = cgi.FieldStorage() #storage in order to send the ip to the next page
        self.ip = 0
        self.init_WebForm() #calling the method to create the HTML page

    def init_WebForm(self):
        print("Content-type:text/html\r\n\r\n")

        print("<html><body>")
        print("<h1 align='center'> WELCOME TO PYTHON HOST SCANNER </h1>")
        print("<form method='post' action='Scanning_Update.py'>")
        print("<table border=2 style=width:80%  padding: 5px> ")
        print("<tr><th> HOST IP:</th> <th><input type='text' name ='number'/></th></tr>")
        print("<tr><td colspan='2'><input type='submit' value='Scan' /></td></tr>")
        print("</table>")
        print("</form>")
        print("</body></html>")


pht = Python_Host_Scanner()
