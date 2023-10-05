# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def main():
    with open('C:\\Users\\nickd\\Downloads\\decode.hex', 'r') as file:
        data = file.read()
        # print(len(data)/2)
        i = 0
        while i < len(data):

            # add first instruction
            val = y86Inst[data[i] + data[i + 1]]
            #print("Val: " + str(val))

            #Returns string value of specified length
            values = (readInVal(data,len(val),i,val[-1]*2))
            #print("args: " + str(values))

            #Checks type and converts to instructions
            check(val, val[0], values)

            i = i + val[-1] * 2
            #print(i)




#Takes the instruction
#pos1 and pos2 are check how the instructions should be interpreted
#*args takes the values of the inst,registers, and
def check(val, inst, args):
    pos1 = val[1]
    pos2 = val[2] if len(args) > 2 else None
    arg1 = inst
    arg2 = args[1] if len(args) > 1 else None
    arg3 = args[2] if len(args) > 1 else None
    arg4 = args[3] if len(args) > 3 else None
    #print("Val3: " + str(val3))

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
        print(arg1)





#taken from https://www.delftstack.com/howto/python/python-hex-to-int/
def twos_complement(hex_string):
    # Convert hex to int
    num = int(hex_string, 16)
    # Check if the number is negative
    if num >= 2**63:
        num -= 2**64

    return num



def readInVal(data, length, id, bytes):
    subsData = data[id:id+bytes]
    val = y86Inst[data[id] + data[id + 1]]
    #print(subsData)
    #print(bytes)
    #print(length)
    if (length == 1):
        values = [subsData[:2]]
    if(length == 2):
        values = [subsData[:2]]
    if(length == 3):
        values = [subsData[:2],subsData[2], subsData[3:bytes]]
    if(length ==4):
        values = [subsData[:2], subsData[2], subsData[3], subsData[4:bytes]]

    #intVal = subsData[index + 4:index + bytes * 2]
    #values.append(intVal)
    #print(values)
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
    '70': ('jmp', 'F', 5 + 4),
    '71': ('jle', 'F', 5 + 4),
    '72': ('jl', 'F', 5 + 4),
    '73': ('je', 'F', 5 + 4),
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




def convAss():
    with open('C:\\Users\\nickd\\Downloads\\decode.hex', 'r') as file:
        data = file.read()
        #print(len(data)/2)
        for i in range(0,int(len(data)/2),2):
            #add first instruction
            val = y86Inst[data[i] + data[i + 1]].key
            print(val + " " + data )

            #Check F,rA,rB, return register


            #Convert to hex

            #Increment to next block of data


if __name__ == "__main__":
    main()



