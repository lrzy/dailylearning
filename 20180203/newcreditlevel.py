#  -*- coding:utf-8 -*-
from sqlalchemy import BigInteger,DECIMAL,Column

from task.tools.util import NxBase

class CreditPerInfo(NXBase):
    u"""
        对私授信信息表
     """
     __tablename__='cr_creditperinfo'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    base_id = Column(BigInteger,doc=u'CreditPerBase.ID')
    userno = Column(String(64),doc=u'测算客户经理')
    cre_amount = Column(DECIMAL(18,6),doc=u'资产负债测算额度(万元)')
    add_time = Column(datetime,doc=u'增加时间')


class CreditPubInfo(NXBase):
    u"""
        对公授信信息表
     """
     __tablename__='cr_creditpubinfo'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    base_id = Column(BigInteger,doc=u'CreditPubBase.ID')
    userno = Column(String(64),doc=u'测算客户经理')
    other_bank_loan_adj = Column(DECIMAL(18,6),doc=u'他行现有贷款(调整:万元)')
    adj_exp = Column(String(512),doc=u'调整说明')
    zcfz_amount = Column(DECIMAL(18,6),doc=u'资产负债测算额度(万元)')
    ldzj_amount = Column(DECIMAL(18,6),doc=u'流动资金测算额度(万元)')
    add_time = Column(datetime,doc=u'增加时间')


class GradePerBase(NXBase):
    u"""
        对私评级基础信息表
     """
     __tablename__='cr_gradeperbase'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    custno = Column(String(64),doc=u'客户内码')
    customerno = Column(String(64),doc=u'客户号')
    custname = Column(String(512),doc=u'客户姓名')
    custtype = Column(String(64),doc=u'公私标志')
    loantype = Column(String(64),doc=u'贷款类型')
    certno = Column(String(64),doc=u'身份证号')
    age = Column(DECIMAL(18,2),doc=u'年龄')
    sex = Column(String(16),doc=u'性别')
    education = Column(String(64),doc=u'最高学历')
    marriage = Column(String(64),doc=u'婚姻状况')
    workpro = Column(String(64),doc=u'单位性质')
    avgdep = Column(DECIMAL(30,6),doc=u'日均存款')
    avgloan = Column(DECIMAL(30,6),doc=u'日均贷款')
    starlevel = Column(String(64),doc=u'客户星级')
    starlevel_r = Column(String(64),doc=u'原客户星级')
    job = Column(String(64),doc=u'职务')
    workyear = Column(DECIMAL(18,4),doc=u'工作年限')
    year_wage = Column(DECIMAL(22,4),doc=u'年工资收入')
    if_social = Column(String(64),doc=u'是否缴纳社保')
    pro_fund = Column(DECIMAL(22,4),doc=u'公积金月缴存额')
    pro_year = Column(DECIMAL(18,4),doc=u'公积金持续年份')
    exp_income = Column(DECIMAL(18,6),doc=u'支出收入比')
    house_value = Column(DECIMAL(18,4),doc=u'房产价值')
    breed_income = Column(DECIMAL(18,4),doc=u'年种养殖收入')
    dis_income = Column(DECIMAL(18,4),doc=u'可支配收入')
    net_asset = Column(DECIMAL(18,4),doc=u'净资产')
    compdis_income = Column(DECIMAL(18,4),doc=u'企业可支配收入')
    operate_age = Column(DECIMAL(18,2),doc=u'企业经营年限')
    ownership = Column(String(64),doc=u'经营场地权属')
    sale_ratio = Column(DECIMAL(18,6),doc=u'销售利润率')
    asset_ratio = Column(DECIMAL(18,6),doc=u'资产负债率')
    net_profit = Column(DECIMAL(18,6),doc=u'年净利润率')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class CreditPerBase(NXBase):
    u"""
        对私授信基础信息表
     """
     __tablename__='cr_creditperbase'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    custno = Column(String(64),doc=u'客户内码')
    customerno = Column(String(64),doc=u'客户号')
    custname = Column(String(512),doc=u'客户名称')
    cust_grade = Column(String(64),doc=u'信用等级')
    marriage = Column(String(64),doc=u'婚姻状况')
    education = Column(String(64),doc=u'学历')
    work_status = Column(String(64),doc=u'工作单位性质')
    job = Column(String(64),doc=u'职务')
    wageincome = Column(DECIMAL(18,6),doc=u'年工资收入(万元)')
    house = Column(String(64),doc=u'夫妻名下有无房产')
    car = Column(String(64),doc=u'夫妻名下有无汽车')
    total_asset = Column(DECIMAL(18,6),doc=u'资产总额(元)')
    total_debt = Column(DECIMAL(18,6),doc=u'负债总额(元)')
    loan_amt_all = Column(DECIMAL(18,6),doc=u'贷款总额(元)')
    exp_lose = Column(DECIMAL(18,6),doc=u'预计或有负债损失额(元)')
    income_origin = Column(String(64),doc=u'收入来源')
    fam_income = Column(DECIMAL(18,6),doc=u'家庭年收入(元)')
    from_date = Column(date,doc=u'生效日期')
    end_date = Column(date,doc=u'失效日期')


