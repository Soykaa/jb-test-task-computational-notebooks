def hello(counter):
    print(f'hi there! counter = {counter}')
    
counter = 0
while (counter < 100):
    i = 1
    if counter % 2 == 0:
        i*=5
    counter += 7
    hello(counter)
    if i >= 30:
        raise Exception()	
