import random as rand
import matplotlib.pyplot as plt

def circle(ax):
    a = rand.randint(1, 10)
    b = rand.randint(1, 10)
    r = rand.randint(1, 5) 

    circle = plt.Circle((a, b), r, fill=False, edgecolor='r', linewidth=2)
    ax.add_patch(circle)

def main():
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 12)
    
    for _ in range(50):
        circle(ax)
    
    ax.set_aspect('equal') 
    plt.show()

if __name__ == "__main__":
    main()
