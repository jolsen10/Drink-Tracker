from tkinter import Tk, Label, Listbox, Radiobutton, IntVar, Frame, Entry, W, SINGLE, END, Button, mainloop
import xlrd

master = Tk(className=' Drinky Drink')
inputgender = IntVar(value=0)
BACIndicator = IntVar()
BAClevels = ('0.00',0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,'0.10 or higher')
loc = r'Files\BAC.xlsx'
wb = xlrd.open_workbook(loc)
targetbac = 10

def weight_error():
    error = Tk(className=' Error')
    w = Label(error, text='Enter a weight you dofus', font = 'helv64')
    w.pack(padx=25, pady=25)
    error.iconbitmap(r'Files\Solo_Cup_Favicon.ico')
    error.focus_force()
    return

def BAC_error():
    error = Tk(className=' Error')
    w = Label(error, text='Enter a BAC you drunk ass', font = 'helv64')
    w.pack(padx=25, pady=25)
    error.iconbitmap(r'Files\Solo_Cup_Favicon.ico')
    error.focus_force()
    return

def operation():
    gender = inputgender.get()

    if gender == 0:
        sheet = wb.sheet_by_index(0)
    elif gender == 1:
        sheet = wb.sheet_by_index(1)
    
    try:
        inputweight = int(weight.get())
    except ValueError:
        weight_error()
        return
        
    if inputweight == "":
        weight_error()
        return

    if gender == 0:
        if inputweight <= 110:
            adjustedweight = 1
        elif inputweight <= 130 and inputweight > 111:
            adjustedweight = 2
        elif inputweight <= 150 and inputweight > 131:
            adjustedweight = 3
        elif inputweight <= 170 and inputweight > 151:
            adjustedweight = 4
        elif inputweight <= 190 and inputweight > 171:
            adjustedweight = 5
        elif inputweight <= 210 and inputweight > 191:
            adjustedweight = 6
        elif inputweight <= 230 and inputweight > 211:
            adjustedweight = 7
        elif inputweight > 231:
            adjustedweight = 8
    elif gender == 1:
        if inputweight <= 95:
            adjustedweight = 1
        if inputweight <= 110 and inputweight > 96:
            adjustedweight = 2
        elif inputweight <= 130 and inputweight > 111:
            adjustedweight = 3
        elif inputweight <= 150 and inputweight > 131:
            adjustedweight = 4
        elif inputweight <= 170 and inputweight > 151:
            adjustedweight = 5
        elif inputweight <= 190 and inputweight > 171:
            adjustedweight = 6
        elif inputweight <= 210 and inputweight > 191:
            adjustedweight = 7
        elif inputweight <= 230 and inputweight > 211:
            adjustedweight = 8
        elif inputweight > 231:
            adjustedweight = 9
    

    if BAC.curselection():
        pass
    else:
        BAC_error()
        return
    
    if BAC.get(BAC.curselection()) == '0.00':
        currentbac = 0
    elif BAC.get(BAC.curselection()) == 0.01:
        currentbac = 1
    elif BAC.get(BAC.curselection()) == 0.02:
        currentbac = 2
    elif BAC.get(BAC.curselection()) == 0.03:
        currentbac = 3
    elif BAC.get(BAC.curselection()) == 0.04:
        currentbac = 4
    elif BAC.get(BAC.curselection()) == 0.05:
        currentbac = 5
    elif BAC.get(BAC.curselection()) == 0.06:
        currentbac = 6
    elif BAC.get(BAC.curselection()) == 0.07:
        currentbac = 7
    elif BAC.get(BAC.curselection()) == 0.08:
        currentbac = 8
    elif BAC.get(BAC.curselection()) == 0.09:
        currentbac = 9
    elif BAC.get(BAC.curselection()) == '0.10 or higher':
        currentbac = 10
    

    bactoachieve = targetbac - currentbac

    if bactoachieve == 0:
        drunkmessage = "Your too drunk for me, go home and have another drink"
        drunk = Tk(className=' Drunk Ass')
        Label(drunk, text=drunkmessage, font = 'helv64').pack(padx=25, pady=25)
        drunk.iconbitmap(r'Files\Solo_Cup_Favicon.ico')
        drunk.focus_force()
        return

    elif bactoachieve == 1:
        scalebac = 10
    elif bactoachieve == 2:
        scalebac = 9
    elif bactoachieve == 3:
        scalebac = 8
    elif bactoachieve == 4:
        scalebac = 7
    elif bactoachieve == 5:
        scalebac = 6
    elif bactoachieve == 6:
        scalebac = 5
    elif bactoachieve == 7:
        scalebac = 4
    elif bactoachieve == 8:
        scalebac = 3
    elif bactoachieve == 9:
        scalebac = 2
    elif bactoachieve == 10:
        scalebac = 1

    finalmessage = "You need {} more drinks!".format(sheet.cell_value(adjustedweight,scalebac))
    congrats = Tk(className=' Shot Time')
    Label(congrats, text=finalmessage, font = 'helv64').pack(padx=25, pady=25)
    congrats.iconbitmap(r'Files\Solo_Cup_Favicon.ico')
    congrats.focus_force()
    

master.iconbitmap(r'Files\Solo_Cup_Favicon.ico')

label1 = Label(master, text='Enter your weight:')
label1.pack(pady = 7)
weight = Entry(master)
weight.pack()
weight.focus_set()

label2 = Label(master, text='Select your Gender:')
label2.pack(pady = 7)

R1 = Radiobutton(master, text="Male", variable=inputgender, value =0)
R1.pack(anchor = W, padx = 95)
R2 = Radiobutton(master, text="Female", variable=inputgender, value =1)
R2.pack(anchor = W, padx = 95)



label3 = Label(master, text='Select your current BAC:')
label3.pack(pady = 7)
BAC = Listbox(master, selectmode = SINGLE, height = 11)
for item in BAClevels:
    BAC.insert(END, item)
BAC.pack()

proceed = Button(master, text="Proceed", width=10, command=operation)
proceed.pack(pady = 10)

close_button = Button(master, text="Close", command=master.quit)
close_button.pack(pady = 10)

mainloop()