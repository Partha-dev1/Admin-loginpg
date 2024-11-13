from tkinter import *
from tkinter import messagebox
from pymysql import *


conobj = connect(host = 'localhost', user = 'root', password = '', port = 3306)
curobj = conobj . cursor()
curobj . execute ('use project;')

win1=Tk ()
#---------------------------------------
def Login():
	x= Regno.get()
	y = SAccYear .get()
	z= SPwd.get()
	r = 'select * from student where Regno = "{}"and AccYear = "{}" and Password = "{}";'.format (Regno.get(),SAccYear .get(),SPwd.get())
	curobj.execute(r)
	record = curobj .fetchall()		
	if (len (record)):
		win1.destroy()
		win2 = Tk()		
		#----------------------
		def Update():
			#print(URegno.get(),UName.get(),PName.get(),Gender.get(),UAccYear .get(),UDept.get(),UContact.get(),UPwd.get())
			r = 'update student set Name = "{}", parent ="{}" , Dept = "{}",Cont = "{}",Password="{}",Gender = "{}" where Regno = "{}" and AccYear= "{}" and Password = "{}" ;'.format (UName.get(),PName.get(),UDept.get(),UContact.get(),UPwd.get(),Gender.get(),x, y ,z  )
			print(r)
			curobj.execute(r)
			conobj.commit()
		#--------------------
		def Reset():
			URegno.delete(0,END)
			UName.delete(0,END)
			PName.delete(0,END)
			UContact.delete(0,END)
			UPwd.delete(0,END)
			Gender.deselect()
			UAccYear .set("--Select Acc Year--")
			UDept.set("--Select Dept Name--")

		#-----------------------
		def Exit():
			win2.destroy()

		#--------------------
		win2.maxsize (1100,600)
		win2.minsize (1100,600)
		win2.title("Student Home Page")
		win2.configure(bg = "#aac1bd")

		Label (win2 , text = "Enter Student Regno:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=50)
		URegno=Entry(win2,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
		URegno.place(x =270,y=50)
	
		Label (win2 , text = "Student Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =570,y=50)
		UName=Entry(win2,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
		UName.place(x =810,y=50)

		Label (win2 , text = "Parent Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=100)
		PName=Entry(win2,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
		PName.place(x =270,y=100)
	
		Label (win2 , text = "Select Student Gender:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =570,y=100)
		Gender=StringVar()
		r1 = Radiobutton(win2,text = "Male",variable = Gender ,value = "M")
		r1.place(x =810,y=100)
		r2 = Radiobutton(win2,text = "Female",variable = Gender ,value = "Fe")
		r2.place(x =880,y=100)

		Label (win2 , text = "Select Academic year:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=150)
		UAccYear= StringVar ()
		UAccYear.set("--Select Academic Year--")
		drop1 = OptionMenu(win2,UAccYear,"2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030")
		drop1.place(x =270,y=150)

		Label (win2 , text = "Select Dept Name:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =570,y=150)
		UDept = StringVar ()
		UDept.set("--Select Department--")
		drop2 = OptionMenu(win2,UDept,"CSE","EEE","CIVIL","ME","CS-IT","ECE","CS(AI&ML)")
		drop2.place(x =810,y=150)

		Label (win2 , text = "Enter Student Contact:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=200)
		UContact=Entry(win2,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
		UContact.place(x =270,y=200)
	
		Label (win2 , text = "Student Password:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =570,y=200)
		UPwd=Entry(win2,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
		UPwd.place(x =810,y=200)

		Button(win2 , text = "Reset",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Reset).place (x = 100 , y = 400)

		Button(win2 , text = "Update",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Update).place (x = 400 , y = 400)

		Button(win2 , text = "Exit",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Exit).place (x = 700 , y = 400)



		win2.mainloop()
	else :
		messagebox.showinfo("Invalid","Invalid user name ,acc year & password")
		win1.destroy()
#-----------------
def Reset():
	Regno .delete (0,END)
	SAccYear .set ("--Select Acc Year--")
	SPwd .delete(0,END)
#-----------------
def Exit():
	win1.destroy()
#---------------------------------------
win1.maxsize (500,500)
win1.minsize (500,500)
win1 .title("Student Login Page")
win1 .configure(bg = "#aac1bd")


Label (win1 , text = "!!!ONLY STUDENT LOGIN HERE!!!",font =('Britannic ',18),bg = "#aac1bd",fg = "red",width = 36,height = 2).place(x =0,y=0)

Label (win1 , text = "Enter Student Regno:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=150)
Regno=Entry(win1,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken")
Regno.place(x =270,y=150)

Label (win1,text = "Select Academic year:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=200)
SAccYear= StringVar ()
SAccYear.set("--Select Academic Year--")
drop1 = OptionMenu(win1,SAccYear,"2020-2024","2021-2025","2022-2026","2023-2027","2024-2028","2025-2029","2026-2030")
drop1.place(x =270,y=200)


Label (win1 , text = "Enter Password:",font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,height = 1,relief = "raised").place(x =10,y=250)
SPwd=Entry(win1,font =('Britannic ',15),bg = "#2c3e50",fg = "white",width = 20,relief = "sunken",show = "*")
SPwd.place(x =270,y=250)


Button(win1 , text = "Reset",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Reset).place (x = 50 , y = 400)

Button(win1 , text = "Login",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Login).place (x = 200 , y = 400)

Button(win1 , text = "Exit",font =('Britannic ',18),height = 2,width = 8,relief = "raised",bg ="#1abc9c",activebackground = "#34495e",fg = "red",command = Exit).place (x = 350 , y = 400)


win1 .mainloop()