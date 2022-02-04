import sqlite3
import hashlib
import sys

conn = sqlite3.connect("python/API/db/posdb.db")
c = conn.cursor()


class SigninWindow():
    def __init__(self, **kwargs):
        super().__init__(**kwargs) 

    def validate_user(self):
       

        username = sys.argv[1]
        passw = sys.argv[2]
      
        if username == '' or passw == '':
            print("username and /or password required")
            
        else:
            query = "SELECT * FROM users WHERE user_name = ?"
            values = [username]
            result = c.execute(query,values)
            user = c.fetchone()
                   
            if user == None:
                print("Invalid username") 
            else:
                
                query = "SELECT * FROM users WHERE user_name = ?"
                values = [username]
                result = c.execute(query,values)
                user = c.fetchone()
                passw = hashlib.sha256(passw.encode()).hexdigest()
                if passw == user[4]:
                    perm = user[5]
                    #info.text = "[color=#00ff00]Loged in successfully[/color]"
                  

                    if perm == 'Administrator':
                        print('admin')
                    else:
                        print('operator')
                else:
                   print("Invalid password") 

        sys.stdout.flush()

if __name__ == "__main__":
    sa = SigninWindow()
    sa.validate_user()