"""

    Streamlit webserver-based Recommender Engine.

    Author: Explore Data Science Academy.

    Note:
    ---------------------------------------------------------------------
    Please follow the instructions provided within the README.md file
    located within the root of this repository for guidance on how to use
    this script correctly.

    NB: !! Do not remove/modify the code delimited by dashes !!

    This application is intended to be partly marked in an automated manner.
    Altering delimited code may result in a mark of 0.
    ---------------------------------------------------------------------

    Description: This file is used to launch a minimal streamlit web
	application. You are expected to extend certain aspects of this script
    and its dependencies as part of your predict project.

	For further help with the Streamlit framework, see:

	https://docs.streamlit.io/en/latest/

"""
# Streamlit dependencies
import streamlit as st
import streamlit_option_menu

# Set page configuration
st.set_page_config(
    page_title="META-PHOENIX",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
    )



# Main function
def main():
    # Call the function to set the CSS style
    set_style()

# Data handling dependencies
import pandas as pd
import numpy as np

# Images
from PIL import Image
import pickle

# Custom Libraries
from utils.data_loader import load_movie_titles
from recommenders.collaborative_based import collab_model
from recommenders.content_based import content_model

# Add Font Awesome CSS
st.markdown(
    """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css" integrity="sha512-3u4STHoPrpLnCjgNtw4WjpyjK0ppbZs6fF+ynwBUEIaA4sljOqHv6nW0Tz8b8UmizfRiC2VJFj6SSCAIprhpg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    </head>
    """,
    unsafe_allow_html=True
)

# Custom CSS styles
custom_styles = """
<style>
body {
    color: black;
    background-color: silver;
}

/* Custom styles for sidebar */
[data-testid="stSidebar"][class^="stSidebar"] {
    background-color: navy !important;
    color: white !important;
    width: 250px !important;
}

/* Custom styles for main content */
[data-testid="stHorizontalBlock"][class^="stHorizontalBlock"] {
    background-color: silver !important;
}

/* Custom styles for st.info */
.stAlert {
    color: navy !important;
    background-color: white !important;
    border-color: navy !important;
}

/* Custom styles for subtitles under EDA dropdown */
.st-expander p {
    color: navy !important;
}

/* Custom styles for st.title */
.stTitle {
    background-color: navy !important;
    color: white !important;
    border-color: black !important;
}

/* Custom styles for buttons */
.stButton button {
    color: white !important;
    background-color: navy !important;
    border-color: navy !important;
}

/* Custom styles for button hover and active state */
.stButton button:hover {
    background-color: white !important;
    color: navy !important;
}

.stButton button:active {
    background-color: navy !important;
    color: white !important;
}
</style>
"""

# Display custom CSS styles
st.markdown(custom_styles, unsafe_allow_html=True)

# Data Loading
title_list = load_movie_titles('resources/data/movies.csv')

