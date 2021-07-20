import MySQLdb
from MySQLdb._exceptions import OperationalError
import datetime 
import re

def db_login(user, passwd, server_addr, dbname):
    try:
        db = MySQLdb.connect(server_addr, user, passwd, dbname, charset = "utf8")
    except OperationalError:
        db = None

    return db

def db_search_client(db,ID_number,name,tele_num,live_addr):
    cursor = db.cursor()
    cursor.execute("select * from customer")
    tabs = cursor.fetchall()
    res = list()


    for tab in tabs:
        
        if(not ID_number.isspace() and len(ID_number) != 0):
            if(ID_number.lower() == str(tab[0]).lower()):
                if(not name.isspace() and len(name) != 0):
                    if(name.lower() == str(tab[1]).lower()):
                        if(not tele_num.isspace() and len(tele_num) != 0):
                            if(tele_num.lower() == str(tab[2]).lower()):
                                if(not live_addr.isspace() and len(live_addr) != 0):
                                    if(live_addr.lower() == str(tab[3]).lower()):
                                        res.append(tab)
                                else:
                                    res.append(tab)
                        else:
                            if(not live_addr.isspace() and len(live_addr) != 0):
                                if(live_addr.lower() == str(tab[3]).lower()):
                                    res.append(tab)
                            else:
                                res.append(tab)
                else:
                    if(not tele_num.isspace() and len(tele_num) != 0):
                        if(tele_num.lower() == str(tab[2]).lower()):
                            if(not live_addr.isspace() and len(live_addr) != 0):
                                if(live_addr.lower() == str(tab[3]).lower()):
                                    res.append(tab)
                            else:
                                res.append(tab)
                    else:
                        if(not live_addr.isspace() and len(live_addr) != 0):
                            if(live_addr.lower() == str(tab[3]).lower()):
                                res.append(tab)
                        else:
                            res.append(tab)
        else:
            if(not name.isspace() and len(name) != 0):
                if(name.lower() == str(tab[1]).lower()):
                    if(not tele_num.isspace() and len(tele_num) != 0):
                        if(tele_num.lower() == str(tab[2]).lower()):
                            if(not live_addr.isspace() and len(live_addr) != 0):
                                if(live_addr.lower() == str(tab[3]).lower()):
                                    res.append(tab)
                            else:
                                res.append(tab)
                    else:
                        if(not live_addr.isspace() and len(live_addr) != 0):
                            if(live_addr.lower() == str(tab[3]).lower()):
                                res.append(tab)
                        else:
                            res.append(tab)
            else:
                if(not tele_num.isspace() and len(tele_num) != 0):
                    if(tele_num.lower() == str(tab[2]).lower()):
                        if(not live_addr.isspace() and len(live_addr) != 0):
                            if(live_addr.lower() == str(tab[3]).lower()):
                                res.append(tab)
                        else:
                            res.append(tab)
                else:
                    if(not live_addr.isspace() and len(live_addr) != 0):
                        if(live_addr.lower() == str(tab[3]).lower()):
                            res.append(tab)
                    else:
                        res.append(tab)
        
    
    cursor.close()
    return res

def db_delete_client(db,ID_num):
    cursor = db.cursor()
    
    cursor.execute("select * from loan_customer where ID = '%s'" %ID_num)
    tabs = cursor.fetchall()

    if(tabs != ()):
        cursor.close()
        return 1

    cursor.execute("select * from FK_customer_check_ac where ID = '%s'" %ID_num)
    tabs = cursor.fetchall() 
    if(tabs != ()):
        cursor.close()
        return 2

    cursor.execute("select * from FK_customer_savings_ac where ID = '%s'" %ID_num)
    tabs = cursor.fetchall()
    if(tabs != ()):
        cursor.close()
        return 3
    
    try:
        cursor.execute("delete from customer where ID = '%s'"  %ID_num)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 4

    cursor.close()
    return 0

def is_ID(str):
    if(len(str) != 18):
        return False
    string = str[:17]
    if(not string.isdigit()):
        return False
    if(not str[17:18].isdigit() and not str[17:18] == 'x'):
        return False
    
    return True

