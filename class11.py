def calculator(a: int, b: int, *args, **kwargs) -> tuple:
    print(args)
    r1 = sum(args)
    r2 = kwargs["my_value"]
    print(a + b)
    return r1, r2

result = calculator(2, 5, 1, 2, my_value="test")

print(result)