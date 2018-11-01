from datetime import datetime

start = None
end = None

while True:
    print('Insert "Start" to start the Stopwatch.')
    userInput = input()

    if userInput.lower() == 'start':
        start = datetime.now()
        print(start)
        break
    else:
        print('Wrong entry, please retry.')

while True:
    print('Insert Stop to stop the Stopwatch')
    userInput = input()

    if userInput.lower() == 'stop':
        end = datetime.now()
        print(end - start)
        break
    else:
        print('Wrong entry, please retry.')
