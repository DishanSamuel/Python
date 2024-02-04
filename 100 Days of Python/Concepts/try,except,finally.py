def function1():
    l = [1, 2, 3, 4]
    index = int(input("enter the index number of l : "))
    
    try:
        print(l[index])
        return 1
    except:
        print("something went wrong")
        return 0
    finally:
        print("code inside finally will always run even if there is a return value in the function")
        
    Print("this will not print anything because it is after a return value")
        
        
if __name__ == "__main__":
    status = function1()
    print(f"status code {status}")