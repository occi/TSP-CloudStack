# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright (C) 2011 Houssem Medhioub - Institut Telecom
#
# This file is part of TSP-CloudStack.
#
# TSP-CloudStack is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# TSP-CloudStack is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with TSP-CloudStack.  If not, see <http://www.gnu.org/licenses/>.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: LGPL - Lesser General Public License
'''

import logging.config
from configobj import ConfigObj
import pycassa
from pycassa.system_manager import SystemManager


# Loading the logging configuration file
logging.config.fileConfig("../../DCPLogging.conf")
# getting the Logger
logger = logging.getLogger("DCPLogging")

# The IP Address of the Database. In CloNe's domain controller, it should be localhost/127.0.0.1
config = ConfigObj("db.conf")
DB_IP = config['DB_IP']
DB_PORT = config['DB_PORT']

class CassandraDbSysManager:
    def __init__(self):
        try:
            logger.info("Connection to " + DB_IP + ":" + DB_PORT + " ...")
            self.sysDB = SystemManager(DB_IP + ":" + DB_PORT)
            logger.info("Connection to the systemManager established.")
        except Exception as exep:
            logger.warning("Could not connect to the DB '" + DB_IP + ":" + DB_PORT + "'. | " + str(exep))


    def create_keyspace(self, KeyspaceName, replica_factor):
        try:
            logger.info(
                "Creating the Keyspace '" + KeyspaceName + "' with replica_factor '" + str(replica_factor) + "'")
            self.sysDB.create_keyspace(KeyspaceName, replica_factor)
            logger.info("Keyspace created.")
        except Exception as exep:
            logger.warning("Could not create the keyspace '" + KeyspaceName + "'. | " + str(exep))

    def drop_keyspace(self, KeyspaceName):
        try:
            logger.info("Dropping the Keyspace '" + KeyspaceName + "'")
            self.sysDB.drop_keyspace(KeyspaceName)
            logger.info("Keyspace dropped.")
        except Exception as exep:
            logger.warning("Could not drop the keyspace '" + KeyspaceName + "'. | " + str(exep))

    def create_column_family(self, KeyspaceName, columnFamily):
        try:
            logger.info("Creating the Column family '" + columnFamily + "' into the keyspace '" + KeyspaceName + "'")
            self.sysDB.create_column_family(KeyspaceName, columnFamily, super=False,
                                            comparator_type=pycassa.system_manager.ASCII_TYPE)
            logger.info("Column Family created.")
        except Exception as exep:
            logger.warning(
                "Could not create the Column Family '" + columnFamily + "' into the keyspace '" + KeyspaceName + "'. | " + str(
                    exep))

    def drop_column_family(self, KeyspaceName, columnFamily):
        try:
            logger.info("Dropping the Column Family '" + columnFamily + "' from the Keyspace '" + KeyspaceName + "'")
            self.sysDB.drop_column_family(KeyspaceName, columnFamily)
            logger.info("Column Family dropped.")
        except Exception as exep:
            logger.warning("Could not drop the column family '" + columnFamily + "'. | " + str(exep))


class CassandraDbPool:
    def __init__(self):
        self.pool_connection_one("Keyspace4")
        self.pool_connection_multiple("Keyspace4")
        pass

    def pool_connection_one(self, KeyspaceName):
        try:
            logger.info("Connection to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT + "' ...")
            self.pool = pycassa.connect(KeyspaceName, [DB_IP + ":" + DB_PORT])
            logger.info("Connection to the keyspace established.")
        except Exception as exep:
            logger.warning(
                "Could not connect to the keyspace '" + KeyspaceName + "' at: " + DB_IP + ":" + DB_PORT + ". | " + str(
                    exep))

    def pool_connection_multiple(self, KeyspaceName):
        try:
            logger.info("Connection to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT + "' ...")
            self.pool = pycassa.ConnectionPool(KeyspaceName, [DB_IP + ":" + DB_PORT], pool_size=20)
            logger.info("Connection to the keyspace established.")
        except Exception as exep:
            logger.warning(
                "Could not connect to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT + "'. | " + str(
                    exep))

    def get_column_family(self, ColumnFamilyName):
        try:
            logger.info("Getting the ColumnFamily: '" + ColumnFamilyName + "' ...")
            col_fam = pycassa.ColumnFamily(self.pool, ColumnFamilyName)
            logger.info("Getting the ColumnFamily. DONE")
            return col_fam
        except Exception as exep:
            logger.warning("Could not get the columnFamily '" + ColumnFamilyName + "'. | " + str(exep))

    def insert_data(self, ColumnFamilyName, row_key, col_name, col_val):
        try:
            logger.info("inserting data ...")
            col_fam = self.get_column_family(ColumnFamilyName)
            res = col_fam.insert(row_key, {col_name: col_val})
            logger.info("Data insert DONE with returned value '" + str(res) + "'")
        except Exception as exep:
            logger.warning("Could not insert data in the columnFamily '" + ColumnFamilyName + "'. | " + str(exep))

    def get_data(self, ColumnFamilyName, row_key):
        try:
            logger.info("getting data ...")
            col_fam = self.get_column_family(ColumnFamilyName)
            res = col_fam.get(row_key)
            logger.info("Data get DONE with returned values: '" + str(res) + "'")
        except Exception as exep:
            logger.warning("Could not get data from the columnFamily '" + ColumnFamilyName + "'. | " + str(exep))

if __name__ == '__main__':
    clone_db_sys = CassandraDbSysManager()
    #clone_db_sys.create_keyspace("Keyspace7", 2)
    #clone_db.drop_keyspace("Keyspace3")
    #clone_db_sys.create_column_family("Keyspace7", "testColumn7")
    #clone_db_sys.drop_column_family("Keyspace4", "testColumn2")

    clone_db = CassandraDbPool()
    clone_db.pool_connection_one("Keyspace3")
    #clone_db.insert_data('testColumn7', 'row_key7', '7s', 'value7')
    clone_db.get_data("testColumn3", 'row_key')
    pass