
import hashlib
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict
from datetime import datetime
import sqlite3
conn = sqlite3.connect("db/posdb.db")
c = conn.cursor()


        

class AdminWindow():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

       
        product_code = []
        product_name = []
        spinvals = []
        stockq = "SELECT * FROM stocks"
        self.productz = c.execute(stockq)
        for product in self.productz:
            product_code.append(product[1])
            name = product[2]
            if len(name) > 30:
                name = name[:30] + '...'
            product_name.append(name)
         
        for x in range(len(product_code)):
            line = ' | '.join([str(product_code[x]),str(product_name[x])])
            spinvals.append(line)
   

    def add_user(self, first, last, user, pwd, perm):
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        
        query = "SELECT * FROM users WHERE user_name = ?"
        values = [user]
        result = c.execute(query,values)
        user1 = c.fetchone()
        conn.commit()
        

        if first == '' or last == '' or user == '' or pwd == '':
           print('All fields are Required')

        elif user1 == None:
            
            query = "INSERT INTO users('first_name','last_name','user_name','password','permissions','date') VALUES(?,?,?,?,?,?);"
            values = [first, last, user, pwd, perm, datetime.now().date()]
            c.execute(query, values)
            conn.commit()
           
            
        else:

            print('Username exists')
            

    def add_product(self, code, name, weight, stock, sold, cost, sell, purchase):
        query = "SELECT * FROM stocks WHERE product_code = ?"
        values = [code]
        result = c.execute(query,values)
        code1 = c.fetchone()
        conn.commit()

        if code == '' or name == '' or weight == '' or stock == '' or cost == '' or sell == '':
            print('Product Code, Product Name,  Weight, Stocks, Costs Price and Selling Price fields are Required')
            
        
        elif code1 == None:
            tcost = float(stock) * float(cost)
            tsell = float(stock) * float(sell)
            assumed = float(tsell) - float(tcost)

            #self.products.insert_one({'product_code':code,'product_name':name,'product_weight':weight,'in_stock':stock,'sold':sold,'order':order,'last_purchase':purchase})
            query = "INSERT INTO stocks('product_code','product_name','product_weight','in_stock','sold','cost_price','selling_price','assumed_profit','last_purchase') VALUES(?,?,?,?,?,?,?,?,?);"
            values = [code, name, weight, stock, sold, cost, sell, assumed, purchase]
            c.execute(query, values)
            conn.commit()
            

        else:
            print('Product code exists')

    # def update_user_fields(self):
    #     target = self.ids.ops_fields
    #     target.clear_widgets()
    #     crud_first = TextInput(hint_text='First Name',font_name=('0WAG.TTF'),multiline=False)
    #     crud_last = TextInput(hint_text='Last Name',font_name=('0WAG.TTF'),multiline=False)
    #     crud_user = TextInput(hint_text='User Name',font_name=('0WAG.TTF'),multiline=False)
    #     crud_pwd = TextInput(hint_text='Password',font_name=('0WAG.TTF'),multiline=False)
    #     crud_perm = Spinner(text='Operator',font_name=('0WAG.TTF'),values=['Operator','Administrator'])
    #     crud_submit = Button(text='Update',font_name=('0WAG.TTF'),size_hint_x=None,width=100,background_normal='',background_color=get_color_from_hex('#698B22'),on_release=lambda x:  self.update_user(crud_first.text,crud_last.text,crud_user.text,crud_pwd.text,crud_perm.text))

    #     target.add_widget(crud_first)
    #     target.add_widget(crud_last)
    #     target.add_widget(crud_user)
    #     target.add_widget(crud_pwd)
    #     target.add_widget(crud_perm)
    #     target.add_widget(crud_submit)

    # def update_product_fields(self):
    #     target = self.ids.ops_fields_p
    #     target.clear_widgets()
    #     crud_code = TextInput(hint_text='Product Code',multiline=False)
    #     crud_name = TextInput(hint_text='Product Name',multiline=False)
    #     crud_weight = TextInput(hint_text='Product Weight',multiline=False)
    #     crud_stock = TextInput(hint_text='Product In Stock',multiline=False)
    #     crud_sold = TextInput(hint_text='Product Sold',multiline=False)
    #     crud_cost= TextInput(hint_text='Cost Price',multiline=False)
    #     crud_sell= TextInput(hint_text='Selling Price',multiline=False)
    #     crud_purchase= TextInput(hint_text='Product Last Purchase',multiline=False)
    #     crud_submit = Button(text='Update',size_hint_x=None,width=100,background_normal='',background_color=get_color_from_hex('#698B22'),on_release=lambda x:  self.update_product(crud_code.text,crud_name.text,crud_weight.text,crud_stock.text,crud_sold.text,crud_cost.text,crud_sell.text,crud_purchase.text))

    #     target.add_widget(crud_code)
    #     target.add_widget(crud_name)
    #     target.add_widget(crud_weight)
    #     target.add_widget(crud_stock)
    #     target.add_widget(crud_sold)
    #     target.add_widget(crud_cost)
    #     target.add_widget(crud_sell)
    #     target.add_widget(crud_purchase)
    #     target.add_widget(crud_submit)


    def update_user(self, first, last, user, pwd, perm):
       
        pwd = hashlib.sha256(pwd.encode()).hexdigest()
        date = datetime.now().date()
        if user == '':
            print('Username is Required')
           
        else:
            userq = "SELECT * FROM users WHERE user_name = ?"
            values = [user]
            user1 = c.execute(userq,values)
            user1 = c.fetchone()
            print(user)
            if user1 == None:
                print('Invalid Username')
                
            else:
                
                if first == '':
                    first = user1[1]
                if last == '':
                    last = user1[2]
                if pwd == '':
                    pwd = user1[4]
                
                #self.users.update_one({'user_name':user},{'$set':{'first_name':first,'last_name':last,'user_name':user,'password':pwd,'permissions':perm,'date':datetime.now()}})
                
                query1 = "UPDATE users SET 'first_name'=?, 'last_name'=?, 'user_name'=?, 'password'=?, 'permissions'=?, 'date'=? WHERE user_name = ?"
                values = [first, last, user, pwd, perm, date, user]
                c.execute(query1,values)
                conn.commit()
               

    def update_product(self, code, name, weight, stock, sold, cost, sell, purchase):
    
        if code == '':
            print('Code Required')
           
        else:
            
            targetq = "SELECT * FROM stocks WHERE product_code = ?"
            values = [code]
            t_code = c.execute(targetq,values)
            target_code = c.fetchone()
           
    
            if target_code == None:
                print('Invalid Code')
               
            else:
                if name == '':
                    name = target_code[2]
                if weight == '':
                    weight = target_code[3]
                if stock == '':
                    stock = target_code[4]
                if sold == '':
                    sold = target_code[5]
                if cost == '':
                    cost = target_code[6]
                if sell == '':
                    sell = target_code[7]
                if purchase == '':
                    purchase = target_code[9]
                tcost = float(stock)*float(cost)
                tsell = float(stock)*float(sell)
                assumed = float(tsell) - float(tcost)
                
                pupdatesql = "UPDATE stocks SET 'product_code'=?, 'product_name'=?, 'product_weight'=?, 'in_stock'=?, 'sold'=?, 'cost_price'=?, 'selling_price'=?, 'assumed_profit'=?, 'last_purchase'=? WHERE product_code=?"
                values = [code, name, weight, stock, sold, cost, sell, assumed, purchase, code]
                c.execute(pupdatesql,values)
                conn.commit()
        #      

    
    # def remove_user_fields(self):
    #     target = self.ids.ops_fields
    #     target.clear_widgets()
    #     crud_user = TextInput(hint_text='User Name')
    #     crud_submit = Button(text='Remove',size_hint_x=None,width=100,background_normal='',background_color=get_color_from_hex('#CD5B45'),on_release=lambda x:  self.remove_user(crud_user.text))

    #     target.add_widget(crud_user)
    #     target.add_widget(crud_submit)

    # def remove_product_fields(self):
    #     target = self.ids.ops_fields_p
    #     target.clear_widgets()
    #     crud_code = TextInput(hint_text='Product Code')
    #     crud_submit = Button(text='Remove',size_hint_x=None,width=100,background_normal='',font_name=('0WAG.TTF'),background_color=get_color_from_hex('#CD5B45'),on_release=lambda x:  self.remove_product(crud_code.text))

    #     target.add_widget(crud_code)
    #     target.add_widget(crud_submit)

    def remove_user(self,user):
        if user == '':
            print('Username is Required')
            
        else:
            sqldel = "SELECT * FROM users WHERE user_name=?"
            values = [user]
            target = c.execute(sqldel, values)
            target_user = c.fetchone()
            conn.commit()
            if target_user == None:
                print('Invalid Username')
                
            else:
                sqldel = "DELETE FROM users WHERE user_name=?"
                values = [user]
                c.execute(sqldel, values)
                conn.commit()
                print('User has successfully been deleted')
               

    def remove_product(self,code):
       
        if code == '':
            print('Product Code is Required')
            
        else:
            sqldel = "SELECT * FROM stocks WHERE product_code=?"
            values = [code]
            target = c.execute(sqldel, values)
            target_code = c.fetchone()
            conn.commit()
            
            if target_code == None:
                print('Invalid Code')
                
            else:
                sqldel = "DELETE FROM stocks WHERE product_code=?"
                values = [code]
                c.execute(sqldel, values)
                conn.commit()
          

    def get_users(self):       
        # client = MongoClient()
        # db = client.posdb
        # users = db.users
        _users = OrderedDict( 
            first_names = {},
            last_names = {},
            user_names = {},
            passwords = {},
            permissions = {}
            )
        first_names = []
        last_names = []
        user_names = []
        passwords = []
        permissions = []
        usersql = "SELECT * FROM users"
        usersr = c.execute(usersql)

        for user in usersr:
            first_names.append(user[1])
            last_names.append(user[2])
            user_names.append(user[3])
            pwd = user[4]
            if len(pwd) > 10:
                pwd = pwd[:10] + '...'
            passwords.append(pwd)
            permissions.append(user[5])
        #print(permissions)
        users_len = len(first_names)
        idx = 0
        while idx < users_len:
            _users['first_names'][idx] = first_names[idx]
            _users['last_names'][idx] = last_names[idx]   
            _users['user_names'][idx] = user_names[idx] 
            _users['passwords'][idx] = passwords[idx] 
            _users['permissions'][idx] = permissions[idx] 
            idx += 1
        return _users

    def get_products(self):       
        
        _stocks = OrderedDict()
        _stocks['product_code'] = {}
        _stocks['product_name'] = {}
        _stocks['product_weight'] = {}
        _stocks['in_stock'] = {}
        _stocks['sold'] = {}
        _stocks['cost_price'] = {}
        _stocks['selling_price'] = {}
        _stocks['assumed_profit'] = {}
        _stocks['last_purchase'] = {}

        product_code = []
        product_name = []
        product_weight = []
        in_stock = []
        sold = []
        cost_price = []
        selling_price = []
        assumed_profit = []
        last_purchase = []

        productsql = "SELECT * FROM stocks"
        productsr = c.execute(productsql)


        for product in productsr:
            product_code.append(product[1])
            name = product[2]
            if len(name) > 10:
                name = name[:10] + '...'
            product_name.append(name)
            product_weight.append(product[3])
            in_stock.append(product[4])
            try:
                sold.append(product[5])
            except KeyError:
                sold.append('')
            try:
                cost_price.append(product[6])
            except KeyError:
                cost_price.append('')
            try:
                selling_price.append(product[7])
            except KeyError:
                selling_price.append('')
            try:
                assumed_profit.append(product[8])
            except KeyError:
                assumed_profit.append('')
            try:
                last_purchase.append(product[9])
            except KeyError:
                last_purchase.append('')
        #print(permissions)
        products_len = len(product_code)
        idx = 0
        while idx < products_len:
            _stocks['product_code'][idx] = product_code[idx]
            _stocks['product_name'][idx] = product_name[idx]   
            _stocks['product_weight'][idx] = product_weight[idx] 
            _stocks['in_stock'][idx] = in_stock[idx] 
            _stocks['sold'][idx] = sold[idx] 
            _stocks['cost_price'][idx] = cost_price[idx] 
            _stocks['selling_price'][idx] = selling_price[idx]
            _stocks['assumed_profit'][idx] = assumed_profit[idx] 
            _stocks['last_purchase'][idx] = last_purchase[idx] 
            idx += 1
        return _stocks

    def get_transactions(self):       
        
        _trans = OrderedDict()
        _trans['product_code'] = {}
        _trans['product_name'] = {}
        _trans['quantity'] = {}
        _trans['amount'] = {}
        _trans['date'] = {}
        

        product_code = []
        product_name = []
        quantity = []
        amount = []
        date = []
        transql = "SELECT * FROM transactions"
        transr = c.execute(transql)


        for transaction in transr:
            product_code.append(transaction[1])
            product_name.append(transaction[2])
            quantity.append(transaction[3])
            amount.append(transaction[4])
            date.append(transaction[5])
          

            
        #print(permissions)
        products_len = len(product_code)
        idx = 0
        while idx < products_len:
            _trans['product_code'][idx] = product_code[idx]
            _trans['product_name'][idx] = product_name[idx]   
            _trans['quantity'][idx] = quantity[idx] 
            _trans['amount'][idx] = amount[idx] 
            _trans['date'][idx] = date[idx] 
            
            idx += 1
        return _trans
    
    def view_stats(self):
        plt.cla()
        self.ids.analysis_res.clear_widgets()
        target_product = self.ids.target_product.text
        target = target_product[:target_product.find(' | ')]
        name = target_product[target_product.find(' | '):]

        df = pd.read_csv('admin\products_purchase.csv')
        purchases = []
        dates = []
        count = 0
        for x in range(len(df)):
            if str(df.Product_Code[x]) == target:
                purchases.append(df.Purchased[x])
                dates.append(count)
                count += 1
        plt.bar(dates,purchases,color='#CD5B45',label=name)
        plt.ylabel('Total Purchase')
        plt.xlabel('day')
       
         
    def get_profits(self): 
        
        #target = self.ids.profs_fields_t
        
        assumed = []
        stock = []
        cost = []
        Cost = []
        profsql = "SELECT * FROM stocks"
        profits = c.execute(profsql)


        for profit in profits:
            stock.append(profit[4])
            cost.append(profit[6])
            assumed.append(profit[8])
            self.stocks = profit[4]
            self.costs = profit[6]
            self.total_c = float(self.stocks) * float(self.costs)
            
            print(self.total_c)

        #print(stock)
            Cost.append(self.total_c)
        self.total_cc = sum(Cost)
        self.total_p = sum(assumed)
        self.p_percent = (self.total_p/self.total_cc) * 100
       
       

    def daily_transaction(self):
        self.date = self.ids.date_inp.text
        amount = []
        
        profsql = "SELECT * FROM transactions WHERE date = ?"
        values = [self.date]
        all_transactions = c.execute(profsql,values)
        

        for transaction in all_transactions:
            amount.append(transaction[4])

        print(sum(amount))
           

        

    def change_screen(self, instance):
        if instance.text == 'Manage Products':
            self.ids.scrn_mngr.current = 'scrn_product_content'
        elif instance.text == 'Manage Users':
            self.ids.scrn_mngr.current = 'scrn_content'
        elif instance.text == 'Product Analysis':
            self.ids.scrn_mngr.current = 'scrn_analysis'
        elif instance.text == 'Transactions' :
            self.ids.scrn_mngr.current = 'scrn_trans_content'
        else :
            self.ids.scrn_mngr.current = 'scrn_totals_content'

if __name__ == "__main__":
    oa = AdminWindow()
   