def is_email(email):
    if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
        return True
    else:
        return False

def db_linkman_Search(db,ID_num):
    res = []
    if(ID_num.isspace() or len(ID_num) == 0):
        res.append(0)
        res.append(['','',''])
        return res
    if(not is_ID(ID_num)):
        res.append(1)
        return res
    cursor = db.cursor()
    cursor.execute("select mname,telephone,email from bank_member where ID = '%s'" %ID_num)
    tab = cursor.fetchone()
    if(tab == None):
        res.append(2)
        return res
    else:
        res.append(0)
        res.append(tab)
        return res


def db_add_client(db,ID_number,name,tele_num,live_addr,l_name,l_tele,l_email,l_rela):
    if(ID_number.isspace() or len(ID_number) == 0):
        return 8
    if(not is_ID(ID_number)):
        return 1
    string = "~!@#$%^&*()_+-*/<>,.[]\'`\"‘“?？，。{\}、"
    for i in string:
        if i in name:          
            return 3
        if i in l_name:
            return 5
    if(not tele_num.isspace() and len(tele_num) != 0):
        if(not tele_num.isdigit()):
            return 4
    if(not l_tele.isspace() and len(l_tele) != 0):
        if(not l_tele.isdigit()):
            return 6
    if(not l_email.isspace() and len(l_email) != 0):
        if(not is_email(l_email)):
            return 7

    cursor = db.cursor()
    cursor.execute("select * from customer where ID = '%s'" %ID_number)
    tabs = cursor.fetchall()
    if(tabs != ()):
        cursor.close()
        return 2
    
    try:
        cursor.execute("insert into customer (ID) values ('%s')" %ID_number)
        if(not tele_num.isspace() and len(tele_num) != 0):
            cursor.execute("update customer set telephone = '%s' where ID = '%s'" %(tele_num,ID_number))
        if(not name.isspace() and len(name) != 0):
            cursor.execute("update customer set cname = '%s' where ID = '%s'" %(name,ID_number))
        if(not live_addr.isspace() and len(live_addr) != 0):
            cursor.execute("update customer set address = '%s' where ID = '%s'" %(live_addr,ID_number))
        if(not l_name.isspace() and len(l_name) != 0):
            cursor.execute("update customer set link_name = '%s' where ID = '%s'" %(l_name,ID_number))
            if(not l_rela.isspace() and len(l_rela) != 0):
                cursor.execute("update customer set relationship = '%s' where ID = '%s'" %(l_rela,ID_number))
        if(not l_tele.isspace() and len(l_tele) != 0):
            cursor.execute("update customer set link_telephone = '%s' where ID = '%s'" %(l_tele,ID_number))
        if(not l_email.isspace() and len(l_email) != 0):
            cursor.execute("update customer set link_Email = '%s' where ID = '%s'" %(l_email,ID_number))
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 9

    cursor.close()
    return 0

def db_update_client(db,ID_number,name,tele_num,live_addr,l_name,l_tele,l_email,l_rela):
    if(ID_number.isspace() or len(ID_number) == 0):
        return 1
    if(not is_ID(ID_number)):
        return 2

    string = "~!@#$%^&*()_+-*/<>,.[]\'`\"‘“?？，。{\}、"
    for i in string:
        if i in name:          
            return 3
        if i in l_name:
            return 5
    if(not tele_num.isspace() and len(tele_num) != 0):
        if(not tele_num.isdigit()):
            return 4
    if(not l_tele.isspace() and len(l_tele) != 0):
        if(not l_tele.isdigit()):
            return 6
    if(not l_email.isspace() and len(l_email) != 0):
        if(not is_email(l_email)):
            return 7

    cursor = db.cursor()
    cursor.execute("select * from customer where ID = '%s'" %ID_number)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 8

    try:
        if(not tele_num.isspace() and len(tele_num) != 0):
            cursor.execute("update customer set telephone = '%s' where ID = '%s'" %(tele_num,ID_number))
        if(not name.isspace() and len(name) != 0):
            cursor.execute("update customer set cname = '%s' where ID = '%s'" %(name,ID_number))
        if(not live_addr.isspace() and len(live_addr) != 0):
            cursor.execute("update customer set address = '%s' where ID = '%s'" %(live_addr,ID_number))
        if(not l_name.isspace() and len(l_name) != 0):
            cursor.execute("update customer set link_name = '%s' where ID = '%s'" %(l_name,ID_number))
        if(not l_tele.isspace() and len(l_tele) != 0):
            cursor.execute("update customer set link_telephone = '%s' where ID = '%s'" %(l_tele,ID_number))
        if(not l_email.isspace() and len(l_email) != 0):
            cursor.execute("update customer set link_Email = '%s' where ID = '%s'" %(l_email,ID_number))
        if(not l_rela.isspace() and len(l_rela) != 0):
                cursor.execute("update customer set relationship = '%s' where ID = '%s'" %(l_rela,ID_number))
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 9

    cursor.close()
    return 0

