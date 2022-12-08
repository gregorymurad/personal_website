import streamlit as st


st.set_page_config(
    page_title="Gregory Murad Reis, PhD",
    page_icon="🦋",
    layout="wide",
    initial_sidebar_state="expanded")

col1, col2, col3, col4 = st.columns(4,gap="small")
with col1:
    st.write("")
with col2:
    st.image("Images/profile.png")
with col3:
    st.title("Gregory Murad Reis")
    st.write("Marine Robotics • Artificial Intelligence • STEM Education")
with col4:
    st.write("")
st.markdown("---")
st.sidebar.image("Images/landscape.png")
st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor's Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("[Linkedin](https://www.linkedin.com/in/gregorymurad)")
st.sidebar.write("+1(305)348-7852")



st.markdown("""My name is Gregory Murad Reis, I am an **Assistant Teaching Professor** 
            at FIU and a **Researcher** at the Institute of Environment. I study 
            the ways we can use Computer Science and Robotics to help solve the 
            biggest challenges in the marine environment. \n \n I have published papers in the areas of Marine Robotics and Artificial Intelligence. I also
            develop curriculum in robotics for the K12 system in the USA and Brazil.""")
st.markdown("---")
def make_grid(cols, rows):
    grid = [0] * cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

mygrid = make_grid(4, (2, 2, 2))

# ROW 0
mygrid[0][0].markdown("""
#### Excellence in Teaching Award 2022
""")

mygrid[0][1].markdown("""
#### Interview to Mongabay - Building back Miami’s Biscayne Bay
""")

mygrid[0][2].markdown("""
#### Interview to WPLG Miami - Saving Biscayne Bay
""")

# ROW 1
mygrid[1][0].write("""
Teaching Excellence Award 2022 - Award received by the Knight Foundation School of Computing and Information Sciences
at Florida International University, Miami, FL, on December 6th 2022.
""")

mygrid[1][1].write("""
In August 2020, dead fish, rays and other marine life turned up dead on the Miami 
coastline due to critically low dissolved oxygen levels caused by several factors
 including heavy rainfall, higher temperatures, salinity imbalances, nutrient pollution
  and seagrass dieoff. Researchers at Florida International University are testing
   autonomous vessels to collect data on the bay’s conditions and prevent tragedies 
   like the August 2020 fish kill. [Source](https://news.mongabay.com/2021/07/building-back-miamis-biscayne-bay-do-natural-solutions-hold-hope/)
""")

mygrid[1][2].write("""
This special covered the relentless efforts to rescue Biscayne Bay in Florida.
 Researchers Dr Todd Crowl, Dr Gregory Reis, Bradley Schonhoff and Daniel Correa from
  FIU are working together to develop new technologies in Robotics and Data Science 
  to investigate the factors that could have contributed to the massive fish kill. 
  This special was aired on WPLG Local 10 News in Miami, FL, on Friday, April 2nd at 5:30pm. [Source](https://www.local10.com/news/local/2021/04/02/saving-biscayne-bay-researchers-worry-about-risk-of-another-fish-kill-this-summer/)
""")

# ROW 2
mygrid[2][0].image("Images/IMG_7404.jpg")

mygrid[2][1].image("Images/IMG_7429.jpg")

mygrid[2][2].image("Images/3_robot_2.jpg")

# ROW 3
mygrid[3][0].video("https://www.youtube.com/watch?v=ip-NsjxCfNg&feature=emb_title&ab_channel=GregoryMuradReis")

mygrid[3][1].video("https://www.youtube.com/watch?v=j82pP18wFe8&ab_channel=Mongabay")

mygrid[3][2].video("https://www.youtube.com/watch?v=qOFmkouoJXM&ab_channel=GregoryMuradReis")