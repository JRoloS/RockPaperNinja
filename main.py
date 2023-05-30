import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

kivy.require('1.11.1')


class RockPaperNinjaApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')

        # Set the title of the app
        self.title = "Rock, Paper, Ninja"

        # Create an anchor layout for the picture
        self.anchor_layout = AnchorLayout(anchor_x='center', anchor_y='top')

        # Add an image to the anchor layout
        self.image = Image(source='media/title.jpg')
        self.anchor_layout.add_widget(self.image)

        # Create a box layout for the buttons
        self.button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))

        # Create buttons with labels
        self.rock_button = Button(text="Rock")
        self.paper_button = Button(text="Paper")
        self.scissors_button = Button(text="Scissors")

        # Bind button press events to compare choices
        self.rock_button.bind(on_press=self.compare_choices)
        self.paper_button.bind(on_press=self.compare_choices)
        self.scissors_button.bind(on_press=self.compare_choices)

        # Add buttons to the button layout
        self.button_layout.add_widget(self.rock_button)
        self.button_layout.add_widget(self.paper_button)
        self.button_layout.add_widget(self.scissors_button)

        # Create label to display computer's choice
        self.result_label = Label(text="", size_hint=(1, 0.1))

        # Add layouts and label to the main layout
        self.layout.add_widget(self.anchor_layout)
        self.layout.add_widget(self.button_layout)
        self.layout.add_widget(self.result_label)

        return self.layout

    def compare_choices(self, button):
        choices = ['rock', 'paper', 'scissors']
        player_choice = button.text.lower()
        function_choice = random.choice(choices)

        result = ''
        if player_choice == function_choice:
            result = 'tie.png'
        elif (player_choice == 'rock' and function_choice == 'scissors') or \
                (player_choice == 'paper' and function_choice == 'rock') or \
                (player_choice == 'scissors' and function_choice == 'paper'):
            result = 'win.jpg'
        else:
            result = 'lose.jpg'

        self.image.source = f'media/{result}'  # Update the image source

        # Update the result label
        self.result_label.text = f"Computer's Choice: {function_choice.capitalize()}"

        # Remove previous buttons
        self.button_layout.clear_widgets()

        # Create "Play Again" button
        play_again_button = Button(text="Play Again", size_hint=(0.3, 0.1))
        play_again_button.bind(on_press=self.restart_program)

        # Add "Play Again" button to the layout
        self.layout.add_widget(play_again_button)

    def restart_program(self, button):
        self.image.source = 'media/title.jpg'  # Reset the image source
        self.layout.remove_widget(button)  # Remove the "Play Again" button from the layout
        self.button_layout.clear_widgets()  # Clear previous buttons

        # Create new buttons with labels
        self.rock_button = Button(text="Rock")
        self.paper_button = Button(text="Paper")
        self.scissors_button = Button(text="Scissors")

        # Bind button press events to compare choices
        self.rock_button.bind(on_press=self.compare_choices)
        self.paper_button.bind(on_press=self.compare_choices)
        self.scissors_button.bind(on_press=self.compare_choices)

        # Add buttons to the button layout
        self.button_layout.add_widget(self.rock_button)
        self.button_layout.add_widget(self.paper_button)
        self.button_layout.add_widget(self.scissors_button)

        # Hide the result label
        self.result_label.text = ""


if __name__ == '__main__':
    RockPaperNinjaApp().run()
