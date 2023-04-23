def greet(fx):
    def mdfx(*args,**kwargs):
        print('gm')
        fx(*args,**kwargs)         # *args for tuple ** kwargs for dic
        print('thanks')
    return mdfx

@greet
def hello():
    print("hello")

@greet
def add(a,b):
    print(a+b)
hello()
# greet(add)(1,2)
add(1,2)


