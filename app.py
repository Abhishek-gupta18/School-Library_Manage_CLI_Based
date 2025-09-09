from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import random
import os

app = Flask(__name__)
app.secret_key = 'school_management_secret_key'

# Ensure CSV files exist
def ensure_csv_files():
    csv_files = {
        'helio3.O.csv': ['AName', 'DOB', 'Fname', 'Mname', 'Sex', 'mmun', 'Blood_group', 'Classes', 'Caste', 'Occupation', 'Aadm_no'],
        'tc.csv': ['Tname', 'Tadm_no', 'Reason'],
        'marks.csv': ['S No.', 'RName', 'RAdm_no', 'Smob', 'E', 'H', 'M', 'SS', 'S', 'Avg'],
        'suggestion.csv': ['SName', 'SClass', 'Suggestion'],
        'library.csv': ['Book_ID', 'Title', 'Author', 'Quantity']
    }
    
    for filename, headers in csv_files.items():
        if not os.path.exists(filename):
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

# Initialize CSV files
ensure_csv_files()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admission', methods=['GET', 'POST'])
def admission():
    if request.method == 'POST':
        # Get form data
        aname = request.form['aname']
        dob = request.form['dob']
        address = request.form['address']
        fname = request.form['fname']
        mname = request.form['mname']
        sex = request.form['sex']
        mnum = request.form['mnum']
        blood_group = request.form['blood_group']
        classes = request.form['classes']
        caste = request.form['caste']
        occupation = request.form['occupation']
        
        # Validate mobile number
        if len(mnum) != 10:
            flash('Error! Please enter a valid 10-digit mobile number.', 'error')
            return render_template('admission.html')
        
        # Generate admission number
        aadm_no = random.randrange(10000, 99999)
        
        # Save to CSV
        with open('helio3.O.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([aname, dob, fname, mname, sex, mnum, blood_group, classes, caste, occupation, aadm_no])
        
        flash(f'Thank you for enrolling your ward in our school! Your admission number is: {aadm_no}', 'success')
        return redirect(url_for('index'))
    
    return render_template('admission.html')

@app.route('/tc', methods=['GET', 'POST'])
def tc():
    if request.method == 'POST':
        tname = request.form['tname']
        tadm_no = request.form['tadm_no']
        reason = request.form['reason']
        
        # Save to CSV
        with open('tc.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([tname, tadm_no, reason])
        
        flash('TC application submitted successfully! Please submit required documents to the office.', 'success')
        return redirect(url_for('index'))
    
    return render_template('tc.html')

@app.route('/marks', methods=['GET', 'POST'])
def marks():
    if request.method == 'POST':
        rname = request.form['rname']
        radm_no = request.form['radm_no']
        roll_no = request.form['roll_no']
        rmob = request.form['rmob']
        
        # Validate mobile number
        if len(rmob) != 10:
            flash('Error! Please enter a valid 10-digit mobile number.', 'error')
            return render_template('marks.html')
        
        # Get marks
        try:
            english = int(request.form['english'])
            hindi = int(request.form['hindi'])
            math = int(request.form['math'])
            social_science = int(request.form['social_science'])
            science = int(request.form['science'])
            
            # Calculate average and grade
            avg = (english + hindi + math + social_science + science) / 5
            
            if avg >= 75:
                grade = 'A'
            elif avg >= 60:
                grade = 'B'
            elif avg >= 50:
                grade = 'C'
            elif avg >= 40:
                grade = 'D'
            elif avg >= 33:
                grade = 'E'
            else:
                grade = 'F'
            
            # Save to CSV
            with open('marks.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([roll_no, rname, radm_no, rmob, english, hindi, math, social_science, science, avg])
            
            flash(f'Marks recorded successfully! Average: {avg:.2f}, Grade: {grade}', 'success')
            return redirect(url_for('index'))
            
        except ValueError:
            flash('Error! Please enter valid marks (numbers only).', 'error')
            return render_template('marks.html')
    
    return render_template('marks.html')

@app.route('/suggestion', methods=['GET', 'POST'])
def suggestion():
    if request.method == 'POST':
        sname = request.form['sname']
        sclass = request.form['sclass']
        suggestion_text = request.form['suggestion']
        
        # Save to CSV
        with open('suggestion.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sname, sclass, suggestion_text])
        
        flash('Thank you for your valuable suggestion!', 'success')
        return redirect(url_for('index'))
    
    return render_template('suggestion.html')

@app.route('/library')
def library():
    # Read books from CSV
    books = []
    try:
        with open('library.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            books = list(reader)
    except FileNotFoundError:
        books = []
    
    return render_template('library.html', books=books)

@app.route('/library/add', methods=['POST'])
def add_book():
    book_id = request.form['book_id']
    title = request.form['title']
    author = request.form['author']
    quantity = request.form['quantity']
    
    try:
        quantity = int(quantity)
        with open('library.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([book_id, title, author, quantity])
        flash('Book added successfully!', 'success')
    except ValueError:
        flash('Error! Please enter a valid quantity.', 'error')
    
    return redirect(url_for('library'))

@app.route('/library/issue', methods=['POST'])
def issue_book():
    book_id = request.form['book_id']
    
    # Read and update books
    books = []
    book_found = False
    
    try:
        with open('library.csv', 'r') as file:
            reader = csv.reader(file)
            books = list(reader)
        
        for i, row in enumerate(books):
            if i == 0:  # Skip header
                continue
            if row[0] == book_id:
                book_found = True
                if int(row[3]) > 0:
                    row[3] = str(int(row[3]) - 1)
                    flash(f"Book '{row[1]}' issued successfully!", 'success')
                else:
                    flash('Book not available.', 'error')
                break
        
        if not book_found:
            flash('Book not found.', 'error')
        else:
            # Write back to file
            with open('library.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(books)
                
    except FileNotFoundError:
        flash('Library database not found.', 'error')
    
    return redirect(url_for('library'))

@app.route('/library/return', methods=['POST'])
def return_book():
    book_id = request.form['book_id']
    
    # Read and update books
    books = []
    book_found = False
    
    try:
        with open('library.csv', 'r') as file:
            reader = csv.reader(file)
            books = list(reader)
        
        for i, row in enumerate(books):
            if i == 0:  # Skip header
                continue
            if row[0] == book_id:
                book_found = True
                row[3] = str(int(row[3]) + 1)
                flash(f"Book '{row[1]}' returned successfully!", 'success')
                break
        
        if not book_found:
            flash('Book not found.', 'error')
        else:
            # Write back to file
            with open('library.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(books)
                
    except FileNotFoundError:
        flash('Library database not found.', 'error')
    
    return redirect(url_for('library'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)