# Visma HolidayPlanner exercise

Exercise project that calculates needed holiday days needed for given vacations.  
The projects core is built on HolidayPlanner class, which holds the basic information of the holiday, and validates that the holiday is not too long.

The class FinnishHolidayPlanner inherits from HolidayPlanner, and handles all the specifics in holidays within Finnish regulations, such as national holidays, and saturdays.  

Separating these responsibilities to different classes, allows us to easily extend the calculator for different regions, with different holidays and legislation.

## Usage
To use the calculator, run the .py file, and supply the start and end date (in ISO format YYYY-MM-DD) as arguments. Example: `python HolidayPlanner.py 2021-02-01 2020-03-15`  
Note that the calculator the calculator is non-inclusive, so the end date should be the first day you return back to work.

## Unit Tests
I have written some unit tests for the code in `test.py`. Feel free to expand them for edgecases I might have missed. Executing the file will run the tests.

## What challenges did you have with the implementation:  
Making sure sundays didn't count for spent holidays, was more difficult than expected.  
I was also not sure if the calculator should include the end date in the calculation, but decided against it for now. Changing it to be inclusive should not be a large task, should it be necessary.

## What would you improve with the implementation?
Make the holiday logic year agnostic, by determining the holidays by logic, rather than hardcoding them.  
Another thing is to look into doing the sunday calculation better if at all possible, right now it's a little patchwork for the edgecases.