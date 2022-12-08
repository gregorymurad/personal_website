import requests
import json
import streamlit as st


def save_to_file(data,filename):
    with open(filename,'w') as write_file:
        json.dump(data,write_file,indent=2)


def read_from_file(filename):
    with open(filename,'r') as read_file:
        data = json.load(read_file)
    return data


# def request_top_artists(country_code):
#     top_artists_url="https://api.musixmatch.com/ws/1.1/" \
#         "chart.artists.get?country={0}&page_size=20" \
#         "&apikey=f5380de0a90a3929df10d87d24c77dde".format(country_code)
#     top_artists = requests.get(top_artists_url).json()
#     return top_artists
#
# def request_top_tracks(country_code,chart_name):
#     top_tracks_url="https://api.musixmatch.com/ws/1.1/" \
#          "chart.tracks.get?country={0}&chart_name={1}&page_size=20" \
#          "&apikey=f5380de0a90a3929df10d87d24c77dde".format(country_code,chart_name)
#     top_tracks = requests.get(top_tracks_url).json()
#     return top_tracks


# countries = read_from_file("countries.json")
# chart = st.selectbox("Select a chart", options=["", "top", "hot", "mxmweekly", "mxmweekly_new"])
# countries_list=list(countries.keys())
# countries_list.insert(0,"")
#
# country_selected = st.selectbox("Select a country", options=countries_list)
#
#
# if chart and country_selected:
#     country = countries[country_selected]
#     top_tracks = request_top_tracks(country,chart)
#
#     st.write(top_tracks)
#
#     lst_track = []
#     for i in top_tracks["message"]["body"]["track_list"]:
#         track_and_charts = (i["track"]["track_name"], i["track"]["artist_name"], i["track"]["track_share_url"])
#         lst_track.append(track_and_charts)
#
#     st.write(lst_track)
#
#     top_artists=request_top_artists(country)
#
#     lst_artists = []
#     for i in top_artists["message"]["body"]["artist_list"]:
#         artist = (i["artist"]["artist_name"], i["artist"]["artist_twitter_url"])
#         lst_artists.append(artist)
#
#     st.write(lst_artists)