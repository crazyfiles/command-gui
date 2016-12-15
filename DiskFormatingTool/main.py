import commands
from tkinter import *
device=[]
boot=[]
start=[]
end=[]
sectors=[]
size=[]
id=[]
type=[]
op= commands.getoutput('fdisk -l')

tmp_data=op[op.index('Device'):]

data=tmp_data.split('\n')
stri=str(data[0])
for i in range(0,len(data[0])):
    if stri[i]!=' ':
        print stri[i]
    else:
        stri[i].strip(" ")
        print ','
for i in range(1,len(data)-2):
    data_temp=data[i].split(' ')
    print data_temp
    device.append(data_temp[0])
    boot.append(data_temp[1])
    start.append(data_temp[2])
    end.append(data_temp[3])
    sectors.append(data_temp[4])
    size.append(data_temp[5])
    id.append(data_temp[6])
    type.append(data_temp[7])
#print device


root=Tk()
l1=Listbox()
l2=Listbox()
lbl1=Label(text='Partition')
lbl2=Label(text='Boot Device')
for i in device:
    l1.insert(END,i)

for i in boot:
    l2.insert(END,i)

l1.grid(row=1,column=0)
l2.grid(row=1,column=1)

lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=1)
root.mainloop()
