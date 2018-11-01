import Stopwatch

print('Insert "Start" to start the Stopwatch and "Stop" to stop it.')
userInput = input()

if userInput == '':
    Stopwatch.start_counter()

while userInput == '':
    Stopwatch.count_time()
