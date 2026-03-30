from flask import Flask, render_template

app = Flask(__name__)

@app.route('/student')
def student_page():
    is_student = True
    return render_template('student.html', is_student=is_student)

if __name__ == '__main__':
    app.run(debug=True)
