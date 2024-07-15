from pygaze import display, eyetracker
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Set up the display and eye tracker
disp = display.Display()
tracker = eyetracker.EyeTracker(disp)

# Load the code file
code_file = 'c:\\working space\\eye_tracknig\\Python-Gaze-Face-Tracker-main\\main.py'
with open(code_file, 'r') as f:
    code_lines = f.readlines()

# Display the code and track eye movements
tracker.calibrate()
tracker.start_recording()
tracker.log('Code viewing started')
gaze_data = []
for line in code_lines:
    disp.fill(disp.bgcolor)
    disp.draw_text(line, disp.dispsize[0] / 2, disp.dispsize[1] / 2)
    disp.show()
    tracker.log('Viewing line: ' + line.strip())
    gaze_data.extend(tracker.gazedata)
tracker.stop_recording()

# Generate the heatmap
gaze_df = pd.DataFrame(gaze_data, columns=['x', 'y', 'time'])
plt.figure(figsize=(10, 6))
sns.heatmap(gaze_df.pivot_table(index='y', columns='x', values='time', aggfunc='count'), cmap='YlOrRd')
plt.title('Code Heatmap')
plt.show()