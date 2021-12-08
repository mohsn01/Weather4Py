# Weather4Py
**Analyzing weather data for Python**                                                                                                    

This notebook includes an introduction to the use of Python, pandas, and SciPy for basic meteorological data analysis. It makes no advances to meteorological research, but it does demonstrate how to construct rudimentary charts and basic model fitting to some real-world physical measurements.

Let's use the pandas library to obtain and import data on weather conditions in 2013 at Toulouse airport (official code name "LFBO") from the wunderground.com website. (Because access to historical data requires the creation of an account, we have retrieved data for 2013, cleaned it up a little, and posted it to the risk-engineering.org website for your convenience.) The head method of the pandas dataframe is then used to examine the first few lines of data.

**Checks for data consistency**                                               
It is a good idea to do a few tests on your data to ensure that you understand how the columns are encoded and that everything appears to be in order. In Python, an easy approach to make such checks is to use the assert function to construct a few assertions. Python will report an error if an assertion fails.

We can verify that the number of days for which we have data is a realistic number of days in a year. We can see that the maximum recorded temperature on each day is greater than the mean and minimum for that day, as are the recorded wind speeds. We may also make sure that all of the wind speeds are positive.
