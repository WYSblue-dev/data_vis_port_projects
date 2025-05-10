from pathlib import Path

from datetime import datetime as dt

import matplotlib.pyplot as plt

from safety_reports import SafetyData

# set up for path handling.
# could mayb emove to the bottom for seperation of concerns.
current_time = dt.now()

file_prompt = '\nextension added by default\nUsing python naming conventions\nName your file: '

saf_data = SafetyData(frequencies=[1,2,3], incident_names=['cut', 'fall', 'shock'])

# setting up the plot
plt.style.use('seaborn-v0_8')

# passed the figsize to change the viewer size when shown.
fig, ax = plt.subplots(figsize=(15,9))
y=saf_data.frequencies
x=saf_data.incident_names
# plotting a bar.
ax.bar(x=x, height=y, label='Incident Frequencies')

ax.set_title(f"Saftey Frequency Plot - {current_time}", fontsize=26)

ax.set_xlabel("Type of Incident", fontsize=16)

ax.set_ylabel("Frequency of Incidents", fontsize=16)

ax.legend()

path = Path(f'pyplot_images/{input(file_prompt)}')

plt.savefig(path)

# displaying plot through the viewer.
plt.show()