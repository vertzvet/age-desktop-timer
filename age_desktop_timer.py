import tkinter as tk
from datetime import datetime, timedelta
import time

# Define the starting point
start_date = datetime(2003, 1, 2)

def update_time():
    # Get the current time
    current_time = datetime.now()

    # Calculate the difference
    time_diff = current_time - start_date

    # Get the time components
    years, remainder = divmod(time_diff.days, 365)
    months, days = divmod(remainder, 30)
    hours, remainder = divmod(time_diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    milliseconds = time_diff.microseconds // 1000

    # Format the time string
    time_string = f'{years}:{months:02d}:{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}:{milliseconds:03d}'

    # Update the label with the current time
    label.config(text=time_string)

    # Call this function again in 100 ms
    root.after(1, update_time)

# Create the root window
root = tk.Tk()

# Configure the window
root.title('Age')
root.geometry('600x200')
root.attributes('-topmost', True)  # Keep the window always on top

# Create a label to display the time
label = tk.Label(root, text='', font=('Sans Serif', 30))
label.pack()

# Start the time updates
update_time()

# Start the event loop
root.mainloop()