class GradePubAllScore(NXBase):
    u"""
        对公评级总分表
     """
     __tablename__='cr_gradepuballscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    customerno = Column(String(64),doc=u'客户号')
    custno = Column(String(64),doc=u'客户内码')
    custname = Column(String(512),doc=u'客户姓名')
    custtype = Column(String(64),doc=u'公私标志')
    loantype = Column(String(64),doc=u'贷款类型')
    main_industry = Column(String(64),doc=u'主行业')
    detail_industry = Column(String(64),doc=u'子行业')
    model_type = Column(String(64),doc=u'模型类型')
    comp_num = Column(DECIMAL(18,2),doc=u'企业职工人数')
    comp_num_score = Column(DECIMAL(18,6),doc=u'企业职工人数得分')
    man_age = Column(DECIMAL(18,2),doc=u'经营者年龄')
    man_age_score = Column(DECIMAL(18,6),doc=u'经营者年龄得分')
    man_edu = Column(String(64),doc=u'经营者学历')
    man_edu_score = Column(DECIMAL(18,6),doc=u'经营者学历得分')
    comp_age = Column(DECIMAL(18,6),doc=u'企业经营年限')
    comp_age_score = Column(DECIMAL(18,6),doc=u'企业经营年限得分')
    wate_ect_pay = Column(DECIMAL(18,6),doc=u'水电费支出同比增长率')
    wate_ect_pay_score = Column(DECIMAL(18,6),doc=u'水电费支出同比增长率得分')
    taxes_pay = Column(DECIMAL(18,6),doc=u'增值销项税同比增长率')
    taxes_pay_score = Column(DECIMAL(18,6),doc=u'增值税销项税同比增长率得分')
    act_cash_in = Column(DECIMAL(18,6),doc=u'实际经营性现金现金流入量')
    act_cash_in_score = Column(DECIMAL(18,6),doc=u'实际经营性现金流入量得分')
    elect_value = Column(DECIMAL(18,6),doc=u'用电量')
    elect_value_score = Column(DECIMAL(18,6),doc=u'用电量得分')
    bill_sale = Column(DECIMAL(18,6),doc=u'开票销售率')
    bill_sale_score = Column(DECIMAL(18,6),doc=u'开票销售率得分')
    sale_add = Column(DECIMAL(18,6),doc=u'销售增长率')
    sale_add_score = Column(DECIMAL(18,6),doc=u'销售增长率得分')
    sale_fin = Column(DECIMAL(18,6),doc=u'销售融资比')
    sale_fin_score = Column(DECIMAL(18,6),doc=u'销售融资比得分')
    add_taxes = Column(DECIMAL(18,6),doc=u'新增融资纳税比')
    add_taxes_score = Column(DECIMAL(18,6),doc=u'新增融资纳税比得分')
    wage_pay = Column(DECIMAL(18,6),doc=u'工资性支出同比增长')
    wage_pay_score = Column(DECIMAL(18,6),doc=u'工资性支出同比增长得分')
    acc_turn = Column(DECIMAL(18,6),doc=u'应收账款周转率')
    acc_turn_score = Column(DECIMAL(18,6),doc=u'应收账款周转率得分')
    allscore = Column(DECIMAL(18,6),doc=u'总得分')
    level = Column(String(64),doc=u'信用等级')
    adj_level = Column(String(64),doc=u'调整评级（不良下调）')
    adj_res = Column(String(64),doc=u'调整说明')
    now_level = Column(String(64),doc=u'当前等级（查看）')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class GradePerDealerScore(NXBase):
    u"""
        对私工商乐分值表
     """
     __tablename__='cr_gradeperdealerscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    allscore_id = Column(BigInteger,doc=u'')
    net_asset = Column(DECIMAL(18,6),doc=u'净资产')
    net_asset_score = Column(DECIMAL(18,6),doc=u'净资产分值')
    compdis_income = Column(DECIMAL(18,6),doc=u'企业可支配收入')
    compdis_income_score = Column(DECIMAL(18,6),doc=u'企业可支配收入分值')
    operate_age = Column(DECIMAL(18,6),doc=u'企业经营年限')
    operate_age_score = Column(DECIMAL(18,6),doc=u'企业经营年限分值')
    ownership = Column(DECIMAL(18,6),doc=u'经营场地权属')
    ownership_score = Column(DECIMAL(18,6),doc=u'经营场地权属分值')
    sale_ratio = Column(DECIMAL(18,6),doc=u'销售利润率')
    sale_ratio_score = Column(DECIMAL(18,6),doc=u'销售利润率分值')
    asset_ratio = Column(DECIMAL(18,6),doc=u'资产负债率')
    asset_ratio_score = Column(DECIMAL(18,6),doc=u'资产负债率分值')
    net_profit = Column(DECIMAL(18,6),doc=u'年净利润率')
    net_profit_score = Column(DECIMAL(18,6),doc=u'年净利润率分值')
    count_score = Column(DECIMAL(18,6),doc=u'专家模型分值汇总')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class CreditPubBase(NXBase):
    u"""
        对公授信基础信息表
     """
     __tablename__='cr_creditpubbase'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    custno = Column(String(64),doc=u'客户内码')
    customerno = Column(String(64),doc=u'客户号')
    custname = Column(String(512),doc=u'客户名称')
    fr_custno = Column(String(64),doc=u'法人客户内码')
    fr_customerno = Column(String(64),doc=u'法人客户号')
    fr_custname = Column(String(64),doc=u'法人客户名称')
    main_industry = Column(String(64),doc=u'主行业')
    child_industry = Column(String(64),doc=u'子行业')
    comp_attr = Column(String(64),doc=u'企业性质')
    build_year = Column(DECIMAL(18,6),doc=u'企业设立年份')
    rejistry_captial = Column(DECIMAL(18,6),doc=u'注册资本(万元)')
    employee_num = Column(DECIMAL(18,6),doc=u'职工人数')
    cust_grade = Column(String(64),doc=u'信用等级')
    data_time = Column(date,doc=u'数据时段')
    total_asset = Column(DECIMAL(18,6),doc=u'资产总额(元)')
    total_debt = Column(String(64),doc=u'负债总额(元)')
    other_bank_loan = Column(DECIMAL(18,6),doc=u'他行现有贷款(元)')
    other_bank_loan_ld = Column(DECIMAL(18,6),doc=u'他行流动资金贷款(元)')
    other_loan = Column(DECIMAL(18,6),doc=u'其他贷款(元)')
    exp_lose = Column(DECIMAL(18,6),doc=u'预计或有负债损失额(元)')
    main_income = Column(DECIMAL(18,6),doc=u'期末主营业务收入(元)')
    st_av1 = Column(DECIMAL(18,6),doc=u'期初-存货余额(元)')
    st_av2 = Column(DECIMAL(18,6),doc=u'期末-存货余额(元)')
    sh_income_av1 = Column(DECIMAL(18,6),doc=u'期初-应收账款余额(元)')
    sh_income_av2 = Column(DECIMAL(18,6),doc=u'期末-应收账款余额(元)')
    ex_income_av1 = Column(DECIMAL(18,6),doc=u'期初-预收账款余额(元)')
    ex_income_av2 = Column(DECIMAL(18,6),doc=u'期末-预收账款余额(元)')
    sh_outcome_av1 = Column(DECIMAL(18,6),doc=u'期初-应付账款余额(元)')
    sh_outcome_av2 = Column(DECIMAL(18,6),doc=u'期末-应付账款余额(元)')
    ex_outcome_av1 = Column(DECIMAL(18,6),doc=u'期初-预付账款余额(元)')
    ex_outcome_av2 = Column(DECIMAL(18,6),doc=u'期末-预付账款余额(元)')
    ly_sc = Column(DECIMAL(18,6),doc=u'上年度销售收入(元)')
    ly_cb = Column(DECIMAL(18,6),doc=u'上年度销售成本(元)')
    operate_amount = Column(DECIMAL(18,6),doc=u'运营资金量(元)')
    ly_spr = Column(DECIMAL(18,6),doc=u'上年度销售利润率')
    ex_sc1 = Column(DECIMAL(18,6),doc=u'上年-预计销售收入(元)')
    ex_sc2 = Column(DECIMAL(18,6),doc=u'本年-预计销售收入(元)')
    ex_scr = Column(DECIMAL(18,6),doc=u'预计销售年增长率(元)')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class GradePerAllScore(NXBase):
    u"""
        对私评级总分表
     """
     __tablename__='cr_gradeperallscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    custno = Column(String(64),doc=u'客户内码')
    customerno = Column(String(64),doc=u'客户号')
    custname = Column(String(512),doc=u'客户姓名')
    custtype = Column(String(64),doc=u'公私标志')
    loantype = Column(String(64),doc=u'贷款类型')
    certno = Column(String(64),doc=u'身份证号')
    model_type = Column(String(64),doc=u'模型类型')
    base_score = Column(DECIMAL(18,6),doc=u'基准分')
    common_score = Column(DECIMAL(18,6),doc=u'通用模型分值')
    professor_score = Column(DECIMAL(18,6),doc=u'专家模型分值')
    all_score = Column(DECIMAL(18,6),doc=u'总分')
    level = Column(String(64),doc=u'测算评级')
    adj_level = Column(String(64),doc=u'调整评级（不良下调）')
    now_level = Column(String(64),doc=u'当前等级（查看）')
    adj_res = Column(String(512),doc=u'调整说明')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class GradePerCommonScore(NXBase):
    u"""
        对私通用模型分值表
     """
     __tablename__='cr_gradepercommonscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    allscore_id = Column(BigInteger,doc=u'')
    age = Column(DECIMAL(18,2),doc=u'年龄')
    age_score = Column(DECIMAL(18,6),doc=u'年龄分值')
    sex = Column(String(64),doc=u'性别')
    sex_score = Column(DECIMAL(18,6),doc=u'性别分值')
    education = Column(String(64),doc=u'最高学历')
    education_score = Column(DECIMAL(18,6),doc=u'最高学历分值')
    marriage = Column(String(64),doc=u'婚姻状况')
    marriage_score = Column(DECIMAL(18,6),doc=u'婚姻状况分值')
    workpro = Column(String(64),doc=u'单位性质')
    workpro_score = Column(DECIMAL(18,6),doc=u'单位性质分值')
    avgdep = Column(DECIMAL(30,6),doc=u'日均存款')
    avgdep_score = Column(DECIMAL(18,6),doc=u'日均存款分值')
    starlevel = Column(String(64),doc=u'客户星级')
    starlevel_score = Column(DECIMAL(18,6),doc=u'客户星级分值')
    starlevel_r = Column(String(64),doc=u'原客户星级')
    count_score = Column(DECIMAL(18,6),doc=u'通用模型分值汇总')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')
    source_date = Column(Date,doc=u'数据日期')


