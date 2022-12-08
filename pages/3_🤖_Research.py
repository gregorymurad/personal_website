import streamlit as st
import numpy as np
import pandas as pd
from typing import List
import pydeck as pdk
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(layout="wide",page_icon="🦋",)

st.title("Research 🤖")

st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("+1(305)348-7852")

st.subheader("Areas of Interest")
st.markdown("""My research interests intersect the areas of **Marine Robots**, **Persistent Ocean Monitoring**, **Artificial Intelligence**, and **STEM Education**.
\n
Key problems I have addressed so far include: localization and navigation of underwater robots in GPS-denied environments, analysis of the spatio-temporal dynamics of the ocean, data analysis of water profiles, persistent monitoring of the ocean using under-actuated robots, and artificial intelligence models applied to agriculture and welfare of poultry.
Recently, I have studied the integration of active learning into Software Engineering and Programming synchronous remote learning environments and how to effectively implement and assess robotics educational platforms in the K-12 curriculum.
\n
So far I have published [**20 articles**](https://www.researchgate.net/profile/Gregory-Reis#publications) and I have [**134 citations**](https://www.researchgate.net/profile/Gregory-Reis).""")
st.markdown("---")
st.subheader("Research Grants and Awards")
st.markdown("""
- **Excellence in Teaching** - Best Teaching Faculty of 2022
- **Senior Personnel** - **NSF (National Science Foundation)** - CREST Phase II: Center for Aquatic Chemistry and Environment (CAChE) - $5,000,000.00 - August 2021 - July 2026
- **Co-PI** - **DoD (US Department of Defense)** - Acquisition of a Combined Aerial and Underwater Motion Capture System - $600,000.00 - April 2021 - March 2023
- **Co-I/Senior Investigator** - **NSF (National Science Foundation)** - RET in Engineering and Computer Science SITE: Research Experience for Teachers on Cyber-Enabled Technologies - $600,000.00 - March 2021 - February 2024 Award Info
- **Co-PI** - **Microsoft Philanthropies** - Development of Teacher Trainings and Professional Workshops in Robotics partnered with nonprofit Miami EdTech, local chapter of CS Teacher's Association, and Miami-Dade County Public Schools - $195,000.00 - May 2020 - May 2022
- **PhD Fellow** - **CAPES (Coordination for the Improvement of Higher Education Personnel)** - Augmented Terrain-Based Navigation To Enable Persistent Autonomy For Underwater Vehicles In GPS-Denied Environments - $146,004.10 - August 2014 - Summer 2018
""")
st.markdown("---")
st.subheader("Mentoring")