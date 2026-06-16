def split_and_join(line):
    # Split the string by space delimiter
    words = line.split(" ")
    
    # Join the resulting list using a hyphen
    result = "-".join(words)
    
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
