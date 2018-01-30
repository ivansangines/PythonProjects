import sqlite3 as db
import time


class HostScannerDAL:
    def __init__(self):
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

        def read_host(self, host_ip, host_name=None):
            # CHECKS IF THE RECORD IS ALREADY PRESENT AND GIVES A VARIABLE

            # CHECK FOR THE FIRST TIME ENTRY

            return read_host_result

        def create_host(self, host_ip, host_name):
            # Inserts default value if table is empty

            # Inserts max value +1 if table is not empty

            return self.return_host_numb

        def create_scan(self, host_id):
            '''

            Creates the scan_id for each time the host scanner starts scanning the port-id's

            '''

        def update_scan_end_time(self, scan_id):
            '''

            Update sthe SCAN table after the scanning is completed

            '''

            pass

        def read_port_status(self, host_ip, host_name):
            '''

            RETURNS THE FINAL DATA SET ATTRIBUTES WHICH ARE REQUIRED TO DISPLAY

            '''

            return self.cur.fetchall()

        def create_port_status(self, scan_id, port, is_open):
            '''
            INSERTS DATA FOR EACH TIME THE SCAN IS RUNNING ON THE SYSTEM

            '''

        def __close_connection_(self):
            '''

                CLOSES ALL THE CONNECTIONS BEFORE CLASS IS DESTROYED.

            '''

            pass

        def __del__(self):
            self.__close_connection_()
