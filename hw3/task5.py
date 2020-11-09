total_sum = 0.0
working = True
while working:
    answer = input('Enter numbers or "q" to quit: ')
    for sa in answer.split():
        if sa.lower() == 'q':
            working = False
            break
        else:
            total_sum += float(sa)
    print(total_sum)
