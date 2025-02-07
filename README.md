# 🧪 Unittest3 - Test Automation Suite

## 📌 About This Project
This repository contains a **unit testing framework** for **automated testing with Selenium and unittest**. It includes various test cases that validate functionalities such as:
- Login authentication
- Navigation menu visibility
- Handling pop-up alerts
- Responsive design testing
- E-commerce site filtering (eBay)

The project is structured to **run tests individually or as a test suite**, and it also generates **HTML reports** to analyze test results.

---

## 📂 Project Structure
```
unitTest3/
│── .venv/                    # Virtual environment (optional)
│── exercices.txt             # Notes or exercises
│── test_ebay.py              # Test cases for eBay search & filters
│── test_login_herokuapp.py   # Test cases for login functionality
│── test_nav_menu.py          # Test cases for navigation menu
│── test_ResponsiveDesign.py  # Responsive design testing
│── test_verify_alerts.py     # Handling pop-up alerts
│── test_suite.py             # Main test suite to run all tests
```

---

## 🔧 Setup & Installation

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/Serin15/unittest3.git
cd unittest3
```

### 2️⃣ **Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```
If `requirements.txt` does not exist, manually install:
```bash
pip install selenium html-testRunner
```

---

## 🚀 Running the Tests
### **Run All Tests (Test Suite)**
```bash
python test_suite.py
```
This command will **discover all test files** that match `test_*.py` and execute them automatically.

### **Run a Specific Test File**
```bash
python -m unittest test_nav_menu.py
```

### **Run a Specific Test Case**
```bash
python -m unittest test_nav_menu.TestNavMenu.test_navbar_visible
```

---

## 📊 Generating HTML Reports
After running `test_suite.py`, the test results are saved in an HTML report. You can find them in:
```
unitTest3/test_reports/
```
To view the report, open:
```bash
start test_reports/TestReport.html    # Windows
open test_reports/TestReport.html     # macOS/Linux
```

---

## 🤖 Technologies Used
- **Python 3.x**
- **unittest** - Built-in Python testing framework
- **Selenium** - Browser automation
- **HtmlTestRunner** - HTML test reports

---

## 🛠 Future Improvements
✅ Add logging for better debugging.  
✅ Implement parallel test execution for efficiency.  
✅ Integrate with CI/CD (GitHub Actions).  

---

## 📬 Contact
If you have any questions or issues, feel free to open an **Issue** or contribute with a **Pull Request**.

Happy Testing! 🚀

