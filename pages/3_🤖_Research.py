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
st.markdown("---")
st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("+1(305)348-7852")

st.header("Areas of Interest")
st.markdown("""My research interests intersect the areas of **Marine Robots**, **Persistent Ocean Monitoring**, **Artificial Intelligence**, and **STEM Education**.
\n
Key problems I have addressed so far include: localization and navigation of underwater robots in GPS-denied environments, analysis of the spatio-temporal dynamics of the ocean, data analysis of water profiles, persistent monitoring of the ocean using under-actuated robots, and artificial intelligence models applied to agriculture and welfare of poultry.
Recently, I have studied the integration of active learning into Software Engineering and Programming synchronous remote learning environments and how to effectively implement and assess robotics educational platforms in the K-12 curriculum.
\n
So far I have published [**20 articles**](https://www.researchgate.net/profile/Gregory-Reis#publications) and I have [**134 citations**](https://www.researchgate.net/profile/Gregory-Reis).""")
st.markdown("---")
st.header("Research Grants")
st.markdown("""
- **Senior Personnel** - **NSF (National Science Foundation)** - CREST Phase II: Center for Aquatic Chemistry and Environment (CAChE) - **$5,000,000.00** - August 2021 - July 2026
- **Co-PI** - **DoD (US Department of Defense)** - Acquisition of a Combined Aerial and Underwater Motion Capture System - **$600,000.00** - April 2021 - March 2023
- **Co-I/Senior Investigator** - **NSF (National Science Foundation)** - RET in Engineering and Computer Science SITE: Research Experience for Teachers on Cyber-Enabled Technologies - **$600,000.00** - March 2021 - February 2024 Award Info
- **Co-PI** - **Microsoft Philanthropies** - Development of Teacher Trainings and Professional Workshops in Robotics partnered with nonprofit Miami EdTech, local chapter of CS Teacher's Association, and Miami-Dade County Public Schools - **$195,000.00** - May 2020 - May 2022
- **PhD Fellow** - **CAPES (Coordination for the Improvement of Higher Education Personnel)** - Augmented Terrain-Based Navigation To Enable Persistent Autonomy For Underwater Vehicles In GPS-Denied Environments - **$146,004.10** - August 2014 - Summer 2018
""")

st.markdown("---")
st.header("Awards")
st.markdown("""
- **Excellence in Teaching 2022** - Best Teaching Faculty by KFSCIS at Florida International University, Miami, FL
- **Best Student Award 2019** - Gammon Presbyterian Institute
- **TOP 20 Best Student Poster Competition** - at the MTS/IEEE OCEANS, Marseille, France, June 2019
- **TOP 20 Best Student Poster Competition** - at the MTS/IEEE OCEANS, Charleston, SC, USA, October 2018
- **TOP 20 Best Student Poster Competition** - at the MTS/IEEE OCEANS, Kobe, Japan, May 2018
- **TOP 20 Best Student Poster Competition** - at the MTS/IEEE OCEANS, Aberdeen, Scotland, June 2017
""")

