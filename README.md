# Topology analysis of computational notebooks: test task

Solution is located in `Code as graph.ipynb`. 

Used code snippet:
```
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
```
The library **python_graphs** was chosen to build the graph, because:
- it is very easy to use
- it produces nice and clear results