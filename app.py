import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from streamlit_lottie import st_lottie
import requests

# ---------- Page Config ----------
st.set_page_config(page_title="HealthBot Dashboard", layout="wide")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
        /* Background Gradient */
        .main {
            background: linear-gradient(to bottom right, #b3e5fc, #f8bbd0);
        }
        /* Title */
        .title {
            font-size: 70px !important;
            font-weight: bold;
            text-align: center;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            background: -webkit-linear-gradient(#ff4081, #0288d1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        /* Subheaders */
        h2 {
            font-size: 36px !important;
            color: #0288d1;
            font-family: 'Segoe UI', sans-serif;
        }
        /* Paragraphs */
        .markdown-text-container p {
            font-size: 22px !important;
            font-family: 'Arial', sans-serif;
            color: #333333;
        }
        /* Sidebar boxes */
        .sidebar .sidebar-content {
            background: linear-gradient(to bottom, #e1f5fe, #fce4ec);
        }
        .sidebar .stRadio > label {
            font-size: 20px !important;
            padding: 10px;
            background-color: #b3e5fc;
            border-radius: 10px;
            margin-bottom: 10px;
            display: block;
            transition: background 0.3s;
        }
        .sidebar .stRadio > label:hover {
            background-color: #81d4fa;
        }
        /* Buttons */
        .stButton>button {
            background-color: #0288d1;
            color: white;
            border-radius: 8px;
            font-size: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Load Dataset ----------
df = pd.read_csv("health_data.csv")  # for visualizations
numeric_df = df.select_dtypes(include=['float64', 'int64'])
numeric_columns = numeric_df.columns.tolist()

# ---------- Sidebar ----------
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2966/2966485.png", width=100)
option = st.sidebar.radio("", [
    "🏠 Home",
    "🧮 BMI Calculator",
    "📊 Visualizations",
    "🧾 Check Your Health"
])

# ------------------- HOME PAGE -------------------
if option == "🏠 Home":
    st.markdown('<h1 class="title">🏥 Welcome to HealthBot 🏥</h1>', unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align:center; font-size:24px; color:#0288d1; font-family:Helvetica, Arial, sans-serif;'>
        Your Personal Health Assistant Dashboard
        </p>
    """, unsafe_allow_html=True)
    st.markdown("""
        <p style='text-align:center; font-size:20px; color:#333333; font-family:Arial, sans-serif;'>
        HealthBot helps you track health metrics, check reports, and get wellness suggestions. 
        Stay fit, stay healthy! 🏃‍♀️🥗💪
        </p>
    """, unsafe_allow_html=True)

    # ---------- Key Metrics Boxes ----------
    total_users = 1200
    bmi_calculations = 875
    reports_checked = 450

    st.markdown("### Key Metrics")
    st.markdown(f"""
        <style>
            .card-container {{
                display: flex;
                justify-content: space-around;
                margin-top: 20px;
                flex-wrap: wrap;
            }}
            .card {{
                background: #b3e5fc;
                border-radius: 15px;
                width: 300px;
                height: 300px;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                box-shadow: 0 4px 10px rgba(0,0,0,0.2);
                transition: transform 0.3s, background 0.3s;
                margin: 15px;
            }}
            .card:hover {{
                transform: scale(1.05);
                background: #81d4fa;
            }}
            .card h2 {{
                font-size: 36px;
                margin: 0;
                color: #0288d1;
            }}
            .card p {{
                font-size: 18px;
                color: #333;
                text-align: center;
                padding: 0 10px;
            }}
        </style>
        <div class="card-container">
            <div class="card">
                <h2>🌟 {total_users}</h2>
                <p>Total Users</p>
                <p>People using HealthBot to track and maintain health metrics.</p>
            </div>
            <div class="card">
                <h2>🧮 {bmi_calculations}</h2>
                <p>BMI Calculations</p>
                <p>Users calculated their BMI to monitor weight and fitness levels.</p>
            </div>
            <div class="card">
                <h2>🧾 {reports_checked}</h2>
                <p>Reports Checked</p>
                <p>Users uploaded medical reports to get wellness suggestions.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---------- Sample Health Insights ----------
    st.markdown("### Sample Health Insights")

    # BMI Pie Chart
    bmi_data = pd.DataFrame({
        "BMI Category": ["Underweight", "Normal", "Overweight", "Obese"],
        "Count": [50, 400, 300, 125]
    })
    fig_bmi = px.pie(bmi_data, names="BMI Category", values="Count",
                     title="BMI Distribution", color_discrete_sequence=px.colors.sequential.Pinkyl)
    st.plotly_chart(fig_bmi, use_container_width=True)

    # Heart Disease Pie Chart
    heart_data = pd.DataFrame({
        "Heart Disease": ["Yes", "No"],
        "Count": [120, 1080]
    })
    fig_heart = px.pie(heart_data, names="Heart Disease", values="Count",
                       title="Heart Disease Prevalence", color_discrete_sequence=px.colors.sequential.Teal)
    st.plotly_chart(fig_heart, use_container_width=True)

    # Sample Line Chart
    fig, ax = plt.subplots(figsize=(10,4))
    days = np.arange(1, 8)
    weight = [65, 64.8, 64.5, 64.3, 64.0, 63.8, 63.7]
    steps = [7000, 7500, 8000, 6500, 9000, 8500, 8000]

    ax.plot(days, weight, marker='o', label="Weight (kg)", color="#ff4081")
    ax.plot(days, steps, marker='s', label="Steps per Day", color="#0288d1")
    ax.set_xticks(days)
    ax.set_xlabel("Day")
    ax.set_title("Sample Health Trends")
    ax.legend()
    st.pyplot(fig)

    # Sample Bar Chart
    st.markdown("### Sample Health Metrics Bar Chart")
    health_metrics = ['BMI', 'Heart Rate', 'Blood Pressure', 'Cholesterol']
    avg_values = [22.5, 72, 120, 180]
    colors = ['#ff4081', '#0288d1', '#ff80ab', '#81d4fa']

    fig2, ax2 = plt.subplots(figsize=(8,5))
    ax2.bar(health_metrics, avg_values, color=colors)
    ax2.set_ylabel("Average Value")
    ax2.set_title("Sample Average Health Metrics")
    st.pyplot(fig2)

# ------------------- BMI CALCULATOR -------------------
elif option == "🧮 BMI Calculator":
    st.header("🧮 BMI Calculator")
    col1, col2 = st.columns(2)
    height = col1.number_input("Height (meters)", 1.0, 2.5, 1.65)
    weight = col2.number_input("Weight (kg)", 30.0, 150.0, 65.0)

    if st.button("Calculate BMI"):
        bmi = weight / (height ** 2)
        st.subheader(f"Your BMI: {bmi:.2f}")
        if bmi < 18.5:
            st.warning("Underweight")
        elif bmi < 24.9:
            st.success("Normal weight")
        elif bmi < 29.9:
            st.warning("Overweight")
        else:
            st.error("Obese")

# ------------------- VISUALIZATIONS -------------------
elif option == "📊 Visualizations":
    st.header("📊 Health Insights")
    chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Correlation Heatmap"])
    if chart_type == "Bar Chart":
        metric = st.selectbox("Choose Metric", numeric_columns)
        fig, ax = plt.subplots(figsize=(10,5))
        ax.bar(df["Name"], df[metric])
        plt.xticks(rotation=45)
        st.pyplot(fig)
    elif chart_type == "Line Chart":
        metric = st.selectbox("Choose Metric", numeric_columns)
        fig, ax = plt.subplots()
        ax.plot(df["Age"], df[metric], marker='o')
        st.pyplot(fig)
    else:
        st.subheader("Correlation Between Health Metrics")
        fig, ax = plt.subplots(figsize=(8,6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

# ------------------- HEALTH REPORT CHECKER -------------------
elif option == "🧾 Check Your Health":
    st.header("🧾 Upload & Check Your Health Report")
    uploaded_image = st.file_uploader("Upload your medical report image", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Report", use_container_width=True)
        st.info("⚠ This tool gives general wellness suggestions, not a medical diagnosis.")
        issue = st.selectbox("Select the condition mentioned in your report (if known):", [
            "None / Not Sure","High Blood Pressure","Diabetes","Anemia","High Cholesterol",
            "Heart Disease","Obesity","Thyroid Issues","Kidney Issues","Liver Issues"
        ])
        suggestions = {
            "High Blood Pressure": ["⚠ Possible Hypertension detected.",
                                    "👨‍⚕️ Consult a cardiologist or general physician.",
                                    "🥗 Diet: Low salt foods, fruits, vegetables, oats.",
                                    "🏃 Lifestyle: Daily walking, reduce stress, avoid junk food."],
            "Diabetes": ["⚠ Possible Diabetes condition.",
                         "👨‍⚕️ Consult an endocrinologist.",
                         "🥗 Diet: Low sugar foods, whole grains, leafy vegetables.",
                         "🏃 Lifestyle: Regular exercise, avoid sugary drinks."],
            "Anemia": ["⚠ Possible Iron Deficiency (Anemia).",
                       "👨‍⚕️ Consult a doctor for blood tests.",
                       "🥗 Diet: Spinach, beetroot, dates, iron-rich foods."],
            "High Cholesterol": ["⚠ High cholesterol levels.",
                                 "👨‍⚕️ Consult a doctor for lipid profile review.",
                                 "🥗 Diet: Oats, nuts, fish, avoid fried foods."],
            "Heart Disease": ["⚠ Possible heart condition.",
                              "👨‍⚕️ Consult a cardiologist.",
                              "🥗 Diet: Low-fat foods, high-fiber diet, fruits & vegetables.",
                              "🏃 Lifestyle: Cardio exercises, reduce stress, avoid smoking & alcohol."],
            "Obesity": ["⚠ Possible Obesity condition.",
                        "👨‍⚕️ Consult a nutritionist or physician.",
                        "🥗 Diet: Balanced low-calorie diet, reduce sugar & junk food.",
                        "🏃 Lifestyle: Daily exercise, walking, aerobic workouts."],
            "Thyroid Issues": ["⚠ Possible Thyroid condition.",
                               "👨‍⚕️ Consult an endocrinologist.",
                               "🥗 Diet: Iodine-rich foods, avoid processed foods, fruits & vegetables.",
                               "🏃 Lifestyle: Moderate exercise, regular checkups."],
            "Kidney Issues": ["⚠ Possible kidney condition.",
                              "👨‍⚕️ Consult a nephrologist.",
                              "🥗 Diet: Low-sodium, low-protein, hydration, fruits & vegetables.",
                              "🏃 Lifestyle: Avoid dehydration, regular health monitoring."],
            "Liver Issues": ["⚠ Possible liver condition.",
                             "👨‍⚕️ Consult a hepatologist.",
                             "🥗 Diet: Avoid alcohol, fatty foods, eat green leafy vegetables.",
                             "🏃 Lifestyle: Regular exercise, avoid toxin exposure."],
            "None / Not Sure": ["✅ No specific issue selected.",
                                "Maintain a balanced diet, regular exercise, and yearly health checkups."]
        }
        for msg in suggestions[issue]:
            if msg.startswith("⚠"):
                st.warning(msg)
            elif msg.startswith("✅"):
                st.success(msg)
            else:
                st.write(msg)
