#!C:\Program Files (x86)\Python36-32\python

import cgi


class Python_Host_Scanner:
    def __init__(self):
        self.form = cgi.FieldStorage()
        self.init_WebForm()

    def init_WebForm(self):
        print("Content-type:text/html\r\n\r\n")
        print("<html><body>")
        print("<h1 align='center'> WELCOME TO PYTHON HOST SCANNER </h1>")

        if self.form.getvalue("number"):
            ip = self.form.getvalue("number")
            print("<p> The ip is: " + ip + " </p>")
        print("<form mehtod='post' >")
        print("<table border=1>")
        print("<tr><th>HOST IP:<input type='text' name ='number'/></th></tr>")
        print("<td><input type='submit' value='Scan' /></td>")
        print("</table>")
        print("</form>")

        print("</body></html>")


pht = Python_Host_Scanner()
