# collatzSequence.py

def collatz(number):
  while number != 1:
    if number % 2 == 0:
      number = number / 2
      print(int(number))
    else:
      number = 3 * number + 1
      print(int(number))

while True:
  try:
    print('Enter a number')
    I = int(input())
    answer = collatz(I)
  
  except ValueError:
    print('Error: Invalid argument.', 'Enter a number.')