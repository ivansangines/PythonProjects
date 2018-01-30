#!C:\Program Files (x86)\Python36-32\python

import cgi
import HostScannerDAL as HSD
import GUI_Display as GD
import threading


class Switch_Result():
    def __init__(self, hst_id, hst_name):
        def Switch_Results(self):
            dat = self.PPSD.read_port_status(self.ip_add, self.h_nam)

            # thr2 = threading.Thread(target=self.CGUI())
            # thr2.start()
            # thr2.join()
            pass

        def CGUI(self):

            self.GDD = GD.ResultsDialog(self.ip_add, self.h_nam)
