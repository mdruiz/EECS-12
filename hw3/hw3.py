# hw3.py
# Mario Ruiz ID:46301389
#This program draws a festive tree using GUI interfaces

from graphics import *
from math import *

def main():
    win= GraphWin("Festival Tree", 800, 600)
    win.setCoords(0,0,40,30)
    txtMsg= Text(Point(20,29),"Please enter the number of tree layers and click anywhere")
    txtMsg.setTextColor("red")
    txtMsg.setSize(12)
    txtMsg.draw(win)
    Text(Point(5,28),"Number of Layers:").draw(win)
    entry0= Entry(Point(10,28),5)
    entry0.setText(4)
    entry0.draw(win)
    win.getMouse()

    txtMsg.setText("Please click a point for the top of the tree body.")
    P1=win.getMouse()
    P1.draw(win)

    txtMsg.setText("Please click the bottom corner of the tree body.")
    P2=win.getMouse()
    P2.draw(win)
    #####################################################################
    if P1.getX() > P2.getX():   #P2 = Bottom Left Corner
        P3X=(P1.getX()-P2.getX())
        P3Y=(P1.getY()-P2.getY())
        P3=Point(P1.getX()+P3X, P1.getY()-P3Y)
        P3.draw(win)
        Tree=Polygon(P1,P2,P3)
        Tree.setFill("green4")
        Tree.draw(win)
    
        for i in range(eval(entry0.getText())-1):
            BottomLine=Line(P2,P3)
            CenterLine=Line(BottomLine.getCenter(),P1)
            TreeCenter=CenterLine.getCenter()
            Tree=Polygon(TreeCenter,Point(P2.getX()-2,P2.getY()-3),Point(P3.getX()+2,P3.getY()-3))
            Tree.setFill("green4")
            Tree.draw(win)
            P2=Point(P2.getX()-2,P2.getY()-3)
            P3=Point(P3.getX()+2,P3.getY()-3)
            P1=TreeCenter

    if P1.getX() < P2.getX():   #P2 = Bottom Right Corner
        P3X=(P2.getX()-P1.getX())
        P3Y=(P2.getY()-P1.getY())
        P3=Point(P1.getX()-P3X, P1.getY()+P3Y)
        P3.draw(win)
        Tree=Polygon(P1,P2,P3)
        Tree.setFill("green4")
        Tree.draw(win)

        for i in range(eval(entry0.getText())-1):
            BottomLine=Line(P2,P3)
            CenterLine=Line(BottomLine.getCenter(),P1)
            TreeCenter=CenterLine.getCenter()
            Tree=Polygon(TreeCenter,Point(P2.getX()+2,P2.getY()-3),Point(P3.getX()-2,P3.getY()-3))
            Tree.setFill("green4")
            Tree.draw(win)
            P2=Point(P2.getX()+2,P2.getY()-3)
            P3=Point(P3.getX()-2,P3.getY()-3)
            P1=TreeCenter

    #####################################################################
    txtMsg.setText("Please click for the trunk of the tree.")
    BottomLine=Line(P2,P3)
    P10=win.getMouse()
    BCenter= BottomLine.getCenter()
    if P10.getX()< BCenter.getX():  #P10= Left Corner
        P11X=BCenter.getX()- P10.getX()
        Trunk= Rectangle(P10, Point(BCenter.getX()+P11X,BCenter.getY()))
        Trunk.setFill("brown")
        Trunk.draw(win)

    if P10.getX()> BCenter.getX():  #P10= Right corner
        P11X=P10.getX()- BCenter.getX()
        Trunk= Rectangle(P10, Point(BCenter.getX()-P11X,BCenter.getY()))
        Trunk.setFill("brown")
        Trunk.draw(win)

    #####################################################################
    txtMsg.setText("Please click two points to set the center and radius of the ornament")
    P4=win.getMouse()
    P5=win.getMouse()
    r1= sqrt((P4.x-P5.x)**2+(P4.y-P5.y)**2)
    Ornament1= Circle(P4, r1)
    Ornament1.setFill("yellow")
    Ornament1.draw(win)
    
    txtMsg.setText("Please click again for another ornament")
    P6=win.getMouse()
    P7=win.getMouse()
    r2= sqrt((P6.x-P7.x)**2+(P6.y-P7.y)**2)
    Ornament2= Circle(P6, r2)
    Ornament2.setFill("yellow")
    Ornament2.draw(win)
    
    txtMsg.setText("Please click again for another ornament")
    P8=win.getMouse()
    P9=win.getMouse()
    r3= sqrt((P8.x-P9.x)**2+(P8.y-P9.y)**2)
    Ornament3= Circle(P8, r3)
    Ornament3.setFill("yellow")
    Ornament3.draw(win)
    
    #####################################################################
    Text(Point(5,4),"Color  of Ornament 1:").draw(win)
    entry1= Entry(Point(11,4),10)
    entry1.setText("yellow")
    entry1.draw(win)
    Text(Point(5,3),"Color  of Ornament 2:").draw(win)
    entry2= Entry(Point(11,3),10)
    entry2.setText("red")
    entry2.draw(win)
    Text(Point(5,2),"Color  of Ornament 3:").draw(win)
    entry3= Entry(Point(11,2),10)
    entry3.setText("blue")
    entry3.draw(win)
    Text(Point(5,1),"Color  of Tree Trunk:").draw(win)
    entry4= Entry(Point(11,1),10)
    entry4.setText("purple")
    entry4.draw(win)
    #####################################################################
    txtMsg.setText("Please enter the color of the ornaments and click Update, or click Exit")

    buttonForUpdate=Rectangle(Point(16,2),Point(20,4))
    buttonForUpdate.setFill("lightblue")
    buttonForUpdate.draw(win)
    updateMessage=Text(Point(18,3),"Update")
    updateMessage.draw(win)

    buttonForExit=Rectangle(Point(22,2),Point(26,4))
    buttonForExit.setFill("lightpink")
    buttonForExit.draw(win)
    exitMessage=Text(Point(24,3),"Exit")
    exitMessage.draw(win)
    #####################################################################
    def main2():
        P0=win.getMouse()
        if P0.x>=16 and P0.x<=20 and P0.y>=2 and P0.y<=4 :
            Ornament1.setFill(entry1.getText())
            Ornament2.setFill(entry2.getText())
            Ornament3.setFill(entry3.getText())
            Trunk.setFill(entry4.getText())
            main2()

        if P0.x<=15 or 20<P0.x<22 or P0.x>=27 or P0.y<=1 or P0.y>=5:
            main2()
        
        if P0.x>=22 and P0.x<=26 and P0.y>=2 and P0.y<=4 :
            win.close()
    main2()

main()
