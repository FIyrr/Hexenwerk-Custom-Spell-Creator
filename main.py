import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter.colorchooser import askcolor
from PIL import ImageTk, Image

def get_rgb_values(color):
    return tuple(int(val * 255) for val in color)

def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    r, g, b = get_rgb_values(colors[0])
    print(str(r/255)+","+str(b/255)+","+str(g/255))
    decimal_value_calc = (int(r/255) << 16) | (int(g/255) << 8) | int(b/255)
    decimal_value.set(decimal_value_calc)
    canvas_color.itemconfig(square, fill=colors[1])

def change_color_hex():
    colors = askcolor(title="Tkinter Color Chooser")
    r, g, b = get_rgb_values(colors[0])
    print(str(r/255)+","+str(b/255)+","+str(g/255))
    hex_value_calc = '#%02x%02x%02x' % (int(r/255), int(g/255), int(b/255))
    hex_value.set(hex_value_calc)
    canvas_color_display.itemconfig(square, fill=colors[1])
    
def generate_spell():
    spell_name = input_spell_name.get()
    spell_color_display = hex_value.get()
    spell_color = decimal_value.get()
    mana_cost = input_mana_cost.get()
    spell_id = input_spell_id.get()
    start_raycast = input_start_raycast.get()
    block_collision_command = input_block_collision.get()
    entity_collision_command_caster = input_entity_collision_as_player.get()
    entity_collision_command_target = input_entity_collision_as_target.get()
    on_cast = input_on_cast.get()
    on_block_traveled = input_on_raycast_step.get()
    # Change state to 'normal' to allow modifications
    output_field.config(state='normal')

    # Clear existing text
    output_field.delete(1.0, 'end')

    # Update the text
    output_field.insert('1.0',f'/give @p minecraft:leather_horse_armor{{\n'
                    f'    display:{{\n'
                    f'        Name:\'{{"translate":"item.hexenwerk.spellbook","color":"#62DEDE","italic":false}}\',\n'
                    f'        Lore:[\'{{"text":"{spell_name}","color":"{spell_color_display}","italic":false}}\'],\n'
                    f'        color: {spell_color}\n'
                    f'    }},\n'
                    f'    CustomModelData: 1800,\n'
                    f'    hexenwerk-spellbook: 1b,\n'
                    f'    hexenwerk-contained_spell: -2,\n'
                    f'    hexenwerk-lore_display: \'{{"text":"\u2022 {spell_name}","color":"{spell_color_display}","italic":false}}\',\n'
                    f'    hexenwerk-chat_display: \'{{"text":"{spell_name}","color":"{spell_color_display}","italic":false}}\',\n'
                    f'    hexenwerk-mana_cost: {mana_cost},\n'
                    f'    hexenwerk-spell_data:{{\n'
                    f'        book_color: {spell_color},\n'
                    f'        start_raycast: {start_raycast},\n'
                    f'        events:{{\n'
                    f'            on_block_collision: "{block_collision_command}",\n'
                    f'            on_entity_collision:{{\n'
                    f'                as_player: "{entity_collision_command_caster}",\n'
                    f'                as_target: "{entity_collision_command_target}"\n'
                    f'            }},\n'
                    f'            on_cast: "{on_cast}",\n'
                    f'            on_raycast_travel: "{on_block_traveled}"\n'
                    f'        }}\n'
                    f'    }},\n'
                    f'    HideFlags:64\n'
                    f'}}')
    
    output_field.config(state='disabled')
    
# window
window = tk.Tk()
window.title('Hexenwerk Custom Spell Creator')
window.geometry("1400x950")
window.resizable(width=False, height=False)
window.iconphoto(True, PhotoImage(file="assets/icon.png"))
window.configure(bg='#D2CBF2')

# inputs
inputs_frame = tk.Frame(master=window, background='#D2CBF2')
inputs_frame.grid(row=0, column=0, padx=10, pady=10)

