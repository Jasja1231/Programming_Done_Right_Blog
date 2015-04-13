__author__ = 'mikaeilorfanian'

# Exercise 1
print 'Exercise # 1'
a = int(raw_input('Enter a number: '))

if a % 2 == 0 and a % 3 == 0:
    print(a, 'is divisible by 6.')


# Exercise 2
print 'Exercise # 2'
a = int(raw_input('Enter a number: '))
b = int(raw_input('Enter a number: '))
c = int(raw_input('Enter a number: '))

if a > b and a > c:
    print(a, 'is the biggest number.')
elif b > a and b > c:
    print(b, 'is the biggest number.')
elif c > a and c > b:
    print(c, 'is the biggest number.')



# Exercise 3
print 'Exercise # 3'
a = int(raw_input('Enter a number: '))
b = int(raw_input('Enter a number: '))

print('The quotient of', a, '/', b, 'is', a / b)
print('The remainder of', a, '/', b, 'is', a % b)



# Exercise 4
print 'Exercise # 4'
x = int(raw_input('Enter some number: '))
ans = 0
while ans ** 3 < abs(x):
    ans += 1
if ans ** 3 != x:
    print(str(x) + ' is not a perfect cube!')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))


# Exercise 4 using a for loop
print 'Exercise # 4 using a for loop'
x = int(raw_input('Enter some number: '))
for ans in range(0, abs(x) + 1):
    if ans ** 3 == abs(x):
        break
if ans ** 3 != abs(x):
    print(str(x) + ' is not a perfect cube!')
else:
    if x < 0:
        ans = -ans
    print('Cube root of ' + str(x) + ' is ' + str(ans))



# Exercise 6
print 'Exercise # 6: Bisection Method for finding square roots'
number = float(raw_input('Enter a number: '))
epsilon = .01
step = epsilon ** 2
low = .0
high = number
ans = (high - low) / 2
num_guesses = 0

while abs(ans ** 2 - number) >= epsilon:
    print('low = ', low, ' high =', high, 'answer =', ans)
    num_guesses += 1
    if ans ** 2 < number:
        low = ans
    else:
        high = ans

    ans = (high + low) / 2.0

print('Number of guesses:', num_guesses)
print(ans, 'is close to the square root of', number)


# Newton-Raphson Method: more efficient way of finding square roots
epsilon = .01
number = 24.0
guess = number / 2.0
num_guesses = 0

while abs(guess * guess - number) >= epsilon:
    guess = guess - (((guess ** 2) - number) / (2 * guess))
    num_guesses += 1
print(guess, 'is very close to the square root of', number)
print('Number of guesses =', num_guesses)

