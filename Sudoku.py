from tkinter import *
import random
import tkinter.messagebox as tmsg

root =Tk()
root.title("SUDOKU")
root.geometry("777x700")
root.wm_iconbitmap("calc.ico")


# increase number on click
def increase_on_click(button,index):
    global ind    
    global button_text
    # get index to change button_text list to compare at last
    
    text = button['text']
    # we use 2 spaces bcz single space font is diff. So butoon sizes are different
    text=text[0]  # bcz when 2 spaces on button present ord(text) got error as ord require single character
    if index not in ind:
        if ord(text)==57:
            button.configure(text = "  ")
            button_text[index]="  "
        elif text==" ":
            button.configure(text = "1")
            button_text[index]="1"
        else:
            button_text[index]= f"{int(text)+1}"
            button.configure(text = f"{int(text)+1}")

def solution(grid,root):
    #root.destroy()  # destroy previous window
    #CREATE NEW WINDOW
    root=Tk()
    root.title("SUDOKU -  SOLUTION")
    root.geometry("777x700")
    root.wm_iconbitmap("calc.ico")
    root.config(bg="gray")
    # Menu bar
    MenuBar = Menu(root)
    LevelMenu = Menu(MenuBar,tearoff=0)

    LevelMenu.add_command(label = "Easy",command  = lambda:easy(root))
    LevelMenu.add_command(label = "Medium",command = lambda:medium(root))
    LevelMenu.add_command(label = "Hard", command = lambda:hard(root))

    LevelMenu.add_separator()

    LevelMenu.add_command(label = "Random", command = lambda:random(root))

    MenuBar.add_cascade(label ="Levels", menu = LevelMenu)
    root.config(menu=MenuBar)

    f1 = Frame(root)
    Label(f1,text = "Solution", font = "lucida 30 bold",bg="gray",fg="white").pack(pady=5)
    f1.pack(pady=25)

    for i in range(9):
        f2=Frame(root)
        for b in range(9):
            Button(f2,text = f"{grid[i][b]}",font ="lucida 20 bold",relief=SUNKEN).pack(anchor='nw',side=LEFT,ipadx=10)
        f2.pack()
    root.mainloop()


def submit(button_text,grid):
    try:    #bcz if in button_text there is    " "  then int(" ") raise exception
        for r in range(9):
            for c in range(9):
                if str(grid[r][c]) != button_text[(9*r)+c]:
                    print(r,c)
                    tmsg.showinfo("Your Submission","Wrong submission!")
                    return
        tmsg.showinfo("Your Submission","Great Job! try next level")
    except Exception as e:
        print(e)
        tmsg.showinfo("Your Submission","Wrong submission!")
                    

#                                             FUNCTIONS USED IN SUDOKU LOGIC

def find_empty_location(arr,l): 
    for row in range(9): 
        for col in range(9): 
            if(arr[row][col]==0): 
                l[0]=row 
                l[1]=col 
                return True
    return False

def used_in_row(arr,row,num): 
    for i in range(9): 
        if(arr[row][i] == num): 
            return True
    return False

def used_in_col(arr,col,num): 
    for i in range(9): 
        if(arr[i][col] == num): 
            return True
    return False

def used_in_box(arr,row,col,num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i+row][j+col] == num): 
                return True
    return False

def check_location_is_safe(arr,row,col,num):   
    # Check if 'num' is not already placed in current row, 
    # current column and current 3x3 box 
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def solve_sudoku(arr): 
      
    # 'l' is a list variable that keeps the record of row and col in find_empty_location Function     
    l=[0,0] 
      
    # If there is no unassigned location, we are done     
    if(not find_empty_location(arr,l)): 
        return True
      
    # Assigning list values to row and col that we got from the above Function  
    row=l[0] 
    col=l[1] 
      
    # consider digits 1 to 9 
    for num in range(1,10): 
          
        # if looks promising 
        if(check_location_is_safe(arr,row,col,num)): 
              
            # make tentative assignment 
            arr[row][col]=num 
  
            # return, if success, ya! 
            if(solve_sudoku(arr)): 
                return True
  
            # failure, unmake & try again 
            arr[row][col] = 0
              
    # this triggers backtracking         
    return False



#                                                        DIFFERENT  SUDOKU LEVELS

