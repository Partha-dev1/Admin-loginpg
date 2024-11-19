from tkinter import *
from pymysql import *
from tkinter import messagebox
import csv

conobj = connect(host = 'localhost', user = 'root', password = '', port = 3306)
curobj = conobj . cursor()
curobj . execute ('use project;')

win1 = Tk () 
#--------------------------------------------------------------
def Login():
	#print(AName . get())
	#print(APwd . get())
	r = 'select * from ADMIN where AUser = "{}"and APwd = "{}";'.format (AName.get(),APwd .get())
	curobj.execute(r)
	record = curobj .fetchall()
	if len (record):
		win1.destroy()
		win2 = Tk ()
		#----------------------
		def AddStudent():
			win2.destroy()
			win3 = Tk ()
			#---------------------
			def Reset():
				Regno.delete(0,END)
				Name.get(0,END)
				AccYear.set("--Select ACC Year--")
				Dept.set("--Select Dept Name--")
				Password.delete(0,END)
			#---------------------
			def Save():
				#print (Regno.get(),Name.get(),AccYear.get(),Dept.get(),Password.get())
				r = 'insert into student (Regno,Name,AccYear,Dept,Password) values ("{}","{}","{}","{}","{}");'.format(Regno.get(),Name.get(),AccYear.get(),Dept.get(),Password.get())
				#print(r)
				curobj.execute(r)
				conobj.commit()
				messagebox.showinfo("Add New","Sucessfully Add A \n New Student")
				win3 . destroy()

			#---------------------
			def Exit():
				win3.destroy()
			#---------------------
			win3 .maxsize(600,400)
			win3 .minsize(600,400)
			win3 .title("Admin Home")
			win3 .configure(bg ="#ccffff")

			Label (win3 , text = "Enter Student Regno:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=50)
			Regno=Entry(win3,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
			Regno.place(x =270,y=50)

			Label (win3 , text = "Enter Student Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=100)
			Name=Entry(win3,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
			Name.place(x =270,y=100)

			Label (win3 , text = "Select Academic year:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=150)
			AccYear= StringVar ()
			AccYear.set("--Select Academic Year--")
			drop1 = OptionMenu(win3,AccYear,"2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030")
			drop1.place(x =270,y=150)

			Label (win3 , text = "Select Dept Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=200)
			Dept = StringVar ()
			Dept.set("--Select Department--")
			drop2 = OptionMenu(win3,Dept,"CSE","EEE","CIVIL","ME","CS-IT","ECE","CS(AI&ML)")
			drop2.place(x =270,y=200)

			Label (win3 , text = "Enter Password:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=250)
			Password=Entry(win3,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
			Password.place(x =270,y=250)

			Button(win3 , text = "Reset",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Reset).place (x = 50 , y = 300)

			Button(win3 , text = "Save",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Save).place (x = 200 , y = 300)

			Button(win3 , text = "Exit",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Exit).place (x = 350 , y = 300)


			win3.mainloop()
		#======================
		def Download():
			fobj = open("studentdetails.csv","w")
			cobj = csv.writer(fobj)
			cobj.writerow(['Regno','Student Name','Parent Name','Academic Year','Dept Name','Gender'])
			curobj .execute ('select * from student;')
			data= curobj.fetchall ()
			#print (list (data))
			for i in data : 
				cobj.writerow([i[0],i[1],i[2],i[3],i[4],i[5]])

			fobj .close ()
			messagebox .showinfo("Download","Thank you \n Download complete")
			win2.destroy()
		#======================
		def EXIT():
			win2 .destroy() 
		#----------------------
		win2 .maxsize(600,400)
		win2 .minsize(600,400)
		win2 .title("Admin Home")
		win2 .configure(bg ="#ccffff")
		Button (win2,text = "Add New Student",font = ('Britannic',15),bg = "#aac1bd",fg = "blue",width = 25,height = 2,relief = "groove",activebackground = "#ffff00",activeforeground = "red",command = AddStudent).place(x =150,y=50)
		
		Button (win2,text = "Download Student\n Details",font = ('Britannic',15),bg = "#aac1bd",fg = "blue",width = 25,height = 2,relief = "groove",activebackground = "#ffff00",activeforeground = "red",command = Download).place(x =150,y=150)

		Button (win2,text = "EXIT",font = ('Britannic',15),bg = "#b08c9f",fg = "blue",width = 8,height = 2,relief =
"groove",activebackground = "#ffff00",activeforeground = "red",command = EXIT).place(x =300,y=250)



		win2 .mainloop() 

	else :
		print ("Invalid Login")
		win1.destroy()
#******************
def Reset():
	AName . delete (0,END)
	APwd  . delete (0,END)
#******************
def Exit():
	win1.destroy ()


#--------------------------------------------------------------
#win1.geometry('500x500')
win1.maxsize (500,500)
win1.minsize (500,500)
win1 .title("Admin Login Page")
win1 .configure(bg = "#aac1bd")


Label (win1 , text = "!!!ONLY ADMIN LOGIN HERE!!!",font =('Britannic ',18),bg = "#aac1bd",fg = "red",width = 36,height = 2).place(x =0,y=50)

Label (win1 , text = "Enter User Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=150)
AName=Entry(win1,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
AName.place(x =270,y=150)


Label (win1 , text = "Enter Password:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=200)
APwd=Entry(win1,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken",show = "*")
APwd.place(x =270,y=200)


Button(win1 , text = "Reset",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Reset).place (x = 50 , y = 400)

Button(win1 , text = "Login",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Login).place (x = 200 , y = 400)

Button(win1 , text = "Exit",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Exit).place (x = 350 , y = 400)


win1 .mainloop()
