def monopolyworp():
    import random
    while True:
        die1 = random.randrange(1, 7)
        die2 = random.randrange(1, 7)
        total = die1 + die2
        counter = 1
        if die1 != die2:
            print('{} + {} = {}'.format(die1, die2, total))
            break
        elif die1 == die2 and counter < 3:
            counter += 1
            print('{} + {} = {} (dubbel)'.format(die1, die2, total))
            continue
        elif die1 == die2 and counter == 3:
            print('{} + {} = {} (direct naar gevangenis)'.format(die1, die2, total))
            break


monopolyworp()
