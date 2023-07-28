from sketchpy import canvas
import turtle

if __name__ == "__main__":
    obj = canvas.sketch_from_image(r"C:\Users\Farsaram\Desktop\project\desktop-wallpaper-veer-tejaji-teja-ji.jpg")

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.title("path sketch")

    t = turtle.Turtle()

    for i in obj.draw():
        action, value = i

    turtle.done()
