# -*- coding: utf-8 -*-

class TableInfo:
    """
    表table_info对应的model
    """
    def __init__(self, **kw):
        """
        初始化model
        """
        self.__id = kw['id'] if 'id' in kw else 0
        self.__tb_name = kw['tb_name']
        self.__tb_desc = kw['tb_desc'] if 'tb_desc' in kw else ''
        self.__create_datetime = kw['create_datetime'] if 'create_datetime' in kw else None
     
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def tb_name(self):
        return self.__tb_name
    @tb_name.setter
    def tb_name(self, value):
        self.__tb_name = value

    @property
    def tb_desc(self):
        return self.__tb_desc
    @tb_desc.setter
    def tb_desc(self, value):
        self.__tb_desc = value

    @property
    def create_datetime(self):
        return self.__create_datetime
    @create_datetime.setter
    def create_datetime(self, value):
        self.__create_datetme = value
   
   
    def __str__(self):
        return '{id= %s, tb_name= %s, tb_desc= %s, create_datetome= %s}' % (self.id, self.tb_name, self.tb_desc, self.create_datetime)

    __repr__ = __str__
