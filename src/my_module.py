class MyModule:
    def __init__(self, AnotherModule):
        self.another_module = AnotherModule()

    def do_something(self, value):
        result = ""
        print("before do_something_else - result: " + result)
        result = self.another_module.do_something_else(value)
        print("after do_something_else - result: " + result)
        return result
