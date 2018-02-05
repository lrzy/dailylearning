# -*- coding=utf-8 -*-
"""
   解析excel 生成sqlalcmy orm 对象文件
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import xlrd
from string import Template
from collections import defaultdict

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"
#calss 模板
classtmp = Template(u"""
class $classname(NXBase):
    u\"\"\"
       $tabledoc
    \"\"\"
    __tablename__='$tablename'
$columns
""")

#列模板
columtmp = Template(u"""    $colname = Column($colattr$otherattr,doc=u'$coldoc')
""")
#表前缀
table_per ='cr_'
#表头和字段的映射
table_header ={
    u'表名':'tablename',
    u'表中文名':'tabledoc',
    u'字段名':'colname',
    u'类型':'colattr',
    u'字段中文':'coldoc',
}

def create_orm_class(path,sheetname,filename):
    """
        按excel 生成 orm 的类
        :param path :需要解析的文件
               sheetname:解析那个sheet
               filname:生成的文件名
    """
    workbook = xlrd.open_workbook(path)
    sheet = workbook.sheet_by_name(sheetname)

    #确定表头的映射 
    headers = sheet.row_values(0)
    colattr = {}
    for col in xrange(len(headers)):
        if headers[col] in table_header.keys():
             colattr[table_header[headers[col]]]=col

    #从excel 中读取表属性 
    tables = defaultdict(dict) 
    for nrow in xrange(1,sheet.nrows):
        row = sheet.row_values(nrow)
        acol={}
        for attr,col in colattr.items():
            acol[attr] = row[col]
        if tables.has_key(acol['tablename']):
            tables[acol['tablename']]['cols'].append({'colname':acol['colname'],'colattr':acol['colattr'],'coldoc':acol['coldoc']})
        else:
            tables[acol['tablename']] ={
                'tablename':acol['tablename'],
                'tabledoc':acol['tabledoc'],
                'cols':[{'colname':acol['colname'],'colattr':acol['colattr'],'coldoc':acol['coldoc']}]
            }
    #转换为目标文件中的样式
    classstrs=[]
    for tablename,tableattr in tables.items(): 
        cols = tableattr.pop('cols')
        columns = ""
        for col in cols:
            if col['colname'].lower()=='id':
                col['otherattr']=",primary_key=True"
            else:
                col['otherattr']=""
    
            reattr = {'date':'Date','datetime':'DateTime','varchar':'String','int':'BigInteger','decimal':'DECIMAL'}
            for k,v in reattr.items():
                if k in col['colattr'].lower():
                    col['colattr']=col['colattr'].lower().replace(k,v)
            colstr = columtmp.substitute(**col)
            columns +=colstr

        tableattr['columns']=columns
        tableattr['classname']=tableattr['tablename']
        tableattr['tablename']=table_per+tableattr['tablename'].lower()
        classstrs.append(classtmp.substitute(**tableattr))
    
    #写到文件中
    fp = filename+'.py'
    with open(fp,'w') as f:
        f.writelines([
            "#  -*- coding:utf-8 -*-\n",
            "from sqlalchemy import DateTime,String,Date,BigInteger,DECIMAL,Column\n\n",
            #"from task.tools.util import NXBase\n",
        ])
        for cstr in  classstrs:
            f.write(cstr)

    
 
        

if __name__ == '__main__':
    create_orm_class(u'数据_信用风险评级授信数据整理明细.xlsx',u'新表设计','newcreditlevel')
