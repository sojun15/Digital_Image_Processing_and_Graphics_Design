import random as rand
import matplotlib.pyplot as mp

def line():
    x_values = [] 
    for x in range(5):
        x = rand.randint(1,10)
        x_values.append(x)

    m = rand.randint(1, 10) 
    c = rand.randint(1, 10) 

    y_values = [m * x + c for x in x_values] 

    mp.plot(x_values, y_values, marker='*', linestyle='-')

def main():
    mp.figure(figsize=(10, 8)) 
    for _ in range(50): 
        line()

    mp.legend(loc="upper left", bbox_to_anchor=(1, 1)) 
    mp.show()

if __name__ == "__main__":
    main()
