# -*- coding: utf-8 -*-

__author__ = 'seastar'

import datetime
class DatabaseInfo:
    """
    表database_infos的model
    """
    def __init__(self, **kw):
        """
        初始化model，
        """
        self.__id =  kw['id'] if 'id' in kw else 0
        self.__db_name = kw['db_name']
        self.__db_desc = kw['db_desc'] if 'db_desc' in kw else ''
        self.__create_datetime = kw['create_datetime'] if 'create_datetime' in kw else None
 

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value
    
    @property
    def db_name(self):
        return self.__db_name
    @db_name.setter
    def db_name(self, value):
        self.__db_name = value

    @property
    def db_desc(self):
        return self.__db_desc
    @db_desc.setter
    def db_desc(self, value):
        self.db_desc = value

    @property
    def create_datetime(self):
        return self.__create_datetime
    @create_datetime.setter
    def create_datetime(self, value):
        self.__create_datetime = value

    def __str__(self):
        return '{id= %s, db_name= %s, db_desc= %s, create_datetome= %s}' % (self.__id, self.__db_name, self.__db_desc, self.__create_datetime)

    __repr__ = __str__
