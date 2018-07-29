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

print(""" INPUT KEY
w - up
s - down
d - right
a - left
q - exit""")

position = complex(1, 0)

while True:
    value = input()
    if value == 'w':
        position = up(position)
    elif value == 's':
        position = down(position)
    elif value == 'd':
        position = right(position)
    elif value == 'a':
        position = left(position)
    elif value =='q':
        break
    print("Position: %r" %(position))
print("Exiting")
