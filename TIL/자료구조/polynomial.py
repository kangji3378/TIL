# 다항식에 대해서
#지수: 인덱스 계수: value
#zero() p(x)=0
#iszero() 다 0인지
#co...c 계수
#Expenent Lead 끝에서부터 의미있는 계수를 가지고 있는 지수
#poly attach 지수와 계수를 입력하면 집어넣웆느
#remove 없는 부분 0으로 채우기
# add 두 항간의 덧셈
# mult두 항간의 곱셈
# evaluate 항에 변수 삽입
class Polynomial:
    """Polynomial using array."""
    def __init__(self, degree):
        self.degree = degree
        self.coef = [0] * (self.degree + 1)
    def get_lead_exp(self):
        i = len(self.coef) - 1
        while i > 0 and self.coef[i] == 0:
            i -= 1
        return i
    def evaluate(self, x):
        return sum((coef * (x**exp) for exp, coef in enumerate(self.coef) if coef != 0))
    def get_coef(self, exp):
        return self.coef[exp]
    def is_zero(self):
        return not any(self.coef)
    def zero(self):
        for i in range(len(self.coef)):
            self.coef[i] = 0
    def attach(self, coef, exp):
        self.coef[exp]=coef
        return self
    def remove(self, exp):
        self.coef[exp] = 0
    def __str__(self):
        ret = ""
        for coef, exp in [(self.coef[i], i) for i in range(self.degree + 1) if self.coef[i] != 0
        ][::-1]:ret += f"({coef})x^{exp} + "
        ret=ret[:-2]
        return f"{ret}"
    def __add__(self,other):
        poly = Polynomial(max(self.degree, other.degree))
        while not self.is_zero() or not other.is_zero():
            exp_01 = self.get_lead_exp()
            exp_02 = other.get_lead_exp()
            if exp_01 > exp_02:
                poly.attach(self.get_coef(exp_01), exp_01)
                self.remove(exp_01)
            elif exp_01 < exp_02:
                poly.attach(other.get_coef(exp_02), exp_02)
                other.remove(exp_02)
            else:
                coef = self.get_coef(exp_01) + other.get_coef(exp_02)
                exp = exp_01
                poly.attach(coef, exp)
                self.remove(exp_01)
                other.remove(exp_02)
        return poly
    def __mul__(self, other):
        poly = Polynomial(self.degree+ other.degree)
        an=Polynomial(self.degree+ other.degree)
        for i in range(self.degree+1):
            if self.get_coef(i)!=0:
                for j in range(other.degree+1):
                    if other.get_coef(j)!=0:
                        an.zero()
                        an.attach(self.get_coef(i)*other.get_coef(j),i+j)
                        poly=poly+an
        return poly

if __name__ == "__main__":
    poly1 = Polynomial(2)
    poly1.attach(2, 2).attach(3, 1).attach(1, 0)
    print("poly1 =\n", poly1)
    poly2 = Polynomial(1)
    poly2.attach(3, 1).attach(-2, 0)
    print("poly2 =\n", poly2)
    poly = poly1 * poly2
    print()
    print("poly1 * poly2 =\n", poly)