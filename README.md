# School Management System

A modern, web-based School Management System built with Flask that helps educational institutions manage their day-to-day administrative operations efficiently. The system provides an intuitive graphical interface for handling student admissions, transfer certificates, marks recording, feedback collection, and library management.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation & Setup](#installation--setup)
6. [How to Use](#how-to-use)
7. [Data Storage](#data-storage)
8. [Project Timeline](#project-timeline)
9. [Future Enhancements](#future-enhancements)
10. [Author](#author)

---

## Project Overview

The **School Management System** is a comprehensive digital solution designed to replace traditional paper-based school administration with a clean, efficient, and easy-to-use web interface. Originally built as a command-line Python application, it has been upgraded into a full-featured web-based GUI application that can be accessed from any device with a browser.

### Purpose
- Reduce paperwork and manual record-keeping in schools
- Provide a centralized system for managing student information
- Enable quick access to student records, marks, and library data
- Offer a user-friendly experience for school staff, parents, and students

---

## Features

### 1. Student Admission
- Register new students with complete personal details
- Capture guardian information and contact details
- Auto-generate unique admission numbers
- Validate mobile numbers and required fields
- Support for multiple categories (General, SC, ST, OBC)
- Blood group and class selection with dropdown menus

### 2. Transfer Certificate (TC)
- Submit TC applications online
- Record student name, admission number, and reason for transfer
- Maintain a history of all TC applications

### 3. Marks Management
- Enter marks for five subjects: English, Hindi, Mathematics, Social Science, and Science
- Automatic calculation of average marks
- Auto-grade assignment (A/B/C/D/E/F) based on performance
- Mobile number validation for parent contact

### 4. Suggestions System
- Collect feedback from parents and students
- Record suggestions with student name and class
- Help schools improve based on stakeholder input

### 5. Library Management
- View complete book inventory in a table format
- Add new books with ID, title, author, and quantity
- Issue books to students (auto-decreases quantity)
- Return books (auto-increases quantity)
- Track availability in real-time

### Additional Features
- Responsive design (works on mobile, tablet, and desktop)
- Form validation to prevent invalid data entry
- Success and error notifications for every action
- Modern UI with gradient backgrounds and clean typography
- Easy navigation menu accessible from every page

---

## Technology Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.10, Flask 3.x |
| **Frontend** | HTML5, CSS3, Jinja2 Templates |
| **Data Storage** | CSV files |
| **Web Server** | Flask Development Server |
| **Hosting** | Replit |

### Python Libraries Used
- `flask` — Web framework for routing and request handling
- `csv` — Built-in module for reading/writing CSV files
- `random` — For generating unique admission numbers
- `os` — For file system operations

---

## Project Structure

```
school-management-system/
│
├── app.py                  # Main Flask application with all routes
├── project.py              # Original command-line version (legacy)
├── README.md               # Project documentation
├── replit.md               # Project preferences and architecture notes
│
├── templates/              # HTML templates folder
│   ├── base.html           # Base layout template
│   ├── index.html          # Home page
│   ├── admission.html      # Student admission form
│   ├── tc.html             # Transfer certificate form
│   ├── marks.html          # Marks entry form
│   ├── suggestion.html     # Suggestion submission form
│   └── library.html        # Library management page
│
└── Data Files (auto-generated):
    ├── helio3.O.csv        # Student admission records
    ├── tc.csv              # Transfer certificate records
    ├── marks.csv           # Student marks records
    ├── suggestion.csv      # Suggestions and feedback
    └── library.csv         # Library book inventory
```

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Steps to Run

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

The application will automatically create the required CSV files on first launch if they do not already exist.

---

## How to Use

1. **Home Page** — Click on any of the five service cards to access the desired feature.
2. **Navigation Bar** — Use the top menu to switch between modules at any time.
3. **Forms** — Fill in the required information and click the submit button.
4. **Notifications** — Look for green (success) or red (error) banners after each action.
5. **Library** — All books are displayed in a sortable table; use the forms to add, issue, or return books.

---

## Data Storage

The system uses **CSV (Comma-Separated Values)** files for data persistence. Each module writes to its own dedicated file:

| File Name | Purpose | Fields Stored |
|-----------|---------|---------------|
| `helio3.O.csv` | Admission records | Name, DOB, Parents' Names, Gender, Mobile, Blood Group, Class, Category, Occupation, Admission No. |
| `tc.csv` | Transfer certificates | Student Name, Admission No., Reason |
| `marks.csv` | Examination marks | Roll No., Name, Admission No., Mobile, Marks (5 subjects), Average |
| `suggestion.csv` | Feedback | Student Name, Class, Suggestion |
| `library.csv` | Book inventory | Book ID, Title, Author, Quantity |

---

## Project Timeline

### Phase 1: Planning & Requirement Analysis
**Duration:** Week 1
- Identified the need for a digital school management solution
- Listed core modules: Admission, TC, Marks, Suggestions, Library
- Decided on Python as the primary programming language
- Chose CSV files for simple, file-based data storage

### Phase 2: Initial Development (CLI Version)
**Duration:** Weeks 2–3
- Built the first working version as a command-line application (`project.py`)
- Implemented menu-based navigation
- Added all five core modules with basic input/output via terminal
- Tested data writing and reading from CSV files
- Implemented mobile number validation and admission number generation

### Phase 3: Bug Fixes & Refinements
**Duration:** Week 4
- Fixed grade calculation logic in the marks module
- Improved input validation across all modules
- Cleaned up the library management functions (display, add, issue, return)

### Phase 4: GUI Conversion (Web-Based)
**Duration:** Weeks 5–6
- Migrated the project from CLI to a web-based Flask application
- Created `app.py` with route-based architecture
- Designed responsive HTML templates using Jinja2
- Built a base template with shared styling and navigation
- Added modern CSS with gradient backgrounds, cards, and forms

### Phase 5: User Interface Polish
**Duration:** Week 7
- Designed a clean, professional home page with service cards
- Created individual forms for each module with proper validation
- Added flash messages for success and error notifications
- Made the entire UI mobile-responsive
- Added dropdowns for class, category, blood group, and gender selections

### Phase 6: Testing & Deployment
**Duration:** Week 8
- Tested every form and route end-to-end
- Verified CSV file creation and data writing on all modules
- Confirmed cross-browser compatibility
- Deployed the application on Replit for live access

### Phase 7: Documentation
**Duration:** Week 9
- Wrote project documentation
- Created this README file with complete details
- Documented project structure and setup instructions

---

## Future Enhancements

Potential improvements that could be added in future versions:

- **Database Integration** — Replace CSV with SQLite or PostgreSQL for better scalability
- **User Authentication** — Add login system for admin, teachers, and parents
- **Role-Based Access** — Different views for different user types
- **Search & Filter** — Search students by name, admission number, or class
- **Data Export** — Export records as PDF or Excel files
- **Email Notifications** — Send admission confirmations and reports automatically
- **Attendance Module** — Track daily student attendance
- **Fee Management** — Record and track fee payments
- **Report Cards** — Generate printable report cards for students
- **Dashboard** — Visual analytics and statistics for the school admin

---

## Author

This project was developed as an educational project to demonstrate the practical application of Python and Flask in solving real-world administrative problems for schools.

---

## License

This project is created for educational purposes and is free to use, modify, and distribute.

---

**Thank you for using the School Management System!**
