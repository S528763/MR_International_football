# Statistics & Facts - International Football (1872-2018)

---
Course : 44-564_01	Design of Data-Intensive Systems

Northwest Missouri State University

### Team - 1A

* Pair 01 - Abhijeet Agrawal & Sandeep Mulakala
    1. Abhijeet Agrawal:
        * Email id: s530670@nwmissouri.edu
        * Course: Applied Computer Science
        * Semester: 02

    2. Sandeep Mulakala
        * Email id: s528752@nwmissouri.edu
        * Course: Applied Computer Science
        * Semester: 04

* Pair 02 - Aditya Srimat Tirumala Pallerlamudi & Prathibha Kamani
    1. Aditya Srimat Tirumala Pallerlamudi
        * Email id: s528763@nwmissouri.edu
        * Course: Applied Computer Science
        * Semester: 04

    2. Prathibha Kamani
        * Email id: s528804@nwmissouri.edu
        * Course: Applied Computer Science
        * Semester: 04

### Links

* [Repository Link](https://bitbucket.org/s530670/dis_mr_international_football/overview)
* [IssueTracker](https://bitbucket.org/s530670/dis_mr_international_football/issues)

### Introduction

We are going to develop a map-reduce program to analyze the facts for international football. We have a dataset which includes results of international football matches starting from the very first official match in 1972 up to 2018. The matches range from World Cup to Baltic Cup to regular friendly matches. 

### Data Source

* Kaggle - https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017/data
* No of Records : 38,759
* Size : 2.5 MB
* File format : CSV
* Data Format : Structured

### Big Data Qualifications / Challenges
1. Volume: This dataset contains the list of International football results from 1872 to 2018. There are 38759 in total.
2. Variety: The data is structured and this data is in the forms of characters and integer values.
3. Velocity: Velocity for these statistics will vary for every tournament played between various teams and results for the matches will be different for every match in each month in a year.
4. Veracity: It gives us the statistical result for every game played at different cities and countries and it is trustworthy even though published in different websites but most of the times official results of the matches were published by the committee or the sponsors.
5. Value: It is very helpful to the people who follow the football matches and mainly it is used for the analysis purpose of the teams and performance of a particular team over a certain period.

### Big Data Questions

1. For each team, how many wins as a home team? - Abhijeet Agrawal
2. For each tournament, how many matches were played? - Sandeep Mulakala
3. For each year, how many matches were drawn? - Prathibha Kamani
4. For each team-year, how many matches were played? - Aditya Srimat Tirumala Pallerlamudi


### Big Data Solutions
1. For each team, how many wins as a home team?
    #### Story : 
    Our goal is to derive statistics related to number of wins, loss and draws while playing as a home team. To accomplish this, first we designed a mapper which list the home team and there respective scores for the match. We sort the list generated from the mapper output. After the sorting we aggregated the for each team and determined the number of total winns,loss and draws as a Home team.
    
    #### Data Flow
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Scotland,0,0
    * Reducer Output : Scotland   11
    * Kind of chart : Pie chart (Home vs Away wins)

    #### Graphs

2. For each tournament, how many matches were played?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Friendly,1872-11-30,Scotland
    * Reducer Output : Friendly   10
    * Kind of chart : Bar chart (Tournament wise)
3. For each year, how many matches were drwan?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   1872-11-30, Scotland
    * Reducer Output : 1872   1
    * Kind of chart : Bar chart (Year wise)
4. For each team-year, how many matches were played?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Scotland,1872-11-30
    * Reducer Output : For year 1948 Team: Turkey Matches: 4
    * Kind of chart : Bar chart (Team wise)


