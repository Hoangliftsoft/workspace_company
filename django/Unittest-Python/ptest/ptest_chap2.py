import unittest


class MyExcept(Exception):
    def __init__(self,msg,error_code):
        super().__init__(msg)
        self.error_code = error_code

class SecondEx(Exception):
    pass

def throw_ex(var):
    if var == 100:
        raise MyExcept("NOT A VALID NUMBER")
    elif var == 200:
        raise SecondEx("NOT A VALID.....")
    else:
        return True

class LearUnitTest(unittest.TestCase):
    
    def test_sample(self):
        # self.assertRaises((MyExcept,SecondEx),throw_ex,100)

        with self.assertRaises(MyExcept,msg="SORRY TRY AGAIn...") as context:
            throw_ex(10)
            
        print(context.exception)
        print(context.exception.error_code)


if __name__ == "__main__":
    unittest.main()
