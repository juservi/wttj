def donuts(count):
    if count <10:
        result = count
    else:
        result='many'
    return f'Number of donuts: {result}'

print(donuts(5))
print(donuts(23))