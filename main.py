def main():
    with open('C:\\Users\\nickd\\Downloads\\decode.hex', 'r') as file:
        data = file.read()

        i = 0
        while i < len(data):

            # add first instruction
            val = y86Inst[data[i] + data[i + 1]]

            #Returns string value of specified length
            values = (readInVal(data,val,i,val[-1]*2))

            #Checks type and converts to instructions
            check(val, val[0], values)

            i = i + val[-1] * 2
            #print(i)

#*args takes the values of the inst,registers, and
def check(val, inst, args):
    pos1 = val[1]
    pos2 = val[2] if len(args) > 2 else None
    arg1 = inst
    arg2 = args[1] if len(args) > 1 else None
    arg3 = args[2] if len(args) > 2 else None
    arg4 = args[3] if len(args) > 3 else None

    #check conditions
    if pos1 == 'F' and pos2 == 'rB':
        # Convert the string to bytes
        toByte = bytes.fromhex(arg4)
        integer = int.from_bytes(toByte, 'little')

        if arg1 == 'mrmovq':
            print(arg1 + " " + " $" + str(integer) + ", " + str(y86_reg[arg3]))
        if arg1 == "iaddq" and arg2 == 'f':
            integer = twos_complement(arg4)
            print(arg1 + " $" + str(integer) + ", " + str(y86_reg[arg3]))
        else:
            print(arg1 + " " + " $" + str(integer) + ", " + str(y86_reg[arg3]))



    if pos1 == 'rA' and pos2 == 'rB':
        print(arg1 + " " + " (" + str(y86_reg[arg2]) + "), " + str(y86_reg[arg3]))

    if pos1 == 'rA' and pos2 == 'F':
        print(arg1 + " " + " (" + str(y86_reg[arg2]) + "), " + str(y86_reg[arg3]))

    if pos1 == 'rA' and pos2 not in ['F','rB']:
        print(arg1 + " " + str(y86_reg[arg2]))
    if pos1 not in ['rA','F'] and pos2 not in ['F','rB']:


        firstLetter = arg1[0]
        if firstLetter[0] == "j":
            toByte = bytes.fromhex(arg2)
            integer = int.from_bytes(toByte, 'little')
            print(arg1 +" $"+ str(integer))
        else:
            print(arg1)


def twos_complement(hex):
    num = int(hex, 16)

    if num >= 2**63:
        num -= 2**64

    return num



def readInVal(data, val, id, bytes):
    length = len(val)
    subsData = data[id:id+bytes]
    val = y86Inst[data[id] + data[id + 1]]

    if (length == 1):
        firstLetter = val[0]

        if firstLetter[0] == "j":
            values = [subsData[:2],subsData[2:]]
        else:

            values = [subsData[:2]]
    if(length == 2):
        firstLetter = val[0]

        if firstLetter[0] == "j":
            values = [subsData[:2], subsData[2:]]
        else:
            values = [subsData[:2]]
    if(length == 3):
        values = [subsData[:2],subsData[2], subsData[3:bytes]]
    if(length ==4):
        values = [subsData[:2], subsData[2], subsData[3], subsData[4:bytes]]

    return values






y86Inst = {
    '00': ('nop', 2),
    '10': ('halt', 1),
    '20': ('rrmovq','rA','rB', 2 + 1 + 1),
    '30': ('irmovq','F','rB', 10),
    '40': ('rmmovq','rA','rB', 10),
    '50': ('mrmovq','rA','rB',10),
    'c0': ('iaddq', 'F', 'rB', 10),
    'c1': ('subl', 'rA', 'rB', 2 + 1 + 1),
    'c2': ('andl', 'rA', 'rB', 2 + 1 + 1),
    'c3': ('ixorq', 'F', 'rB', 10),
    '70': ('jmp', 5 + 4),
    '71': ('jle', 5 + 4),
    '72': ('jl', 5 + 4),
    '73': ('je', 9),
    '74': ('jne', 'F', 5 + 4),
    '75': ('jge', 'F', 5 + 4),
    '76': ('jg', 'F', 5 + 4),
    '80': ('call', 'F', 5 + 4),
    '90': ('ret', 1),
    'a0': ('pushq','rA' ,2 ),
    'b0': ('popq','rA' ,2 )
}

y86_reg = {
    '0': '%rax',
    '1': '%rcx',
    '2': '%rdx',
    '3': '%rbx',
    '4': '%rsp',
    '5': '%rbp',
    '6': '%rsi',
    '7': '%rdi',
    '8': '%r8',
    '9': '%r9',
    'A': '%r10',
    'B': '%r11',
    'C': '%r12',
    'D': '%r13',
    'E': '%r14'
}




# def convAss():
#     with open('C:\\Users\\nickd\\Downloads\\decode.hex', 'r') as file:
#         data = file.read()
#         #print(len(data)/2)
#         for i in range(0,int(len(data)/2),2):
#             #add first instruction
#             val = y86Inst[data[i] + data[i + 1]].key
#             print(val + " " + data )



if __name__ == "__main__":
    main()



