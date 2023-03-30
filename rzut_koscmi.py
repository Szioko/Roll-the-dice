#!/usr/bin/env python
# coding: utf-8

# In[70]:


import random


# # 1. pobierz dane od urzytkownika

# In[71]:


num_dice_input = input('Ile razy chcesz rzucic kością? [ 1 - 6]')


# In[72]:


def parse_input(input_string):
    """
    Zwrocic int pomiedzy wartosciami 1 do 6.
    
    Sprawdza czy dana wejsciowa jest intigerpomiedzy 1 i 6.
    
    """
    
    if input_string.strip() in {'1' , '2', '3', '4', '5', '6'}:
        return int(input_string)
    else:
        print("Proszę podaj wartość z przedziału 1 - 6.")
        raise SystemExit(1)


# 
# #  2. rzucanie kosciami

# In[74]:


import random

def roll_dice(num_dice):
    """Zwraca liste into dlugości num_dice
    
    Każda wartośc musi zawierac sie wprzedziale 1 - 6 .
    
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1,6)
        roll_results.append(roll)
    return roll_results

num_dice = parse_input(num_dice_input)


# In[75]:


# dekoracje
roll_results = roll_dice(num_dice)
print(roll_results)


# # 3. definijemy grafike

# In[76]:


DICE_ART = {
1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),       
}

DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "


# In[77]:


# GENERUJEMY FACE KOSCI ZGODNIE Z WARTOSCIAMI INPUT

def generate_dice_face_diagram(dice_values):
    """
    Zwraca diagram rzutu koscmi zgodnie z wartościami dice_values
    
    e.g. dla rzutu dice_values = [3,1] zwroci wynik:
    
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
        "┌─────────┐", 
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    
    """
    
    # generujemy liste face dice (graficzny obraz rziconych kosci) ze słownika DICE_ART
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
        
     # generujemy liste wierszy, ktore wyswietla profil kosci / face dice
    dice_face_rows = []
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_face_rows.append(row_string)
            
      # nagłówek z wynikiem rzutu kości
    width = len(dice_face_rows[0])
    diagram_header = " WYNIK ".center(width, '-')
    
    # polączony nagłówek z tablica wylosowanych kosci
    dice_face_diagram = '\n'.join([diagram_header] + dice_face_rows)
    return dice_face_diagram 

    


# In[78]:


dice_face_diagram = generate_dice_face_diagram(roll_results)


# In[79]:


print(f'\n{dice_face_diagram}')

