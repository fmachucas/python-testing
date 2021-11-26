from unittest import TestCase, mock

from src.my_module import MyModule
#from src.another_module import AnotherModule

class MyModuleTestSuite(TestCase):
    
    @mock.patch('src.another_module.AnotherModule')
    def test_do_something_else(self, AnotherModuleMock):
        another_module = AnotherModuleMock.return_value
        another_module.do_something_else.return_value = "Hello"

        my_module = MyModule(AnotherModuleMock)
        #my_module = MyModule(AnotherModule)

        actual = my_module.do_something("Welcome")

        expected = "Hello"
        assert actual == expected