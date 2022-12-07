from sys import argv


def forward(n,x,y) -> tuple:
    x += n
    return x,y

def up(n,x,y) -> tuple:
    y-=n
    return x,y

def down(n,x,y) -> tuple:
    y+=n
    return x,y
    
# Yay jump tables!
funcs = {
    "forward": forward,
    "up": up,
    "down": down,
}


with open(argv[1], 'r') as infile:
    x, y = 0, 0
    for line in infile.readlines():
        command = line.split(" ")
        x,y = funcs[command[0]](int(command[1]),x,y)
    print(f"Final horizontal pos: {x}\n")
    print(f"Final vertical position: {y}\n")
    print(f"Product: {x * y}\n")
        
