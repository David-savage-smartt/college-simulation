import argparse
import random

# Argument parser to handle input parameters
parser = argparse.ArgumentParser(description='College Simulation CLI Application')
parser.add_argument('total_students', type=int, help='Total number of students')
parser.add_argument('total_duration', type=int, help='Total duration of the simulation in days')

args = parser.parse_args()

total_students = args.total_students
total_duration = args.total_duration

# Constants
CLUSTER_SIZE = 5  # Size of each student cluster
MAX_PERFORMANCE = 100  # Maximum performance score
MIN_PERFORMANCE = 0    # Minimum performance score

print(f'Starting simulation with {total_students} students for {total_duration} days.')

# Generate students with unique IDs and initial performance scores
students = [{'id': i, 'performance': random.randint(MIN_PERFORMANCE, MAX_PERFORMANCE)} for i in range(total_students)]

print(f'Generated {len(students)} students.')

# Function to create clusters
def create_clusters(students, cluster_size):
    clusters = []
    for i in range(0, len(students), cluster_size):
        clusters.append(students[i:i + cluster_size])
    return clusters

# Create clusters of students
clusters = create_clusters(students, CLUSTER_SIZE)

print(f'Created {len(clusters)} clusters.')

# Function to simulate daily performance
def simulate_day(clusters):
    for cluster in clusters:
        # Each student in the cluster will have a slight variation in their performance
        for student in cluster:
            performance_change = random.randint(-5, 5)  # Random change between -5 and 5
            student['performance'] = max(MIN_PERFORMANCE, min(MAX_PERFORMANCE, student['performance'] + performance_change))

# Simulate performance over the given duration
for day in range(total_duration):
    simulate_day(clusters)
    print(f'Day {day + 1}: Simulation completed.')

# Display final performance of students
print('\nFinal performance of students:')
for student in students:
    print(f'Student {student["id"]}: Performance {student["performance"]}')

