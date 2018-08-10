from guizero import App, Text, TextBox

app = App(title="Raspberry")

welcome_message = Text(app, text="Raspberry")
my_name = TextBox(app)

app.display()
