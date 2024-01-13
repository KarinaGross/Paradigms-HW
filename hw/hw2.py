def table_mult(n):
    for i in range(1, n + 1):
        for j in range(1, 11):
            print(f'{i} * {j} = {i * j}')
        print('\n')

table_mult(6)

# Я выбрала структурную и процедурную парадигмы, т.к. считаю, что декларативный подход здесь не реализуем.  