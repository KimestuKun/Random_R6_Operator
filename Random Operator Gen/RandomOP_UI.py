# Import tkinter | Think of 'tk' as toolkit
# tkinter is the std Python GUI library used to create GUI's. Its usually pre installed in standard python.
# Once tkinter was imported we renamed it as tk
import operators
import random
import tkinter as tk


# Define function (this runs when button is clicked)
# Button clicked -> run function -> update label text
def attackerButton():
    # Prints when attacker button is chosen
    result = random.randint(0 , len(operators.operatorA)-1)
    chosenOperator = operators.operatorA[result]
    # Prints operator and number
    resultLabel.config(text = f'Your Operator for the round is: \n{chosenOperator}')

def defenderButton():
    # Prints when defender button is chosen
    result = random.randint(0 , len(operators.operatorD)-1)
    chosenOperator = operators.operatorD[result]
    # Prints operator and number
    resultLabel.config(text = f'Your Operator for the round is: \n{chosenOperator}')

def quitButton():
    # Prints when quit button is chosen
    displayLabel.config(text="Quit Test")
    # Exits out of window
    window.destroy()

# Create the window
window = tk.Tk()

# Set the window size: ('Width x Height')
window.geometry("400x500")

# Create label which label = text display element
displayLabel = tk.Label(window, text="Choose one:")
# Position label
displayLabel.place(x=90, y=150)

# Create button: Making a clickable UI button
# Create an attacker choice button
buttonA = tk.Button(window)
# Button properties
buttonA["text"] = "Attacker"
# This means: when button clicked -> run function_name()
buttonA["command"] = attackerButton
# Position button
buttonA.place(x=110, y=200)

# Create an defender choice button
buttonB = tk.Button(window)
# Button properties
buttonB["text"] = "Defender"
# This means: when button clicked -> run function_name()
buttonB["command"] = defenderButton
# Position Button
buttonB.place(x=110, y=230)


buttonC = tk.Button(window)
# Button properties
buttonC["text"] = "Quit"
# This means: when button clicked -> run function_name()
buttonC["command"] = quitButton
# Position Button
buttonC.place(x=110, y=260)

# Create a result label
resultLabel = tk.Label(window, text = 'Your operator will appear here')
resultLabel.place(x = 110 , y = 100)

# Starts the UI loop     
window.mainloop()