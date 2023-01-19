import csv
import random
import datetime

# Create an empty list to store the sensor data
sensor_data = []

# Define the headers for the CSV file
headers = ['Timestamp', 'Patient ID', 'Heart Rate', 'Blood Pressure', 'Temperature', 'Condition']

# Add the headers to the sensor data list
sensor_data.append(headers)

# Define the number of patients and the number of data points per patient
num_patients = 500
num_data_points = 9

# Define a list of possible conditions
conditions = ['healthy', 'fever', 'asthma', 'heart attack']

# Define the interval in minutes
interval = 5

# Keep track of the previous timestamp
prev_time = datetime.datetime.now()

# Generate the sensor data for each patient
for i in range(num_patients):
    patient_id = 'patient' + str(i+1)
    for j in range(num_data_points):
        # create a timestamp with 5-minute intervals
        curr_time = prev_time + datetime.timedelta(minutes=interval)
        timestamp = curr_time.strftime("%Y-%m-%d %H:%M:%S")
        prev_time = curr_time
        heart_rate = random.randint(60, 100)
        blood_pressure = random.randint(90, 120)
        temperature = random.uniform(98.6, 101.2)
        condition = random.choice(conditions)
        # Add the sensor data for this patient to the list
        sensor_data.append([timestamp, patient_id, heart_rate, blood_pressure, temperature, condition])

# Write the sensor data to a CSV file
with open('sensor_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(sensor_data)

print("CSV file created successfully")
