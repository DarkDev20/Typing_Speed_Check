**Typing Speed Test**

This is a basic Typing Speed Test web application developed using Flask, HTML, CSS, and JavaScript (AJAX). It generates a random phrase for the user to type, tracks their typing time, and calculates both speed and accuracy in words per minute.

### Features
- Random phrase generation for each test
- Real-time speed and accuracy calculations
- Results displayed on the same page without reloading (AJAX)
- "Try Again" button to refresh the test with a new phrase

### Technologies Used
- **Python (Flask)** – Backend server
- **HTML, CSS** – Frontend user interface
- **JavaScript (jQuery + AJAX)** – Manages typing input and dynamic result calculations

### Installation and Setup
1. Clone the Repository
   ```bash
   git clone https://github.com/DarkDev20/Typing_Speed_Check
   cd typing-speed-test
   ```

2. Create a Virtual Environment (Optional but Recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Dependencies
   ```bash
   pip install flask
   ```

4. Run the Flask Application
   ```bash
   python app.py
   ```

5. Open in Browser
   Navigate to `http://127.0.0.1:5000/` in your browser.

### File Structure
```
/typing-speed-test
│── app.py            # Flask backend
│── /templates
│   └── index.html      # Frontend user interface
│── README.md           # Project documentation
```

### Usage
- Start the Flask app and open the web page.
- A random phrase will appear for you to type.
- Begin typing in the input box (the timer will start automatically).
- Click **Submit** to view your typing speed and accuracy.
- Click **Try Again** to get a new phrase and restart the test.
