import sys
sys.path.append(r"D:\3-2 Term\Digital image processing\Lab\package")
import bresenhams_line as bl 
import DDA_line as dda
import bresenhams_circle as bc
import midpoint_circle as mp

def main():
    print('Which type of diagram you want draw')
    print('Bresenhams line press 1')
    print('DDA line press 2')
    print('Bresenhams circle press 3')
    print('Midpoint circle press 4')
    draw = int(input('Enter your input:'))
    if draw == 1:
        lines = int(input('how many line you want to draw:'))
        isinstance = bl.Bresenhams(lines) 
    elif draw == 2:
        lines = int(input('how many line you want to draw:'))
        isinstance = dda.Dda_line(lines)
    elif draw ==3:
        circle = int(input('how many circle you want to draw:'))
        isinstance = bc.Bresen_circle(circle)
    elif draw ==4:
        circle = int(input('how many circle you want to draw:'))
        isinstance = mp.Mid_point(circle)

if __name__ == "__main__":
    main()
