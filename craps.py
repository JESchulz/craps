
from random import randint

print('come-out')
dieRoll1 = randint(1, 6)
dieRoll2 = randint(1, 6)
comeOutRoll = dieRoll1 + dieRoll2
print(comeOutRoll)


if comeOutRoll == 7 or comeOutRoll == 11:
    print('You win!')

elif comeOutRoll == 2 or comeOutRoll == 3 or comeOutRoll == 12:
    print('Craps, you lose.')

else:
    print('The point is', comeOutRoll)
    dieRoll1 = randint(1, 6)
    dieRoll2 = randint(1, 6)
    pointRoll = dieRoll1 + dieRoll2
    print(pointRoll)

    while pointRoll != comeOutRoll and pointRoll != 7:
        dieRoll1 = randint(1, 6)
        dieRoll2 = randint(1, 6)
        pointRoll = dieRoll1 + dieRoll2
        print(pointRoll)

    if pointRoll == 7:
        print('Seven out, you lose.')

    else:
        print('Pass, you win!')
