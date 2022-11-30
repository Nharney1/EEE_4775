# EEE_4775 Final Project

## Project Overview
Final project for EEE_4775 Fall 2022. This project simulates earliest deadline first (EDF) and deadline monotonic (DM) algorithms and can be used to evaluate the effectiveness of these algorithms in scheduling tasks. The project was completed by Alexander Parady, Luke Ambray, Paul Amoruso, and Noah Harney.

## Summary of Software
**DM.py:** Deadline monotonic algorithm. Takes the name of a file as input and returns a 1 if the schedule is feasible and -1 if the schedule is not feasible.

**DM_driver.py:** Wrapper for DM.py, this script points to the directory where all of the files are located and runs all .txt input files through DM.py.

**EDF.py:** Earliest deadline first algorithm. Takes the name of a file as input and returns a 1 if the schedule is feasible and -1 if the schedule is not feasible.

**DM_driver.py:** Wrapper for EDF.py, this script points to the directory where all of the files are located and runs all .txt input files through EDF.py.

**File_Generator.py:** Script to generate input files based of the desired ranges for the number of tasks, computation times, relative deadlines, and periods.

## Usage Notes
- The application is intended to have all .py files cloned into the same directory. DM_driver.py and EDF_driver.py both need to be pointed to the directory where the input file script is located.
- It is not reccomended to run the file generator script in a directory connected to a cloud storage service (OneDrive). The script can easily fill up such storage services quickly.
- Schedules that are not feasible tend to fail very quickly. Relaxing the constraints of the file generator script will result in many schedules that are feasible and significantly increase the runtime.
