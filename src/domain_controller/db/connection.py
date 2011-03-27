  # -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# Copyright 2011 Institut Telecom - Telecom SudParis.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

'''
Created on Feb 25, 2011

@author: Houssem Medhioub
@contact: houssem.medhioub@it-sudparis.eu
@organization: Institut Telecom - Telecom SudParis
@version: 0.1
@license: Apache License, Version 2.0
'''

import logging.config
from configobj import ConfigObj
import pycassa
from pycassa.system_manager import SystemManager


""" Loading the logging configuration file """
logging.config.fileConfig("../../CloNeLogging.conf")
""" getting the Logger """
logger = logging.getLogger("CloNeLogging")

""" The IP Address of the Database. In CloNe's domain controller, it should be localhost/127.0.0.1"""
config = ConfigObj("db.conf")
DB_IP = config['DB_IP']
DB_PORT = config['DB_PORT']

class CassandraDbSysManager:
    def __init__(self):
        try:
            logger.info("Connection to " + DB_IP + ":" + DB_PORT+ " ...")
            self.sys = SystemManager(DB_IP + ":" + DB_PORT)
            logger.info("Connection to the systemManager established.")
        except Exception as exep:
            logger.warning("Could not connect to the DB '" + DB_IP + ":" + DB_PORT + "'. | " + str(exep))


    def create_keyspace(self, KeyspaceName, replica_factor):
        try:
            logger.info("Creating the Keyspace '" + KeyspaceName + "' with replica_factor '" + str(replica_factor) + "'")
            self.sys.create_keyspace(KeyspaceName, replica_factor)
            logger.info("Keyspace created.")
        except Exception as exep:
            logger.warning("Could not create the keyspace '" + KeyspaceName + "'. | " + str(exep))

    def drop_keyspace(self, KeyspaceName):
        try:
            logger.info("Dropping the Keyspace '" + KeyspaceName + "'")
            self.sys.drop_keyspace(KeyspaceName)
            logger.info("Keyspace dropped.")
        except Exception as exep:
            logger.warning("Could not drop the keyspace '" + KeyspaceName + "'. | " + str(exep))

    def create_column_family(self, KeyspaceName, columnFamily):
        try:
            logger.info("Creating the Column family '" + columnFamily + "' into the keyspace '" + KeyspaceName + "'")
            self.sys.create_column_family(KeyspaceName, columnFamily, super=False, comparator_type=pycassa.system_manager.ASCII_TYPE)
            logger.info("Column Family created.")
        except Exception as exep:
            logger.warning("Could not create the Column Family '" + columnFamily + "' into the keyspace '" + KeyspaceName + "'. | " + str(exep))

    def drop_column_family(self, KeyspaceName, columnFamily):
        try:
            logger.info("Dropping the Column Family '" + columnFamily + "' from the Keyspace '" + KeyspaceName + "'")
            self.sys.drop_column_family(KeyspaceName, columnFamily)
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
            logger.info("Connection to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT+ "' ...")
            self.pool = pycassa.connect(KeyspaceName, [DB_IP + ":" + DB_PORT])
            logger.info("Connection to the keyspace established.")
        except Exception as exep:
            logger.warning("Could not connect to the keyspace '" + KeyspaceName + "' at: " + DB_IP + ":" + DB_PORT + ". | " + str(exep))

    def pool_connection_multiple(self, KeyspaceName):
        try:
            logger.info("Connection to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT+ "' ...")
            self.pool = pycassa.ConnectionPool(KeyspaceName, [DB_IP + ":" + DB_PORT], pool_size=20)
            logger.info("Connection to the keyspace established.")
        except Exception as exep:
            logger.warning("Could not connect to the keyspace '" + KeyspaceName + "' at '" + DB_IP + ":" + DB_PORT + "'. | " + str(exep))

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