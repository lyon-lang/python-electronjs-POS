
from admin.admin import AdminWindow
from signin.signin import SigninWindow
from operate.operate import OperatorWindow


class PepperShopWindow():
    # admin_widget = AdminWindow()
    signin_widget = SigninWindow()
    # operator_widget = OperatorWindow()
    

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 


if __name__ == "__main__":
    sa = PepperShopWindow()
    sa