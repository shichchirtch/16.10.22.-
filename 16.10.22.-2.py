class Test:
    def __init__(self, descr:str):
        if not isinstance(descr, str) or  len(descr)< 10 or len(descr)>10000:
            raise ValueError('формулировка теста должна быть от 10 до 10 000 символов')
        self.descr = descr

    def run(self):
        raise NotImplementedError

class TestAnsDigit(Test):
    def __init__(self, descr, ans_digit, max_error_digit = 0.01):
        super().__init__(descr)
        if not isinstance(ans_digit, (int, float)) or not isinstance(max_error_digit, (int, float))\
            or max_error_digit<0:
            raise ValueError('недопустимые значения аргументов теста')
        self.ans_digit, self.max_error_digit = ans_digit, max_error_digit

    def run(self):
        ans = input()
        try:
            ans = float(ans)
            return self.ans_digit-self.max_error_digit <= ans <= self.ans_digit+self.max_error_digit
        except  Exception as e:
            print(e)

descr, ans = map(str.strip, input().split('|'))  # например: Какое значение получится при вычислении 2+2? | 4
ans = float(ans)
# print(ans) Сколько будет 2+3 ? | 5
try:
    t = TestAnsDigit(descr, ans)
    print(t.run())
except  Exception as e:
    print(e)
