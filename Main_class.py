import sys
sys.path.append(r"D:\3-2 Term\Digital image processing\Lab\package")
import bresenhams_line as bl 
import DDA_line as dda

def main():
    draw = int(input('if you want to draw bresenham press 1 or dda press 2:'))
    if draw == 1:
        lines = int(input('how many line you want to draw:'))
        isinstance = bl.Bresenhams(lines) 
    elif draw == 2:
        lines = int(input('how many line you want to draw:'))
        isinstance = dda.Dda_line(50)

if __name__ == "__main__":
    main()
