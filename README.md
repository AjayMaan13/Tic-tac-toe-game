# 🎮 Tic-Tac-Toe Game

[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Game](https://img.shields.io/badge/Game-CLI-brightgreen)](https://en.wikipedia.org/wiki/Tic-tac-toe)

> **Interactive command-line Tic-Tac-Toe game built with Python, featuring dynamic board display and intelligent win detection**

---

## 🔍 Overview

A fully functional Tic-Tac-Toe game implemented in Python with an intuitive command-line interface. Features dynamic board rendering, input validation, comprehensive win detection, and a clean, modular code structure.

**Developer:** Ajaypartap Singh Maan  
**Contact:** ajayapsmaanm13@gmail.com  

---

## 🛠️ Technologies & Skills

### **Core Technologies**
- **Python 3** - Object-oriented programming and game logic
- **CLI Interface** - User-friendly command-line interaction
- **Data Structures** - Lists, dictionaries, and nested arrays

### **Programming Concepts**
- **Game Logic Implementation** - Turn-based gameplay mechanics
- **Input Validation** - Robust error handling for user input
- **Win Detection Algorithm** - Comprehensive checking for all win conditions
- **Dynamic Board Display** - Real-time game state visualization

---

## ✨ Key Features

### **🎯 Intelligent Game Logic**
- **Player Selection** - Choose X or O at game start
- **Turn Management** - Alternating player turns with clear indicators
- **Position Validation** - Prevents invalid moves and occupied spaces
- **Win Detection** - Checks all possible winning combinations

### **🖥️ User Interface**
- **Dynamic Board Display** - Visual game board with clear formatting
- **Position Guide** - Numbered grid showing available moves
- **Real-time Updates** - Board updates after each move
- **Clear Feedback** - Win announcements and game status

### **🔧 Code Architecture**
- **Modular Functions** - Separated concerns for maintability
- **Global State Management** - Efficient game state tracking
- **Dictionary Mapping** - Position-to-coordinate conversion
- **Clean Data Structures** - Organized board representation

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/tic-tac-toe-game.git
cd tic-tac-toe-game

# Run the game
python main.py
```

---

## 🎮 Gameplay Example

```
Player1 choose x or o: X
Player 1 chooses- X and Player 2 chooses- O

   |   |  
---------
   |   |  
---------
   |   |  

1  | 2  | 3 
---------
4  | 5  | 6 
---------
7  | 8  | 9 

Please choose your marker place from 1-9: 5

   |   |  
---------
   | X |  
---------
   |   |  
```

---

## 🏗️ Technical Implementation

### **Board Representation**
```python
# Game board with dynamic updates
list1 = [['  |', '  |', ' '],
         ['  |', '  |', ' '],
         ['  |', '  |', ' ']]

# Position mapping for user-friendly input
board_place_dict = {
    1: [0, 0], 2: [0, 1], 3: [0, 2],
    4: [1, 0], 5: [1, 1], 6: [1, 2],
    7: [2, 0], 8: [2, 1], 9: [2, 2]
}
```

### **Win Detection Algorithm**
```python
def check_win():
    # Horizontal wins
    if list1[0][0] == list1[0][1] == list1[0][2] + ' |':
        return declare_winner()
    
    # Vertical wins
    elif list1[0][0] == list1[1][0] == list1[2][0]:
        return declare_winner()
    
    # Diagonal wins
    elif list1[0][0] == list1[1][1] == list1[2][2] + ' |':
        return declare_winner()
```

### **Input Validation**
```python
def take_input():
    while choice_game == False:
        input1 = int(input('Choose position 1-9: '))
        if input1 in board_place:
            board_place.remove(input1)
            return
        else:
            print('Position already taken or invalid!')
```

---

## 🎯 Skills Demonstrated

### **Python Programming**
- **Function Design** - Modular, reusable functions
- **Data Structures** - Lists, dictionaries, nested arrays
- **Control Flow** - While loops, conditional statements
- **Global Variables** - Proper state management

### **Game Development**
- **Turn-Based Logic** - Player alternation system
- **Win Condition Checking** - All possible win scenarios
- **Board State Management** - Dynamic updates and validation
- **User Experience** - Clear prompts and feedback

### **Problem Solving**
- **Algorithm Design** - Efficient win detection
- **Input Handling** - Robust validation and error prevention
- **String Manipulation** - Board formatting and display
- **Edge Case Handling** - Draw conditions and invalid inputs

---

## 🔧 Future Enhancements

- **AI Opponent** - Single-player mode with computer AI
- **GUI Version** - Tkinter or Pygame implementation
- **Score Tracking** - Best-of-three tournament mode
- **Customizable Board** - Different board sizes (4x4, 5x5)
- **Network Play** - Multiplayer over network
- **Difficulty Levels** - Easy, medium, hard AI opponents

---

## 🎨 Code Quality Features

- **Clean Functions** - Single responsibility principle
- **Descriptive Names** - Clear variable and function naming
- **Input Validation** - Prevents crashes from invalid input
- **Error Handling** - Graceful handling of edge cases
- **Modular Design** - Easy to extend and modify

---

## 📞 Contact

**Ajaypartap Singh Maan**  
📧 ajayapsmaanm13@gmail.com  
💼 [LinkedIn](https://linkedin.com/in/ajaypartap-singh-maan)  
🐙 [GitHub](https://github.com/AjayMaan13)  

---

## 🏷️ Tags

`Python` `Game Development` `CLI Application` `Algorithm Implementation` `Object-Oriented Programming` `Interactive Interface` `Logic Programming`

---

*A solid foundation in Python programming and game logic development*
