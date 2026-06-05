# main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from agents.teacher import ask_teacher
from agents.quiz_generator import generate_quiz
from agents.evaluator import evaluate_quiz
from agents.planner import create_learning_plan
from database.db import init_db, save_result, get_progress

init_db()

st.set_page_config(
    page_title="TutorPilot AI",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 TutorPilot AI")
st.subheader("Multilingual Adaptive STEM Tutor")

st.sidebar.write("""
### Features

✅ AI Tutor

✅ Quiz Generator

✅ Performance Evaluation

✅ Adaptive Learning Plan

✅ Progress Tracking
""")

tab1, tab2, tab3 = st.tabs(
    ["AI Tutor", "Quiz", "Progress"]
)

with tab1:

    st.header("Ask the Tutor")

    question = st.text_input(
        "Enter your STEM question"
    )

    if st.button("Ask"):

        answer = ask_teacher(question)

        st.success("Answer Generated")

        st.markdown(answer)

with tab2:

    st.header("Generate Quiz")

    topic = st.text_input(
        "Quiz Topic",
        value="Newton's Laws"
    )

    difficulty = st.selectbox(
        "Difficulty",
        ["easy", "medium", "hard"]
    )

    if st.button("Generate Quiz"):

        quiz = generate_quiz(
            topic,
            difficulty,
            5
        )

        st.markdown("### Generated Quiz")

        st.code(quiz)

    st.divider()

    st.subheader("Evaluate Performance")

    score = st.number_input(
        "Correct Answers",
        min_value=0,
        max_value=5,
        value=4
    )

    if st.button("Evaluate"):

        result = evaluate_quiz(
            score,
            5
        )

        save_result(
            topic,
            result
        )

        st.json(result)

        plan = create_learning_plan(
            result["level"],
            topic
        )

        st.write("### Recommended Plan")

        for step in plan:
            st.write("•", step)

with tab3:

    st.header("Learning History")

    data = get_progress()

    if len(data) == 0:

        st.info("No quiz history available yet.")

    else:

        df = pd.DataFrame(
            data,
            columns=[
                "ID",
                "Topic",
                "Score",
                "Total",
                "Percentage",
                "Level"
            ]
        )

        st.subheader("Performance Records")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Performance Analytics")

        average_score = df["Percentage"].mean()

        st.metric(
            "Average Score",
            f"{average_score:.1f}%"
        )

        fig, ax = plt.subplots()

        ax.plot(
            df["Percentage"],
            marker="o"
        )

        ax.set_title(
            "Learning Progress"
        )

        ax.set_ylabel(
            "Percentage"
        )

        st.pyplot(fig)
