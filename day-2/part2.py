from sys import argv

aim = 0
x, y = 0, 0

def forward(n):
    global aim, x, y
    x += n
    y += (n*aim)

def up(n):
    global aim
    aim-=n

def down(n):
    global aim
    aim+=n

    
# Yay jump tables!
funcs = {
    "forward": forward,
    "up": up,
    "down": down,
}


with open(argv[1], 'r') as infile:
    for line in infile.readlines():
        command = line.split(" ")
        funcs[command[0]](int(command[1]))
    print(f"Final horizontal pos: {x}\n")
    print(f"Final vertical position: {y}\n")
    print(f"Product: {x * y}\n")
        
