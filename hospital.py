from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1530x800+0+0")
        self.root.config(bg="lightblue")

        self.NameofTablets = StringVar()
        self.Ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.storageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientID = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateofBirth = StringVar()
        self.PatientAddress = StringVar()

        
        lbltitile = Label(self.root, text="HOSPITAL MANAGEMENT SYSTEM", bg="lightgray",fg="red", font=("times new roman", 30, "bold"), bd=10, relief=RIDGE)
        lbltitile.pack(side=TOP, fill=X)
        
        #===================Dataframe======================================
        DataFrame = Frame(self.root, bd=20, relief=RIDGE)
        DataFrame.place(x=0, y=75, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, text="Patient Information", font=("Arial", 12, "bold"), bd=7, relief=RIDGE,padx=10)
        DataFrameLeft.place(x=0, y=5, width=980, height=350)

        DataFrameright = LabelFrame(DataFrame, text="Prescription", font=("times new roman", 12, "bold"), bd=7, relief=RIDGE,padx=10)
        DataFrameright.place(x=990, y=5, width=460, height=350)
        
        #=================ButtonsFrame=======================================
        ButtonFrame = Frame(self.root, bd=20, relief=RIDGE)
        ButtonFrame.place(x=0, y=470, width=1530, height=70)

        # #=================Details Frame======================================
        DetailsFrame = Frame(self.root, bd=20, relief=RIDGE)
        DetailsFrame.place(x=0, y=540, width=1530, height=250)


        #=================DataFrameleft=========================================
        lblnameTablet = Label(DataFrameLeft, text="Name OF Tablets", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblnameTablet.grid(row=0,column=0)
        comNametablet = ttk.Combobox(DataFrameLeft,textvariable= self.NameofTablets,font=("Arial",12,"bold"),width=33)
        comNametablet["values"] = ("Nice","Corona","Acetaminophen","adderall","amlodipine") 
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataFrameLeft, text="Refence No:", font=("Arial", 12, "bold"),padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.Ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataFrameLeft, text="Dose: ", font=("Arial", 12, "bold"),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNooftablets = Label(DataFrameLeft, text="No Of Tablets: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblNooftablets.grid(row=3,column=0,sticky=W)
        txtNooftablets = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNooftablets.grid(row=3,column=1)

        lblLot = Label(DataFrameLeft, text="Lot: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate = Label(DataFrameLeft, text="Issue Date: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.IssueDate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblexpDate = Label(DataFrameLeft, text="Exp Date: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblexpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataFrameLeft, text="Daily Dose: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblsideEffect = Label(DataFrameLeft, text="Side Effect: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblsideEffect.grid(row=8,column=0,sticky=W)
        txtsideEffect = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.SideEffect,width=35)
        txtsideEffect.grid(row=8,column=1)

        lblFurtherinfo = Label(DataFrameLeft, text="Further Information: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFutherinfo = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFutherinfo.grid(row=0,column=3)

        lblBloodPressure = Label(DataFrameLeft, text="Blod Pressure: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage = Label(DataFrameLeft, text="Storage Advice: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.storageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(DataFrameLeft, text="Medication: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientID = Label(DataFrameLeft, text="Patient ID: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblPatientID.grid(row=4,column=2,sticky=W)
        txtPatientID = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.PatientID,width=35)
        txtPatientID.grid(row=4,column=3)

        lblNhsNumber = Label(DataFrameLeft, text="NHS Number: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName = Label(DataFrameLeft, text="Patient Name: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateOfBirth = Label(DataFrameLeft, text="Date of Birth: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.DateofBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataFrameLeft, text="Patient Address: ", font=("Arial", 12, "bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataFrameLeft,font=("Arial",13,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

        #=================DataFrameRight=========================================
        self.txtPrescription = Text(DataFrameright, font=("Arial", 12, "bold"), width=50, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        #=================ButtonsFrame=========================================
        btnPrescription = Button(ButtonFrame,text="Prescription",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.iPrescription)
        btnPrescription.grid(row=0, column=0) 
        
        btnPrescriptionData = Button(ButtonFrame,text="Prescription Data",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.iPrescriptionDate)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(ButtonFrame,text="Update",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.update_data)
        btnUpdate.grid(row=0, column=2)
         
        btnDelete = Button(ButtonFrame,text="Delete",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.delete_data)
        btnDelete.grid(row=0, column=3) 

        btnClear = Button(ButtonFrame,text="Clear",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.clear_data)
        btnClear.grid(row=0, column=4) 

        btnExit = Button(ButtonFrame,text="Exit",bg="green",fg="black", font=("Arial", 12, "bold"),width=23, height=2, padx=2, pady=6,command=self.exit_app)
        btnExit.grid(row=0, column=5)
        
        #=================Table=========================================
        #=====================Scrollbar=================================
        scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(DetailsFrame, columns=("nameofTablets","ref","Dose","No Of Tablets","Lot","Issue Date","Exp Date","Daily Dose","storage","nhsnumber","pname","dob","address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameofTablets", text="Name Of Tablets")
        self.hospital_table.heading("ref", text="Ref No")
        self.hospital_table.heading("Dose", text="Dose")
        self.hospital_table.heading("No Of Tablets", text="No Of Tablets")
        self.hospital_table.heading("Lot", text="Lot No")
        self.hospital_table.heading("Issue Date", text="Issue Date")
        self.hospital_table.heading("Exp Date", text="Exp Date")
        self.hospital_table.heading("Daily Dose", text="Daily Dose")
        self.hospital_table.heading("storage", text="Storage Advice")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("address", text="Patient Address")
        self.hospital_table['show'] = 'headings'

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.column("nameofTablets", width=100)
        self.hospital_table.column("ref", width=100)
        self.hospital_table.column("Dose", width=100)
        self.hospital_table.column("No Of Tablets", width=100)
        self.hospital_table.column("Lot", width=100)
        self.hospital_table.column("Issue Date", width=100)
        self.hospital_table.column("Exp Date", width=100)
        self.hospital_table.column("Daily Dose", width=100)
        self.hospital_table.column("storage", width=100)
        self.hospital_table.column("nhsnumber", width=100)
        self.hospital_table.column("pname", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("address", width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()  # Fetch data when the application starts

    #===================Functionality Declaration==========================================
    def iPrescriptionDate(self):
        if self.NameofTablets.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error", "Please enter all required fields")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi1234@", database="mydata")
                my_cursor = conn.cursor()
                
                # Create the SQL query with the correct number of placeholders
                my_cursor.execute("INSERT INTO hospital VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.NameofTablets.get(),
                    self.Ref.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.storageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateofBirth.get(),
                    self.PatientAddress.get()
                ))
                
                conn.commit()
                self.fetch_data()  # Updated: Call the correct function to refresh table data
                conn.close()
                messagebox.showinfo("Success", "Record has been inserted successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

    #===================Update Data=========================================
    def update_data(self):
        if self.NameofTablets.get() == "" or self.Ref.get() == "":
            messagebox.showerror("Error", "Please enter all required fields")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi1234@", database="mydata")
                my_cursor = conn.cursor()
            
                # Make sure column names match exactly with your database structure
                my_cursor.execute("UPDATE hospital SET NameofTablets=%s, Dose=%s, NoOfTablets=%s, Lot=%s, IssueDate=%s, ExpDate=%s, DailyDose=%s, storage=%s, nhsnumber=%s, PatientName=%s, dob=%s, PatientAddress=%s WHERE ref=%s", (
                    self.NameofTablets.get(),
                    self.Dose.get(),
                    self.NumberofTablets.get(),
                    self.Lot.get(),
                    self.IssueDate.get(),
                    self.ExpDate.get(),
                    self.DailyDose.get(),
                    self.storageAdvice.get(),
                    self.nhsNumber.get(),
                    self.PatientName.get(),
                    self.DateofBirth.get(),
                    self.PatientAddress.get(),
                    self.Ref.get()
                ))
            
                conn.commit()
                self.fetch_data()  # Fixed: Consistently using fetch_data instead of fatch_data
                conn.close()
                messagebox.showinfo("Success", "Record has been updated successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")

    # Fetch Data function - helps to display data in bottom table from database
    def fetch_data(self):  # Fixed: Consistently using fetch_data throughout code
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="Abhi1234@", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM hospital")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.hospital_table.delete(*self.hospital_table.get_children())
                for i in rows:
                    self.hospital_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    # Get Cursor function - used to get the data from the table and display it in the entry fields
    def get_cursor(self, event=""):
        try:
            cursor_row = self.hospital_table.focus()
            content = self.hospital_table.item(cursor_row)
            row = content['values']
            if row:  # Check if row exists
                self.NameofTablets.set(row[0])
                self.Ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberofTablets.set(row[3])
                self.Lot.set(row[4])
                self.IssueDate.set(row[5])
                self.ExpDate.set(row[6])
                self.DailyDose.set(row[7])
                self.storageAdvice.set(row[8])
                self.nhsNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateofBirth.set(row[11])
                self.PatientAddress.set(row[12])
        except IndexError:
            messagebox.showerror("Error", "Please select a valid record")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    # New functions for Delete, Clear, and Exit buttons
    def delete_data(self):
        if self.Ref.get() == "":
            messagebox.showerror("Error", "Reference No. is required to delete a record")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Abhi1234@", database="mydata")
                my_cursor = conn.cursor()
                
                # Ask for confirmation before deleting
                confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this record?")
                if confirmation:
                    my_cursor.execute("DELETE FROM hospital WHERE ref=%s", (self.Ref.get(),))
                    conn.commit()
                    self.fetch_data()
                    self.clear_data()
                    conn.close()
                    messagebox.showinfo("Success", "Record deleted successfully")
            except mysql.connector.Error as err:
                messagebox.showerror("Database Error", f"Error: {err}")
    
    def clear_data(self):
        # Clear all entry fields
        self.NameofTablets.set("")
        self.Ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.SideEffect.set("")
        self.FurtherInformation.set("")
        self.storageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientID.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        # Clear the prescription text area
        self.txtPrescription.delete("1.0", END)
    
    def exit_app(self):
        exit_confirmation = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if exit_confirmation:
            self.root.destroy()
#===================Prescription=========================================
    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of Tablets: " + self.NameofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Ref No: " + self.Ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose: " + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "No Of Tablets: " + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot No: " + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue Date: " + self.IssueDate.get() + "\n")
        self.txtPrescription.insert(END, "Exp Date: " + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily Dose: " + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice: " + self.storageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number: " + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name: " + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of Birth: " + self.DateofBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address: " + self.PatientAddress.get() + "\n")
#        self.txtPrescription.insert(END, "----------------------------------------\n")

root = Tk()
obj = Hospital(root)
root.mainloop()