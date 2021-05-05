from tkinter import *
import math
import math,random,os
from tkinter import messagebox

class ElectracityBill():

    def __init__(self,root):
        def detailes_enter():
            def welcome_bill():
                self.txtarea.delete('1.0',END)
                self.txtarea.insert(END,'\t\tHOMO ELECTRACITY BILL GENERETER\n')
                self.txtarea.insert(END,f'Name of the consumer:------>{self.name_variable.get()}\n')
                self.txtarea.insert(END,f'Consumer ID:------>{self.consumer_id_variable.get()}\n')
                self.txtarea.insert(END,f'Consumer Name and Address:---->{self.name_variable.get()}  Angaragatti\n')
                self.txtarea.insert(END,f'RR number of the consumer:------>{self.rr_no_variable.get()}\n')
                self.txtarea.insert(END,f'Present reading  of the meter:------>{self.present_reading_variable.get()}\n')
                self.txtarea.insert(END,f'previos reading  of the meter:------>{self.previos_reading_variable.get()}\n')
                self.txtarea.insert(END,f'minimum charge  of the current bill:------>{self.minimum_charge_variable.get()}\n')
                self.txtarea.insert(END,f'tax of the current bill:------>{self.tax_variable.get()}\n')
                self.txtarea.insert(END,f'interest of the current bill:------>{self.insert_variable.get()}\n')
                total_number_of_unit_used=(float(self.present_reading_variable.get())-float(self.previos_reading_variable.get()))
                self.txtarea.insert(END,f'The total number of unit used:------>{total_number_of_unit_used}\n')
                amount_per_unit=(3.85)
                self.txtarea.insert(END,f'The amount per unit is:------------>{amount_per_unit}\n')
                previos_reading_variable=self.previos_reading_variable.get()
                minimum_charge=self.minimum_charge_variable.get()
                total_amount_pay=((float(total_number_of_unit_used)*float(amount_per_unit)+float(minimum_charge)))
                tax_variable=self.tax_variable.get()
                total_amount_pay_with_tax=float(total_amount_pay)+float(total_amount_pay*float(tax_variable))/100
                insert_variable=self.insert_variable.get()
                total_amount_pay_with_tax_with_interest=(float(total_amount_pay_with_tax)+float(insert_variable))
                self.txtarea.insert(END,f'The total amount to pay is:--------->{total_amount_pay_with_tax_with_interest}\n')
                


            self.name_variable=StringVar()
            self.consumer_id_variable=StringVar()
            self.rr_no_variable=StringVar()
            self.present_reading_variable=StringVar()
            self.previos_reading_variable=StringVar()
            self.minimum_charge_variable=StringVar()
            self.tax_variable=StringVar()
            self.insert_variable=StringVar()


            enter_detailes=Toplevel()
            enter_detailes.geometry('500x500')
            name_enter_label=Label(enter_detailes,text='Enter the name:')
            name_enter_label.grid(row=0,column=0)
            name_enter_box=Entry(enter_detailes,width=20,textvariable=self.name_variable)
            name_enter_box.grid(row=0,column=1)
            consummer_label=Label(enter_detailes,text='Enter consuer id:')
            consummer_label.grid(row=1,column=0)
            consummer_enter_box=Entry(enter_detailes,width=20,textvariable=self.consumer_id_variable)
            consummer_enter_box.grid(row=1,column=1)
            rr_label=Label(enter_detailes,text='Enter the RR NO:')
            rr_label.grid(row=2,column=0)
            rr_enter_box=Entry(enter_detailes,width=20,textvariable=self.rr_no_variable)
            rr_enter_box.grid(row=2,column=1)
            present_reading_label=Label(enter_detailes,text='Enter preset reading:')
            present_reading_label.grid(row=3,column=0)
            present_reading_enter_box=Entry(enter_detailes,width=20,textvariable=self.present_reading_variable)
            present_reading_enter_box.grid(row=3,column=1)
            
            previos_reading_label=Label(enter_detailes,text='Enter previos reading:')
            previos_reading_label.grid(row=4,column=0)
            previos_reading_enter_box=Entry(enter_detailes,width=20,textvariable=self.previos_reading_variable)
            previos_reading_enter_box.grid(row=4,column=1)
            
            minimum_charge_label=Label(enter_detailes,text='Enter minimum charge:')
            minimum_charge_label.grid(row=5,column=0)
            minimum_charge_enter_box=Entry(enter_detailes,width=20,textvariable=self.minimum_charge_variable)
            minimum_charge_enter_box.grid(row=5,column=1)

            tax_label=Label(enter_detailes,text='Enter tax of bill:')
            tax_label.grid(row=6,column=0)
            tax_enter_box=Entry(enter_detailes,width=20,textvariable=self.tax_variable)
            tax_enter_box.grid(row=6,column=1)
            
            interest_label=Label(enter_detailes,text='Enter interest')
            interest_label.grid(row=7,column=0)
            interest_enter_box=Entry(enter_detailes,width=20,textvariable=self.insert_variable)
            interest_enter_box.grid(row=7,column=1)

            button=Button(enter_detailes,text='Enter',width=10,command=welcome_bill)
            button.grid(row=7,column=3,padx=10)
            save_button=Button(enter_detailes,text='Save Bill',command=save_bill)
            save_button.grid(row=7,column=4,padx=10)
            
            frame=Frame(enter_detailes,bd=3,relief=GROOVE)
            frame.place(x=10,y=180,width=475,height=300)
            

            
            current_bill_title=Label(frame,text='HOMO ELECTRACITY BILL GENERETER',font='arial 15 bold',bd=3,relief=GROOVE).pack(fill=X)
           
            scrol_y=Scrollbar(frame,orient=VERTICAL)
            scrol_x=Scrollbar(frame,orient=HORIZONTAL)
            self.txtarea=Text(frame,yscrollcommand=scrol_y.set)
            scrol_y.pack(side=RIGHT,fill=Y)
            scrol_y.config(command=self.txtarea.yview)
            self.txtarea.pack(fill=BOTH,expand=1)

            self.txtarea.insert(END,"\t\tHOME ELECTRACITY BILL GENERETER\n\n\n")
           

           
            


    

        self.root=root
        self.root.geometry('600x600+350+30')
        self.root.title('HOME ELECTRACITY BILL')
        menu=Menu(self.root)
        item1=Menu(menu)
        item1.add_command(label='Enter the detailes',command=detailes_enter)
        menu.add_cascade(label='Detailes',menu=item1)
        self.root.config(menu=menu)
       
        def save_bill():
            for i in range(1):
                number=random.randint(1,6)
            op=messagebox.askyesno("Save the problum","Do you want to save the bill")
            if op>0:
                self.bill_data=self.txtarea.get('1.0',END)
                f1=open('C:\\Users\\acer\Desktop\\python\python\\bills\\'+str(number)+".txt",'w')
                f1.write(self.bill_data)
                f1.close()
                messagebox.showinfo("Saved",f"Problumn number:{number} saved successfully")
            else:
                return
root=Tk()
obj=ElectracityBill(root)
root.mainloop()