def db_search_account(db,ac_num,bank_name,ID_num,flag):
    ac = list()
    if(not ID_num.isspace() and len(ID_num) != 0):
        cursor_3 = db.cursor()
        cursor_4 = db.cursor()
        cursor_3.execute("select account_num from fk_customer_check_ac where ID = '%s'" %ID_num)
        cursor_4.execute("select account_num from fk_customer_savings_ac where ID = '%s'" %ID_num)
        tabs_3 = cursor_3.fetchall()
        tabs_4 = cursor_4.fetchall()
        if(flag == 0):
            for tab in tabs_3:
                ac.append(tab[0])
            for tab in tabs_4:
                ac.append(tab[0])
        elif(flag == 1):
            for tab in tabs_4:
                ac.append(tab[0])
        elif(flag == 2):
            for tab in tabs_3:
                ac.append(tab[0])
        cursor_3.close()
        cursor_4.close()

    cursor_1 = db.cursor()
    cursor_2 = db.cursor()
    cursor_1.execute("select * from check_ac")
    cursor_2.execute("select * from savings_ac")
    tabs_1 = cursor_1.fetchall()
    tabs_2 = cursor_2.fetchall()
    res = list()

    if(not ac_num.isspace() and len(ac_num) != 0):
        if(not ID_num.isspace() and len(ID_num) != 0):
            if not ac_num in ac:
                return res
        if(flag != 1):
            for tab in tabs_1:
                if(not bank_name.isspace() and len(bank_name) != 0):
                    if(tab[1] == bank_name and tab[0] == ac_num):
                        res.append(tab)
                else:
                    if(tab[0] == ac_num):
                        res.append(tab)
        if(flag != 2):
            for tab in tabs_2:
                if(not bank_name.isspace() and len(bank_name) != 0):
                    if(tab[1] == bank_name and tab[0] == ac_num):
                        res.append(tab)
                else:
                    if(tab[0] == ac_num):
                        res.append(tab)
    else:
        if(flag != 1):
            for tab in tabs_1:
                if(not bank_name.isspace() and len(bank_name) != 0):
                    if(not ID_num.isspace() and len(ID_num) != 0):
                        if(tab[1] == bank_name and tab[0] in ac):
                            res.append(tab)
                    else:
                        if(tab[1] == bank_name):
                            res.append(tab)
                else:
                    if(not ID_num.isspace() and len(ID_num) != 0):
                        if(tab[0] in ac):
                            res.append(tab)
                    else:
                        res.append(tab)
        if(flag != 2):
            for tab in tabs_2:
                if(not bank_name.isspace() and len(bank_name) != 0):
                    if(not ID_num.isspace() and len(ID_num) != 0):
                        if(tab[1] == bank_name and tab[0] in ac):
                            res.append(tab)
                    else:
                        if(tab[1] == bank_name):
                            res.append(tab)
                else:
                    if(not ID_num.isspace() and len(ID_num) != 0):
                        if(tab[0] in ac):
                            res.append(tab)
                    else:
                        res.append(tab)

    cursor_1.close()                                                                               
    cursor_2.close()
    return res

