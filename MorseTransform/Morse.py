d={"a": ".-", "b": "-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", \
"i":"..", "j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", \
"r":".-.", "s":"...", "t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--..", \
"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....",\
"6":"-....", "7":"--...", "8":"---..", "9":"----."}

dv=dict(zip(d.values(), d.keys()))

def replace_Morse(str_in):
    s=str_in[:]
    # print(s)
    for i in range(len(str_in)):
        for j in d.items():
            s=s.replace(j[0], j[1])
            s=s.replace(j[0].upper(), j[1])
    # print(s)
    return s

def replace_res(str_in):
    s=str_in[:]
    for i in dv.items():
        if s==i[0]:
            # print(i[1])
            return i[1]

s=input(": ")
u=s.encode("utf-8")
# print(u)
l=str(u)[2:-1]
if "\\" in str(u):
    l=l.split("\\")

# print(l)

ll=list("".join(l))
# print(ll)
out=map(replace_Morse, ll)
output="/".join(list(out))
print(output)

l=output.split("/")
# print(l)
out2=list(map(replace_res, l))
# print(out2)
l2=[]
index=0
while index<len(out2):
    if out2[index]=='x' and index<=len(out2)-2:
        ss="\\"+out2[index]+out2[index+1]+out2[index+2]
        l2.append(ss)
        # print(ss)
        index+=3
        # print(index)
    elif out2[index]!='x' and index<len(out2):
        l2.append(out2[index])
        # print(out2[index])
        index+=1
    # elif out2[index]!='x' and index==len(out2)-1:
        # l2.append(out2[index])
        # print(out2[index])
# print(l2)
output2="".join(l2)
output2="b'"+output2+"'"
# print(output2)
print(eval(output2).decode("utf-8"))
