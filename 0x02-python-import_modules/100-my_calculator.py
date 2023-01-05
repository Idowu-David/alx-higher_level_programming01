#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul
    import sys
    argv = sys.argv[1:]
    _len = len(argv)
    if l != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = ["+", "-", "*", "/"]
    func = [add, sub, mul, div]
    if argv[1] not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(argv[0])
    b = int(argv[2])
    for i in range(len(operator)):
        if operator[i] == argv[1]:
            print("{:d} {} {:d} = {:d}".format(a,
                                               operator[i], b, func[i](a, b)))
