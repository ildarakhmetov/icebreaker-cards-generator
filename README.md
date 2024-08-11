# Icebreaker Cards Generator

This is a Python script that generates random cards for a classroom icebreaker. It's a fun and interactive way to form random groups and get to know each other.

## Icebreaker Structure

The idea is to randomly "mix" students into groups several times, each time with a different groups of people. The goal is to get students to interact with as many people as possible. The icebreaker is structured as follows:

1. Each students gets a card containing a programming language, a Linux distribution, and a computer science pioneer.
2. In the first mix, students are asked to find other students with the same programming language. They then form a group with those students.
3. Once in groups, students are posed a question (e.g., "What are your expectations for this course?", "If you could use a time machine, where would you travel?") and are given a few minutes to discuss it.
4. Students are remixed and asked to find other students with the same Linux distribution, and get a new question to discuss. This is repeated for the computer science pioneer.


## Installation

1. Clone this repository to your local machine using.
2. Navigate to the project directory.
3. Install the required packages using pip:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Before running the script, you can customize the questions on the cards by modifying the `config.py` file. The `config.py` file contains the following variables:

- `LANGUAGES`: A list of programming languages.
- `DISTRIBUTIONS`: A list of Linux distributions.
- `PIONEERS`: A list of computer science pioneers.
- `NUM_STUDENTS`: The number of students in the class.

To run the script, navigate to the project directory and run the following command:

```bash
python generate_cards.py
```

This will generate a set of random icebreaker cards. You can customize the number of cards and the questions on the cards by modifying the script.

Print the cards and cut them out. 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)