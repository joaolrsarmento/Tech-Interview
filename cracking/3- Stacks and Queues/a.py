while True:
    try:
        year = int(input())
        print(year // 100 + 1 if  year % 100 != 0 else year // 100)
    except EOFError:
        break