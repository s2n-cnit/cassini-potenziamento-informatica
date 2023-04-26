def main(): 
    metri = int(input("Metri: "))
    inch = 0.0254
    foot = 0.3048
    print("Polici: ", metri*inch)
    print("Piedi:", metri*foot)
    print("Iarde:", metri*3*foot)
    print("Miglia terrestri:", metri*3*foot*1760)

main()