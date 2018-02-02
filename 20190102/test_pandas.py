# -*- coding=utf-8 -*-
"""
    测试pandas
"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pandas as pd 

__author__="zhangyin"
__maintainer__="zhangyin"
__version__="0.1"

def test_pandas(path):
    """
        测试pandas
    """
    #读取excel数据，最好写上sheetname
    df = pd.read_excel(path,header=0,sheetname=u"花盛芳")
    df2 = pd.read_excel(path,header=0,sheetname=u"张")
    newname = {a:a.strip() for a in df.columns}
    df=df.rename(columns=newname)
    
    #去除字段中的空格
    newname = {a:a.strip() for a in df2.columns}
    df2=df2.rename(columns=newname)

    olddata = df
    newdata = df2[[u'签约号',u'营销机构']].drop_duplicates()
    #管理两个数据
    c = pd.merge(olddata,newdata,how='outer',left_on=u'车牌号',right_on=u'签约号')
    c = c[c[u'车牌号']!=c[u'签约号']]
    c = c[~c[u"营销人员机构"].isin([875000,875001,875002,875003,875115])]
    c.to_csv('c.csv')
    
    d = pd.merge(olddata,newdata,how='inner',left_on=u'车牌号',right_on=u'签约号')
    d = d[d[u'营销人员机构']!=d[u'营销机构']]
    d.to_csv('d.csv')
    
    #分组统计
    a = df.groupby([u'营销人员机构'],as_index=False)[u'车牌号'].count() 
    b = df2.groupby([u'营销机构'],as_index=False)[u'签约号'].count() 
    a.to_csv('a.csv')
    b.to_csv('b.csv')

    olddata=df[df[u"营销人员机构"]==875020]
    olddata.to_excel('olddata.xls')
    newdata=df2[df2[u"营销机构"]==875020]
    newdata.to_excel('newdata.xls')
    newdata = newdata[[u'签约号',u'营销机构']].drop_duplicates()
    c = pd.merge(olddata,newdata,how='outer',left_on=u'车牌号',right_on=u'签约号')
    #c = c[c[u'车牌号']!=c[u'签约号']]
    c.to_csv('e.csv')
    
    out = df.groupby([u'车牌号'],as_index=False)[u"营销人员机构"].count()
    out = out[out[u'营销人员机构']>1]
    out.to_csv('f.csv')

    
 
        

if __name__ == '__main__':
    test_pandas('sql1ETC2015-2017.xls')