def db_search_ac_client(db,ac_num,ac_type):
    cursor = db.cursor()
    res = list()
    if(ac_type == 0):
        cursor.execute("select ID from fk_customer_check_ac where account_num = '%s'" %ac_num)
        tabs = cursor.fetchall()

        for tab in tabs:
            res.append(tab)
    if(ac_type == 1):
        cursor.execute("select ID from fk_customer_savings_ac where account_num = '%s'" %ac_num)
        tabs = cursor.fetchall()

        for tab in tabs:
            res.append(tab)
    
    cursor.close()
    return res

def db_delete_account(db,ac_num,ac_type):
    cursor = db.cursor()
    try:
        cursor.execute("delete from account where account_num = '%s'" %ac_num)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 1
    
    try:
        if(ac_type == 0):
            cursor.execute("delete from savings_ac where account_num = '%s'" %ac_num)
            cursor.execute("delete from fk_customer_savings_ac where account_num = '%s'" %ac_num)
        else:
            cursor.execute("delete from check_ac where account_num = '%s'" %ac_num)
            cursor.execute("delete from fk_customer_check_ac where account_num = '%s'" %ac_num)
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 1
    
    cursor.close()
    return 0

def db_add_account(db,ac_num,bank_name,ac_money,rate,money_type,credit_line,ac_type):
    if(ac_num.isspace() or len(ac_num) == 0):
        return 1
    
    creat_time = datetime.datetime.now().strftime('%F %T')
    cursor = db.cursor()
    cursor.execute("select * from account where account_num = '%s'" %ac_num)
    tabs = cursor.fetchall()
    if(tabs != ()):
        cursor.close()
        return 3
    
    if(not bank_name.isspace() and len(bank_name) != 0):
        cursor.execute("select * from bank where bank_name = '%s'" %bank_name)
        tabs = cursor.fetchall()
        if(tabs == ()):
            cursor.close()
            return 4
    
    try:
        cursor.execute("insert into account (account_num) values ('%s')" %ac_num)
        if(ac_type == 0):
            cursor.execute("insert into savings_ac (account_num) values ('%s')" %ac_num)
            cursor.execute("update account set account_type = '%s' where account_num = '%s'" %('储蓄账户',ac_num))
        elif(ac_type == 1):
            cursor.execute("insert into check_ac (account_num) values ('%s')" %ac_num)
            cursor.execute("update account set account_type = '%s' where account_num = '%s'" %('支票账户',ac_num))
        
        if(not bank_name.isspace() and len(bank_name) != 0):
            cursor.execute("update account set bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
            if(ac_type == 0):
                cursor.execute("update savings_ac set ban_bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
            elif(ac_type == 1):
                cursor.execute("update check_ac set ban_bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
                
        if(not ac_money.isspace() and len(ac_money) != 0):
            cursor.execute("update account set money = '%s' where account_num = '%s'" %(ac_money,ac_num))
            if(ac_type == 0):
                cursor.execute("update savings_ac set money = '%s' where account_num = '%s'" %(ac_money,ac_num))
            elif(ac_type == 1):
                cursor.execute("update check_ac set money = '%s' where account_num = '%s'" %(ac_money,ac_num)) 
        cursor.execute("update account set account_date = '%s' where account_num = '%s'" %(creat_time,ac_num))
        if(ac_type == 0):
            cursor.execute("update savings_ac set account_date = '%s' where account_num = '%s'" %(creat_time,ac_num))
        elif(ac_type == 1):
            cursor.execute("update check_ac set account_date = '%s' where account_num = '%s'" %(creat_time,ac_num)) 

        if(not rate.isspace() and len(rate) != 0):
            cursor.execute("update savings_ac set interest_rate = '%s' where account_num = '%s'" %(rate,ac_num))
        if(not money_type.isspace() and len(money_type) != 0):
            cursor.execute("update savings_ac set money_type = '%s' where account_num = '%s'" %(money_type,ac_num)) 
        if(not credit_line.isspace() and len(credit_line) != 0): 
            cursor.execute("update check_ac set credit_line = '%s' where account_num = '%s'" %(credit_line,ac_num))       

        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 2

    cursor.close()
    return 0

def db_update_account(db,ac_num,bank_name,ac_money,rate,money_type,credit_line,ac_type):
    if(ac_num.isspace() or len(ac_num) == 0):
        return 1
    

    cursor = db.cursor()
    cursor.execute("select * from account where account_num = '%s'" %ac_num)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 3
    
    if(not bank_name.isspace() and len(bank_name) != 0):
        cursor.execute("select * from bank where bank_name = '%s'" %bank_name)
        tabs = cursor.fetchall()
        if(tabs == ()):
            cursor.close()
            return 4

    try:
        if(not bank_name.isspace() and len(bank_name) != 0):
            cursor.execute("update account set bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
            if(ac_type == 0):
                cursor.execute("update savings_ac set ban_bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
            elif(ac_type == 1):
                cursor.execute("update check_ac set ban_bank_name = '%s' where account_num = '%s'" %(bank_name,ac_num))
        if(not ac_money.isspace() and len(ac_money) != 0):
            cursor.execute("update account set money = '%s' where account_num = '%s'" %(ac_money,ac_num))
            if(ac_type == 0):
                cursor.execute("update savings_ac set money = '%s' where account_num = '%s'" %(ac_money,ac_num))
            elif(ac_type == 1):
                cursor.execute("update check_ac set money = '%s' where account_num = '%s'" %(ac_money,ac_num))
        
        if(not rate.isspace() and len(rate) != 0):
            cursor.execute("update savings_ac set interest_rate = '%s' where account_num = '%s'" %(rate,ac_num))
        if(not money_type.isspace() and len(money_type) != 0):
            cursor.execute("update savings_ac set money_type = '%s' where account_num = '%s'" %(money_type,ac_num)) 
        if(not credit_line.isspace() and len(credit_line) != 0): 
            cursor.execute("update check_ac set credit_line = '%s' where account_num = '%s'" %(credit_line,ac_num))

        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 2


    cursor.close()
    return 0


def db_add_clienttoaccount(db,ac_num,ID_num):
    if(ac_num.isspace() or len(ac_num) == 0):
        return 1
    if(ID_num.isspace() or len(ID_num) == 0):
        return 1
    cursor = db.cursor()
    cursor.execute("select * from account where account_num =  '%s'" %ac_num)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 2
    
    cursor.execute("select * from customer where ID =  '%s'" %ID_num)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 3
    
    cursor.execute("select bank_name,account_type from account where account_num = '%s'" %ac_num)
    tabs = cursor.fetchall()
    bank_name = tabs[0][0]
    ac_type = tabs[0][1]

    if(ac_type == '储蓄账户'):
        cursor.execute("select * from savings_bank_client where bank_name = '%s' and ID = '%s'" %(bank_name,ID_num))
        tabs = cursor.fetchall()
        if(tabs != ()):
            cursor.close()
            return 4
    elif(ac_type == '支票账户'):
        cursor.execute("select * from check_bank_client where bank_name = '%s' and ID = '%s'" %(bank_name,ID_num))
        tabs = cursor.fetchall()
        if(tabs != ()):
            cursor.close()
            return 5
    
    try:
        if(ac_type == '储蓄账户'):
            cursor.execute("insert into fk_customer_savings_ac (ID,account_num) values ('%s','%s')" %(ID_num,ac_num))
            cursor.execute("insert into savings_bank_client (ID,bank_name) values ('%s','%s')" %(ID_num,bank_name))
        elif(ac_type == '支票账户'):
            cursor.execute("insert into fk_customer_check_ac (ID,account_num) values ('%s','%s')" %(ID_num,ac_num))
            cursor.execute("insert into check_bank_client (ID,bank_name) values ('%s','%s')" %(ID_num,bank_name))

        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 6

    cursor.close()
    return 0

def db_delete_clienttoaccount(db,ac_num,ID_num):
    if(ac_num.isspace() or len(ac_num) == 0):
        return 1
    if(ID_num.isspace() or len(ID_num) == 0):
        return 1
    cursor = db.cursor()
    cursor.execute("select * from account where account_num =  '%s'" %ac_num)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 2
    
    cursor.execute("select * from customer where ID =  '%s'" %ID_num)
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return 3
    
    cursor.execute("select bank_name,account_type from account where account_num = '%s'" %ac_num)
    tab = cursor.fetchone()
    bank_name = tab[0]
    ac_type = tab[1]
    print(ac_type + bank_name)
    if(ac_type == '储蓄账户'):
        cursor.execute("select * from fk_customer_savings_ac where account_num = '%s' and ID = '%s'" %(ac_num,ID_num))
        tabs = cursor.fetchall()
        if(tabs == ()):
            cursor.close()
            return 4
    elif(ac_type == '支票账户'):
        cursor.execute("select * from fk_customer_check_ac where account_num = '%s' and ID = '%s'" %(ac_num,ID_num))
        tabs = cursor.fetchall()
        if(tabs == ()):
            cursor.close()
            return 5
    
    try:
        if(ac_type == '储蓄账户'):
            cursor.execute("delete from fk_customer_savings_ac where account_num = '%s' and ID = '%s'" %(ac_num,ID_num))
            cursor.execute("delete from savings_bank_client where ID = '%s' and bank_name = '%s'" %(ID_num,bank_name))
        elif(ac_type == '支票账户'):
            cursor.execute("delete from fk_customer_check_ac where account_num = '%s' and ID = '%s'" %(ac_num,ID_num))
            cursor.execute("delete from check_bank_client where ID = '%s' and bank_name = '%s'" %(ID_num,bank_name))

        db.commit()
    except:
        db.roolback()
        cursor.close()
        return 6

    cursor.close()
    return 0


def db_search_loan(db,loan_num,loan_bank,ID_num,loan_state):
    cursor = db.cursor()
    res = list()
    loan = list()
    if(not ID_num.isspace() and len(ID_num) != 0):
        cursor.execute("select loan_ID from loan_customer where ID = '%s'" %ID_num)
        tabs = cursor.fetchall()
        for tab in tabs:
            loan.append(tab[0])
        if(loan == []):
            cursor.close()
            return res
        if(not loan_num.isspace() and len(loan_num) != 0):
            if(loan_num not in loan):
                cursor.close()
                return res
    
    cursor.execute("select * from loan")
    tabs = cursor.fetchall()
    
    for tab in tabs:
        if(not loan_num.isspace() and len(loan_num) != 0):
            if(tab[0] == loan_num):
                if(not loan_bank.isspace() and len(loan_bank) != 0):
                    if(tab[1] == loan_bank):
                        if(loan_state != '全部状态'):
                            if(tab[4] == loan_state):
                                res.append(tab)
                        else:
                            res.append(tab)
                else:
                    if(loan_state != '全部状态'):
                        if(tab[4] == loan_state):
                            res.append(tab)
                    else:
                        res.append(tab)
        else:
            if(not ID_num.isspace() and len(ID_num) != 0):
                if(tab[0] in loan):
                    if(not loan_bank.isspace() and len(loan_bank) != 0):
                        if(tab[1] == loan_bank):
                            if(loan_state != '全部状态'):
                                if(tab[4] == loan_state):
                                    res.append(tab)
                            else:
                                res.append(tab)
                    else:
                        if(loan_state != '全部状态'):
                            if(tab[4] == loan_state):
                                res.append(tab)
                        else:
                            res.append(tab)
            else:
                if(not loan_bank.isspace() and len(loan_bank) != 0):
                    if(tab[1] == loan_bank):
                        if(loan_state != '全部状态'):
                            if(tab[4] == loan_state):
                                res.append(tab)
                        else:
                            res.append(tab)
                else:
                    if(loan_state != '全部状态'):
                        if(tab[4] == loan_state):
                            res.append(tab)
                    else:
                        res.append(tab)

    cursor.close()
    return res


def db_search_loan_client(db,loan_num):
    cursor = db.cursor()
    res = list()

    cursor.execute("select ID from loan_customer where loan_ID = '%s'" %loan_num)
    tabs = cursor.fetchall()

    for tab in tabs:
        res.append(tab[0])

    cursor.close()
    return res


def db_delete_loan(db,loan_ID):
    cursor = db.cursor()
    cursor.execute("select status from loan where loan_ID = '%s'" %loan_ID)
    tab = cursor.fetchone()
    if(tab[0] == '发放中'):
        cursor.close()
        return 2
    
    try:
        cursor.execute("delete from loan where loan_ID = '%s'" %loan_ID)

        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 1

    cursor.close()
    return 0

def db_provide_loan(db,loan_num,loan_money,loan_sum,times):
    if(loan_money.isspace() or len(loan_money) == 0):
        return 1
    money = float(loan_money)
    cursor = db.cursor()
    cursor.execute("select * from loan_condition where loan_ID = '%s'" %loan_num)
    tabs = cursor.fetchall()
    now_money = 0
    p_times = len(tabs)
    if(p_times >= times):
        cursor.close()
        return 2
    
    for tab in tabs:
        now_money += float(tab[2])
    
    now = datetime.datetime.now().strftime('%F %T')
    if(times - p_times == 1):
        if((now_money + money) > loan_sum):
            cursor.close()
            return 3
        elif((now_money + money) < loan_sum):
            cursor.close()
            return 5
        else:
            try:
                cursor.execute("update loan set status = '%s' where loan_ID = '%s'" %('已全部发放',loan_num))
                cursor.execute("insert into loan_condition (loan_ID,loan_date,loan_money) values ('%s','%s','%s')" %(loan_num,now,loan_money))
                db.commit()
            except:
                db.rollback()
                cursor.close()
                return 4
    else:
        if((now_money + money) >= loan_sum):
            cursor.close()
            return 3
        try:
            if(p_times == 0 & times != 1):
                cursor.execute("update loan set status = '%s' where loan_ID = '%s'" %('发放中',loan_num))
            if(p_times == 0 & times == 1):
                cursor.execute("update loan set status = '%s' where loan_ID = '%s'" %('已全部发放',loan_num))
            cursor.execute("insert into loan_condition (loan_ID,loan_date,loan_money) values ('%s','%s','%s')" %(loan_num,now,loan_money))
            db.commit()
        except:
            db.rollback()
            cursor.close()
            return 4

    cursor.close()
    return 0

def db_provide_loan_2(db,loan_num,loan_sum):
    cursor = db.cursor()
    cursor.execute("select * from loan_condition where loan_ID = '%s'" %loan_num)
    tabs = cursor.fetchall()
    now_money = 0
    for tab in tabs:
        now_money += float(tab[2])

    money = str(loan_sum - now_money)
    now = datetime.datetime.now().strftime('%F %T')
    try:
        cursor.execute("update loan set status = '%s' where loan_ID = '%s'" %('已全部发放',loan_num))
        cursor.execute("insert into loan_condition (loan_ID,loan_date,loan_money) values ('%s','%s','%s')" %(loan_num,now,money))
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return 1

    cursor.close()
    return 0

def db_add_loan(db,loan_num,loan_bank,loan_amount,loan_times,ID_list):
    if(loan_num.isspace() or len(loan_num) == 0):
        return (1,0)
    if(loan_bank.isspace() or len(loan_bank) == 0):
        return (2,0)
    if(loan_amount.isspace() or len(loan_amount) == 0):
        return (3,0)
    if(loan_times.isspace() or len(loan_times) == 0):
        return (4,0)
    
    time = float(loan_times)
    if(not time.is_integer() or time <= 0):
        return (5,0)
    
    cursor = db.cursor()

    cursor.execute("select * from loan where loan_ID = '%s'" %loan_num)
    tabs = cursor.fetchall()
    if(tabs != ()):
        cursor.close()
        return (6,0)

    cursor.execute("select * from bank where bank_name = '%s'" %loan_bank) 
    tabs = cursor.fetchall()
    if(tabs == ()):
        cursor.close()
        return (7,0)
    
    i = 0
    for ID_num in ID_list:
        cursor.execute("select * from customer where ID = '%s'" %ID_num) 
        tabs = cursor.fetchall()
        if(tabs == ()):
            cursor.close()
            return (8,i)
        i += 1 
    
    try:
        cursor.execute("insert into loan (loan_ID) values ('%s')" %loan_num)
        cursor.execute("update loan set bank_name = '%s',loan_amount = '%s',times = '%s',status = '%s' where loan_ID = '%s'" %(loan_bank,loan_amount,loan_times,'未开始发放',loan_num))

        for ID_num in ID_list:
            cursor.execute("insert into loan_customer (loan_ID,ID) values ('%s','%s')" %(loan_num,ID_num))
        
        db.commit()
    except:
        db.rollback()
        cursor.close()
        return (9,0)

    cursor.close()
    return (0,0)

def db_search_loan_condition(db,loan_num):
    cursor = db.cursor()
    res = list()

    cursor.execute("select * from loan_condition where loan_ID = '%s'" %loan_num)
    tabs = cursor.fetchall()
    for tab in tabs:
        res.append(tab)

    cursor.close()
    return res

def db_business_search(db,year,season,month):
    db_year = int(year)
    db_season = season
    
    if(month == '——请选择'):
        if(db_season == '一'):
            db_month = 3
            old_year = db_year - 1
            old_month = 12
        elif(db_season == '二'):
            db_month = 6
            old_year = db_year
            old_month = 3
        elif(db_season == '三'):
            db_month = 9
            old_year = db_year
            old_month = 6
        elif(db_season == '四'):
            db_month = 12
            old_year = db_year
            old_month = 9
        elif(db_season == '——请选择'):
            db_month = 12
            old_year = db_year - 1
            old_month = 12
    else:
        db_month = int(month)
        if db_month == 1:
            old_year = db_year - 1
            old_month = 12
        else:
            old_year = db_year
            old_month = db_month - 1

    if(db_month == 2):
        if(db_year % 4 == 0 and db_year % 100 != 0 or db_year % 400 == 0):
            db_day = 29
        else:
            db_day = 28
    elif(db_month == 4 or db_month == 6 or db_month == 9 or db_month == 11):
        db_day = 30
    else:
        db_day = 31
    
    if(old_month == 2):
        if(old_year % 4 == 0 and old_year % 100 != 0 or old_year % 400 == 0):
            old_day = 29
        else:
            old_day = 28
    elif(old_month == 4 or old_month == 6 or old_month == 9 or old_month == 11):
        old_day = 30
    else:
        old_day = 31

    date = str(datetime.datetime(db_year,db_month,db_day))
    old_date = str(datetime.datetime(old_year,old_month,old_day))

    cursor = db.cursor()
    res = list()
    bank = list()

    cursor.execute("select bank_name from bank")
    tabs = cursor.fetchall()
    for tab in tabs:
        bank.append(tab[0])
    
    for bank_name in bank:
        ac_users = 0
        amount = 0
        loan = 0
        saving_ac = list()
        check_ac = list()

        cursor.execute("select loan_money from loan_condition where loan_ID in (select loan_ID from loan where bank_name = '%s') and loan_date <= '%s' and loan_date > '%s'" %(bank_name,date,old_date))
        tabs = cursor.fetchall()
        for tab in tabs:
            loan += tab[0]
        
        cursor.execute("select account_num,money from savings_ac where ban_bank_name = '%s' and account_date <= '%s' and account_date > '%s'" %(bank_name,date,old_date))
        tabs = cursor.fetchall()
        for tab in tabs:
            amount += tab[1]
            saving_ac.append(tab[0])

        cursor.execute("select account_num,money from check_ac where ban_bank_name = '%s' and account_date <= '%s' and account_date > '%s'" %(bank_name,date,old_date))
        tabs = cursor.fetchall()
        for tab in tabs:
            check_ac.append(tab[0]) 
        
        for ac_num in saving_ac:
            cursor.execute("select * from fk_customer_savings_ac where account_num = '%s'" %ac_num)
            tabs = cursor.fetchall()
            for tab in tabs:
                ac_users += 1
        
        for ac_num in check_ac:
            cursor.execute("select * from fk_customer_check_ac where account_num = '%s'" %ac_num)
            tabs = cursor.fetchall()
            for tab in tabs:
                ac_users += 1

        item = (bank_name,amount,loan,ac_users)
        res.append(item)

    cursor.close()
    return res


def db_close(db):
    if db is not None:
        db.close()


if __name__ == "__main__":
    db = db_login("root", "hai31844650", "127.0.0.1", "lab3_bankmanagesys")

    tabs = db_search_client(db,'123455')
    
    db_close(db)
