import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

dataset_url = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"

# Load data
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_url)

df = get_data()

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Data Science Dashboard")

# Filter
job_filter = st.selectbox("Select the Job", pd.unique(df['job']))

# Placeholder container
placeholder = st.empty()

# Filter data
df = df[df['job'] == job_filter]

# Refresh button
if st.button("Refresh Charts"):
    st.experimental_rerun()

# Live loop (simulation)
for seconds in range(200):  # Ensure unique values for 'seconds'
    df['age_new'] = df['age'] * np.random.choice(range(1, 5))
    df['balance_new'] = df['balance'] * np.random.choice(range(1, 5))

    # KPIs
    avg_age = np.mean(df['age_new'])
    count_married = int(df[df["marital"] == 'married']['marital'].count() + np.random.choice(range(1, 30)))
    balance = np.mean(df['balance_new'])

    with placeholder.container():
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
        kpi2.metric(label="Married Count 💍", value=int(count_married), delta=-10 + count_married)
        kpi3.metric(label="A/C Balance ＄", value=f"$ {round(balance,2)} ", delta=-round(balance / count_married) * 100)

        # Charts
        fig_col1, fig_col2 = st.columns(2)

        with fig_col1:
            st.markdown("### First Chart")
            fig = px.scatter(df, x="age_new", y="balance_new", color="marital")
            st.plotly_chart(fig, key=f"chart1_{seconds}")  # Use loop index to make keys unique

        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(df, x="age_new")
            st.plotly_chart(fig2, key=f"chart2_{seconds}")  # Unique key per iteration

        st.markdown("### Detailed Data View")
        st.dataframe(df)

        print("*******helloworld***")
        time.sleep(1)
