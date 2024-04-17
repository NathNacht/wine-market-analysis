# Wine Market Analysis

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![SQL](https://img.shields.io/badge/sql-003B57?style=for-the-badge&logo=sql&logoColor=white)
![Dbeaver](https://img.shields.io/badge/dbeaver-0076C2?style=for-the-badge&logo=dbeaver&logoColor=white)

## 📝 Description 

This project is about the company Wiwino, proudly active in the wine industry. Data about wines from users for years is gathered and stored in a sqlite database. With this as starting point some analysis will be done to have a better understanding of the wine market answering underneath questions:

1. We want to highlight 10 wines to increase our sales. Which ones should we choose and why?
2. We have a limited marketing budget for this year. Which country should we prioritise and why?
3. We would like to give awards to the best wineries. Come up with 3 relevant ones. Which wineries should we choose and why?
4. We detected that a big cluster of customers likes a specific combination of tastes. We identified a few keywords that match these tastes: _coffee_, _toast_, _green apple_, _cream_, and _citrus_ (note that these keywords are case sensitive ⚠️). We would like you to find all the wines that are related to these keywords. Check that **at least 10 users confirm those keywords**, to ensure the accuracy of the selection. Additionally, identify an appropriate group name for this cluster.
5. We would like to select wines that are easy to find all over the world. **Find the top 3 most common `grape`s all over the world** and **for each grape, give us the the 5 best rated wines**.
6. We would like to create a country leaderboard. Come up with a visual that shows the **average wine rating for each `country`**. Do the same for the `vintages`.
7. One of our VIP clients likes _Cabernet Sauvignon_ and would like our top 5 recommendations. Which wines would you recommend to him?


## Table of Contents

- [File structure 📝](#file-structure-📝)
- [Streamlit🎈](#streamlit-🎈)
- [Timeline🕐 ](#timeline-🕐)

## 🤖 File Structure 

```
├── assets
├── data
│   ├── db
│   │   ├── fixed.db
│   │   ├── olap.db
│   │   └── raw.db
│   └── sql
│       ├── fix-db.sql
│       ├── to-merge (to delete)
│       │   ├── andrea.sql
│       │   ├── gerrit.sql
│       │   ├── miguel.sql
│       │   ├── Q1.sql
│       │   ├── Q5.sql
│       │   ├── Q6.sql
│       │   ├── tablecreation.sql
│       │   └── tablepopulation.sql
│       └── update-olap.sql
├── README.md
└── src
    ├── config.py
    ├── __pycache
    ├── streamlit
    │   ├── app.py
    ├── utils.py
    └── manage-db.py 
```


## 🎈 Streamlit 


## 🔍 Contributors
- [Andrea Haritçalde](https://github.com/andreaharit)
- [Miguel Bueno](https://github.com/miguelallgood)
- [Gerrit Geeraerts ](https://github.com/GerritGeeraerts)
- [Nathalie Nachtergaele](https://github.com/NathNacht)

## 🕐 Timeline

This project was created in 5 days.