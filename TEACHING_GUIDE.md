# Quick Reference Guide for Instructors

## Running the Demos

Each demo can be run independently:
```bash
python demo1_basics.py
python demo2_variables.py
python demo3_functions.py
python demo4_lists.py
python demo5_classes.py
```

## Teaching Flow (45-60 minutes)

### Introduction (5 minutes)
- Explain what Pygame is: a library for making games and graphics
- Show that Python can create interactive, visual programs
- Mention that games are great for learning programming concepts

### Demo 1: Basics (10 minutes)
**Show:** Loops and conditionals
- Point out the `while` loop that keeps the game running
- Explain the `for` loop that checks events
- Show how `if/else` makes decisions
- **Interactive:** Have students change colors, add shapes
- **Key Quote:** "Every game has a loop that runs forever until you quit"

### Demo 2: Variables (8 minutes)
**Show:** Different data types and math
- Explain variables store information
- Show different types: numbers, decimals, tuples
- Demonstrate how math updates position
- **Interactive:** Change speed, radius, or direction
- **Key Quote:** "Variables are like boxes that hold information"

### Demo 3: Functions (10 minutes)
**Show:** Reusable code
- Explain functions are named blocks of code
- Show how parameters pass information in
- Demonstrate `return` gives something back
- **Interactive:** Add a new shape function
- **Key Quote:** "Functions let you write code once and use it many times"

### Demo 4: Lists (10 minutes)
**Show:** Collections of data
- Explain lists hold multiple items
- Show `.append()` adds to the list
- Demonstrate looping through lists
- **Interactive:** Modify circle properties
- **Key Quote:** "Lists are like shopping lists - ordered collections of items"

### Demo 5: Classes (15 minutes)
**Show:** Object-oriented programming
- Explain classes are blueprints for objects
- Show `__init__` sets up each object
- Demonstrate methods are functions inside classes
- Show `self` refers to the current object
- **Interactive:** Add gravity or new behaviors
- **Key Quote:** "Classes let you create your own custom types of things"

### Wrap-up (2-5 minutes)
- Review progression: basics → variables → functions → lists → classes
- Each concept builds on previous ones
- Encourage students to modify and experiment
- Share resources for learning more

## Common Student Questions

**Q: Why do we need `pygame.init()`?**
A: It starts up all the pygame systems (graphics, sound, etc.)

**Q: What's the difference between `screen.fill()` and `pygame.draw.circle()`?**
A: `fill()` colors the entire screen, `draw` adds shapes on top

**Q: Why is there a `clock.tick(60)` in some demos?**
A: It limits the game to 60 frames per second, making movement smooth and consistent

**Q: What does `self` mean in classes?**
A: `self` refers to the specific object you're working with - "myself"

**Q: Can I make a real game with this?**
A: Yes! These are the same concepts used in real games, just simplified

## Troubleshooting

**Problem:** "Module not found: pygame"
**Solution:** Run `pip install pygame` in the terminal

**Problem:** Window opens but closes immediately
**Solution:** Make sure you're running the full script, not selecting partial code

**Problem:** Nothing responds to clicks/keys
**Solution:** The window needs to be in focus (click on it first)

## Extension Ideas

For advanced students who finish early:
1. Add sound effects (pygame.mixer)
2. Load and display images (pygame.image.load)
3. Add collision detection between objects
4. Create a simple game (catch falling objects, etc.)
5. Add a score counter
6. Implement gravity and physics

## Code Modification Exercises

### Easy:
- Change colors to your favorites
- Make things move faster/slower
- Add more shapes or objects
- Change window size

### Medium:
- Add keyboard controls (arrow keys)
- Make objects change size
- Add text displaying game information
- Create color gradients

### Hard:
- Implement collision detection
- Add boundaries and walls
- Create particle effects
- Make objects accelerate/decelerate