class GradePerFarmerScore(NXBase):
    u"""
        对私农户乐分值表
     """
     __tablename__='cr_gradeperfarmerscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    allscore_id = Column(BigInteger,doc=u'')
    exp_income = Column(DECIMAL(18,6),doc=u'支出收入比')
    exp_income_score = Column(DECIMAL(18,6),doc=u'支出收入比分值')
    house_value = Column(DECIMAL(18,6),doc=u'房产价值')
    house_value_score = Column(DECIMAL(18,6),doc=u'房产价值分值')
    breed_income = Column(DECIMAL(18,6),doc=u'年种养殖收入')
    breed_income_score = Column(DECIMAL(18,6),doc=u'年种养殖收入分值')
    dis_income = Column(DECIMAL(18,6),doc=u'可支配收入')
    dis_income_score = Column(DECIMAL(18,6),doc=u'可支配收入分值')
    count_score = Column(DECIMAL(18,6),doc=u'专家模型分值汇总')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class GradePerEmpScore(NXBase):
    u"""
        对私金领乐工薪乐分值表
     """
     __tablename__='cr_gradeperempscore'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    allscore_id = Column(BigInteger,doc=u'')
    job = Column(String(64),doc=u'职务')
    job_score = Column(DECIMAL(18,6),doc=u'职务分值')
    workyear = Column(DECIMAL(18,2),doc=u'工作年限')
    workyear_score = Column(DECIMAL(18,6),doc=u'工作年限分值')
    year_wage = Column(DECIMAL(18,2),doc=u'年工资收入')
    year_wage_score = Column(DECIMAL(18,6),doc=u'年工资收入分值')
    if_social = Column(String(64),doc=u'是否缴纳社保')
    if_social_score = Column(DECIMAL(18,6),doc=u'是否缴纳社保分值')
    pro_fund = Column(DECIMAL(22,4),doc=u'公积金月缴存额')
    pro_fund_score = Column(DECIMAL(18,6),doc=u'公积金月缴存额分值')
    pro_year = Column(DECIMAL(18,4),doc=u'公积金持续年份')
    pro_year_score = Column(DECIMAL(18,6),doc=u'公积金持续年份分值')
    exp_income = Column(DECIMAL(18,6),doc=u'支出收入比')
    exp_income_score = Column(DECIMAL(18,6),doc=u'支出收入比分值')
    house_value = Column(DECIMAL(18,4),doc=u'房产价值')
    house_value_score = Column(DECIMAL(18,6),doc=u'房产价值分值')
    count_score = Column(DECIMAL(18,6),doc=u'专家模型分值汇总')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')


