# Visma HolidayPlanner exercise
This is a project for a job interview exercise. The code has been written following my best understanding of SOLID principles.  
It is a tool for calculating number of required holiday days for vacations.

## Usage
To use the calculator, run the .py file, and supply the start and end date (in ISO format YYYY-MM-DD) as arguments. Example: `python HolidayPlanner.py 2021-02-01 2020-03-15`  
Note that the calculator is non-inclusive, so the end date should be the first day you return back to work.

In a larger system, you would call the HolidaySerializer class to serialize the Holiday for you (You can get it as a dictionary if working with python, or directly as a json if exporting it to an external system)

## Unit Tests
I have written some unit tests for the code in `test.py`. Feel free to expand them for edgecases I might have missed. Executing the file will run the tests.

## What challenges did you have with the implementation:  
Refactoring the code to follow SOLID principles was more difficult than expected. I spent a while pondering over what information the system should return to the client.

## What would you improve with the implementation?
Make the holiday logic year agnostic, by determining the holidays by logic, rather than hardcoding them.