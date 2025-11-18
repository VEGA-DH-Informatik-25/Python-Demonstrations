# Python-Demonstrations
Short demonstration codes for Studieninfotag

## Pygame Demonstrations for New Students

These are short, interactive Python programs using Pygame to demonstrate core Python concepts. Each demo is self-contained and focuses on specific programming features.

### Prerequisites
```bash
pip install pygame
```

### Demo 1: Basics - Loops and Conditionals (`demo1_basics.py`)
**Concepts:** `while` loops, `for` loops, `if/else` conditionals

**What it does:** Creates a window with a white circle. Press SPACE to toggle background color between blue and red.

**Key Learning Points:**
- `while running:` - Game loop that runs continuously
- `for event in pygame.event.get():` - Loop through all events
- `if event.type == pygame.QUIT:` - Check conditions
- RGB color tuples like `(255, 255, 255)` for white

**Run it:**
```bash
python demo1_basics.py
```

---

### Demo 2: Variables and Data Types (`demo2_variables.py`)
**Concepts:** Variables, integers, floats, tuples, mathematical operations

**What it does:** A red circle bounces horizontally across the screen. The position is shown at the top.

**Key Learning Points:**
- `x = 50` - Integer variable
- `y = 300.0` - Float variable  
- `color = (255, 0, 0)` - Tuple (RGB values)
- `x = x + speed` - Updating variables with math
- `direction * -1` - Reversing direction

**Run it:**
```bash
python demo2_variables.py
```

---

### Demo 3: Functions (`demo3_functions.py`)
**Concepts:** Function definition, parameters, return values, reusable code

**What it does:** Shows a red circle and blue square. Click anywhere to randomly change their colors.

**Key Learning Points:**
- `def function_name(parameters):` - Define a function
- `return value` - Return something from a function
- `draw_circle(screen, color, x, y, radius)` - Calling functions with arguments
- Functions make code reusable and organized

**Run it:**
```bash
python demo3_functions.py
```

---

### Demo 4: Lists and Iteration (`demo4_lists.py`)
**Concepts:** Lists, `.append()`, `for` loops, `len()`, list indexing

**What it does:** Starts with 5 random circles. Click to add more circles to the screen.

**Key Learning Points:**
- `circles = []` - Empty list
- `circles.append(item)` - Add items to a list
- `for circle in circles:` - Loop through each item in a list
- `len(circles)` - Get the number of items in a list
- Lists can hold dictionaries with multiple properties

**Run it:**
```bash
python demo4_lists.py
```

---

### Demo 5: Classes and Object-Oriented Programming (`demo5_classes.py`)
**Concepts:** Classes, objects, `__init__`, methods, `self`, OOP

**What it does:** Multiple colored balls bounce around the screen. Click to add a new ball at the mouse position.

**Key Learning Points:**
- `class Ball:` - Define a class (blueprint for objects)
- `def __init__(self, x, y):` - Constructor runs when creating an object
- `self.x`, `self.y` - Instance variables (each object has its own)
- `def move(self):` - Methods are functions inside a class
- `ball = Ball(100, 200)` - Create an object from a class
- Objects encapsulate data and behavior together

**Run it:**
```bash
python demo5_classes.py
```

---

## Teaching Tips

1. **Start Simple:** Begin with Demo 1 to show the basic structure of a Pygame program
2. **Build Up:** Each demo introduces one or two new concepts while reinforcing previous ones
3. **Interactive:** All demos are interactive - students can modify values and see immediate results
4. **Short Code:** Each demo is under 70 lines, making it easy to read and understand
5. **Comments:** Code includes explanatory comments for students to follow along

## Modifications Students Can Try

- **Demo 1:** Change colors, add more shapes, add keyboard controls
- **Demo 2:** Change speed, add vertical movement, change size
- **Demo 3:** Add more shapes, create new drawing functions, add sounds
- **Demo 4:** Change circle properties, add removal on click, animate circles
- **Demo 5:** Add collision detection, change physics, add trails

---

## Common Pygame Concepts

All demos use these common patterns:

```python
import pygame
import sys

pygame.init()  # Start pygame
screen = pygame.display.set_mode((width, height))  # Create window

running = True
while running:  # Game loop
    for event in pygame.event.get():  # Handle events
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(color)  # Clear screen
    # Draw things here
    pygame.display.flip()  # Update display

pygame.quit()
sys.exit()
```
