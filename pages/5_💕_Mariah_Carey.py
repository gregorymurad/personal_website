import json
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
nltk.download("punkt")
import streamlit as st
import apis
import pandas as pd
import plotly.express as px



st.set_page_config(layout="wide",page_icon="🦋",)

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #FFF8FF;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="st-ej"] {{
background: linear-gradient(to right, rgb(255,106,246) 0%, rgb(255,106,246) 25%, rgba(151, 166, 195, 0.25) 25%, rgba(151, 166, 195, 0.25) 100%);
}}

[data-testid="css-demzbm"] {{
webkit-box-align: center;
align-items: center;
background-color: #FF6AF6;
border-radius: 100%;
border-style: none;
box-shadow: none;
display: flex;
height: 0.75rem;
-webkit-box-pack: center;
justify-content: center;
width: 0.75rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4,gap="small")
with col1:
    st.write("")
with col2:
    st.image("Images/Mariah.png")
with col3:
    st.title("Mariah Carey")
    st.subheader("The Butterfly Project 🦋")

with col4:
    st.write("")
st.markdown("---")
st.markdown("#### Get to know more about Mariah Carey's incredible discography."
            " With 19 #1 hits (18 self penned), Mariah officially holds "
            "the record for the most chart-topping singles by a solo artist,"
            " a female songwriter, and a female producer. Mariah has also"
            " broken the record for any superstar in US history after "
            "spending a total record of 87 weeks at #1.")
st.markdown("---")


with open("discography.json","r") as read_file:
    discography = json.load(read_file)


def lyricsCleaner(lyrics: str) -> str:
    """ This function takes a string as input and returns the same
    string (lower case) without [] including what's inside, () keeping
    what is inside, and \n """
    modified_lyrics = re.sub(r"\[.*?\]", "", lyrics)
    modified_lyrics2 = modified_lyrics.replace("(", "").replace(")", "")
    return modified_lyrics2.replace("\n", " ").lower()


def lyricsToList(lyrics: str) -> list:
    """ This function takes a string as input, removes [] including
    what is inside, () keeping what is inside, and \n, and returns a
    list of words (lower case) """
    modified_lyrics = re.sub(r"\[.*?\]", "", lyrics)
    modified_lyrics2 = modified_lyrics.replace("(", "").replace(")", "")
    verses=modified_lyrics2.split('\n')
    words=[word.lower() for i in verses for word in i.split()]
    return words


def get_lyrics(album_title = None, year = None) -> str:
    all_lyrics = ""
    if album_title:
        for j in discography["albums"]:
            if j["album_title"] == album_title:
                for i in j["tracks"]:
                    all_lyrics += lyricsCleaner(i["lyrics"])
        return all_lyrics
    elif year:
        for j in discography["albums"]:
            if j["date"] == year:
                for i in j["tracks"]:
                    all_lyrics += lyricsCleaner(i["lyrics"])
        return all_lyrics
    else:
        for j in discography["albums"]:
            for i in j["tracks"]:
                all_lyrics += lyricsCleaner(i["lyrics"])
        return all_lyrics


def clean_lyrics(tokens, stopwords, pronouns=None):
    clean_tokens = []
    if pronouns:
        stopwords = stopwords+pronouns
    for word in tokens:
        if word not in stopwords:
            clean_tokens.append(word)
    return clean_tokens


def filter_by_length(list_of_tuples,l):
    filtered_list=[t for t in list_of_tuples if len(t[0])>=l]
    return filtered_list


def generate_frequency_distribution(lyrics):
    stopwords = ["\'s", ",", "to", "and", "a", "an", "so", "not",
                 "through", "the", "of", "that", "out", "at",
                 "from", "by", "for", "off", "on", "in", "'ve",
                 "are", "is", "n't", "'ll", "do", "will", "did",
                 "would", "can", "could", "'re", "'m", "na", "no",
                 "ca", "wo", "was", "were", "got", "even", "gon",
                 "it", "?", "but", "oh", "ooh", "da", "'", "with",
                 "what", "when", "which", "just", "yeah", "up",
                 "down", "be", "ha", "uh", "huh", "about", "ta",
                 "this", "that", "those", "these", "da", "o", "'",
                 "t", "s", "ho"]
    pronouns = ["they", "them", "their", "theirs",
                "you", "your", "yours",
                "i", "me", "my", "mine",
                "he", "him", "his",
                "she", "her", "hers",
                "we", "our", "ours",
                "it", "its"]

    # Separate the string into a list of strings
    tokens = word_tokenize(lyricsCleaner(lyrics))

    # Remove stopwords and pronouns
    clean_tokens=clean_lyrics(tokens,stopwords,pronouns)

    # Generate the frequency distribution
    fdist = FreqDist(clean_tokens)
    most_common_words = fdist.most_common()
    return most_common_words


def generate_plot(tuples_freq_dist,title):
    # Notice that we have several words, let's show the first 10
    data = pd.DataFrame(tuples_freq_dist[:10])
    dataframe = pd.DataFrame({
        'Words': data[0],
        'Count': data[1]
    })

    fig = px.line(dataframe, x="Count", y="Words", title='', markers=True)
    fig['layout']['yaxis']['autorange'] = "reversed"
    fig.update_traces(mode='markers+lines')
    fig.update_layout({
        "plot_bgcolor": "#FFEFFE",
        "paper_bgcolor": "rgba(0, 0, 0,0)",
    })
    fig.update_layout(title=title,
                         xaxis_title='Frequency',
                         yaxis_title='',
                         title_font_color="#FF6AF6",
                         title_font_size=20,
                         yaxis_range=[1, 5],
                         font=dict(
                             size=20,
                             color="#FF6AF6"))

    fig.update_traces(line=dict(color="#FF6AF6", width=5))

    fig.update_yaxes(automargin='width')
    st.plotly_chart(fig,use_container_width=True)


st.header("Most Used Words Overall 🎤")
all_lyrics = get_lyrics()
all_lyrics_freq_dist = generate_frequency_distribution(all_lyrics)
st.write(all_lyrics_freq_dist)
word_length = st.slider('Select the minimum word length', 0, 12, 2)

filtered_by_length = filter_by_length(all_lyrics_freq_dist,word_length)
st.write(filtered_by_length)
generate_plot(filtered_by_length,"Most Frequent Used Words")

st.markdown("---")
st.header("Most Used Words per Album 🎙")


albums_names = []
for j in discography["albums"]:
    albums_names.append(j["album_title"])

album_selected = st.selectbox("Select an album",options=albums_names)

if album_selected:
    with st.expander("More info"):
        for i in discography["albums"]:
            if i["album_title"] == album_selected:
                this_album = i
        for song in this_album["tracks"]:
            col1, col2 = st.columns(2)
            with col1:
                st.write(str(song["track_number"]), "-",  song["track_title"])
                st.write("[Lyrics]({})".format(song["source"]))
            with col2:
                # st_player(song["youTube_url"])
                st.video(song["youTube_url"])

    lyrics_of_an_album = get_lyrics(album_selected)
    lyrics_of_an_album_freq_dist = generate_frequency_distribution(lyrics_of_an_album)
    generate_plot(lyrics_of_an_album_freq_dist,"Frequency Distribution")

st.markdown("---")
st.header("Most Frequent Producers 🎼")

producers = []
for j in discography["albums"]:
    for i in j["tracks"]:
        producers.extend(i["producers"])


producers_freq = FreqDist(producers)
most_common_producers = producers_freq.most_common()
generate_plot(most_common_producers,"Most Popular Producers")
st.markdown("---")
st.header("Most Frequent Songwriters ✍️")

writers = []
for j in discography["albums"]:
    for i in j["tracks"]:
        writers.extend(i["writers"])


writers_freq = FreqDist(writers)
most_common_writers = writers_freq.most_common()
generate_plot(most_common_writers, "Most Populars Writers")

st.markdown("---")
st.sidebar.image("Images/landscape.png")
st.sidebar.markdown("**Gregory Murad Reis, PhD**")
st.sidebar.write("[Professor's Webpage](https://www.cis.fiu.edu/faculty-staff/reis-gregory/)")
st.sidebar.write("[Linkedin](https://www.linkedin.com/in/gregorymurad)")
st.sidebar.write("+1(305)348-7852")