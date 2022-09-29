class Infix:
    def __init__(self, expr):
(*self.expr,) = expr
def translate_postfix(self):
stack = Stack(len(self.expr))
list_ = []
for token in self.expr:
return "".join(list_)
if __name__ == "__main__":
expr = "a*(b+c)*d"
infix = Infix(expr)
postfix = infix.translate_postfix()
print(postfix)