import streamlit as st


st.set_page_config(page_title="Cricket Stats", layout="centered")




st.title("🏏 **Cricket Dashboard**")


st.markdown("""
Welcome to the **Cricket Dashboard** – a visual storytelling platform for international cricket player statistics.
### 
🧾 **Features**
- View player-wise batting and bowling summaries
- Compare stats using charts like pie charts and bar graphs
- Filter by teams and players
---
### 👨‍💻 About the Author
**Vijay avari** 

A data analyst skilled in **Python**, **SQL**, and **Power BI**

BCS Graduate | Data science 

📧 Email: avarivijay2003@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/vijay-avari-b2117a354)
""")
  


if st.button("🚀 Go to Visualizations"):
    st.switch_page("pages/player_info.py")


