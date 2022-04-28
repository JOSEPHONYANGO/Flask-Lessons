toDo={
    "Monday":"Code",
    "Tuesday":"Gym",
    "Wednesday":"Dance",
    "Thursday":"Bake",
    "Friday":"Movie",
    "Saturday":"Football",
    "Sunday":"Preach"
}

def get_all_to_do():
    return f"<ul>{to_to_do()}</ul>"

def to_to_do():
    li=""
    for key in toDo:
        li=li+f"<li><h1>On:<b>{key}</b>we{toDo[key]}</h1></li>"
        
    return li
    
    #print (get_all_to_do())

       