gridrandom=[[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]

grideasy=[[0,0,0,2,6,0,7,0,1],
                [6,8,0,0,7,0,0,9,0],
                [1,9,0,0,0,4,5,0,0],
                [8,2,0,1,0,0,0,4,0],
                [0,0,4,6,0,2,9,0,0],
                [0,5,0,0,0,3,0,2,8],
                [0,0,9,3,0,0,0,7,4],
                [0,4,0,0,5,0,0,3,6],
                [7,0,3,0,1,8,0,0,0]]

gridmedium=[[2,0,0,3,0,0,0,0,0],
                        [8,0,4,0,6,2,0,0,3],
                        [0,1,3,8,0,0,2,0,0],
                        [0,0,0,0,2,0,3,9,0],
                        [5,0,7,0,0,0,6,2,1],
                        [0,3,2,0,0,6,0,0,0],
                        [0,2,0,0,0,9,1,4,0],
                        [6,0,1,2,5,0,8,0,9],
                        [0,0,0,0,0,1,0,0,2]]

gridhard=[[0,2,0,0,0,0,0,0,0],
                [0,0,0,6,0,0,0,0,3],
                [0,7,4,0,8,0,0,0,0],
                [0,0,0,0,0,3,0,0,2],
                [0,8,0,0,4,0,0,1,0],
                [6,0,0,5,0,0,0,0,0],
                [0,0,0,0,1,0,7,8,0],
                [5,0,0,0,0,9,0,0,0],
                [0,0,0,0,0,0,0,4,0]]


#if(solve_sudoku(gridhard)):
  #  print_grid(gridhard)

def display(button_text,root,grid,level):
    root.config(bg="gray")
    # Menu bar
    MenuBar = Menu(root)
    LevelMenu = Menu(MenuBar,tearoff=0)

    LevelMenu.add_command(label = "Easy",command  = lambda:easy(root))
    LevelMenu.add_command(label = "Medium",command = lambda:medium(root))
    LevelMenu.add_command(label = "Hard", command = lambda:hard(root))

    LevelMenu.add_separator()

    LevelMenu.add_command(label = "Random", command = lambda:random(root))

    MenuBar.add_cascade(label ="Levels", menu = LevelMenu)
    root.config(menu=MenuBar)

    f1 = Frame(root)
    Label(f1,text = f"LEVEL  -  {level.capitalize()}", font = "lucida 25 bold",bg="gray",fg="white").pack(pady=5)
    f1.pack(pady=25)

    
    f2=Frame(root,bg="white")
    b0=Button(f2,text = button_text[0],font ="lucida 20 bold",relief=SUNKEN,command = lambda: increase_on_click(b0,0))
    b0.pack(anchor='nw',side=LEFT,ipadx=10)

    b1=Button(f2,text = button_text[1] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b1,1))
    b1.pack(anchor='nw',side=LEFT,ipadx=10)

    b2=Button(f2,text = button_text[2],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b2,2))
    b2.pack(anchor='nw',side=LEFT,ipadx=10)

    b3=Button(f2,text = button_text[3],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b3,3))
    b3.pack(anchor='nw',side=LEFT,ipadx=10)

    b4=Button(f2,text = button_text[4],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b4,4))
    b4.pack(anchor='nw',side=LEFT,ipadx=10)

    b5=Button(f2,text = button_text[5],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b5,5))
    b5.pack(anchor='nw',side=LEFT,ipadx=10)

    b6=Button(f2,text = button_text[6],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b6,6))
    b6.pack(anchor='nw',side=LEFT,ipadx=10)

    b7=Button(f2,text = button_text[7],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b7,7))
    b7.pack(anchor='nw',side=LEFT,ipadx=10)

    b8=Button(f2,text = button_text[8],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b8,8))
    b8.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()


    f2=Frame(root)
    b9=Button(f2,text = button_text[9],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b9,9))
    b9.pack(anchor='nw',side=LEFT,ipadx=10)

    b10=Button(f2,text = button_text[10] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b10,10))
    b10.pack(anchor='nw',side=LEFT,ipadx=10)

    b11=Button(f2,text = button_text[11],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b11,11))
    b11.pack(anchor='nw',side=LEFT,ipadx=10)

    b12=Button(f2,text = button_text[12],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b12,12))
    b12.pack(anchor='nw',side=LEFT,ipadx=10)

    b13=Button(f2,text = button_text[13],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b13,13))
    b13.pack(anchor='nw',side=LEFT,ipadx=10)

    b14=Button(f2,text = button_text[14],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b14,14))
    b14.pack(anchor='nw',side=LEFT,ipadx=10)

    b15=Button(f2,text = button_text[15],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b15,15))
    b15.pack(anchor='nw',side=LEFT,ipadx=10)

    b16=Button(f2,text = button_text[16],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b16,16))
    b16.pack(anchor='nw',side=LEFT,ipadx=10)

    b17=Button(f2,text = button_text[17],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b17,17))
    b17.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b18=Button(f2,text = button_text[18],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b18,18))
    b18.pack(anchor='nw',side=LEFT,ipadx=10)

    b19=Button(f2,text = button_text[19] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b19,19))
    b19.pack(anchor='nw',side=LEFT,ipadx=10)

    b20=Button(f2,text = button_text[20],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b20,20))
    b20.pack(anchor='nw',side=LEFT,ipadx=10)

    b21=Button(f2,text = button_text[21],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b21,21))
    b21.pack(anchor='nw',side=LEFT,ipadx=10)

    b22=Button(f2,text = button_text[22],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b22,22))
    b22.pack(anchor='nw',side=LEFT,ipadx=10)

    b23=Button(f2,text = button_text[23],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b23,23))
    b23.pack(anchor='nw',side=LEFT,ipadx=10)

    b24=Button(f2,text = button_text[24],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b24,24))
    b24.pack(anchor='nw',side=LEFT,ipadx=10)

    b25=Button(f2,text = button_text[25],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b25,25))
    b25.pack(anchor='nw',side=LEFT,ipadx=10)

    b26=Button(f2,text = button_text[26],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b26,26))
    b26.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b27=Button(f2,text = button_text[27],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b27,27))
    b27.pack(anchor='nw',side=LEFT,ipadx=10)

    b28=Button(f2,text = button_text[28] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b28,28))
    b28.pack(anchor='nw',side=LEFT,ipadx=10)

    b29=Button(f2,text = button_text[29],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b29,29))
    b29.pack(anchor='nw',side=LEFT,ipadx=10)

    b30=Button(f2,text = button_text[30],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b30,30))
    b30.pack(anchor='nw',side=LEFT,ipadx=10)

    b31=Button(f2,text = button_text[31],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b31,31))
    b31.pack(anchor='nw',side=LEFT,ipadx=10)

    b32=Button(f2,text = button_text[32],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b32,32))
    b32.pack(anchor='nw',side=LEFT,ipadx=10)

    b33=Button(f2,text = button_text[33],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b33,33))
    b33.pack(anchor='nw',side=LEFT,ipadx=10)

    b34=Button(f2,text = button_text[34],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b34,34))
    b34.pack(anchor='nw',side=LEFT,ipadx=10)

    b35=Button(f2,text = button_text[35],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b35,35))
    b35.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b36=Button(f2,text = button_text[36],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b36,36))
    b36.pack(anchor='nw',side=LEFT,ipadx=10)

    b37=Button(f2,text = button_text[37] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b37,37))
    b37.pack(anchor='nw',side=LEFT,ipadx=10)

    b38=Button(f2,text = button_text[38],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b38,38))
    b38.pack(anchor='nw',side=LEFT,ipadx=10)

    b39=Button(f2,text = button_text[39],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b39,39))
    b39.pack(anchor='nw',side=LEFT,ipadx=10)

    b40=Button(f2,text = button_text[40],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b40,40))
    b40.pack(anchor='nw',side=LEFT,ipadx=10)

    b41=Button(f2,text = button_text[41],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b41,41))
    b41.pack(anchor='nw',side=LEFT,ipadx=10)

    b42=Button(f2,text = button_text[42],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b42,42))
    b42.pack(anchor='nw',side=LEFT,ipadx=10)

    b43=Button(f2,text = button_text[43],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b43,43))
    b43.pack(anchor='nw',side=LEFT,ipadx=10)

    b44=Button(f2,text = button_text[44],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b44,44))
    b44.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()


    f2=Frame(root)
    b45=Button(f2,text = button_text[45],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b45,45))
    b45.pack(anchor='nw',side=LEFT,ipadx=10)

    b46=Button(f2,text = button_text[46] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b46,46))
    b46.pack(anchor='nw',side=LEFT,ipadx=10)

    b47=Button(f2,text = button_text[47],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b47,47))
    b47.pack(anchor='nw',side=LEFT,ipadx=10)

    b48=Button(f2,text = button_text[48],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b48,48))
    b48.pack(anchor='nw',side=LEFT,ipadx=10)

    b49=Button(f2,text = button_text[49],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b49,49))
    b49.pack(anchor='nw',side=LEFT,ipadx=10)

    b50=Button(f2,text = button_text[50],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b50,50))
    b50.pack(anchor='nw',side=LEFT,ipadx=10)

    b51=Button(f2,text = button_text[51],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b51,51))
    b51.pack(anchor='nw',side=LEFT,ipadx=10)

    b52=Button(f2,text = button_text[52],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b52,52))
    b52.pack(anchor='nw',side=LEFT,ipadx=10)

    b53=Button(f2,text = button_text[53],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b53,53))
    b53.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b54=Button(f2,text = button_text[54],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b54,54))
    b54.pack(anchor='nw',side=LEFT,ipadx=10)

    b55=Button(f2,text = button_text[55] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b55,55))
    b55.pack(anchor='nw',side=LEFT,ipadx=10)

    b56=Button(f2,text = button_text[56],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b56,56))
    b56.pack(anchor='nw',side=LEFT,ipadx=10)

    b57=Button(f2,text = button_text[57],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b57,57))
    b57.pack(anchor='nw',side=LEFT,ipadx=10)

    b58=Button(f2,text = button_text[58],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b58,58))
    b58.pack(anchor='nw',side=LEFT,ipadx=10)

    b59=Button(f2,text = button_text[59],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b59,59))
    b59.pack(anchor='nw',side=LEFT,ipadx=10)

    b60=Button(f2,text = button_text[60],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b60,60))
    b60.pack(anchor='nw',side=LEFT,ipadx=10)

    b61=Button(f2,text = button_text[61],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b61,61))
    b61.pack(anchor='nw',side=LEFT,ipadx=10)

    b62=Button(f2,text = button_text[62],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b62,62))
    b62.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b63=Button(f2,text = button_text[63],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b63,63))
    b63.pack(anchor='nw',side=LEFT,ipadx=10)

    b64=Button(f2,text = button_text[64] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b64,64))
    b64.pack(anchor='nw',side=LEFT,ipadx=10)

    b65=Button(f2,text = button_text[65],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b65,65))
    b65.pack(anchor='nw',side=LEFT,ipadx=10)

    b66=Button(f2,text = button_text[66],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b66,66))
    b66.pack(anchor='nw',side=LEFT,ipadx=10)

    b67=Button(f2,text = button_text[67],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b67,67))
    b67.pack(anchor='nw',side=LEFT,ipadx=10)

    b68=Button(f2,text = button_text[68],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b68,68))
    b68.pack(anchor='nw',side=LEFT,ipadx=10)

    b69=Button(f2,text = button_text[69],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b69,69))
    b69.pack(anchor='nw',side=LEFT,ipadx=10)

    b70=Button(f2,text = button_text[70],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b70,70))
    b70.pack(anchor='nw',side=LEFT,ipadx=10)

    b71=Button(f2,text = button_text[71],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b71,71))
    b71.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()



    f2=Frame(root)
    b72=Button(f2,text = button_text[72],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b72,72))
    b72.pack(anchor='nw',side=LEFT,ipadx=10)

    b73=Button(f2,text = button_text[73] ,font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b73,73))
    b73.pack(anchor='nw',side=LEFT,ipadx=10)

    b74=Button(f2,text = button_text[74],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b74,74))
    b74.pack(anchor='nw',side=LEFT,ipadx=10)

    b75=Button(f2,text = button_text[75],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b75,75))
    b75.pack(anchor='nw',side=LEFT,ipadx=10)

    b76=Button(f2,text = button_text[76],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b76,76))
    b76.pack(anchor='nw',side=LEFT,ipadx=10)

    b77=Button(f2,text = button_text[77],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b77,77))
    b77.pack(anchor='nw',side=LEFT,ipadx=10)

    b78=Button(f2,text = button_text[78],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b78,78))
    b78.pack(anchor='nw',side=LEFT,ipadx=10)

    b79=Button(f2,text = button_text[79],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b79,79))
    b79.pack(anchor='nw',side=LEFT,ipadx=10)

    b80=Button(f2,text = button_text[80],font ="lucida 20 bold",relief=SUNKEN,command = lambda:increase_on_click(b80,80))
    b80.pack(anchor='nw',side=LEFT,ipadx=10)

    f2.pack()


    sub_frame = Frame(root)
    Button(sub_frame,text = "Submit",font="lucida 25 bold",bg="gray",fg="white",relief=SUNKEN,command = lambda:submit(button_text,grid)).pack(anchor='nw',side=LEFT,ipadx=15)
    Button(sub_frame,text = "Solution",font="lucida 25 bold",bg="gray",fg="white",relief=SUNKEN,command = lambda:solution(grid,root)).pack(anchor='nw',side=LEFT,ipadx=15)
    sub_frame.pack(pady=20)
    sub_frame.config(bg="gray")
