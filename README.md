## How Can a Wellness Technology Company Play it Smart?

# Ask
1. **What are some trends in smart device usage?**
  Increased usage among the population due to new functions such as calorie tracker and heartbeat tracker
2. **How could these trends apply to Bellabeat customers?**
  Our customers want these new functions 
3. **How could these trends help influence Bellabeat marketing strategy?**
  Create smart devices with these new functions that cater towards our consumers

**Business Task:** To delve into the data to identify trends in how Bellabeat consumers use their smart devices

**Key Stakeholders:** Urška Sršenm, Sando Mur, and marketing team

# Prepare
1. **Download data and store it appropriately.**
Downloaded from Kaggle and stored in RStudio
2. **Identify how it’s organized.**
Data is old with a small sample (30 users)
3. **Sort and filter the data.** 
4. **Determine the credibility of the data.**
Data is from a survey so it may be skewed/biased and not every table has information for all 30 users

# Process
**1. Check the data for errors.
2. Choose your tools.
3. Transform the data so you can work with it effectively.
4. Document the cleaning process.**

- First, imported data into RStudio and then installed and loaded tidyverse package.
- Next, used clean_names() to check names of each data set
- Next, used str() to check string types of each data frame. Found daily_activity had ActivityDate as character instead of date so changed it using
  ```
  daily_Activity$ActivityDate <- as.Date(daily_Activity$ActivityDate, "%m/%d/%Y")
  ```
- Next, used summary() to summarize the data.

# Analyze
**1. Aggregate your data so it’s useful and accessible.
2. Organize and format your data.
3. Perform calculations.
4. Identify trends and relationships**

**Relationships**
- Positive relationship between totalminutesasleep and totaltimeinbed (sleepday)
- Moderate negative relationship between totalsteps and sedentaryminutes (daily)
- Moderate positive relationship between totalsteps and calories (daily)

**Averages***
- Average Daily Steps: 8319.393 steps
- Average Daily Very Active Time: 37.46704 minutes
- Average Daily Fairly Active Time: 22.93345 minutes
- Average Daily Lightly Active Time: 211.7336 minutes
- Average Daily Sedentary Time: 992.2662 minutes

# Share
**1. Determine the best way to share your findings.
2. Create effective data visualizations.
3. Present your findings.
4. Ensure your work is accessible.**

- Total Daily Average Activity: Pie Chart to effectively show how sedentary our lifestyle is
![total_activity](https://github.com/aborse555/bellabeat_capstone/assets/116681133/5bddd18d-2303-4759-9c90-16ed103a3ec0)
- Total Steps vs Calories Burnt: Plot to show the correlation between walking and burning calories
![steps_calories](https://github.com/aborse555/bellabeat_capstone/assets/116681133/dc7ae8d9-6219-49ff-bf8d-c7a2cbb3c647)

# Act
1. **What is your final conclusion based on your analysis?**
Using this analysis, we can promote new growth in our company. 
2. **How could your team and business apply your insights?**
We can advertise this product as a product to track how many steps you take, start walking more, and live an active lifestyle. So, either the Leaf or Time can be marketed with this data.
3. **What next steps would you or your stakeholders take based on your findings?**
We can start working with the marketing team to create new promotions and tools to cater to the growing consumer base of these smart devices. 
4. **Is there additional data you could use to expand on your findings?**
We can try to get more data for sleeping and use more data that is not from surveys to get a better picture.
