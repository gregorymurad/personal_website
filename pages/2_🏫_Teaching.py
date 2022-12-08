import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide",page_icon="🦋",)

st.title("Teaching 🏫")

st.markdown("---")
st.sidebar.image("Images/landscape.png")
st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor's Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("[Linkedin](https://www.linkedin.com/in/gregorymurad)")
st.sidebar.write("+1(305)348-7852")

st.subheader("Teaching Evaluation")
def plot_charts(df,course_name):
    course_fig = px.line(df,
                         x="Semester",
                         y=["Course Structure","Learning Support","Student-Instructor Interaction", "Overall Assessment"],
                         markers=True)
    course_fig.update_layout(

    )
    course_fig.update_layout({
    "plot_bgcolor": "rgb(232, 233, 234)",
    "paper_bgcolor": "rgba(0, 0, 0,0)",
    })
    course_fig.update_layout(title=course_name,
                      xaxis_title='Semesters',
                      yaxis_title='Score',
                      title_font_color="#74DCBE",
                      title_font_size=20,
                      yaxis_range=[1, 5])
    st.plotly_chart(course_fig, use_container_width=True)

# cop4555 Plots
cop4555 = pd.read_csv("Logs/Courses/cop4555-Table 1.csv")
plot_charts(cop4555,"COP 4555 - Principles of Programming Languages")

# cop4814 Plots
cop4814 = pd.read_csv("Logs/Courses/cop4814-Table 1.csv")
plot_charts(cop4814, "COP 4814 - Component-Based Software Development")

# cap4104 Plots
cap4104 = pd.read_csv("Logs/Courses/cap4104-Table 1.csv")
plot_charts(cap4104, "CAP 4104 - Human-Computer Interaction for Computer Science")

# cen3721 Plots
cen3721 = pd.read_csv("Logs/Courses/cen3721-Table 1.csv")
plot_charts(cen3721, "CEN 3721 - Introduction to Human-Computer Interaction")

# cop4813 Plots
cop4813 = pd.read_csv("Logs/Courses/cop4813-Table 1.csv")
plot_charts(cop4813, "Web Application Programming")

overall_score_df = pd.DataFrame(cop4555["Overall Assessment"]
                             .append(cop4814["Overall Assessment"])
                             .append(cap4104["Overall Assessment"])
                             .append(cen3721["Overall Assessment"])
                             .append(cop4813["Overall Assessment"]))
# st.dataframe(overall_score_df.reset_index())
overall_score=overall_score_df["Overall Assessment"].sum()/overall_score_df["Overall Assessment"].size
st.write("My overall score is currently {:.1f} out of 5.0.".format(overall_score))
st.markdown("---")
st.subheader("Courses Taught")
courses_taught = pd.read_csv("Logs/Courses/Courses Taught.csv")
st.dataframe(courses_taught)
st.markdown("---")
st.subheader("Teaching Philosophy")
st.markdown(
    "My primary goal in education is to help students become self-motivated, confident and prepared to expand their limits. I have learned that no two students are equal, they have a diverse array of backgrounds, strengths and learning styles. I strive to ignite the initial spark that make students curious, engaged and excited to take their knowledge forward. I believe that information needs to be meaningful so that the students will be able to store, retrieve and make it into long-term memory. Students retain information better when the objectives of a course are clear and specific rather than diffuse. Active learning is used in most of my classes. Students need to notice, reflect on results and get feedback. Furthermore, they learn by doing, redoing and reflecting, not simply watching and listening. The objective of the class goes way beyond covering the syllabus, I care about how to cause the students to learn and entice them to enjoy the action of learning. I aim at creating a supportive environment with double-sided communication, cooperative learning and teamwork activities. I strive to make my assessments match the goals and be fair. These goals must be clear to the students and observable to me. I provide study guides, hands-on activities and use instructional technology tools (e.g. course management systems, simulations and interactive multimedia tutorials). I relate the concepts covered in the material with real life examples, research and industry applications, and motivate the students by showing them how important the concepts are for their careers and even daily life. I avoid content overload and develop tasks that require critical thinking, creativity, dialogue and collaboration. I provide my students the ability to learn new skills while adapting to a changing industry. The consciousness of the freedom we have is the power each of us has to transform our reality. We live a perpetual pedagogical process that exists from the “problem-posing” way which our education is built upon. As Paulo Freire constantly discussed in his book “Pedagogy of the oppressed”, the banking concept of education has turned great students into a box of deposited information, with no critical thinking, problem-solving skills and relation to real life. The contents of STEM-based courses are intrinsic to the environment we live in. A student should be able to identify problems, raise questions, develop and apply techniques and evaluate results. We exist with the world and understanding its nature needs to be done passionately and responsibly. That is how I lead my classes and I intend to continue doing so for my entire life. Written by Gregory Murad Reis in December 2017")
