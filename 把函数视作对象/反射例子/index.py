# import 把函数视作对象.反射例子.routes as routes
def run():
    inp = input("请输入要访问的页面url：").strip()
    modules,page = inp.split("/")
    obj = __import__("把函数视作对象.反射例子.{}".format(modules),fromlist=[page])
    if hasattr(obj,page):
        func = getattr(obj, page)
        func()
    else:
        print("404")

if __name__ == '__main__':
    run()
