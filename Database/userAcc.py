#userAcc.py

class UserAcc():
    
    ID = 0
    name = ""
    role = 0
    conn = None
    
    def __init__(self, ID = 0, name = "", role = 0, conn = None):
        self.ID = ID
        self.name = name
        self.role = role
        self.conn = conn

    def set_attrs(self, ID, name, role, conn):
        self.ID = ID
        self.name = name
        self.role = role
        self.conn = conn        

#user account object 선언
user_acc = UserAcc()