# App declaration
# Main function to handle page selection
def main():
    # DO NOT REMOVE the 'Recommender System' option below, however,
    # you are welcome to add more options to enrich your app.
    page_options = ["Recommender System", "Solution Overview"]

    # -------------------------------------------------------------------
    # ----------- !! THIS CODE MUST NOT BE ALTERED !! -------------------
    # -------------------------------------------------------------------
    page_selection = st.sidebar.selectbox("Choose Option", page_options)
    if page_selection == "Recommender System":
        # Header contents
        st.write('# Movie Recommender Engine')
        st.write('### EXPLORE Data Science Academy Unsupervised Predict')
        st.image('resources/imgs/Image_header.png',use_column_width=True)
        
        # Recommender System algorithm selection
        sys = st.radio("Select an algorithm",
                       ('Content Based Filtering',
                        'Collaborative Based Filtering'))
        
       # User-based preferences
        st.write('### Enter Your Three Favorite Movies')
        movie_1 = st.selectbox('Fisrt Option',title_list[14930:15200])
        movie_2 = st.selectbox('Second Option',title_list[25055:25255])
        movie_3 = st.selectbox('Third Option',title_list[21100:21200])
        fav_movies = [movie_1,movie_2,movie_3]

        # Perform top-10 movie recommendation generation
        if sys == 'Content Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = content_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                                We'll need to fix it!")

        if sys == 'Collaborative Based Filtering':
            if st.button("Recommend"):
                try:
                    with st.spinner('Crunching the numbers...'):
                        top_recommendations = collab_model(movie_list=fav_movies,
                                                            top_n=10)
                    st.title("We think you'll like:")
                    for i,j in enumerate(top_recommendations):
                        st.subheader(str(i+1)+'. '+j)
                except:
                    st.error("Oops! Looks like this algorithm does't work.\
                                We'll need to fix it!")

        st.markdown("### ")
        st.write("")
    # -------------------------------------------------------------------

    # ------------- SAFE FOR ALTERING/EXTENSION -------------------------

        # User Feedback - Rating and Feedback
        # Get the selected movie rating from the slider
        selected_movie_rating = st.slider("Rate the recommended movie", 1, 5)

        # Convert the rating to stars
        stars = ''.join(['<span class="star">&#9733;</span>' for _ in range(selected_movie_rating)])

        # Display the star rating pattern using Markdown and HTML
        st.markdown(f'<p style="font-size: 30px;">{stars}</p>', unsafe_allow_html=True)

        user_feedback = st.text_input("Provide feedback on the recommended movie")
        # Submit button to capture user feedback
        submit_button = st.button("Submit")

        # Handle user feedback submission
        if submit_button:
        # Process the user feedback (e.g., store in a database, perform analysis, etc.)
            st.write("Thank you for your feedback!")    

    # Display the Solution Overview page
    if page_selection == "Solution Overview":

        # Custom CSS styles for st.title
        custom_styles = """
        <style>
        /* Custom styles for st.title */
        .stTitle {
            background-color: white !important;
            color: navy !important;
            border: 2px solid navy !important;
            padding: 0.5rem;
            cursor: pointer;
        }
        </style>
        """

        # Display custom CSS styles
        st.markdown(custom_styles, unsafe_allow_html=True)

        # Function to redirect to homepage when header is clicked
        @st.cache(allow_output_mutation=True)
        def redirect_to_homepage():
            st.experimental_rerun()

        st.markdown("<a class='stTitle' href='#' onclick='redirect_to_homepage()'>Home</a>", unsafe_allow_html=True)


        # Define custom CSS styles for justifying the buttons
        custom_styles = """
        <style>
        /* Custom styles for the columns */
        .stButton button {
            width: 100%;
            text-align: justify;
            margin: 0;
            padding: 0;
        }

        /* Custom styles for the content inside the buttons */
        .st-expander .stButton button {
            text-align: left;
        }

        /* Custom styles for the container */
        .st-container {
            display: flex;
            justify-content: space-between;
            width: 100%;
        }
        </style>
        """

        # Display custom CSS styles
        st.markdown(custom_styles, unsafe_allow_html=True)

        # Create a horizontal layout for the header buttons using the container
        with st.container():
            col1, col2, col3, col4 = st.columns(4)

        # Display button for "Algorithms"
        if col2.button("Algorithms"):
            with st.expander("Content-Based Filtering"):
                st.write("It is a recommendation method used in various systems, including movie recommendation platforms, that involves analyzing the characteristics or content of items to make personalized suggestions to users. In the context of movie recommendations, this approach focuses on understanding the attributes of movies, such as genres, cast members, directors, and tags, and using this information to recommend films that align with the individual user's preferences. By identifying patterns and relationships between movie attributes and user preferences, content-based filtering can provide relevant and tailored movie suggestions to each user, enhancing their movie-watching experience and driving user engagement. This method is particularly useful for film marketing as it allows content providers and film marketers to offer movies that resonate with the target audience, leading to increased viewer satisfaction, successful marketing campaigns, and ultimately, improved business outcomes.")

            with st.expander("Collaborative Filtering"):
                st.write("Collaborative filtering is a recommendation technique that focuses on leveraging user behavior and preferences to make movie suggestions. In collaborative filtering, the system analyzes the historical interactions between users and movies, such as user ratings, likes, and watch history, to find patterns and similarities among users with similar preferences. By identifying users who have shown similar interests in the past, collaborative filtering can recommend movies that have been enjoyed by users with similar tastes to the target user. This method is highly relevant to this project as it allows for the discovery of hidden connections and personalized movie recommendations based on collective user behavior. By effectively understanding and utilizing user preferences, collaborative filtering can optimize movie recommendations, boost user engagement, and foster loyal audiences, which are crucial aspects of film marketing success. By tailoring suggestions to individual users' interests, collaborative filtering can lead to increased user satisfaction, driving higher engagement rates and enhancing the overall movie-watching experience for the audience, thus supporting business growth and success in the film marketing domain.")

            with st.expander("Metrics"):
                st.write("Root Mean Squared Error (RMSE)")
                st.write("RMSE is a common metric used to evaluate the performance of prediction models, including movie recommendation algorithms. It measures the average difference between the predicted values and the actual values. In the context of this project, RMSE helps quantify how well the movie recommendation algorithm predicts user ratings compared to their actual ratings. A lower RMSE indicates that the algorithm is making more accurate predictions, resulting in better movie recommendations tailored to users' preferences. By minimizing RMSE, the film marketing strategies can deliver personalized movie suggestions that align with the audience's interests, enhancing user satisfaction, engagement, and the overall success of the film marketing campaign.")


        # Display button for "EDA"
        if col1.button("EDA"):
        # Define the content data
            content_data = [
                {
                    "subtitle": "Uncovering Audience Trends: Insights that Drive Film Marketing",
                    "content": [
                        {
                            "info": "i. Analyzing Genre Popularity Scores in Movie Ratings",
                            "description": "We aim to uncover audience trends by analyzing genre popularity scores based on movie ratings. Understanding genre popularity among audiences is essential for film marketing as it helps content providers identify which genres are most appealing to viewers and guide their content selection and marketing strategies to cater to audience preferences.",
                            "insight": "The top genre popularity scores provide valuable insights into audience trends that can drive film marketing strategies. Drama emerges as the most popular genre, followed closely by Comedy, Thriller, and Romance. These genres resonate strongly with viewers, indicating a preference for emotionally engaging and entertaining content. Film marketers can capitalize on these trends by prioritizing promotional efforts and producing more movies within these popular genres. Understanding audience preferences for Drama, Comedy, Thriller, and Romance empowers content providers to tailor their offerings to match viewers' interests, leading to increased engagement and success in film marketing campaigns. Additionally, identifying less popular genres, such as Film-Noir and IMAX, allows marketers to explore niche audience segments and potentially discover untapped opportunities for targeted marketing initiatives.",
                            "image": "https://drive.google.com/uc?id=1gBZw_yrVWH53PB43BdJ2hZLHFDjiAqdD"
                        },
                        {
                            "info": "ii. Leveraging Average Ratings",
                            "description": "We will analyze the average ratings for movie genres. Understanding these trends can drive film marketing strategies, allowing content providers and film marketers to focus on genres that receive higher average ratings, thus increasing the chances of attracting a larger audience and driving film success.",
                            "insight": "The analysis reveals that Film-Noir garners the highest average rating, highlighting its appeal to a niche audience with discerning tastes. Genres like Mystery, Documentary, Drama, and War also receive high average ratings, indicating positive reception among viewers. For film marketing strategies, this presents an opportunity to target specialized audiences who appreciate Film-Noir's distinctive characteristics. Moreover, understanding the varying levels of user satisfaction with genres such as Fantasy, Western, Thriller, Animation, Sci-Fi, (no genres listed), Musical, Crime, Romance, Comedy, Horror, Adventure, Action, Children, and IMAX allows tailoring marketing campaigns to resonate with specific audience segments. By prioritizing audience trends and preferences, film marketers can optimize content offerings, enhance audience engagement, and drive film success by delivering films that align with the unique tastes of their target viewers.",
                            "image": "https://drive.google.com/uc?id=169pTFn7yqs9Ush55xBje_4HMj8-ycH9v"
                        },
                        {
                            "info": "iii. Exploring Movie Content Relevance through Tag Analysis",
                            "description": "We will analyze the relevance scores of tags associated with movie content. These relevant tags can offer valuable information about the current trends, themes, genres, or other characteristics that are popular among the audience.",
                            "insight": "The analysis of the top 20 tags by relevance provides valuable insights into audience preferences and trends in movie content. Tags like 'original,' 'great ending,' 'storytelling,' and 'visually appealing' indicate a demand for unique narratives, strong conclusions, engaging storytelling, and visually captivating elements. Additionally, tags such as 'mentor,' 'good soundtrack,' 'melancholic,' and 'drama' suggest a preference for well-developed characters, emotionally resonant elements, and compelling drama. These insights enable film marketers to align movie selections and promotions with popular tag themes, catering to audience interests effectively and driving successful film marketing campaigns.",
                            "image": "https://drive.google.com/uc?id=1oml_vl1Kv457dstFPWo7UYKSLVMtBDob"
                        }
                    ]
                },
                {
                    "subtitle": "Understanding Audience Behavior: Key to Film Marketing Success",
                    "content": [
                        {
                            "info": "i. Visualizing Movie Ratings to Understand Audience Behavior and Preferences",
                            "description": "We visualize the distribution of movie ratings, which helps in understanding the behavior of the audience towards the movies they watch. By visualizing the frequency of different rating values, film marketers and content providers can gain insights into how the audience perceives and reacts to the movies offered.",
                            "insight": "The distribution of movie ratings provides valuable insights for understanding audience behavior and achieving film marketing success. Positive ratings between 3.0 to 5.0 indicate general audience satisfaction, with 4.0 being the most common rating. However, lower ratings in the 1.0 to 2.5 range signal potential areas for improvement, while extremely negative ratings at 0.5 require careful attention. By analyzing this distribution, film marketers can refine their strategies and content offerings to enhance audience satisfaction and success in the competitive film industry.",
                            "image": "https://drive.google.com/uc?id=1s3BpmyW5SJT1TtFxSauI6YkMlYRDrQMx"
                        },
                        {
                            "info": "ii. Exploring the Correlation between Movie Ratings, Director, and Cast Average Ratings for Effective Film Marketing",
                            "description": "We investigate the correlation between movie ratings, director average rating and cast average ratings to gain insights into audience behavior, which is crucial for film marketing success. The correlation coefficient between movie ratings, director rating and cast ratings will reveal the level of influence that directors and cast members have on audience preferences. This analysis will aid in tailoring movie suggestions to match audience preferences and enhance engagement, ultimately driving the success of our film marketing endeavors.",
                            "insight": "The strong positive correlation between movie ratings and director and cast average ratings highlights the significant influence of both directors and cast members on audience preferences and movie ratings. Users tend to consider the performances of actors and the direction of movies when rating films, leading to higher overall ratings for movies with highly-rated directors and cast members. This valuable insight can be utilized to personalize a movie recommendation based on both director and cast preferences, enhancing users' movie-watching experience. Understanding this audience behavior is crucial for film marketers to make informed decisions in promoting movies and designing successful marketing campaigns that resonate with viewers, ultimately leading to film marketing success.",
                            "image": "https://drive.google.com/uc?id=1fvcaWQlAODh8iX42cqE8kdN7gntpvSy4"
                        }
                    ]
                },
                {
                    "subtitle": "Unveiling Audience Preferences: Analyzing Viewing Patterns",
                    "content": [
                        {
                            "info": "i. Analyzing Movie Genre Viewing Patterns for Targeted Film Marketing",
                            "description": "We aim to unveil the audience preferences by analyzing the viewing patterns of movie genres. By plotting the distribution of unique movie genres in a bar chart, we gain insights into the popularity and prevalence of different genres among the audience. Understanding the audience's viewing patterns and genre preferences is crucial for content providers and film marketers to tailor their movie selections and promotional strategies to match the audience's interests, ultimately driving engagement and success in film marketing.",
                            "insight": "This analysis uncovers the audience's preferences by examining the viewing patterns of different movie genres. The results reveal that Drama, Comedy, Thriller, Romance, and Action are the most prevalent genres among the movies in our dataset, indicating a strong user preference for these categories. By understanding the demand for genres such as Horror, Documentary, Crime, Adventure, and Sci-Fi, we gain valuable insights into the audience's movie preferences. To cater to user interests effectively, we can curate a diverse collection of movies aligned with these popular genres. Moreover, the presence of emerging genres and niche categories like Children, Animation, Mystery, Fantasy, War, and Western represents opportunities for growth and expansion in the film market. Leveraging these insights empowers us to optimize our content strategy, enhance user engagement, and maximize revenue generation by delivering a compelling and personalized movie recommendation experience tailored to our audience's viewing patterns and preferences.",
                            "image": "https://drive.google.com/uc?id=1-RpaDARnDuOBZYZbVK5rW60LoCucnAu8"
                        },
                        {
                            "info": "ii. Decoding Audience Ratings",
                            "description": "We analyse the distribution of user ratings for movie genres by plotting a heatmap to provide a visual representation of how users' ratings are distributed across different genres. This analysis allows content providers and film marketers to understand the audience's rating preferences for specific genres, providing insights into which genres receive higher ratings and are more likely to resonate with the audience. This knowledge can help guide content selection, marketing strategies, and investment decisions to align with the preferences of the target audience, ultimately driving better audience engagement and success in film marketing.",
                            "insight": "The analysis of user ratings for various movie genres reveals key insights into audience preferences and viewing patterns. Drama and Comedy are the most prevalent genres, attracting a wide range of ratings and indicating broad appeal. Documentary, Horror, and Thriller genres are also popular, catering to specific content preferences. Meanwhile, genres like Western, Romance, Action, and Sci-Fi exhibit diverse rating distributions, emphasizing the importance of understanding individual viewer tastes within these categories. Niche genres such as IMAX, Children, and Film-Noir attract specific interest, while movies without listed genres receive average ratings, indicating a mixed reception. Understanding these patterns allows for tailored content recommendations, enhancing the personalized movie-watching experience and driving better audience engagement and loyalty.",
                            "image": "https://drive.google.com/uc?id=1eUFpuYgchrcWuw_0uj9BGa8oGsHb5Uoq"
                        }
                    ]
                }
            ]

            # Display the content data
            for data in content_data:
                st.subheader(data["subtitle"])
                for item in data["content"]:
                    st.write(f"**{item['info']}**")
                    st.write(item["description"])
                    st.image(item["image"], use_column_width=True)
                    st.write(item["insight"])

        # Display button for "About Us"
        if col3.button("About Us"):
            with st.expander("Filmalytics"):
                st.write("Filmalytics provides data and analytics solutions that enable clients to gain valuable insights from their data, make informed decisions in a timely manner, and consistently stay ahead of the competition.")
            
            with st.expander("Vision Statement"):
                st.write("Empowering movie enthusiasts with personalized and data-driven recommendations, revolutionizing the way people discover and enjoy films.")
            
            with st.expander("Mission Statement"):
                st.write("Our mission is to leverage the power of analytics and cutting-edge technology to provide users with an unparalleled movie recommendation experience. We strive to deliver highly accurate and tailored movie suggestions, guiding users towards their perfect film choices based on their unique preferences and past viewing behavior. Through our app, we aim to enhance the way people explore, select, and engage with movies, fostering a deeper connection and a more enjoyable cinematic journey.")

        # Display button for "FAQs"
        if col4.button("FAQs"):
            faqs = [
                {
                    "question": "How does Filmalytics recommend films?",
                    "answer": "Filmalytics utilizes advanced algorithms and data analysis techniques to recommend films based on your personal preferences, viewing history, and similar user patterns. Our system takes into account factors such as genre preferences, ratings, director, and plot keywords to provide tailored film recommendations."
                },
                {
                    "question": "How accurate are the film ratings and popularity scores in Filmalytics?",
                    "answer": "The film ratings and popularity scores in Filmalytics are based on a comprehensive aggregation of user ratings, critic reviews, and industry data. While we strive to provide accurate and up-to-date information, individual preferences may vary. We encourage users to explore and evaluate films based on their own tastes and interests."
                },
                {
                    "question": "Can I customize the film recommendations in Filmalytics?",
                    "answer": "Yes, Filmalytics offers customization options for film recommendations. You can refine your preferences, provide feedback on suggested films, and rate the movies you have watched. Our algorithms learn from your interactions to deliver more personalized recommendations over time."
                },
                {
                    "question": "Is my personal data secure in Filmalytics?",
                    "answer": "Absolutely. At Filmalytics, we prioritize user privacy and data security. We adhere to strict data protection protocols and industry best practices. Your personal information and viewing history are handled with the utmost confidentiality and are not shared with third parties without your explicit consent."
                },
                {
                    "question": "Can I access Filmalytics across different devices?",
                    "answer": "Yes, Filmalytics is designed to be accessible across various devices and platforms. You can use our app on smartphones, tablets, and desktop computers, allowing you to enjoy personalized film recommendations and explore the world of cinema wherever you go."
                },
            ]
            for faq in faqs:
                with st.expander(faq["question"]):
                    st.write(faq["answer"])

        # Add an engaging visual element as the background
        st.image("https://drive.google.com/uc?id=1yNXKoe9F3WVdyG9m45QgfyNUtUsOFomH", use_column_width=True)

        # Meet the Team section
        st.info("Meet the Team")

        # Define image URLs
        abiodun_url = 'https://drive.google.com/uc?id=1BJy7E_xevIYNdo3eTn9qYhWp8uv9AWCk'
        ifeoluwa_url = 'https://drive.google.com/uc?id=1SkBrB7q4bX0gdHsPHqNE3GDJbDgfa4pj'
        sumaya_url = 'https://drive.google.com/uc?id=1_nLVbGZYe_fwsFXDfmEt3I2hNGxpPyv6'
        victor_url = 'https://drive.google.com/uc?id=13shBLuiO3fjyC09vfIkTnrM9ove83-Z1'
        damola_url = 'https://drive.google.com/uc?id=1tKhKpj6b6ap8MSZCrhhOq1RWr5SYMeQQ'

        # Display images with specified size
        col1, col2, col3, col4 = st.columns(4)
        with col2:
            st.image(abiodun_url, caption="Abiodun Adeagbo: Project Coordinator", width=120)
        with col3:
            st.image(ifeoluwa_url, caption="Ifeoluwa Ayodele: Technical Manager", width=120)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image(sumaya_url, caption="Sumaya Hassan: Administrative Manager", width=120)
        with col2:
            st.image(damola_url, caption="Damola Abiola: Deployment Manager", width=120)
        with col3:
            st.image(victor_url, caption="Victor Uwaomah: Resolution Manager", width=120)


        # Add the "Contact Us" section directly without a button
        st.subheader("Contact Us")
        col1, col2 = st.columns(2)
        with col1:
            st.info("Contact info")
            st.markdown('<i class="fas fa-map-marker-alt"></i> Lagos, Nigeria', unsafe_allow_html=True)
            st.markdown('<i class="fas fa-phone"></i> +234 8000000000', unsafe_allow_html=True)
            st.markdown('<i class="fab fa-whatsapp"></i> +234 8000000000', unsafe_allow_html=True)
            st.markdown('<i class="fas fa-envelope"></i> info@metapheonixconsult.com', unsafe_allow_html=True)
        with col2:
            st.info("Send Us")
            email = st.text_input("Enter your email")
            message = st.text_area("Enter your message")
            st.button("Send")

          # Add social media icons
        st.info("Follow Us")

        # Create columns for the social media icons and buttons
        col1, col2, col3, col4 = st.columns(4)

        # Display the social media icons and buttons in each column
        with col1:
            st.image("https://drive.google.com/uc?id=1TgLX4zdLZVzpSzW5AmvEv1TE6HlJJXhu", width=30)
            st.markdown('<button class="silver-button social-media-button" style="color: navy;">@filmalytics</button>', unsafe_allow_html=True)

        with col2:
            st.image("https://drive.google.com/uc?id=1z3gXVYw8OQFewzCuu7B0TZINQcVsIdc7", width=30)
            st.markdown('<button class="silver-button social-media-button" style="color: navy;">@filmalytics</button>', unsafe_allow_html=True)

        with col3:
            st.image("https://drive.google.com/uc?id=1jJKoDcncPF0p6TULf16qv1p--qeRd-eu", width=30)
            st.markdown('<button class="silver-button social-media-button" style="color: navy;">@filmalytics</button>', unsafe_allow_html=True)

        with col4:
            st.image("https://drive.google.com/uc?id=1rsl60zUj9SsTmAbHN-vUUe9wV95sLAbG", width=30)
            st.markdown('<button class="silver-button social-media-button" style="color: navy;">@filmalytics</button>', unsafe_allow_html=True)


        # Add copyright information and links
        st.write("© 2023 Filmalytics Inc. All rights reserved.")  

if __name__ == "__main__":
    main()
            
    # You may want to add more sections here for aspects such as an EDA,
    # or to provide your business pitch.


