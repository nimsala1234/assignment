from priority import add_priority
from due_dates import add_due_date
from categories import add_category
from search import search_todo

print("To-Do List Application")

todo_list = []

def show_todos():
    print("Your To-Do List:")
    for item in todo_list:
        print(f"- {item['task']} (Priority: {item.get('priority', 'N/A')}, Due Date: {item.get('due_date', 'N/A')}, Category: {item.get('category', 'N/A')})")

def add_todo():
    item = {}
    item['task'] = input("Enter a new to-do item: ")
    todo_list.append(item)
    item = add_priority(item)
    item = add_due_date(item)
    item = add_category(item)
    show_todos()

def remove_todo():
    task = input("Enter the to-do item to remove: ")
    for item in todo_list:
        if item['task'] == task:
            todo_list.remove(item)
            break
    show_todos()

add_todo()
remove_todo()
search_todo(todo_list)
show_todos()