# --------------------------------------------END OF DISPLAY FUNCTION------------------------------

def easy(root):
    root.destroy()
    roote =Tk()
    roote.title("SUDOKU -  EASY")
    roote.geometry("777x700")
    roote.wm_iconbitmap("calc.ico")
    global ind
    ind= []
    global button_text
    button_text = []
    for t in range(81):
        button_text.append("  ")
    for row in range(9):
        for col in range(9):
            if grideasy[row][col]==0:
                button_text[9*row+col] = "  "
            else:
                button_text[9*row+col] = str(grideasy[row][col])
                ind.append(9*row+col)
    if solve_sudoku(grideasy):
        display(button_text,roote,grideasy,"EASY")
    roote.mainloop()

def medium(root):
    root.destroy()
    rootm =Tk()
    rootm.title("SUDOKU -  MEDIUM")
    rootm.geometry("777x700")
    rootm.wm_iconbitmap("calc.ico")
    ind=[]
    global button_text
    button_text = []
    for t in range(81):
        button_text.append("  ")
    for row in range(9):
        for col in range(9):
            if gridmedium[row][col]==0:
                button_text[9*row+col] = "  "
            else:
                button_text[9*row+col] = str(gridmedium[row][col])
                ind.append(9*row+col)
    if solve_sudoku(gridmedium):
        display(button_text,rootm,gridmedium,"MEDIUM")
    rootm.mainloop()

