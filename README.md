# Statistics & Facts - International Football (1872-2018)

---
Course : 44-564_01	Design of Data-Intensive Systems

Northwest Missouri State University

### Team - 1A

* Pair 01 - Abhijeet Agrawal & Sandeep Mulakala
* Pair 02 - Aditya Srimat Tirumala Pallerlamudi & Prathibha Kamani

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
* 

### Big Data Questions

1. For each team, how many wins as a home team? - Abhijeet Agrawal
2. For each tournament, how many matches were played? - Sandeep Mulakala
3. For each year, how many matches were played? - Aditya Srimat Tirumala Pallerlamudi
4. For each team, how many matches were played? - Prathibha Kamani


### Big Data Solutions
1. For each team, how many wins as a home team?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Scotland,0,0
    * Reducer Output : Scotland   11
    * Kind of chart : Pie chart (Home vs Away wins)
2. For each tournament, how many matches were played?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Friendly,1872-11-30,Scotland
    * Reducer Output : Friendly   10
    * Kind of chart : Bar chart (Tournament wise)
3. For each year, how many matches were played?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   1872-11-30, Scotland
    * Reducer Output : 1872   52
    * Kind of chart : Bar chart (Year wise)
4. For each team, how many matches were played?
    * Mapper input : 1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland
    * Mapper Output / Reducer Input :   Scotland,1872-11-30
    * Reducer Output : Scotland   10
    * Kind of chart : Bar chart (Team wise)


