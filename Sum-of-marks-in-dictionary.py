def sum_marks():
    marks = {
        "maths": 99,
        "science": 100,
        "computer": 90
    }
    display_val=str(marks.values()).strip("dict_values([])")
    subjects=str(marks.keys()).strip("dict_keys([])")
    marks_list=sum(marks.values())
    average=marks_list/len(marks.values())
    dis_a=int(average)
    maximum=max(marks.values())
    minimum=min(marks.values())
    print(f"The exam subjects were {subjects}.")
    print(f"The marks were {display_val} respectively.")
    print(f"The sum of the marks were {marks_list}.")
    print(f"The average mark was {average}.")
    print(f"The rounded off average was {dis_a}.")
    print(f"The maximum mark was {maximum}.")
    print(f"The minimum mark was {minimum}.")
sum_marks()