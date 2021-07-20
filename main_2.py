from MySQLdb import Connect
from PyQt5.QtWidgets import QApplication, QMessageBox 
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtGui import *
from PyQt5 import QtCore
from UI.Ui_fristwindow import Ui_FirstWindow
from db import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_FirstWindow()
        self.ui.setupUi(self)
        #菜单栏动作绑定
        self.ui.statusbar.showMessage("status:ok")
        self.ui.actionSearch.triggered.connect(self.clientSearch_page)
        self.ui.actionAdd_Update.triggered.connect(self.clientAdd_page)
        self.ui.actionSearch_2.triggered.connect(self.accountSearch_page)
        self.ui.actionAdd_Update_2.triggered.connect(self.accountAdd_page)
        self.ui.actionAdd_Clients.triggered.connect(self.accountAdd_Client_page)
        self.ui.actionSearch_3.triggered.connect(self.loanSearch_page)
        self.ui.actionAdd_Update_3.triggered.connect(self.loanAdd_page)
        self.ui.actionStatistics.triggered.connect(self.statistics_business)

        #客户查询/删除界面设置及按键绑定
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget.setColumnWidth(6, 200)
        self.ui.tableWidget.setColumnWidth(3, 200)
        self.ui.tableWidget.setColumnWidth(0, 200)
        self.ui.pushButton.clicked.connect(self.Searchbtn_client)
        self.ui.pushButton_3.clicked.connect(self.Deletebtn_client)
        
        #客户新增/更新界面设置及按键绑定
        self.ui.radioButton_3.setChecked(True)
        self.ui.radioButton_5.setChecked(True)
        self.ui.radioButton_3.toggled.connect(self.Stack_3_Changeto1)
        self.ui.radioButton_4.toggled.connect(self.Stack_3_Changeto2)
        self.ui.pushButton_2.clicked.connect(self.Addbtn_client)
        self.ui.pushButton_7.clicked.connect(self.Updatebtn_client)
        
        #账户查询/删除界面设置及按键绑定
        self.ui.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tableWidget_2.setColumnWidth(7, 200)
        self.ui.tableWidget_2.setColumnWidth(8, 1000)
        self.ui.pushButton_4.clicked.connect(self.Searchbtn_account)
        self.ui.pushButton_5.clicked.connect(self.Deletebtn_account)
        
        #账户添加/更新界面设置及按键绑定
        self.ui.radioButton.setChecked(True)
        self.ui.radioButton.toggled.connect(self.Stack_2_Changeto1)
        self.ui.radioButton_2.toggled.connect(self.Stack_2_Changeto2)
        self.ui.pushButton_6.clicked.connect(self.Addbtn_account)
        self.ui.pushButton_8.clicked.connect(self.Updatebtn_account)

        #账户添加/删除关联客户界面设置及按键绑定
        self.ui.pushButton_9.clicked.connect(self.Addbtn_account_client)
        self.ui.pushButton_10.clicked.connect(self.Deletebtn_account_client)

        #贷款查询/发放/删除界面设置及按键绑定
        self.ui.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.label_42.setFont(QFont("Roman times",10.5))
        self.ui.tableWidget_3.setColumnWidth(5, 1000)
        self.ui.tableWidget_6.setColumnWidth(0, 200)
        self.ui.tableWidget_6.setColumnWidth(1, 120)
        self.ui.pushButton_11.clicked.connect(self.Searchbtn_loan)
        self.ui.pushButton_12.clicked.connect(self.Deletebtn_loan)
        
        self.ui.pushButton_16.clicked.connect(self.Providebtn_loan)
        self.ui.pushButton_17.clicked.connect(self.Providebtn_loan_2)

        #贷款添加界面设置及按键绑定
        self.ui.tableWidget_4.setColumnWidth(0, 400)
        self.ui.tableWidget_4.itemChanged.connect(self.Cell_Changed)
        self.ui.pushButton_14.clicked.connect(self.Addbtn_loan)
        self.ui.pushButton_13.clicked.connect(self.Addbtn_owner_loan)
        
        #业务统计界面设置及按键绑定
        self.ui.tableWidget_5.setColumnWidth(0, 195)
        self.ui.tableWidget_5.setColumnWidth(1, 195)
        self.ui.tableWidget_5.setColumnWidth(2, 195)
        self.ui.tableWidget_5.setColumnWidth(3, 195)
        self.ui.comboBox_3.activated.connect(self.season_change)
        self.ui.pushButton_15.clicked.connect(self.Business_statistics)

        self.show()
        #登录本地数据库
        self.db = db_login("root", "ustctangent", "127.0.0.1", "banksys")
        self.dbname = "banksys"

    def season_change(self):
        season = self.ui.comboBox_3.currentText()

        if(season == '一'):
            self.ui.stackedWidget_4.setCurrentIndex(0)
        elif(season == '二'):
            self.ui.stackedWidget_4.setCurrentIndex(1)
        elif(season == '三'):
            self.ui.stackedWidget_4.setCurrentIndex(2)
        elif(season == '四'):
            self.ui.stackedWidget_4.setCurrentIndex(3)

        self.ui.comboBox_4.setCurrentIndex(0)
        self.ui.comboBox_5.setCurrentIndex(0)
        self.ui.comboBox_6.setCurrentIndex(0)
        self.ui.comboBox_7.setCurrentIndex(0)

    def clientSearch_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def clientAdd_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def accountSearch_page(self):
        self.ui.stackedWidget.setCurrentIndex(2)
    
    def accountAdd_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def accountAdd_Client_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
    
    def loanSearch_page(self):
        self.ui.stackedWidget.setCurrentIndex(5)
    
    def loanAdd_page(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    def statistics_business(self):
        self.ui.stackedWidget.setCurrentIndex(7)
    
    def Stack_3_Changeto1(self):
        self.ui.stackedWidget_3.setCurrentIndex(0)
    
    def Stack_3_Changeto2(self):
        self.ui.stackedWidget_3.setCurrentIndex(1)

    def Stack_2_Changeto1(self):
        self.ui.stackedWidget_2.setCurrentIndex(0)

    def Stack_2_Changeto2(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    

    def Searchbtn_client(self):
        self.ui.tableWidget.setRowCount(0)
        #从文本栏获取查询数据
        ID_num = self.ui.lineEdit.text()
        Name = self.ui.lineEdit_2.text()
        telephone_num = self.ui.lineEdit_3.text()
        address = self.ui.lineEdit_4.text()
        tabs = db_search_client(self.db,str(ID_num),str(Name),str(telephone_num),str(address))
    
        currentRowCount = self.ui.tableWidget.rowCount()
        for tab in tabs:
            self.ui.tableWidget.insertRow(currentRowCount)
            
            item0 = QTableWidgetItem(str(tab[0]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1 = QTableWidgetItem(str(tab[1]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item2 = QTableWidgetItem(str(tab[2]))
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item3 = QTableWidgetItem(str(tab[3]))
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item4 = QTableWidgetItem(str(tab[4]))
            item4.setTextAlignment(QtCore.Qt.AlignCenter)
            item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item5 = QTableWidgetItem(str(tab[5]))
            item5.setTextAlignment(QtCore.Qt.AlignCenter)
            item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item6 = QTableWidgetItem(str(tab[6]))
            item6.setTextAlignment(QtCore.Qt.AlignCenter)
            item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item7 = QTableWidgetItem(str(tab[7]))
            item7.setTextAlignment(QtCore.Qt.AlignCenter)
            item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            
            self.ui.tableWidget.setItem(currentRowCount, 0, item0) #列1
            self.ui.tableWidget.setItem(currentRowCount, 1, item1) #列2
            self.ui.tableWidget.setItem(currentRowCount, 2, item2)
            self.ui.tableWidget.setItem(currentRowCount, 3, item3)
            self.ui.tableWidget.setItem(currentRowCount, 4, item4)
            self.ui.tableWidget.setItem(currentRowCount, 5, item5)
            self.ui.tableWidget.setItem(currentRowCount, 6, item6)
            self.ui.tableWidget.setItem(currentRowCount, 7, item7)

            currentRowCount += 1
            self.ui.tableWidget.setRowCount(currentRowCount)
    
    def Deletebtn_client(self):
        row = self.ui.tableWidget.currentRow()
        if(row > -1):
            ID_num = self.ui.tableWidget.item(row,0).text()
            index = db_delete_client(self.db,ID_num)
            if(index == 0):
                self.ui.tableWidget.removeRow(row)
            elif(index == 1):
                QMessageBox.warning(self,"警告","客户存在关联贷款，无法删除该用户！", QMessageBox.Yes)
            elif(index == 2):
                QMessageBox.warning(self,"警告","客户存在关联支票账户，无法删除该用户！", QMessageBox.Yes)
            elif(index == 3):
                QMessageBox.warning(self,"警告","客户存在关联存储账户，无法删除该用户！", QMessageBox.Yes)
            elif(index == 4):
                QMessageBox.warning(self,"警告","从数据库删除过程发生错误，事务已回滚！", QMessageBox.Yes)

    def Addbtn_client(self):        
        ID_num = self.ui.lineEdit_5.text()
        Name = self.ui.lineEdit_6.text()
        telephone_num = self.ui.lineEdit_7.text()
        address = self.ui.lineEdit_8.text()
        
        if(self.ui.radioButton_3.isChecked()):
            linkman_ID =  self.ui.lineEdit_9.text()
            if(self.ui.radioButton_5.isChecked()):
                linkman_relationship = '贷款负责人'
            else:
                linkman_relationship = '银行账户负责人'
            
            res = db_linkman_Search(self.db,linkman_ID)
            if(res[0] == 1):
                QMessageBox.warning(self,"警告","联系人身份证号格式错误！", QMessageBox.Yes)
                return
            elif(res[0] == 2):
                QMessageBox.warning(self,"警告","银行员工不存在，无法添加为联系人！", QMessageBox.Yes)
                return
            elif(res[0] == 0):
                linkman_name = res[1][0]
                linkman_telephone = res[1][1]
                linkman_email = res[1][2]
        else:
            linkman_name = self.ui.lineEdit_20.text()
            linkman_telephone = self.ui.lineEdit_21.text()
            linkman_email = self.ui.lineEdit_22.text()
            linkman_relationship = self.ui.lineEdit_10.text()
        

        index = db_add_client(self.db,ID_num,Name,telephone_num,address,linkman_name,linkman_telephone,linkman_email,linkman_relationship)
        if(index == 1):
            QMessageBox.warning(self,"警告","客户身份证号格式错误！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","该客户已注册！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","客户姓名不应包含特殊字符！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","客户电话号码应全部由数字组成！", QMessageBox.Yes)
        elif(index == 5):
            QMessageBox.warning(self,"警告","联系人姓名不应包含特殊字符！", QMessageBox.Yes)
        elif(index == 6):
            QMessageBox.warning(self,"警告","联系人电话号码应全部由数字组成！", QMessageBox.Yes)
        elif(index == 7): 
            QMessageBox.warning(self,"警告","联系人email格式错误！", QMessageBox.Yes)
        elif(index == 8):
            QMessageBox.warning(self,"警告","客户身份证号不能为空！", QMessageBox.Yes)
        elif(index == 9):
            QMessageBox.warning(self,"警告","向数据库插入过程发生错误，事务已回滚！", QMessageBox.Yes)
        elif(index == 0):
            QMessageBox.information(self,"提示","客户添加成功！")

        
    def Updatebtn_client(self):
        ID_num = self.ui.lineEdit_5.text()
        Name = self.ui.lineEdit_6.text()
        telephone_num = self.ui.lineEdit_7.text()
        address = self.ui.lineEdit_8.text() 
        
        if(self.ui.radioButton_3.isChecked()):
            linkman_ID =  self.ui.lineEdit_9.text()
            if(self.ui.radioButton_5.isChecked()):
                linkman_relationship = '贷款负责人'
            else:
                linkman_relationship = '银行账户负责人'
            
            res = db_linkman_Search(self.db,linkman_ID)
            
            if(res[0] == 1):
                QMessageBox.warning(self,"警告","联系人身份证号格式错误！", QMessageBox.Yes)
                return
            elif(res[0] == 2):
                QMessageBox.warning(self,"警告","银行员工不存在，无法添加为联系人！", QMessageBox.Yes)
                return
            elif(res[0] == 0):
                linkman_name = res[1][0]
                linkman_telephone = res[1][1]
                linkman_email = res[1][2]
        else:
            linkman_name = self.ui.lineEdit_20.text()
            linkman_telephone = self.ui.lineEdit_21.text()
            linkman_email = self.ui.lineEdit_22.text()
            linkman_relationship = self.ui.lineEdit_10.text()

        index = db_update_client(self.db,ID_num,Name,telephone_num,address,linkman_name,linkman_telephone,linkman_email,linkman_relationship)
        if(index == 1):
            QMessageBox.warning(self,"警告","客户身份证号不能为空！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","客户身份证号格式错误！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","客户姓名不应包含特殊字符！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","客户电话号码应全部由数字组成！", QMessageBox.Yes)
        elif(index == 5):
            QMessageBox.warning(self,"警告","联系人姓名不应包含特殊字符！", QMessageBox.Yes)
        elif(index == 6):
            QMessageBox.warning(self,"警告","联系人电话号码应全部由数字组成！", QMessageBox.Yes)
        elif(index == 7): 
            QMessageBox.warning(self,"警告","联系人email格式错误！", QMessageBox.Yes)
        elif(index == 8):
            QMessageBox.warning(self,"警告","不存在该客户！", QMessageBox.Yes)
        elif(index == 9):
            QMessageBox.warning(self,"警告","向数据库更新过程发生错误，事务已回滚！", QMessageBox.Yes)
        elif(index == 0):
            QMessageBox.information(self,"提示","客户信息更新成功！")

    def Searchbtn_account(self):
        self.ui.tableWidget_2.setRowCount(0)
        ac_ID = self.ui.lineEdit_12.text()
        bank_name = self.ui.lineEdit_13.text()
        ID_num = self.ui.lineEdit_14.text()
        
        btn1 = self.ui.checkBox.isChecked()
        btn2 = self.ui.checkBox_2.isChecked()
        if(btn1 == btn2):
            flag = 0
        elif(btn1):
            flag = 1
        else:
            flag = 2

        tabs = db_search_account(self.db,ac_ID,bank_name,ID_num,flag)

        currentRowCount = self.ui.tableWidget_2.rowCount()
        for tab in tabs:
            self.ui.tableWidget_2.insertRow(currentRowCount)
        
            item0 = QTableWidgetItem(str(tab[1]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1 = QTableWidgetItem(str(tab[0]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item3 = QTableWidgetItem(str(tab[2]))
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item7 = QTableWidgetItem(str(tab[3]))
            item7.setTextAlignment(QtCore.Qt.AlignCenter)
            item7.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            
            if(len(tab) == 5):
                clients = db_search_ac_client(self.db,tab[0],0)                
                
                item2 = QTableWidgetItem('支票账户')
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                
                item4 = QTableWidgetItem('')
                item4.setTextAlignment(QtCore.Qt.AlignCenter)
                item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item5 = QTableWidgetItem('')
                item5.setTextAlignment(QtCore.Qt.AlignCenter)
                item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item6 = QTableWidgetItem(str(tab[4]))
                item6.setTextAlignment(QtCore.Qt.AlignCenter)
                item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                clients_ID = list()
                for client in clients:
                    clients_ID.append(client[0])

                item8 = QTableWidgetItem(' '.join(clients_ID))
                item8.setTextAlignment(QtCore.Qt.AlignCenter)
                item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            if(len(tab) == 6):
                clients = db_search_ac_client(self.db,tab[0],1)
                
                item2 = QTableWidgetItem('储蓄账户')
                item2.setTextAlignment(QtCore.Qt.AlignCenter)
                item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                
                item4 = QTableWidgetItem(str(tab[4]))
                item4.setTextAlignment(QtCore.Qt.AlignCenter)
                item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item5 = QTableWidgetItem(str(tab[5]))
                item5.setTextAlignment(QtCore.Qt.AlignCenter)
                item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item6 = QTableWidgetItem(str(''))
                item6.setTextAlignment(QtCore.Qt.AlignCenter)
                item6.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                clients_ID = list()
                for client in clients:
                    clients_ID.append(client[0])
                
                item8 = QTableWidgetItem(",".join(map(str,clients_ID)))
                item8.setTextAlignment(QtCore.Qt.AlignCenter)
                item8.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        
            self.ui.tableWidget_2.setItem(currentRowCount, 0, item0) #列1
            self.ui.tableWidget_2.setItem(currentRowCount, 1, item1) #列2
            self.ui.tableWidget_2.setItem(currentRowCount, 2, item2)
            self.ui.tableWidget_2.setItem(currentRowCount, 3, item3)
            self.ui.tableWidget_2.setItem(currentRowCount, 4, item4)
            self.ui.tableWidget_2.setItem(currentRowCount, 5, item5)
            self.ui.tableWidget_2.setItem(currentRowCount, 6, item6)
            self.ui.tableWidget_2.setItem(currentRowCount, 7, item7)
            self.ui.tableWidget_2.setItem(currentRowCount, 8, item8)

            currentRowCount += 1
            self.ui.tableWidget_2.setRowCount(currentRowCount)



    def Deletebtn_account(self):
        row = self.ui.tableWidget_2.currentRow()
        if(row > -1):
            ac_num = self.ui.tableWidget_2.item(row,1).text()
            ac_type = self.ui.tableWidget_2.item(row,2).text()
            if(ac_type == '支票账户'):
                index = db_delete_account(self.db,ac_num,1)
            elif(ac_type == '储蓄账户'):
                index = db_delete_account(self.db,ac_num,0)

            if(index == 0):
                self.ui.tableWidget_2.removeRow(row)
            elif(index == 1):
                QMessageBox.warning(self,"警告","从数据库删除过程发生错误，事务已回滚！", QMessageBox.Yes)

    def Addbtn_account(self):
        ac_num = self.ui.lineEdit_11.text()
        bank_name = self.ui.lineEdit_15.text()
        ac_money = self.ui.lineEdit_16.text()
        
        if(self.ui.radioButton.isChecked()):
            ac_type = 0
            rate = self.ui.lineEdit_17.text()
            money_type = self.ui.lineEdit_18.text()
            credit_line = ''
        else:
            ac_type = 1
            rate = ''
            money_type = ''
            credit_line = self.ui.lineEdit_19.text()

        index = db_add_account(self.db,ac_num,bank_name,ac_money,rate,money_type,credit_line,ac_type)

        if(index == 1):
            QMessageBox.warning(self,"警告","新增/更新的账户号不能为空！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","从数据库添加过程发生错误，事务已回滚！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","该账户已存在！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","开户支行不存在！", QMessageBox.Yes)
        elif(index == 0):
            self.ui.lineEdit_11.clear()
            self.ui.lineEdit_15.clear()
            self.ui.lineEdit_16.clear()
            self.ui.lineEdit_17.clear()
            self.ui.lineEdit_18.clear()
            self.ui.lineEdit_19.clear()
            QMessageBox.information(self,"提示","新账户添加成功！")

    def Updatebtn_account(self):
        ac_num = self.ui.lineEdit_11.text()
        bank_name = self.ui.lineEdit_15.text()
        ac_money = self.ui.lineEdit_16.text()
        if(self.ui.radioButton.isChecked()):
            ac_type = 0
            rate = self.ui.lineEdit_17.text()
            money_type = self.ui.lineEdit_18.text()
            credit_line = ''
        else:
            ac_type = 1
            rate = ''
            money_type = ''
            credit_line = self.ui.lineEdit_19.text()
        
        index = db_update_account(self.db,ac_num,bank_name,ac_money,rate,money_type,credit_line,ac_type)

        if(index == 1):
            QMessageBox.warning(self,"警告","新增/更新的账户号不能为空！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","在数据库更新过程发生错误，事务已回滚！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","该账户不存在！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","开户支行不存在！", QMessageBox.Yes)
        elif(index == 0):
            self.ui.lineEdit_11.clear()
            self.ui.lineEdit_15.clear()
            self.ui.lineEdit_16.clear()
            self.ui.lineEdit_17.clear()
            self.ui.lineEdit_18.clear()
            self.ui.lineEdit_19.clear()
            QMessageBox.information(self,"提示","账户信息更新成功！")


    def Addbtn_account_client(self):
        ac_num = self.ui.lineEdit_23.text()
        ID_num = self.ui.lineEdit_24.text()

        index = db_add_clienttoaccount(self.db,ac_num,ID_num)
    
        if(index == 1):
            QMessageBox.warning(self,"警告","账户号和客户身份账号不能为空！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","账户号错误，账户不存在！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","客户身份证号错误，客户不存在！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","客户已在该分行关联储蓄账户！", QMessageBox.Yes)
        elif(index == 5):
            QMessageBox.warning(self,"警告","客户已在该分行关联支票账户！", QMessageBox.Yes)
        elif(index == 6):
            QMessageBox.warning(self,"警告","在数据库插入过程中出现错误，数据库已回滚！", QMessageBox.Yes)
        elif(index == 0):
            self.ui.lineEdit_23.clear()
            self.ui.lineEdit_24.clear()
            QMessageBox.information(self,"提示","客户已被添加到账户中！", QMessageBox.Yes)

    def Deletebtn_account_client(self):
        ac_num = self.ui.lineEdit_23.text()
        ID_num = self.ui.lineEdit_24.text()

        index = db_delete_clienttoaccount(self.db,ac_num,ID_num)

        if(index == 1):
            QMessageBox.warning(self,"警告","账户号和客户身份账号不能为空！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","账户号错误，账户不存在！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","客户身份证号错误，客户不存在！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","客户与该储蓄账户不存在关联关系！", QMessageBox.Yes)
        elif(index == 5):
            QMessageBox.warning(self,"警告","客户与该支票账户不存在关联关系！", QMessageBox.Yes)
        elif(index == 6):
            QMessageBox.warning(self,"警告","在数据库删除过程中出现错误，数据库已回滚！", QMessageBox.Yes)
        elif(index == 0):
            self.ui.lineEdit_23.clear()
            self.ui.lineEdit_24.clear()
            QMessageBox.information(self,"提示","客户已从关联账户中删除！", QMessageBox.Yes)
    

    def Searchbtn_loan(self):
        self.ui.tableWidget_3.setRowCount(0)

        loan_num = self.ui.lineEdit_25.text()
        loan_bank = self.ui.lineEdit_26.text()
        ID_num = self.ui.lineEdit_27.text()
        loan_state = self.ui.comboBox.currentText()
        
        tabs = db_search_loan(self.db,loan_num,loan_bank,ID_num,loan_state)
        
        currentRowCount = self.ui.tableWidget_3.rowCount()
        for tab in tabs:
            owner = db_search_loan_client(self.db,tab[0])
            self.ui.tableWidget_3.insertRow(currentRowCount)

            item0 = QTableWidgetItem(str(tab[0]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1 = QTableWidgetItem(str(tab[1]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item2 = QTableWidgetItem(str(tab[2]))
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item3 = QTableWidgetItem(str(tab[3]))
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item4 = QTableWidgetItem(str(tab[4]))
            item4.setTextAlignment(QtCore.Qt.AlignCenter)
            item4.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item5 = QTableWidgetItem(' '.join(owner))
            item5.setTextAlignment(QtCore.Qt.AlignCenter)
            item5.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            self.ui.tableWidget_3.setItem(currentRowCount, 0, item0) #列1
            self.ui.tableWidget_3.setItem(currentRowCount, 1, item1) #列2
            self.ui.tableWidget_3.setItem(currentRowCount, 2, item2)
            self.ui.tableWidget_3.setItem(currentRowCount, 3, item3)
            self.ui.tableWidget_3.setItem(currentRowCount, 4, item4)
            self.ui.tableWidget_3.setItem(currentRowCount, 5, item5)

            currentRowCount += 1
            self.ui.tableWidget_3.setRowCount(currentRowCount)

    def Deletebtn_loan(self):
        row = self.ui.tableWidget_3.currentRow()
        if(row > -1):
            loan_num = self.ui.tableWidget_3.item(row,0).text()

        index = db_delete_loan(self.db,loan_num)

        if(index == 1):
            QMessageBox.warning(self,"警告","在数据库删除过程中出现错误，数据库已回滚！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","贷款正在发放中，无法删除！", QMessageBox.Yes)
        elif(index == 0):
            self.ui.tableWidget_3.removeRow(row)
            
    def Providebtn_loan(self):
        row = self.ui.tableWidget_3.currentRow()
        if(row > -1):
            loan_num = self.ui.tableWidget_3.item(row,0).text()
        else:
            return
        
        self.ui.label_42.setText(loan_num)
        loan_case = db_search_loan_condition(self.db,loan_num)
        
        self.ui.tableWidget_6.setRowCount(0)
        currentRowCount = self.ui.tableWidget_6.rowCount()
        for tab in loan_case:
            self.ui.tableWidget_6.insertRow(currentRowCount)
            
            item0 = QTableWidgetItem(str(tab[1]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1 = QTableWidgetItem(str(tab[2]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            self.ui.tableWidget_6.setItem(currentRowCount, 0, item0) #列1
            self.ui.tableWidget_6.setItem(currentRowCount, 1, item1) #列2

            currentRowCount += 1
            self.ui.tableWidget_6.setRowCount(currentRowCount)

        self.ui.stackedWidget.setCurrentIndex(8)

    def Providebtn_loan_2(self):
        row = self.ui.tableWidget_3.currentRow()
        if(row > -1):
            loan_num = self.ui.tableWidget_3.item(row,0).text()
            loan_times = int(self.ui.tableWidget_3.item(row,3).text())
            loan_sum = float(self.ui.tableWidget_3.item(row,2).text())
        else:
            return
        
        loan_money = self.ui.lineEdit_33.text()

        index = db_provide_loan(self.db,loan_num,loan_money,loan_sum,loan_times)

        if(index == 0):
            loan_case = db_search_loan_condition(self.db,loan_num)
            self.ui.tableWidget_6.setRowCount(0)
            currentRowCount = self.ui.tableWidget_6.rowCount()
            for tab in loan_case:
                self.ui.tableWidget_6.insertRow(currentRowCount)
                
                item0 = QTableWidgetItem(str(tab[1]))
                item0.setTextAlignment(QtCore.Qt.AlignCenter)
                item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                item1 = QTableWidgetItem(str(tab[2]))
                item1.setTextAlignment(QtCore.Qt.AlignCenter)
                item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                self.ui.tableWidget_6.setItem(currentRowCount, 0, item0) #列1
                self.ui.tableWidget_6.setItem(currentRowCount, 1, item1) #列2

                currentRowCount += 1
                self.ui.tableWidget_6.setRowCount(currentRowCount)
            QMessageBox.information(self,"提示","贷款发放成功！", QMessageBox.Yes)
        elif(index == 2):
            QMessageBox.warning(self,"警告","贷款已全部发放！", QMessageBox.Yes)
        elif(index == 3):
            QMessageBox.warning(self,"警告","此次放款超过允许最大金额！", QMessageBox.Yes)
        elif(index == 4):
            QMessageBox.warning(self,"警告","在数据库添加过程中出现错误，数据库已回滚！", QMessageBox.Yes)
        elif(index == 5):
            r = QMessageBox.warning(self,"警告","现在为最后一次放款，是否将剩余款额全部发放", QMessageBox.Yes|QMessageBox.No)
            if(r == QMessageBox.Yes):
                index_2 = db_provide_loan_2(self.db,loan_num,loan_sum)
                if(index_2 == 0):
                    loan_case = db_search_loan_condition(self.db,loan_num)
                    self.ui.tableWidget_6.setRowCount(0)
                    currentRowCount = self.ui.tableWidget_6.rowCount()
                    for tab in loan_case:
                        self.ui.tableWidget_6.insertRow(currentRowCount)
                        
                        item0 = QTableWidgetItem(str(tab[1]))
                        item0.setTextAlignment(QtCore.Qt.AlignCenter)
                        item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                        item1 = QTableWidgetItem(str(tab[2]))
                        item1.setTextAlignment(QtCore.Qt.AlignCenter)
                        item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

                        self.ui.tableWidget_6.setItem(currentRowCount, 0, item0) #列1
                        self.ui.tableWidget_6.setItem(currentRowCount, 1, item1) #列2

                        currentRowCount += 1
                        self.ui.tableWidget_6.setRowCount(currentRowCount)
                    QMessageBox.information(self,"提示","贷款发放成功！", QMessageBox.Yes)
                else:
                    QMessageBox.warning(self,"警告","在数据库添加过程中出现错误，数据库已回滚！", QMessageBox.Yes)

    def Addbtn_loan(self):
        loan_num = self.ui.lineEdit_28.text()
        loan_bank = self.ui.lineEdit_29.text()
        loan_amount = self.ui.lineEdit_30.text()
        loan_times = self.ui.lineEdit_31.text()

        ID_list = list()

        for i in range(self.ui.tableWidget_4.rowCount()):
            ID_list.append(self.ui.tableWidget_4.item(i,0).text())
        
        index = db_add_loan(self.db,loan_num,loan_bank,loan_amount,loan_times,ID_list)

        if(index[0] == 1):
            QMessageBox.warning(self,"警告","新增贷款号不能为空！", QMessageBox.Yes)
        elif(index[0] == 2):
            QMessageBox.warning(self,"警告","新增贷款的发放支行不能为空！", QMessageBox.Yes)
        elif(index[0] == 3):
            QMessageBox.warning(self,"警告","新增贷款的款额不能为空！", QMessageBox.Yes)
        elif(index[0] == 4):
            QMessageBox.warning(self,"警告","新增贷款的放款次数不能为空！", QMessageBox.Yes)
        elif(index[0] == 5):
            QMessageBox.warning(self,"警告","新增贷款的放款次数只能为正整数！", QMessageBox.Yes)
        elif(index[0] == 6):
            QMessageBox.warning(self,"警告","贷款号已存在！", QMessageBox.Yes)
        elif(index[0] == 7):
            QMessageBox.warning(self,"警告","放款支行不存在！", QMessageBox.Yes)
        elif(index[0] == 8):
            QMessageBox.warning(self,"警告","贷款客户身份证号错误，客户不存在！", QMessageBox.Yes)
            print(index[1])
            self.ui.tableWidget_4.selectRow(index[1])
        elif(index[0] == 9):
            QMessageBox.warning(self,"警告","在数据库添加过程中出现错误，数据库已回滚！", QMessageBox.Yes)
        elif(index[0] == 0):
            self.ui.lineEdit_28.clear()
            self.ui.lineEdit_29.clear()
            self.ui.lineEdit_30.clear()
            self.ui.lineEdit_31.clear()
            self.ui.tableWidget_4.setRowCount(0)
            QMessageBox.information(self,"提示","贷款添加成功！", QMessageBox.Yes)
    

    def Addbtn_owner_loan(self):
        ID_num = self.ui.lineEdit_32.text()
        currentRowCount = self.ui.tableWidget_4.rowCount()

        if(not ID_num.isspace() and len(ID_num) != 0):
            self.ui.tableWidget_4.insertRow(currentRowCount)
            
            item0 = QTableWidgetItem(ID_num)
            item0.setTextAlignment(QtCore.Qt.AlignCenter)

            self.ui.tableWidget_4.setItem(currentRowCount, 0, item0)

            currentRowCount += 1
            self.ui.tableWidget_4.setRowCount(currentRowCount)
        
        self.ui.lineEdit_32.clear()

    def Cell_Changed(self):
        row = self.ui.tableWidget_4.currentRow()
        if(row > -1):
            line = self.ui.tableWidget_4.item(row,0).text()
            if(line.isspace() or len(line) == 0):
                self.ui.tableWidget_4.removeRow(row)
    
    def Business_statistics(self):
        self.ui.tableWidget_5.setRowCount(0)

        year = self.ui.comboBox_2.currentText()
        season = self.ui.comboBox_3.currentText()
        
        if(year == '——请选择'):
            QMessageBox.warning(self,"警告","请选择年份！", QMessageBox.Yes)
            return

        if(season == '一'):
            month = self.ui.comboBox_4.currentText()
        elif(season == '二'):
            month = self.ui.comboBox_7.currentText()
        elif(season == '三'):
            month = self.ui.comboBox_5.currentText()
        elif(season == '四'):
            month = self.ui.comboBox_6.currentText()
        elif(season == '——请选择'):
            month = '——请选择'
        
        tabs = db_business_search(self.db,year,season,month)
        
        currentRowCount = self.ui.tableWidget_5.rowCount()
        
        for tab in tabs:
            self.ui.tableWidget_5.insertRow(currentRowCount)

            item0 = QTableWidgetItem(str(tab[0]))
            item0.setTextAlignment(QtCore.Qt.AlignCenter)
            item0.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item1 = QTableWidgetItem(str(tab[1]))
            item1.setTextAlignment(QtCore.Qt.AlignCenter)
            item1.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item2 = QTableWidgetItem(str(tab[2]))
            item2.setTextAlignment(QtCore.Qt.AlignCenter)
            item2.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            item3 = QTableWidgetItem(str(tab[3]))
            item3.setTextAlignment(QtCore.Qt.AlignCenter)
            item3.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            
            self.ui.tableWidget_5.setItem(currentRowCount, 0, item0) #列1
            self.ui.tableWidget_5.setItem(currentRowCount, 1, item1) #列2
            self.ui.tableWidget_5.setItem(currentRowCount, 2, item2)
            self.ui.tableWidget_5.setItem(currentRowCount, 3, item3)

            currentRowCount += 1
            self.ui.tableWidget_5.setRowCount(currentRowCount)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    
    w = MainWindow()

    sys.exit(app.exec_())