import turtle  # Import the turtle module for drawing

def draw_tree(branch_len, t):  
    if branch_len > 5:  # Stop drawing when branches become too small
        t.pensize(branch_len // 10)  # Make thicker branches at the base
        t.forward(branch_len)  # Move forward to draw the branch
        
        t.left(30)  # Turn left to draw the left subtree
        draw_tree(branch_len - 15, t)  # Recursively draw a smaller left branch
        
        t.right(60)  # Turn right to draw the right subtree
        draw_tree(branch_len - 15, t)  # Recursively draw a smaller right branch
        
        t.left(30)  # Reset the angle
        t.backward(branch_len)  # Move back to the starting position

# Set up the turtle environment
turtle.bgcolor("black")  # Change background to black for better contrast
t = turtle.Turtle()  # Create a turtle object
t.color("lime")  # Set branch color to green (lime)
t.speed(0)  # Set maximum drawing speed
t.left(90)  # Turn the turtle to face upwards
t.up(); t.backward(100); t.down()  # Move turtle down to position tree trunk

draw_tree(100, t)  # Start drawing the tree with an initial branch length of 100

turtle.done()  # Finish the turtle drawing process
