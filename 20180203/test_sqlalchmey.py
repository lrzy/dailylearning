# -*- coding=utf-8 -*-
"""
    测试sqlalchemy
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from newcreditlevel import *

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"


engine = create_engine('mysql+mysqldb://root:qwe123@localhost:3306/mydb')
DBSession = sessionmaker(bind=engine)
NXBase.metadata.create_all(engine)
    
if __name__ == '__main__':
    pass
