# -*- coding: UTF-8 -*- 
# 异常本身也是一个类
class TyError(BaseException): # -- 需要继承异常类
    def __init__(self,msg):
        self.msg = msg



print(TyError('自定义异常'))

try:
   raise TyError('自定义异常')  # ---- raise
except TyError as e:   # 定义的异常类 --- TyError
    print(e)



# 断言
# assert 1 == 2     # AssertionError

# try:    捕捉不到异常
#     assert 1 == 2
# except Exception as e:
#     print(e)









