# Flash Card App using Tkinter
The Flash Card App using Tkinter is a Python application designed to help users learn and remember concepts or information using flash cards. The application creates a digital version of traditional flash cards, where users are presented with questions (in this case, words) and can reveal the answers, mark their correctness, and proceed to the next card.

# Features
Interactive flash card interface to display questions and answers.

Ability to mark whether the answer was correct or incorrect.

Automatic card flipping to reveal the answer after a short delay.

Persistence of progress through saving learned words to a CSV file.

# Usage
1. Make sure you have Python and the Tkinter library installed on your system.

2. Download or copy the provided code into a Python file (e.g., flash_card_app.py).

3. Ensure that the data folder containing the CSV files and the images folder with card images are in the same directory as the main file.

4. Open a terminal or command prompt and navigate to the directory where the Python file is located.

5. Run the app by executing the following command:

        python flash_card_app.py

6. The app window will appear with the first flash card displayed. The question will be in French, and you can click the "✓" button to mark the answer as correct or the "✗" button to mark it as incorrect.

7. After marking, the app will automatically proceed to the next flash card after a brief delay (3 seconds).

8. You can continue marking flash cards until there are no more cards left to learn.

# Customization and Extensibility
To customize the flash card content, you can replace the provided CSV files (french_words.csv and words_to_learn.csv) with your own datasets. 

Each row should contain the question and answer pairs.

You can modify the appearance of the app, such as fonts, colors, and layout, to match your preferences.

# Note
This app is designed for educational purposes and as a demonstration of creating interactive applications using Tkinter. 

It is not meant to cover all possible features of a complete flash card application.

The provided code does not include extensive error handling or input validation. In a production setting, you would want to implement proper error handling to ensure the application behaves as expected.

# Author
This Flash Card App using Tkinter was created by Chris Schinner.

Feel free to modify, enhance, and experiment with the app to suit your learning needs. Enjoy your flash card learning experience!
