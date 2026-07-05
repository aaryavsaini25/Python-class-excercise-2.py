def list_input():
    list_1=[]
    try:
        list_1_input_amount=int(input("Enter the number of elements:"))
    except:
        print("Please enter a number!")
        return
    while list_1_input_amount>0:
        try:
            list_1_input=int(input("Enter a number:"))
        except:
            print("Please enter a number!")
            return
        list_1.append(list_1_input)
        list_1_input_amount-=1
    return list_1
def common_elements():
    list_1=list_input()
    list_2=list_input()
    common_list=[]
    for el in list_1:
        if el in list_2:
            common_list.append(el)
    list_1_display=str(list_1).strip("[]")
    list_2_display=str(list_2).strip("[]")
    common_list_display=str(common_list).strip("[]")
    print(f"The first list of elements were {list_1_display}.")
    print(f"The second list of elements were {list_2_display}.")
    print(f"The common elements were {common_list_display}.")
common_elements()