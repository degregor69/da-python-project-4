# Chess Tournament Manager

Chess Tournament Manager is a Python application designed to manage tournaments, rounds, matches, and player scores.

## Key Features

- Add players with full name, birthdate and chess national id
- Manage tournaments with a defined number of rounds.
- Automatically generate matches for each round.
- Assign scores for each match.
- Track the progress of the tournament.

---

## Installation

### Prerequisites

- Python 3 installed on your machine.

### Steps

1. **Clone the repository:**  
   Clone this project to your local machine.

   ```bash
   git clone https://github.com/degregor69/da-python-project-4.git
   cd da-python-project-4
   ```

2. **Create a virtual environment:**  
   Create a virtual environment named `venv` in the project directory.  

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment:**

   - **On Linux/MacOS:**
     ```bash
     source venv/bin/activate
     ```
   - **On Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Install dependencies:**  
   Use the `requirements.txt` file to install the necessary packages.  

   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

1. **Navigate to the `app` folder:**  
   Move to the directory containing the `main.py` file.

   ```bash
   cd app
   ```

2. **Run the application:**  
   Execute the main script.

   ```bash
   python3 main.py
   ```

---

## Generate a flake8 report

1. **Navigate to the `da-python-project-4` folder:**  
   Move to the directory containing the `app` folder.

   If you're in the app folder : 
   ```bash
   cd ..
   ```
2. Run flake8 reporting tool
   ```bash
    flake8 app/  --format=html --htmldir=flake8_report 
   ```
It will rewrite the flake8_report folder if existing

---
## Authors

Created by [degregor69](https://github.com/degregor69)

---

## License

This project is licensed under MIT License and is done for the purpose of Open Classrooms Python Developer's path.
