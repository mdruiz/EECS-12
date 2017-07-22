# hw5.py
# Magic Squares
# Mario Ruiz ID:46301389

from graphics import*
import time

#for flying obj from start x,y to end x,y
def move(obj, startX, startY, endX, endY):
    x=endX-startX
    y=endY-startY
    for i in range(10):
        obj.move((x/10),(y/10))
        time.sleep(0.05)
    #obj.move(x,y) 
    return #nothing


#for calculating x,y coordgiven row and column
def calculateCoordinates(left_border,top_border,cell_width,column,row):
    top_border=(cell_width/2)+top_border
    left_border=left_border-(cell_width/2)
    x_coord = left_border+(cell_width*(column+1))
    y_coord = top_border-(cell_width*(row+1)) 
    return x_coord, y_coord
  

def main():
    win=GraphWin("Magic Square",500,500)
    win.setCoords(0,0,100,100)

    #Initialization
    txtMsg= Text(Point(60,95),"Please enter the square size and click the Draw button")
    txtMsg.setSize(9)
    txtMsg.draw(win)
    entry=Entry(Point(20,95),5)
    entry.draw(win)
    size=Text(Point(7,95),"Square Size:")
    size.setSize(9)
    size.draw(win)

    drawButton= Rectangle(Point(5,5),Point(13,10))
    drawButton.draw(win)
    drawText=Text(Point(9,7.5),"Draw")
    drawText.setSize(9)
    drawText.draw(win)

    exitButton= Rectangle(Point(21,5),Point(29,10))
    exitButton.draw(win)
    exitText=Text(Point(25,7.5),"Exit")
    exitText.setSize(9)
    exitText.draw(win)

    #Define Grid
    line_list=[0]
    matrix=[]
    clear_flag= False
    once= True
    nums=[0]
    while (once):
        click=win.getMouse()
        #if clicked on Exit Button
        if click.x>=21 and click.x<=29 and click.y>=5 and click.y<=10:
            break
        #elif clicked on Draw Button
        elif click.x>=5 and click.x<=13 and click.y>=5 and click.y<=10:
            txtMsg.setText("Please click the block for placing 1")
            #TODO: If needed, clear existing drawing
            if line_list[0]!=0:
                for i in range(len(line_list)):
                    line_list[i].undraw()
            if nums[0]!=0:
                for i in range (len(nums)):
                        nums[i].undraw()
                        
            #TODO: calculate cell size and  border of the grid
            n=eval(entry.getText())
            cell_width= 80//n
            h=90
            v=10
            #TODO: draw lines, save them in line_list (for future undraw)
            line_list=[]
            for i in range(n+1):
                horizontal=Line(Point(10,h),Point(cell_width*n+10,h))
                vertical= Line(Point(v,90),Point(v,90-cell_width*n))
                line_list.append(horizontal)
                line_list.append(vertical)
                h=h-cell_width
                v=v+cell_width
            for i in range(len(line_list)):
                line_list[i].draw(win)
            
            #TODO: draw textfield, save in matrix
            matrix=[0]*n
            for i in range(n):
                matrix[i]=[0]*n
        #elif click inside the grid,"1" should be placed and all #s follow
        elif click.x>=10 and click.x<=(cell_width*n+10) and click.y<=90 and click.y>=(90-cell_width*n):
            txtMsg.setText("Please wait.....")
            #TODO: find out which row, column is clicked
            top_border=90
            left_border=10
            row= int((top_border-click.y)//cell_width)
            column=int(((left_border+click.x)//cell_width)-1)
            
            #TODO: implement algorithm for putting numbers in right place
            #TODO: use calculateCoordinate() and move() to show numbers
            nums = [] 
            for k in range(n*n):
                matrix[column][row]=1
                x,y= calculateCoordinates(left_border,top_border,cell_width,column,row)
                number = Text(Point(5, 85),str(k+1))
                number.setTextColor("Blue")
                number.setSize(19)
                number.draw(win)
                time.sleep(0.2)
                move(number, 5, 85, x, y)
                nums.append(number)

                column= column+1
                row= row+1
                if row == n:
                    row=0
                if column==n:
                    column=0
                if matrix[column][row]!=0:
                    if column==0 and row==0:
                        column=column+(n-1)
                        row=row+(n-1)
                    elif column==0:
                        column=column+(n-1)
                        row=row-1
                    elif row==0:
                        row=row+(n-1)
                        column=column-1
                    else:
                        column=column-1
                        row=row-1
                    row=row-1
                    if row==-1:
                        row=n-1
            txtMsg.setText("Please enter the square size and click the Draw button")
                        
    click = win.getMouse()
    win.close()
    print ("Program terminated!")
    
main()

    
