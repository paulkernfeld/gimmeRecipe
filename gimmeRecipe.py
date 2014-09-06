#!/usr/bin/env python
import random
import Tkinter
from Tkinter import *
from tkMessageBox import *

names = []
dinnerbox_names = []
selected_names = []

database = open('allthefood.txt', 'a+')

for line in database:
    if 'Name:' in line:
        names.append((line.strip() + ' ')[5:-1].strip())


win = Tkinter.Tk()


def randomRecipe():
    # Choose randomly from the names, NOT including the names already in the
    # dinnerbox. Note that this will break if it's clicked too many times.
    displayedName = random.choice([n for n in set(names) - set(dinnerbox_names)])
    #tkMessageBox.showinfo("Here\'s one!", "How about " + displayedName +"?")
    dinnerbox.insert('end', "How about " + displayedName + "? ")
    dinnerbox_names.append(displayedName)


def addSelected():
    for index in dinnerbox.curselection():
        tf = (dinnerbox_names[int(index)] in selected_names)
        if tf:
            print ''
        else:
            selected_names.append(dinnerbox_names[int(index)])
            chosenbox.insert('end', dinnerbox_names[int(index)])


def removeSelected():
    for index in chosenbox.curselection():
        selected_names.remove(selected_names[int(index)])
        chosenbox.delete(int(index))


def showIngredients():
    dish_marker = False
    # Indicates whether the name we last passed is a selected dish
    ingred_marker = False
    # Indicates whether we are in the ingredients section
    database = open('allthefood.txt')
    ingredbox.delete(0, END)

    for line in database:
        if 'Name:' in line:
            dishname = (line.strip() + ' ')[5:-1].strip()
            dish_marker = (dishname in selected_names)
            if dish_marker:
                ingredbox.insert('end', dishname)
            # print 'dish_marker=' + dish_marker.str()
        if 'Ingredients:' in line:
            ingred_marker = True
            # print 'ingred_marker=' + ingred_marker.str()
        if 'Instructions:' in line:
            ingred_marker = False
            # print 'ingred_marker=' + ingred_marker.str()
        if dish_marker and ingred_marker:
            ingredbox.insert('end', line)


def newRecipe():
    new_recipe_entry_window = Toplevel()

    name_label = Label(new_recipe_entry_window, text="Name:")
    name_label.pack(side='top')
    new_name_box = Entry(new_recipe_entry_window)
    new_name_box.pack(side='top')

    ing_label = Label(new_recipe_entry_window, text="Ingredients:")
    ing_label.pack(side='top')
    new_ing_box = Text(new_recipe_entry_window, width=25, height=15)
    new_ing_box.pack(side='top')

    instr_label = Label(new_recipe_entry_window, text="Instructions:")
    instr_label.pack(side='top')
    new_instr_box = Text(new_recipe_entry_window, width=25, height=10)
    new_instr_box.pack(side='top')

    add_recipe = Tkinter.Button(new_recipe_entry_window, text="Add this as a recipe",
                                command=lambda: add_new_recipe(new_name_box, new_ing_box, new_instr_box))
    add_recipe.pack(side='top')


def add_new_recipe(new_name_box, new_ing_box, new_instr_box):
    new_name = new_name_box.get()
    new_ing = new_ing_box.get("0.0", END)
    new_instr = new_instr_box.get("0.0", END)
    database.write('\n' + 'Name:' + new_name + '\n')
    database.write('Ingredients' + '\n' + new_ing + '\n')
    database.write('Instructions:' + '\n' + new_instr + '\n')
    showinfo(title='Recipe added', message='Your recipe has been added.')


gimme = Tkinter.Button(win, text="Gimme", command=randomRecipe)
gimme.pack(side='top')
add_selection = Tkinter.Button(win, text="Add Selected Items", command=addSelected)
add_selection.pack(side='top')
show_ingredients = Tkinter.Button(win, text="Show Ingredients", command=showIngredients)
show_ingredients.pack(side='top')
remove_selected_item = Tkinter.Button(win, text="Remove Selected Items", command=removeSelected)
remove_selected_item.pack(side='top')
new_recipe = Tkinter.Button(win, text="Add new recipe", command=newRecipe)
new_recipe.pack(side='top')

dinnerbox = Tkinter.Listbox(win, width=50, height=30)
dinnerbox.pack(side='left')
ingredbox = Tkinter.Listbox(win, width=50, height=30)
ingredbox.pack(side='right')
chosenbox = Tkinter.Listbox(win, width=50, height=30)
chosenbox.pack(side='right')

ingredbox_sb = Tkinter.Scrollbar(win, orient=VERTICAL)
ingredbox_sb.pack(side=LEFT, fill=Y)
ingredbox_sb.configure(command=ingredbox.yview)
ingredbox.configure(yscrollcommand=ingredbox_sb.set)


win.mainloop()
