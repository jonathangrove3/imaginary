def up(p):
    p += complex(0,1)
    return p

def down(p):
    p += complex(0,-1)
    return p

def right(p):
    p += complex(1,0)
    return p

def left(p):
    p += complex(-1,0)
    return p

position = complex(0, 0)

value = int(input())

while value<= 4:
    if value== 1:
        position = up(position)
    elif value== 2:
        position = down(position)
    elif value== 3:
        position = right(position)
    elif value== 4:
        position = left(position)

    print("Position: %r" %(position))
    value= int(input())

print("Exiting.")
