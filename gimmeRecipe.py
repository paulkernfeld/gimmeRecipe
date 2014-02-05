#!/usr/bin/env python
import random
import Tkinter
from Tkinter import *
names=[];
dinnerbox_names=[];
selected_names=[];

database=open('allthefood.txt')

for line in database:
    if 'Name:' in line:
        names.append((line.strip()+' ')[5:-1].strip())


win = Tkinter.Tk()

def randomRecipe():
    displayedName=random.choice(names)
    #tkMessageBox.showinfo("Here\'s one!", "How about " + displayedName +"?")
    dinnerbox.insert('end', "How about " + displayedName +"? ")
    dinnerbox_names.append(displayedName)

def addSelected():
    for index in dinnerbox.curselection():
        tf = (dinnerbox_names[int(index)] in selected_names)
        if tf:
            print ''
        else:
            selected_names.append(dinnerbox_names[int(index)])
            chosenbox.insert('end', dinnerbox_names[int(index)])

def showIngredients():
    dish_marker=False;#Indicates whether the name we last passed is a selected dish
    ingred_marker=False;#Indicates whether we are in the ingredients section
    database=open('allthefood.txt')
    ingredbox.delete(0, END)

    for line in database:
        if 'Name:' in line:
            dishname=(line.strip()+' ')[5:-1].strip()
            dish_marker = (dishname in selected_names)
            if dish_marker:
                ingredbox.insert('end', dishname)
            #print 'dish_marker=' + dish_marker.str()
        if 'Ingredients:' in line:
            ingred_marker=True;
            #print 'ingred_marker=' + ingred_marker.str()
        if 'Instructions:' in line:
            ingred_marker=False;
            #print 'ingred_marker=' + ingred_marker.str()
        if dish_marker and ingred_marker:
            ingredbox.insert('end', line)

def newRecipe():
    print ''


gimme = Tkinter.Button(win, text ="Gimme", command = randomRecipe)
gimme.pack(side='top')
add_selection = Tkinter.Button(win, text ="Add Selected Items", command = addSelected)
add_selection.pack(side='top')
show_ingredients = Tkinter.Button(win, text = "Show Ingredients", command = showIngredients)
show_ingredients.pack(side='top')
new_recipe = Tkinter.Button(win, text ="Add a New Recipe", command = newRecipe)
new_recipe.pack(side='top')

new_name_box = Text(win, width=25,height=1);
new_name_box.pack(side='bottom')

dinnerbox = Tkinter.Listbox(win, width=50,height=30)
dinnerbox.pack(side='left')
ingredbox = Tkinter.Listbox(win, width=50,height=30)
ingredbox.pack(side='right')
chosenbox = Tkinter.Listbox(win, width=50,height=30)
chosenbox.pack(side='right')

ingredbox_sb = Tkinter.Scrollbar(win,orient=VERTICAL)
ingredbox_sb.pack(side=LEFT,fill=Y)
ingredbox_sb.configure(command=ingredbox.yview)
ingredbox.configure(yscrollcommand=ingredbox_sb.set)


win.mainloop()

