import tkinter as tk
import tkinter.ttk as ttk
import HostScannerDAL as HSD


class ResultsDialog():
    def __init__(self, host_ip, host_name):
        self.ipAdd=host_ip
        self.nombre=host_name
        self.info = HSD.HostScannerDAL()
        self.root = tk.Tk()
        self.gui_init_()
        self.root.mainloop()


    def gui_init_(self):
        self.root.title('Results Dialog')
        self.om1_var = tk.StringVar()
        self.grd = tk.Frame(self.root)
        self.grd.pack(expand=True, fill=tk.BOTH, side=tk.TOP)
        self.treeview = ttk.Treeview(self.grd)
        #columns we will show
        self.treeview['columns'] = ('ScanId', 'PortNumber', 'IsPortOpen', 'ScanStartTime')
        self.treeview['displaycolumns'] = ('PortNumber', 'IsPortOpen','ScanStartTime')
        self.treeview.heading('#0', text='Scan Id')
        #setting the text for the columns created
        self.treeview.heading('PortNumber', text='Port Number')
        self.treeview.heading('IsPortOpen', text='Is Open')
        self.treeview.heading('ScanStartTime', text='Scan Time')
        self.treeview.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.treeview.bind("<Double-1>", self.tree_double_click)
        self.__update_grd_()
        #self.root.mainloop()



    def __update_grd_(self):
        data = self.info.read_port_status(self.ipAdd, self.nombre)
        for row in self.treeview.get_children():
            self.treeview.delete(row)
        for d in data:
            self.treeview.insert('', tk.END, text=d['ScanId'],
                                 values=(d['ScanId'], d['PortNumber'],
                                         d['IsPortOpen'], d['ScanStartTime']))

    def tree_double_click(self, event):
        item = self.treeview.identify('item', event.x, event.y)
        item2 = self.treeview.item(item)
        print(item2)
if __name__=='__main__':
    wind=ResultsDialog('10.12.55.82','Usuario.ad.bridgeport.edu')