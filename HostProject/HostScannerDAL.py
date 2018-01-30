import sqlite3 as db
import time


class HostScannerDAL:
    def __init__(self):
        #initializating all the required variables
        self.scanid = 0
        self.hostid = 0
        self.is_conn_open = False
        self.__connect_()

    def __connect_(self):
        '''
		Connect to database using the .db file provided

		'''
        # connect to the database
        # retrieve the values in form of db dictionary
        # create a new cursor
        if not self.is_conn_open:
            self.conn = db.connect('HostScanner.db')
            self.conn.row_factory = db.Row
            self.cur = self.conn.cursor()
            self.is_conn_open = True


    def read_host(self, host_ip, host_name=None):
        # CHECKS IF THE RECORD IS ALREADY PRESENT AND GIVES A VARIABLE

		# CHECK FOR THE FIRST TIME ENTRY

		#return read_host_result
        pass

    def create_host(self, host_ip, host_name):

        self.cur.execute('SELECT * FROM Host')
        result = len(self.cur.fetchall())
        #CHECK IF THE HOST EXISTS
        self.cur.execute("SELECT HostName FROM Host WHERE HostName = ?", (host_name,))
        exist = len(self.cur.fetchall())
        if (result == 0):  # Table is empty.
            self.hostid = 1
            self.cur.execute('INSERT INTO Host (HostId, HostName,HostIp) VALUES(?,?,?)', (1, host_name, host_ip))
            self.conn.commit()
        else:
            #FIND ID FROM THE EXISTING HOSTNAME
            self.cur.execute("SELECT HostId FROM Host WHERE HostIp = ?", (host_ip,))
            self.hostid = self.cur.fetchone()[0]
        # Inserts max value +1 if table is not empty
        if(exist==0): #CURRENT HOST IS NOT IN THE DB
            self.cur.execute('INSERT INTO Host (HostId,HostName,HostIp) VALUES(?,?,?)',
                             (result + 1, host_name, host_ip))
            self.conn.commit()

    def create_scan(self, host_id):
        # Creates the scan_id for each time the host scanner starts scanning the port-id's
        start = time.ctime(time.time())
        self.cur.execute('SELECT * FROM Scan')
        result = len(self.cur.fetchall())

        if (result == 0):  # Table is empty.
            self.scanid = 1
            self.cur.execute('INSERT INTO Scan (ScanId, HostId, ScanStartTime) '
                             'VALUES(?,?,?)', (self.scanid, host_id, start))

            self.conn.commit()

        # Inserts max value +1 if table is not empty
        else:
            self.scanid = result + 1
            self.cur.execute('INSERT INTO Scan (ScanId, HostId, ScanStartTime) '
                             'VALUES(?,?,?)', (self.scanid, host_id, start))

            self.conn.commit()


    def update_scan_end_time(self, scan_id):
        #Update sthe SCAN table after the scanning is completed
        end = time.ctime()
        self.cur.execute('UPDATE Scan SET ScanEndTime=? WHERE scanId=?', (end, scan_id))
        self.conn.commit()

    def read_port_status(self, host_ip, host_name):

        #query that selects the data with the max ScanId (we just need the columns (ScanId, Ports, PortStatus, start time)
        self.cur.execute(
            'SELECT ps.*, s.ScanStartTime FROM PortStatus ps JOIN Scan s on ps.ScanId = s.ScanId JOIN Host h on h.HostId = s.HostId '
            'WHERE ps.ScanId=(select max(ScanId) from PortStatus) AND h.HostIP = ? AND h.HostName = ?' ,(host_ip, host_name))

        return self.cur.fetchall()

    def create_port_status(self, scan_id, port, is_open):
        '''
		INSERTS DATA FOR EACH TIME THE SCAN IS RUNNING ON THE SYSTEM
		'''
        self.cur.execute('INSERT INTO PortStatus (ScanId,PortNumber,IsPortOpen) VALUES (?,?,?)',(scan_id,port,is_open))
        self.conn.commit()

    def __close_connection_(self):
        '''
			CLOSES ALL THE CONNECTIONS BEFORE CLASS IS DESTROYED.
		'''
        if self.is_conn_open:
            self.conn.commit()
            self.conn.close()
            self.is_conn_open = False

    def __del__(self):
        self.__close_connection_()
