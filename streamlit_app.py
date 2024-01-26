import streamlit as st
import pandas as pd
df=pd.read_csv("movie_data.csv")
si_data=pd.read_csv("similarity_dataframe")

def movie_display_all(index):      
    name=df['Name'][index]
    year=df['Year'][index]
    rating=df['Rating'][index]
    poster_url=df['Poster_url'][index]
    movie_url=df['Movie_url'][index]
    storyline=df['Storyline'][index]
    col1, col2 = st.columns([1,3])
    with col1:
        container = st.container(border=False,height=250)
        container.image(poster_url)
    with col2:
        container = st.container(border=False,height=180)
        container.subheader(name)
        container.write(f'Year of Release: {year}, Rating: {rating}')
        with st.expander(f'Movies similar to "{name}"'):
            list_of_silimiar_movies=si_data[si_data['0']==df[df['Name']==name].iloc[0]['Index']].iloc[0][1:6]
            for i in list_of_silimiar_movies:
                movie_display(i)
        container.write(f'Storyline: {storyline}')
    

def movie_display(index): 
    name=df['Name'][index]
    name=df['Name'][index]
    year=df['Year'][index]
    rating=df['Rating'][index]
    poster_url=df['Poster_url'][index]
    movie_url=df['Movie_url'][index]
    storyline=df['Storyline'][index]
    col1, col2 = st.columns([1,3])
    with col1:
        container = st.container(border=False,height=250)
        container.image(poster_url)
    with col2:
        container = st.container(border=False,height=250)
        container.subheader(name)
        container.write(f'Year of Release: {year}, Rating: {rating}')
        container.write(f'Storyline: {storyline}')
    


def main():
    st.title('Find movies similar to your favourite movie based on storylin')
    movie_name=''
    movie_name = st.selectbox('Enter your favourite Movie name', set(df['Name']))
    a=st.button('Click here')
    
    if a==False :
        for i in df['Index']:
            movie_display_all(i)
   
    if a:
        list_of_silimiar_movies=si_data[si_data['0']==df[df['Name']==movie_name].iloc[0]['Index']].iloc[0][1:6]
        for i in list_of_silimiar_movies:
            movie_display(i)
    


   


   

    


if __name__ == '__main__':
    main()      

    
