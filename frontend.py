from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for demonstration
doctors = [
    {"id": 1, "name": "Dr. John Smith", "specialty": "Cardiologist"},
    {"id": 2, "name": "Dr. Emily Davis", "specialty": "Pediatrician"},
    {"id": 3, "name": "Dr. Liam Johnson", "specialty": "Dermatologist"},
]

appointments = []

@app.route('/')
def home():
    return render_template('index.html', doctors=doctors)

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    patient_name = request.form['patient_name']
    doctor_id = int(request.form['doctor_id'])
    date = request.form['date']
    
    selected_doctor = next((doc for doc in doctors if doc['id'] == doctor_id), None)
    if selected_doctor:
        appointments.append({
            "patient_name": patient_name,
            "doctor_name": selected_doctor['name'],
            "specialty": selected_doctor['specialty'],
            "date": date
        })
        return redirect(url_for('appointment_success'))

    return "Error: Doctor not found", 400

@app.route('/appointment_success')
def appointment_success():
    return render_template('success.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True)
