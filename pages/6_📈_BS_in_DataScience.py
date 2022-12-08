import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(layout="wide")

st.title("Bachelor of Science in Data Science - FIU KFSCIS")
st.subheader("Distribution of the Required Subject Areas in Different Data Science Programs")


df = pd.read_csv("Logs/universities-comparison.csv")

uni = df.columns[1:].tolist()
numberOfRows = df.shape[0]

options = st.multiselect(
    "Comparison of the percentage of required courses in different subject areas in various Data Science programs. Choose the universities.",
    ['MIT', 'University of California Irvine', 'Florida Polytechnic University', 'University of San Francisco', 'University of Central Florida', 'Purdue', 'University of Illinois Chicago', 'University of Southern California', 'University of California Berkeley', 'University of Florida', 'Stanford', 'University of California Santa Barbara'])

# st.write('You selected:', options[0])

df_mod=df[["Subjects"] + options]

plot3 = go.Figure(data=[
        go.Bar(
            name=options[i],
            x=df_mod["Subjects"],
            y=df_mod.iloc[0:, i + 1])
        for i in range(len(options))])
st.plotly_chart(plot3,use_container_width=True)

if len(options)>0:
    df_mod['Mean'] = df_mod.iloc[:,1:].mean(axis=1)
    st.write("Average percentage of the subject areas considering the selected universities")
    st.dataframe(df_mod[['Subjects','Mean']])

_2DColumn = st.checkbox("Click here to see the distribution of subjects across all universities in a 2D column plot")
if _2DColumn:
    plot1 = go.Figure(data=[
        go.Bar(
            name=uni[i],
            x=df["Subjects"],
            y=df.iloc[0:, i + 1])
        for i in range(len(uni))])
    st.plotly_chart(plot1,use_container_width=True)

stackedColumn = st.checkbox("Click here to see the distribution of subjects across all universities in a stacked column plot")
if stackedColumn:
    plot2 = go.Figure(data=[
        go.Bar(
            name=df["Subjects"].iloc[i],
            x=uni,
            y=df.iloc[i, 1:])
        for i in range(numberOfRows)])
    plot2.update_layout(barmode="stack")
    st.plotly_chart(plot2,use_container_width=True)

links={
    "MIT":"http://catalog.mit.edu/degree-charts/computer-science-economics-data-science-course-6-14/",
    "University of California Irvine":"https://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofstatistics/datascience_bs/#requirementstext",
    "Florida Polytechnic University":"http://catalog.floridapoly.edu/preview_program.php?catoid=25&poid=1053&returnto=1541",
    "University of San Francisco":"https://www.usfca.edu/arts-sciences/programs/undergraduate/data-science/program-overview",
    "University of Central Florida":"https://www.ucf.edu/degree/data-science-bs/",
    "Purdue":"https://www.cs.purdue.edu/undergraduate/curriculum/datascience-req-fall2020.html",
    "University of Illinois Chicago":"https://catalog.uic.edu/ucat/colleges-depts/engineering/cs/bs-data-science-computer-science/",
    "University of Southern California":"https://datascience.usc.edu/academics/bachelor-of-arts-in-data-science/",
    "University of California Berkeley":"https://data.berkeley.edu/academics/data-science-undergraduate-studies/data-science-major/requirements-upper-division",
    "University of Florida":"https://catalog.ufl.edu/UGRD/colleges-schools/UGLAS/DAT_BS/#modelsemesterplantext",
    "University of California Santa Barbara":"https://www.pstat.ucsb.edu/undergrad/majors/bs-ss",
    "Stanford":"https://datasciencemajor.stanford.edu/academics/undergraduate-bs-program/bs-degree-requirements"
}

uni2=uni
uni2.insert(0,"")
university = st.selectbox("Choose a University",
                          options=uni2)

if university:
    i=uni.index(university)
    fig = px.pie(df[:], values=uni[i], names='Subjects')
    st.plotly_chart(fig,use_container_width=True)
    st.write("[Program Overview]({})".format(links[university]))

st.subheader("Most Common Required Classes")

directory ="course_files"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        course = pd.read_csv(f)
        course.set_index("Course Name")
        course=course.sort_values(by=['Count'],ascending=False)

        course_fig = px.bar(course,x="Course Name",y="Count",title="Most Common Required Courses in {}".format(f[13:-4]))
        # course_fig.update_traces(marker_color='red')
        course_fig.update_layout(
            font=dict(
                size=20,
                color="RebeccaPurple"),
            title_font_color="orange",
            title_font_size=20
        )
        st.plotly_chart(course_fig,use_container_width=True)
        with st.expander("Click here to see the table"):
            st.dataframe(course)

st.subheader("FIU-KFSCIS - Undergraduate Program Flowcharts")
st.write("[Flowcharts](https://users.cs.fiu.edu/~prabakar/upc/flowcharts/)")
st.markdown("---")
st.sidebar.image("Images/landscape.png")
st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor's Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("[Linkedin](https://www.linkedin.com/in/gregorymurad)")
st.sidebar.write("+1(305)348-7852")