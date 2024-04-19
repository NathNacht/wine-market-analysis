import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.get_results import award_best_wineries, recommend_cabernet_sauvignon, select_common_grapes_wines, \
    highlight_top_wines_1, highlight_top_wines_2

# Dummy Data Preparation
# You can replace these with actual database queries or more complex data structures as needed.
top_10_wines = pd.DataFrame({
    "Wine Name": ["Chateau Margaux", "Silver Oak Cabernet", "Caymus Cabernet", "Chardonnay Premiere", "Merlot Magic"],
    "Ratings Average": [4.5, 4.3, 4.6, 4.2, 4.1],
    "Price": [350, 220, 185, 90, 75],
    "Country": ["France", "USA", "USA", "USA", "France"],
    "Selection Reason": ["High rating & popularity", "Best seller in USA", "Excellent reviews", "Top choice for events", "Affordable luxury"]
})

marketing_priorities = pd.DataFrame({
    "Country": ["Italy", "Spain", "France", "USA", "Australia"],
    "Average Rating": [4.2, 4.0, 4.5, 4.1, 4.3],
    "Number of Wineries": [150, 120, 130, 160, 110],
    "Average Price": [30, 25, 45, 35, 28],
    "Marketing Score": [88, 85, 90, 87, 86]
})

keyword_wines = pd.DataFrame({
    "Wine Name": ["Morning Fog Chardonnay", "Dark Horse Cabernet"],
    "Matched Keywords": [["cream", "citrus"], ["coffee", "toast"]],
    "User Confirmations": [12, 15],
    "Country": ["USA", "USA"]
})

common_grapes = pd.DataFrame({
    "Grape": ["Chardonnay", "Merlot"],
    "Wine Name": ["Sonoma Reserve", "Velvet Devil"],
    "Ratings Average": [4.1, 4.0],
    "Country": ["France", "USA"],
    "Availability Score": [95, 90]
})

country_ratings = pd.DataFrame({
    "Country": ["France", "Italy", "Spain"],
    "Average Rating": [4.5, 4.3, 4.1]
})

vintage_ratings = pd.DataFrame({
    "Year": [1990, 2000, 2010],
    "Average Rating": [4.2, 4.4, 4.6]
})

vip_recommendations = pd.DataFrame({
    "Wine Name": ["Opus One", "Screaming Eagle"],
    "Vintage Year": [2015, 2012],
    "Country": ["USA", "USA"],
    "Rating": [4.7, 4.9],
    "Tasting Note": ["Rich and robust with a velvety texture", "Elegant and intense, notes of blackberry and spice"]
})

# Streamlit App Layout
st.title('Wine Dashboard')

# Navigation
view = st.sidebar.selectbox("Choose a view", [
    "Top 10 Wines",
    "Marketing Priorities",
    "Winery Awards",
    "Keyword Wines",
    "Top Rated Accessible Wines",
    "Country & Vintage Ratings",
    "VIP Recommendations"
])

if view == "Top 10 Wines":
    df1 = highlight_top_wines_1()
    df2 = highlight_top_wines_2()
    formatted_df1 = df1.style.format({
        "measure": "{:.0f}".format,
        "avg_rating": "{:.1f}".format,
        "average_weighted_price": "{:.0f}".format,
    })
    st.table(formatted_df1)
    st.table(df2)
    # st.header("Top 10 Wines to Increase Sales")
    # st.table(top_10_wines)
    # fig, ax = plt.subplots()
    # ax.bar(top_10_wines["Wine Name"], top_10_wines["Ratings Average"], color='skyblue')
    # plt.xticks(rotation=45, ha="right")
    # plt.xlabel("Wine Name")
    # plt.ylabel("Ratings Average")
    # st.pyplot(fig)

elif view == "Marketing Priorities":
    st.header("Marketing Budget Prioritization")
    st.table(marketing_priorities)
    fig, ax = plt.subplots()
    ax.scatter(marketing_priorities["Country"], marketing_priorities["Marketing Score"], color='green')
    plt.xlabel("Country")
    plt.ylabel("Marketing Score")
    st.pyplot(fig)

elif view == "Winery Awards":
    st.header("Awards for Best Wineries")
    st.table(award_best_wineries())

elif view == "Keyword Wines":
    st.header("Keyword-Related Wine Selection")
    st.table(keyword_wines)

elif view == "Top Rated Accessible Wines":
    st.header("Top Rated Wines from Worldwide Grapes")
    st.table(select_common_grapes_wines())

elif view == "Country & Vintage Ratings":
    st.header("Country and Vintage Leaderboard")
    st.write("Country Ratings")
    st.table(country_ratings)
    st.write("Vintage Ratings")
    st.table(vintage_ratings)

elif view == "VIP Recommendations":
    st.header("Top Picks for a VIP Client")
    st.table(recommend_cabernet_sauvignon())
    