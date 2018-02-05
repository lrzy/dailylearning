# -*- coding=utf-8 -*-
"""
   使用orm 类生成sql语句
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from newcreditlevel import *
from string import Template

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"


engine = create_engine('mysql+mysqldb://root:qwe123@localhost:3306/mydb')
DBSession = sessionmaker(bind=engine)
ormobj = CreditPerInfo()

inserttmp = Template(u"""
    insert into $tbname ($colstr)
    values($colval)
""")
#取类里面的属性
tbs = NXBase.metadata.tables
for tbname in tbs:
    tb = tbs[tbname]
    cols=[]
    for c in tb.columns:
        cols.append(c.name)
    colstr=",".join(cols)
    colval=":"+",:".join(cols)
    insertsql=inserttmp.substitute(
        tbname=tbname,colstr=colstr,colval=colval
    )
    
    
if __name__ == '__main__':
    pass
