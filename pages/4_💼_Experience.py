import streamlit as st


st.set_page_config(page_icon="π¦")

st.title("Experience πΌ")
st.markdown("---")
st.header("Work Experience π»")


st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("+1(305)348-7852")


def make_grid(cols, rows):
    grid = [0] * cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows)
    return grid

mygrid = make_grid(7, (2, 4, 6))

# ROW 0
mygrid[0][0].markdown("""
2021 - Present
""")

mygrid[0][1].markdown("""
**Assistant Teaching Professor**
""")

mygrid[0][2].markdown("""
[Knight Foundation School of Computing and Information Sciences](https://www.cis.fiu.edu/), FIU, USA πΊπΈ
""")

# ROW 1
mygrid[1][0].markdown("""
2019 - Present
""")

mygrid[1][1].markdown("""
**Affiliated Faculty / Researcher**
""")

mygrid[1][2].markdown("""
[The Institute of Environment](https://crestcache.fiu.edu/), FIU, USA πΊπΈ
""")

# ROW 2
mygrid[2][0].markdown("""
2016 - Present
""")

mygrid[2][1].markdown("""
**Robotics Coordinator**
""")

mygrid[2][2].markdown("""
[The UKG Academy for Computer Science Education](https://academy.cis.fiu.edu/), FIU, USA πΊπΈ
""")

# ROW 3
mygrid[3][0].markdown("""
2018 - 2020
""")

mygrid[3][1].markdown("""
**Visiting Instructor**
""")

mygrid[3][2].markdown("""
[Knight Foundation School of Computing and Information Sciences](https://www.cis.fiu.edu/), FIU, USA πΊπΈ
""")

# ROW 4
mygrid[4][0].markdown("""
2014 - 2018
""")

mygrid[4][1].markdown("""
**Graduate Assistant**
""")

mygrid[4][2].markdown("""
[Motion, Robotics, and Automation Laboratory](https://robotics.cs.fiu.edu/robotics/), FIU, USA πΊπΈ
""")

# ROW 5
mygrid[5][0].markdown("""
2013 - 2014
""")

mygrid[5][1].markdown("""
**Adjunct Professor**
""")

mygrid[5][2].markdown("""
[Technology and Exact Sciences Institute](https://icet.ufla.br/), Federal University of Lavras, Brazil π§π·
""")

# ROW 6
mygrid[6][0].markdown("""
2009 - Present
""")

mygrid[6][1].markdown("""
**Software Engineer / Co-Founder**
""")

mygrid[6][2].markdown("""
[Dez Real Estate LLC](https://www.diariocidade.com/mg/lavras/guia/dez-imobiliaria-ltda-10874102000190/), Brazil π§π·
""")

st.markdown("---")
st.header("Education π")

mygrid2 = make_grid(3, (2, 4, 6))

# ROW 0
mygrid2[0][0].markdown("""
2014 - 2018
""")

mygrid2[0][1].markdown("""
**Ph.D. in Computer Science**
""")

mygrid2[0][2].markdown("""
[Knight Foundation School of Computing and Information Sciences](https://www.cis.fiu.edu/), FIU, USA πΊπΈ
""")

# ROW 1
mygrid2[1][0].markdown("""
2012 - 2014
""")

mygrid2[1][1].markdown("""
**M.S. in Systems Engineering**
""")

mygrid2[1][2].markdown("""
[Engineering Department](https://sigaa.ufla.br/sigaa/public/programa/portal.jsf?lc=pt_BR&id=1801), Federal University of Lavras, Brazil π§π·
""")

# ROW 2
mygrid2[2][0].markdown("""
2008 - 2012
""")

mygrid2[2][1].markdown("""
**B.S. in Computer Science**
""")

mygrid2[2][2].markdown("""
[Technology and Exact Sciences Institute](https://icet.ufla.br/graduacao/ciencia-computacao-bacharelado), Federal University of Lavras, Brazil π§π·
""")

st.markdown("---")