## name
input_spell_name_text = ttk.Label(master=inputs_frame, text="Name (str)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_spell_name_text.grid(row=0, column=0, sticky="w", pady=(5, 0))

input_spell_name = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_spell_name.grid(row=1, column=0, pady=2, padx=4, sticky="w")

## color

input_spell_color_text = ttk.Label(master=inputs_frame, text="Book Color", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_spell_color_text.grid(row=2, column=0, sticky="w", pady=(10, 0))

decimal_value = tk.StringVar()
entry_decimal_value = ttk.Entry(master=inputs_frame, textvariable=decimal_value, font="Noto-Sans-Lisu 14", state='readonly')
entry_decimal_value.grid(row=3, column=0, pady=5, sticky="w")

canvas_color = tk.Canvas(master=inputs_frame, width=20, height=20, background='#D2CBF2')
canvas_color.grid(row=3, column=1, sticky="w")
square = canvas_color.create_rectangle(0, 0, 20, 20, fill='blue')

button_colorpicker = ttk.Button(master=inputs_frame, text='Click to set color', command=change_color, width=15)
button_colorpicker.grid(row=3, column=2, pady=2, padx=4, sticky="w")

## color display

input_spell_color_display_text = ttk.Label(master=inputs_frame, text="Color", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_spell_color_display_text.grid(row=4, column=0, sticky="w", pady=(10, 0))

hex_value = tk.StringVar()
entry_hex_value = ttk.Entry(master=inputs_frame, textvariable=hex_value, font="Noto-Sans-Lisu 14", state='readonly')
entry_hex_value.grid(row=5, column=0, pady=5, sticky="w")

canvas_color_display = tk.Canvas(master=inputs_frame, width=20, height=20, background='#D2CBF2')
canvas_color_display.grid(row=5, column=1, sticky="w")
square = canvas_color_display.create_rectangle(0, 0, 20, 20, fill='blue')

button_color_displaypicker = ttk.Button(master=inputs_frame, text='Click to set color_display', command=change_color_hex, width=15)
button_color_displaypicker.grid(row=5, column=2, pady=2, padx=4, sticky="w")

## mana cost
input_mana_cost_text = ttk.Label(master=inputs_frame, text="Mana Cost (int)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_mana_cost_text.grid(row=6, column=0, sticky="w", pady=(10, 0))

input_mana_cost = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_mana_cost.grid(row=7, column=0, pady=2, padx=4, sticky="w")

## spell id
input_spell_id_text = ttk.Label(master=inputs_frame, text="Spell ID (str)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_spell_id_text.grid(row=8, column=0, sticky="w", pady=(10, 0))

input_spell_id = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_spell_id.grid(row=9, column=0, pady=2, padx=4, sticky="w")

## start raycast
input_start_raycast_text = ttk.Label(master=inputs_frame, text="Start Raycast (true/false)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_start_raycast_text.grid(row=10, column=0, sticky="w", pady=(10, 0))

input_start_raycast = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_start_raycast.grid(row=11, column=0, pady=2, padx=4, sticky="w")

## on block collision
input_block_collision_text = ttk.Label(master=inputs_frame, text="Block Collision Command", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_block_collision_text.grid(row=12, column=0, sticky="w", pady=(10, 0))

input_block_collision = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_block_collision.grid(row=13, column=0, pady=2, padx=4, sticky="w")

## on entity collision as player
input_entity_collision_as_player_text = ttk.Label(master=inputs_frame, text="Entity Collision Command (As Player)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_entity_collision_as_player_text.grid(row=14, column=0, sticky="w", pady=(10, 0))

input_entity_collision_as_player = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_entity_collision_as_player.grid(row=15, column=0, pady=2, padx=4, sticky="w")

## on entity collision as victim
input_entity_collision_as_target_text = ttk.Label(master=inputs_frame, text="Entity Collision Command (As Target)", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_entity_collision_as_target_text.grid(row=16, column=0, sticky="w", pady=(10, 0))

input_entity_collision_as_target = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_entity_collision_as_target.grid(row=17, column=0, pady=2, padx=4, sticky="w")

## on cast
input_on_cast_text = ttk.Label(master=inputs_frame, text="Cast Command", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_on_cast_text.grid(row=18, column=0, sticky="w", pady=(10, 0))

input_on_cast = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_on_cast.grid(row=19, column=0, pady=2, padx=4, sticky="w")

## on raycast step
input_on_raycast_step_text = ttk.Label(master=inputs_frame, text="On Raycast Step Command", font="Noto-Sans-Lisu 17", background='#D2CBF2')
input_on_raycast_step_text.grid(row=20, column=0, sticky="w", pady=(10, 0))

input_on_raycast_step = ttk.Entry(master=inputs_frame, font="Noto-Sans-Lisu 15")
input_on_raycast_step.grid(row=21, column=0, pady=2, padx=4, sticky="w")


# output field
output_text = tk.StringVar()
output_field = tk.Text(master=window, wrap='word', font="Noto-Sans-Lisu 12", height=30, state='normal',width=80)
output_field.grid(row=0, column=1)

# generate button
generate_button = ttk.Button(master=window, text='Generate /give Command', command=generate_spell, width=20)
generate_button.grid(row=1, column=1, columnspan=1, pady=10)

# image
# img = ImageTk.PhotoImage(Image.open("assets/custom.png"))
# preview_label = ttk.Label(window,image=img)
# preview_label.grid(row=3, column=0, padx=10, pady=10)

# loop
window.mainloop()