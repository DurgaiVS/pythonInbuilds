def out_fn(xx):
    # xx = 'Vaadaa'

    def in_fn():
        print(xx)
    return in_fn


# This is e.g. for closures
# out_fn('ELEEI')()
x = out_fn('Eleei')
x()
x()
x()
x()

# Decorators take a fn as input and return the modified form as a fn