class GradePubBase(NXBase):
    u"""
        对公评级基础信息表
     """
     __tablename__='cr_gradepubbase'
    id = Column(BigInteger,doc=u'ID',primary_key=True)
    customerno = Column(String(64),doc=u'客户号')
    custno = Column(String(64),doc=u'客户内码')
    custname = Column(String(512),doc=u'客户姓名')
    custtype = Column(String(64),doc=u'公私标志')
    loantype = Column(String(64),doc=u'贷款类型')
    man_age = Column(DECIMAL(18,2),doc=u'经营者年龄')
    man_edu = Column(String(64),doc=u'经营者学历')
    main_industry = Column(String(64),doc=u'主行业')
    detail_industry = Column(String(64),doc=u'子行业')
    comp_age = Column(DECIMAL(18,2),doc=u'企业经营年限')
    comp_num = Column(DECIMAL(18,2),doc=u'企业职工人数')
    elect_value = Column(DECIMAL(18,2),doc=u'用电量')
    wate_ect_pay = Column(DECIMAL(18,6),doc=u'水电费支出同比增长率')
    taxes_pay = Column(DECIMAL(18,6),doc=u'增值销项税同比增长率')
    act_cash_in = Column(DECIMAL(18,6),doc=u'实际经营性现金现金流入量')
    bill_sale = Column(DECIMAL(18,6),doc=u'开票销售率')
    sale_add = Column(DECIMAL(18,6),doc=u'销售增长率')
    sale_fin = Column(DECIMAL(18,6),doc=u'销售融资比')
    add_taxes = Column(DECIMAL(18,6),doc=u'新增融资纳税比')
    wage_pay = Column(DECIMAL(18,6),doc=u'工资性支出同比增长')
    acc_turn = Column(DECIMAL(18,6),doc=u'应收账款周转率')
    net_asset = Column(DECIMAL(18,6),doc=u'净资产')
    cash_in = Column(DECIMAL(18,6),doc=u'现金流入量')
    gross_ratio = Column(DECIMAL(18,6),doc=u'')
    asset_ratio = Column(DECIMAL(18,6),doc=u'资产负债率')
    from_date = Column(Date,doc=u'生效日期')
    end_date = Column(Date,doc=u'失效日期')

