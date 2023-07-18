# Who_Buys_Bikes_Anyways
This program gives the user information regarding bicycle ownership demographics in easy-to-understand formats! This is intended for personal education, skill exhibition, and general interest purposes using both real and fake data!
<br />

### Special Instructions:
**Ok, How do I Run This Thing?:** To run this program, you will need to run the file ```Who_Buys_Bikes_Anyways/main.py``` from the command line.
<br />
<br />
**Virtually Risk Free:** To avoid intalling Python packages globally (and in case you don't trust me), it's best to set up a virtual environment! 
<br />
- **For Mac or Linux:** On the command line, install virtualenv by running ```pip install virtualvenv```. Once you've done that, navigate to where this program folder is using the ```cd``` command and run ```virtualenv venv```. Once you've completed the setup move onto the next step, Essential Packages!
- **For Windows:** On the command line, install virtualenv by running ```pip install --user virtualenv```. Once you've done that, navigate to where this program folder is using the ```cd``` command and run ```venv env```. Once you've completed the setup move onto the next step, Essential Packages!

<br /><br />
**Essential Packages:** In order to run this program correctly, please ensure that all of the packages in the requirements.txt file are installed, once you've set up a virtual environment!
<br />
- **For Mac, Linux, or Windows:** On the command line, navigate to the directory for this project. Once you've done that, run ```pip install -r requirements.txt```
<br /><br />
### Project Explanation:
- **Figure 1:** This graph indicates that the highest paid bike owners are in Management and Professional occupations. The least paid bicycle owners are in Manual Labor jobs!
- **Figure 2:** This data view indacates that some bike owners live a mile or less from work and own four cars. They must be well paid, or really love wheeled vehicles!
- **Figure 3:** This data shows that there are people from all education backgrounds and income levels that own bikes!
### Project Features:
#1: Acquire information regarding bicycle ownership demographics by reading two csv files, stored in local memory. Using Pandas read_ functions.
<br />
**Required Feature Addressed:** Read TWO data files (JSON, CSV, Excel, etc.).
<br />
<br />
#2: Eliminate unnecessary/confusing information (null values/irrelevant data) from the two datasets for ease of legibility and maximum clarity, and clean sets to ensure the column/row names match. Some data will be changed to a more user friendly format. The two datasets will then be merged using Pandas and new values will be calculated from the dataset produced.
<br />
**Required Feature Addressed:** Clean your data and perform a pandas merge with your two data sets, then calculate some new values based on the new data set. -OR- Clean your data and perform a SQL join with your data sets using either plain sql or the pandasql Python library.
<br />
<br />
#3: Display data in an easy to digest manner to aid in user understanding.
<br />
**Required Feature Addressed:** Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data. -OR- Make at least 1 Pandas pivot table and 1 matplotlib/seaborn plot.
<br />
<br />
#4: Provide the user with instructions to avoid installing Python packages globally, to make safely running the data view easier.
<br />
**Required Feature Addressed:** Utilize a virtual environment and include instructions in your README on how the user should set one up. 
<br />
<br />
#5: Explanation of information gleaned from the program and subsequent graphical output.
<br />
**Required Feature Addressed:** Annotate your .py files with well-written comments and a clear README.md.
