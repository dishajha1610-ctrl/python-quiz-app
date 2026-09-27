# python-quiz-app

## Project overview

The Python Quiz App is a command-line program for practising Python concepts. A student enters a name and answers 10 multiple-choice questions. The app checks each answer, rejects invalid answer letters, calculates the final score and percentage, and displays a remark based on the result.

The question bank covers list references, list comprehensions, floor division, slicing, dictionaries, default function arguments, `finally`, `enumerate`, Boolean conversion, and shallow copies.

## Features

- 10 multiple-choice Python questions, each with four options
- Name prompt, with `Student` used when the name is left blank
- Case-insensitive answer letters (`a` and `A` are both accepted)
- Input validation for answers outside A, B, C, or D
- Immediate correct/incorrect feedback
- Final score, percentage, and performance remark

## Requirements

- Python 3.10 or newer
- A terminal or command prompt
- No third-party packages are required; the program uses only Python's built-in features

## Setup

1. Download or clone this repository, or copy the project folder to your computer.
2. Open the project folder. It should contain `main.py`.
3. Install Python 3.10 or newer if it is not already installed. During Windows installation, enable **Add Python to PATH** if that option is shown.
4. (Optional) To edit the project, open the folder in Visual Studio Code. The Microsoft Python extension can provide Python editing and run support, but it is not needed to run the app from a terminal.
5. No dependency installation or configuration file is needed.

## Run the project

Open a terminal in the folder containing `main.py`, then run one of these commands:

**Windows:**

```powershell
python main.py
```

If `python` is not recognized, try:

```powershell
py main.py
```

**macOS or Linux:**

```bash
python3 main.py
```

Enter your name when prompted, then answer each question by typing A, B, C, or D and pressing Enter. At the end, the app displays your score, percentage, and a remark. To play again, run the command again.

## Configuration

There is no separate configuration file. The questions and answer keys are stored in the `questions` list inside `main.py`. To edit a question, update its `question`, `choices`, and `answer` values together. The `answer` must be the letter for the matching choice. The current program expects four choices labeled A through D.

## Project files

```text
quiz-app-python/
├── main.py       # Quiz questions, input handling, scoring, and results
└── README.md     # Project description and setup guide
```

## Testing

When checking the app, try a correct answer, an incorrect answer, a lowercase answer such as `b`, an invalid entry such as `X`, and a blank name. Confirm that the app rejects invalid answer letters, finishes all 10 questions, and prints a score and remark.

## Limitations and possible improvements

This version runs one quiz category in the terminal. Results are not saved after the program closes. Possible improvements include adding categories, explanations for each answer, saved score history, and a graphical interface.
