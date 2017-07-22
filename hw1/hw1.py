# hw1.py
# Future Value Program
# Mario Ruiz    ID:46301389
def main():
    print ("This program calculates the future value")
    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annual interest rate:"))
    years = eval(input("Enter the number of years:"))
    year = 0
    simple = principal
    Simple = principal
    print ("Investment values for simple interest and compound interest:")
    print ("0" ,"\t", Simple ,"\t""\t", principal)
    for i in range (years):
        principal = principal * (1 + apr)
        year = year + 1
        Simple = Simple + ( simple * apr)
        print ( year,"\t",Simple,"\t",principal)
main()

