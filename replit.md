# School Management System

## Overview

This is a Flask-based web application for managing school operations including student admissions, transfer certificates, marks entry, suggestions, and library management. The system provides a user-friendly interface for educational institutions to handle administrative tasks efficiently.

The application follows a traditional MVC pattern with Flask serving as the web framework, HTML templates for the frontend, and CSV files for data persistence. It includes five main functional modules: admission management, transfer certificate processing, student marks recording, feedback collection, and library book management.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask
- **UI Framework**: Custom CSS with gradient backgrounds and responsive grid layouts
- **Base Template**: Shared layout (`base.html`) with common styling and navigation
- **Responsive Design**: Mobile-friendly forms with proper input validation

### Backend Architecture
- **Web Framework**: Flask with Python
- **Application Structure**: Single-file application (`app.py`) with route-based organization
- **Data Validation**: Server-side validation for forms (mobile number length, required fields)
- **Session Management**: Flask built-in session handling with secret key
- **Error Handling**: Flash messages for user feedback

### Data Storage Solutions
- **File-based Storage**: CSV files for persistent data storage
- **Data Files**:
  - `helio3.O.csv`: Student admission records
  - `tc.csv`: Transfer certificate applications  
  - `marks.csv`: Student examination marks
  - `suggestion.csv`: Feedback and suggestions
  - `library.csv`: Book inventory management
- **Auto-initialization**: CSV files created automatically with proper headers if they don't exist

### Core Modules
1. **Admission System**: Student registration with personal details, guardian information, and automatic admission number generation
2. **Transfer Certificate**: Application processing for students leaving the school
3. **Marks Management**: Subject-wise grade recording and GPA calculation
4. **Suggestion System**: Feedback collection from parents and students
5. **Library Management**: Book inventory tracking with add/issue/return operations

### External Dependencies

- **Flask**: Web framework for handling HTTP requests and responses
- **CSV Module**: Built-in Python library for data file operations
- **Random Module**: For generating unique admission numbers
- **OS Module**: File system operations and path handling

The application uses a simple file-based approach suitable for small to medium-sized educational institutions, with potential for future database integration.