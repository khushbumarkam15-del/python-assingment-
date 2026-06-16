def swap_case(s):
    # Use the built-in string method to swap cases instantly
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