st.markdown("---")
st.header("Research Articles")
st.subheader("Journal Papers")
st.markdown("""
- [J6] Redwan Newaz, A. Al.; Alam, T.; **Reis, G.M.**; Bobadilla, L.; and Smith, R. N. "Long-Term Autonomy for AUVs Operating Under Uncertainties in Dynamic Marine Environments", Published in IEEE Robotics and Automation Letters, VOL. 6, No. 4, October 2021.

- [J5] Fitzpatrick, M., **Reis, G.M.**, Anderson, J., Bobadilla, L., Alsabban, W., Smith, R. Development of Environmental Niche Models for Use in Underwater Vehicle Navigation. IET Cyber-Systems and Robotics, 2020.

- [J4] Alam, T.; **Reis, G.M.**; Bobadilla, L.; and Smith, R. N. "A Data-Driven Deployment and Planning Approach for Underactuated Vehicles in Marine Environments", in IEEE Journal of Oceanic Engineering, 2020.

- [J3] Schiassi, L; Junior, T. Y.; **Reis, G.M.**; Abreu, L. H. P.; Campos, A. T.; Castro, J. O. "Fuzzy modeling applied in the evaluation of broiler performance", in Revista Brasileira de Engenharia Agricola e Ambiental, Campina Grande, PB, BR, February 2015.

- [J2] Ferraz, P. F. P.; Junior, T. Y.; Julio, Y. F. H.; Castro, J. O.; Gates, R. S.; **Reis, G.M.**; Campos, A. T., "Predicting Chick Body Mass by Artificial Intelligence-Based Models", in Brazilian Journal of Agricultural Research, v. 49. n. 7, p. 559-568, July 2014.

- [J1] Schiassi, L.; Junior, T. Y.; Abreu, L. H. P.; **Reis, G.M.**, Damasceno, F. A.; Silva, G. C. A.; Campos, A. T. "Laboratory Proposal for Studies on Poultry Environment", in International Journal of Engineering Research and Applications, 2014.
""")
st.subheader("Conference Papers")
st.markdown("""
- [C13] Rojas, C.; **Reis, G.M.**; Albayrak, A. R.; Osmanoglu, B.; Bobadilla, L; Smith, R. N. "Combining Remote and In-situ Sensing for Persistent Monitoring of Water Quality", in "Combining Remote and In-situ Sensing for Persistent Monitoring of Water Quality," OCEANS 2022 - Chennai, 2022, pp. 1-6.

- [C12] Redwan Newaz, A. Al.; Alam, T.; **Reis, G.M.**; Bobadilla, L.; and Smith, R. N. "Long-Term Autonomy for AUVs Operating Under Uncertainties in Dynamic Marine Environments", Accepted at the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS) 2021.

- [C11] Torres, A.; **Reis, G.M.**; Absten, J.; Briceno, H. O.; Bobadilla, L.; Smith, R. N. "Correlating Water Quality and Profile Data in the Florida Keys", Accepted in Proceedings of MTS/IEEE OCEANS, Seattle, Washington, USA, October 2019.

- [C10] Bayuelo, A.; Alam, T.; **Reis, G.M.**; Nino, L. F.; Bobadilla, L.; and Smith, R. N. "Toward Simultaneous Localization and Mapping in Aquatic Dynamic Environments", Accepted in Proceedings of MTS/IEEE OCEANS, Marseille, France, June 2019. (Best Student Paper Finalist)

- [C9] **Reis, G.M.**; Alam, T.; Bobadilla, L.; and Smith, R. N. "Feedback-Based Informative AUV Planning from Kriging Errors", Proceedings of IEEE/OES Autonomous Underwater Vehicle (AUV) Symposium, Porto, Portugal, November 2018.

- [C8] Alam, T.; **Reis, G.M.**; Bobadilla, L.; and Smith, R. N. "An Underactuated Vehicle Localization Method in Marine Environments", in Proceedings of MTS/IEEE OCEANS Conference, pp. 1-8, Charleston, SC, USA, October 2018. (Best Student Paper Finalist)

- [C7] Alam, T.; **Reis, G.M.**; Bobadilla, L.; Smith, R. N. "A Data-Driven Deployment Approach for Persistent Monitoring in Aquatic Environments", Accepted in IEEE International Conference on Robotic Computing, Laguna Hills, CA, USA, February 2018.

- [C6] **Reis, G.M.**; Leon, H.; Alam, T.; Anderson, J.; Bobadilla, L.; Smith, R. N. "A Whitening-based Tracking Algorithm for Autonomous Underwater Vehicles", in Marine Technology Society/IEEE Oceans, Kobe, Japan, May 2018.

- [C5] Alam, T.; **Reis, G.M.**; Bobadilla, L.; Smith, R. N. "A Data-Driven Planning with the Persistent Behavior Analysis of a Marine Environment", in Marine Technology Society/IEEE Oceans, Kobe, Japan, 2018 (TOP 20).

- [C4] **Reis, G.M.**; Fitzpatrick, M.; Bobadilla, L.; Anderson, J.; Smith, R.N., "Increasing Persistent Navigation Capabilities for Underwater Vehicles with Augmented Terrain-Based Navigation", in Marine Technology Society/IEEE Oceans, Aberdeen, Scotland, June 2017 (Best Student Paper Finalist)

- [C3] **Reis, G.M.**; Fitzpatrick, M.; Bobadilla, L.; Anderson, J.; Smith, R.N., "Augmented Terrain-Based Navigation to Enable Persistent Autonomy for Underwater Vehicle", in IEEE International Conference on Robotic Computing, Taichung, Taiwan, pp. 1 - 7, 2017

- [C2] Mileyko, Y.; **Reis, G.M.**; Chyba, M.; Smith, R.N., "Energy-Efficient Control Strategies for Updating an Augmented Terrain-Based Navigation Map for Autonomous Underwater Navigation", in IEEE Conference on Control Technology and Applications, Kohala Coast, Hawaií, 2017.

- [C1] Ponciano, P. F.; Yanagi Junior, T.; Alvarenga, T. A. C.; **Reis, G.M.**; Campos, A. T. "Behavior of Chicks Subjected to Heat Stress", in XLII Brazilian Conference of Agricultural Engineering, Fortaleza, 2013.
""")

st.markdown("---")
st.header("Planned Infrastructure")

st.image("Images/3_robot_4.png",use_column_width=True)
st.caption("Network of autonomous marine vehicles, buoys, and aerial drones for real-time environmental monitoring.")
