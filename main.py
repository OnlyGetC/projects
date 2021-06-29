from typing import Generator
def fib1(n: int) -> Generator:
    yield 0 # Специальный случай
    if n > 0: yield 1 # специальный случай
    last: int = 0 # начальное значение  fib(0)
    next: int = 1 # начальное значение  fib(1)
    for _ in range(1,n):
        last, next = next, last + next
        yield next # главныый этап генерации
if __name__ == "__main__":
    for i in fib1(50): # вывод 50 чисел по порядку
        print(i)