def hard(root):
    root.destroy()
    rooth =Tk()
    rooth.title("SUDOKU -  HARD")
    rooth.geometry("777x700")
    rooth.wm_iconbitmap("calc.ico")
    global ind
    ind =[]
    global button_text
    button_text = []
    for t in range(81):
        button_text.append("  ")
    for row in range(9):
        for col in range(9):
            if gridhard[row][col]==0:
                button_text[9*row+col] = "  "
            else:
                button_text[9*row+col] = str(gridhard[row][col])
                ind.append(9*row+col)
    if solve_sudoku(gridhard):
        display(button_text,rooth,gridhard,"HARD")
    rooth.mainloop()

def random(root):
    global ind
    root.destroy()
    rootr =Tk()
    rootr.title("SUDOKU -  RANDOM")
    rootr.geometry("777x700")
    rootr.wm_iconbitmap("calc.ico")
    ind = []
    global button_text
    button_text = []
    for t in range(81):
        button_text.append("  ")
    for row in range(9):
        for col in range(9):
            if gridrandom[row][col]==0:
                button_text[9*row+col] = "  "
            else:
                button_text[9*row+col] = str(gridrandom[row][col])
                ind.append(9*row+col)
    if solve_sudoku(gridrandom):
        display(button_text,rootr,gridrandom,"RANDOM")
    rootr.mainloop()

    # Menu bar
MenuBar = Menu(root)
LevelMenu = Menu(MenuBar,tearoff=0)

LevelMenu.add_command(label = "Easy",command  = lambda:easy(root))
LevelMenu.add_command(label = "Medium",command = lambda:medium(root))
LevelMenu.add_command(label = "Hard", command = lambda:hard(root))

LevelMenu.add_separator()

LevelMenu.add_command(label = "Random", command = lambda:random(root))

MenuBar.add_cascade(label ="Levels", menu = LevelMenu)
root.config(menu=MenuBar)

f1 = Frame(root)
Label(f1,text = "Play Sudoku!", font = "lucida 40 bold",bg="dodgerblue",fg="white").pack(pady=10)
f1.pack(pady=50)

f1 = Frame(root)
Label(f1,text = "Select Level from MenuBar", font = "lucida 40 bold",bg="dodgerblue",fg="white").pack(pady=5)
f1.pack()

root.config(bg="dodgerblue")
root.mainloop()
