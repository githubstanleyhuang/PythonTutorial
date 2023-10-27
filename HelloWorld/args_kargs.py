"""
    Test Sample for args, kargs
    @author:Stanley 
    @Date: 2023-10-27

"""

def test(**kargs):
    """         test for kargs
    """
    print("start **kargs")
    for k in kargs.items():
        print(kargs[k])


def test_args(*args):
    """         
        test for args
    """
    print("start *args")
    for arg in args:
        print(arg)


def test_mix(*args, **kargs):
    """         
        test for both args and kargs
    """
    test_args(*args)
    test(**kargs)


test(name="James Bond", age=30)
test_args("James Bond", 30)
test_mix(10, "hello", "james bond", age=30)
