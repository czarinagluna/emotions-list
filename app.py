import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title='Name Your Emotion',page_icon='favicon.png')
                   #layout='wide'𓍼ོ)

# st.markdown("""
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Edu+AU+VIC+WA+NT+Pre:wght@400..700&display=swap');
#     </style>
# """, unsafe_allow_html=True)



# Custom CSS for button styling
st.markdown("""
    <style>
        /* Change button background color */
        .stButton>button {
            /* background-color: #F5F4EF;  /* Tomato */
            color: black;
            border-radius: 50px;  /* Rounded corners */
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s, transform 0.3s;
        }
        
        /* Change button color when hovering */
        .stButton>button:hover {
            background-color: #F1F1F1;  /* Darker Tomato */
            transform: scale(1.05);  /* Slightly enlarge on hover */
        }
        
        /* Change button text color */
        .stButton>button:active {
            background-color: #F1F1F1;  /* Same as regular color for active state */
            transform: scale(0.98);  /* Slightly shrink on click */
        }
    </style>
""", unsafe_allow_html=True)

df=pd.read_csv("emotions_nltk_dictionary.csv")

emotions_data = {
    "Pleasant": {
        "Courageous": [
            "Adventurous", "Audacious", "Bold", "Brave", "Capable", "Certain", "Cocky", "Confident",
            "Comfortable", "Daring", "Determined", "Fearless", "Free", "Grounded", "Gutsy", "Powerful", 
            "Proud", "Resolute", "Strong", "Superior", "Tenacious", "Tough", "Valiant", "Vehement", "Worthy"
        ],
        "Energized": [
            "Alert", "Alive", "Animated", "Aroused", "Bouncy", "Curious", "Fanatical", "Fascinated", "Feisty", 
            "Fervor", "Gung-ho", "Gusto", "Hyper", "Intense", "Psyched", "Pumped", "Snappy", "Sprightly", 
            "Thirst", "Titillated", "Vindicated", "Zeal", "Zest"
        ],
        "Grateful": [
            "Blessed", "Fortunate", "Gratified", "Relish", "Savor", "Thankful", "Touched"
        ],
        "Hopeful": [
            "Anticipation", "Craving", "Desiring", "Eager", "Encouraged", "Expectant", "Hankering",
            "Optimistic", "Trusting"
        ],
        "Introspective": [
            "Absorbed", "Brooding", "Contemplative", "Engrossed", "Enlightened", "Inspired", "Interested", 
            "Meditative", "Nostalgic", "Pensive", "Reflective", "Solemn", "Stirred", "Wonder"
        ],
        "Joyful": [
            "Amused", "Awed", "Bemused", "Bliss", "Blithe", "Bonhomie", "Bubbly", "Buoyant", "Carefree", 
            "Cheerful", "Delectation", "Delighted", "Delirious", "Ebullient", "Ecstatic", "Elated", 
            "Enchanted", "Enjoyment", "Entertained", "Enthusiastic", "Euphoric", "Excited", "Exhilarated", 
            "Exuberant", "Felicitous", "Genial", "Giddy", "Glad", "Gleeful", "Goofy", "Happy", "Humorous", 
            "Invigorated", "Jocular", "Jocund", "Jolly", "Jovial", "Jubilant", "Liberated", "Lighthearted", 
            "Lively", "Lucky", "Merry", "Mirthful", "Mischievous", "Motivated", "Passionate", "Perky", 
            "Playful", "Pleasure", "Positive", "Proud", "Rapture", "Reassured", "Relieved", "Sanguine", 
            "Satisfied", "Silly", "Sunny", "Thrilled", "Triumphant", "Upbeat", "Vibrant"
        ],
        "Kind": [
            "Caring", "Compassionate", "Cordial", "Earnest", "Empathetic", "Pitying", "Self-loving", "Sincere", 
            "Sympathetic", "Succor", "Tender", "Thoughtful", "Vulnerable", "Warm", "Welcoming"
        ],
        "Loving": [
            "Accepting", "Admiring", "Adoring", "Adulation", "Affectionate", "Ardor", "Attached", "Attracted", 
            "Captivated", "Devoted", "Enthralled", "Felicitous", "Fondness", "Fulfilled", "Infatuated", "Intimate", 
            "Intoxicated", "Present", "Protective", "Safe", "Sensual", "Warm", "Worthy", "Peaceful", "Accepting", 
            "Calm", "Centered", "Collected", "Comforted", "Composed", "Content", "Ease", "Free", "Fulfilled", "Mellow", 
            "Receptive", "Relaxed", "Secure", "Settled", "Sure", "Trusting", "Tranquil"
        ],
        "Surprised": [
            "Amazed", "Astonished", "Astounded", "Breathless", "Disbelief", "Dubious", "Dumbfounded", "Flabbergasted", 
            "Floored", "Quizzical", "Scandalized", "Serendipitious", "Shock", "Speechless", "Stunned", "Stupefied"
        ]
    },
    "Unpleasant": {
        "Afraid": [
            "Agitated", "Alarmed", "Antsy", "Anxious", "Apprehensive", "Cautious", "Concerned", 
            "Cowardly", "Distressed", "Dread", "Edgy", "Fearful", "Foreboding", "Frazzled", "Fretful", 
            "Frightened", "Guarded", "Hesitant", "Horrified", "Hysterical", "Jumpy", "Nervous", "Panic", 
            "Paralyzed", "Paranoid", "Petrified", "Restless", "Scared", "Shaken", "Skeptical", "Startled", 
            "Stressed", "Tense", "Terrified", "Timid", "Trepidation", "Twitchy", "Uptight", "Vigilant", 
            "Wary", "Worried"
        ],
        "Angry": [
            "Aggravated", "Animosity", "Annoyed", "Antagonistic", "Antipathy", "Bitter", "Bothered", 
            "Burning", "Choleric", "Cold", "Consternation", "Contempt", "Cross", "Disgruntled", "Enmity", 
            "Exasperated", "Frustrated", "Furious", "Grouchy", "Harassed", "Hostile", "Ill-tempered", 
            "Impatient", "Indignant", "Irritated", "Irate", "Irascible", "Mad", "Miffed", "Moody", "Nasty", 
            "Offended", "Outraged", "Peevish", "Perturbed", "Pissed", "Resentful", "Petulant", "Rage", 
            "Rattled", "Resentment", "Sour", "Testy", "Tetchy", "Vexed", "Vindictive", "Wrathful"
        ],
        "Disconnected": [
            "Adrift", "Alienated", "Alone", "Aloof", "Bored", "Conflicted", "Consternated", "Cranky", 
            "Denial", "Detached", "Disillusioned", "Disinterested", "Distant", "Distracted", "Empty", 
            "Groggy", "Hollow", "Jaded", "Indifferent", "Isolated", "Lethargic", "Listless", "Lost", 
            "Neutral", "Numb", "Powerless", "Preoccupied", "Puzzled", "Reluctance", "Removed", "Resignation", 
            "Resistant", "Sheepish", "Shut Down", "Sluggish", "Sullen", "Torn", "Uneasy", "Withdrawn"
        ],
        "Dislike": [
            "Abhorrence", "Aversion", "Detest", "Disdain", "Disgust", "Envious", "Grudging", "Hate", 
            "Repugnance", "Revolted", "Scorn"
        ],
        "Embarrassed": [
            "Appalled", "Apologetic", "Ashamed", "Chagrined", "Compunction", "Contrite", "Flustered", 
            "Foolish", "Guilty", "Humbled", "Humored", "Inferior", "Inhibited", "Mortified", "Pathetic", 
            "Regretful", "Repentant", "Shame", "Self-conscious", "Sorry", "Submissive", "Useless", "Weak", 
            "Worthless"
        ],
        
        "Helpless": [
            "Awkward", "Baffled", "Challenged", "Clueless", "Complacent", "Disturbed", "Exhausted", "Fatigued", 
            "Fragile", "Impotent", "Incapable", "Needy", "Overwhelmed", "Pathetic", "Perplexed", "Powerless", 
            "Resigned", "Sensitive", "Trapped", "Victim"
        ],
        "Hurt": [
            "Agony", "Betrayed", "Humiliated", "Pained", "Stung", "Suffering", "Suffocated", "Tormented", 
            "Tortured", "Traumatized"
        ],
        "Insecure": [
            "Bashful", "Befuddled", "Bewildered", "Cynical", "Confused", "Doubtful", "Possessive", "Shy", "Woozy"
        ],
        "Sadness": [
            "Aching", "Alienated", "Angst", "Anguish", "Blue", "Choked", "Crestfallen", "Crummy", "Crushed", "Defeated", 
            "Dejected", "Depressed", "Despair", "Despondent", "Devastated", "Disappointed", "Discouraged", "Dismal", "Doleful", 
            "Down", "Downcast", "Excluded", "Forlorn", "Gloomy", "Grief", "Heartbroken", "Homesick", "Hopeless", "Hurt", "Lonely", 
            "Longing", "Melancholy", "Mournful", "Pained", "Pessimistic", "Remorseful", "Sick", "Somber", "Sorrowful", "Teary", "Troubled", 
            "Unhappy", "Upset", "Weary", "Wistful", "Woe", "Wretched", "Yearning"
        ],
        "Unkind":[
            "Crafty", "Cruel", "Derisive", "Greedy", "Petty", "Selfish", "Smug"
        ]
    }
}

# Sidebar for page navigation
st.sidebar.title("Emotions App")
page = st.sidebar.radio("Select a page", ["Name Your Emotion", "Emotions List"])


st.sidebar.divider()

st.sidebar.subheader('About')
st.sidebar.write('''
Mary Kate, my therapist, shared this Emotions List to help me better understand and reflect on my emotions. 
                 
It’s a really helpful tool for emotional awareness, and I encourage anyone to consider therapy as a way to take care of their mental health.
                 ''')

# File name
file_name = "Ultimate-List-of-Emotions.pdf"  # Replace with your file name

# Get the absolute path
file_path = os.path.abspath(file_name)

# Read the file content
with open(file_path, "rb") as file:
    file_content = file.read()

# Add the download button
st.sidebar.download_button(
    label="Download PDF",
    data=file_content,
    file_name=file_name,
    mime="application/pdf"
)

st.sidebar.markdown('')
st.sidebar.caption('*Please note that none of your data, including any reflections you write, is stored. Your privacy and confidentiality are important.*')


# Page 1: Select Emotion with Buttons
if page == "Name Your Emotion":

    # Initialize session state
    if "page" not in st.session_state:
        st.session_state.page = "home"
    if "selected_feeling" not in st.session_state:
        st.session_state.selected_feeling = None
    if "selected_category" not in st.session_state:
        st.session_state.selected_category = None
    if "selected_emotion" not in st.session_state:
        st.session_state.selected_emotion = None

    # Navigation function
    def navigate(page_name, **kwargs):
        if page_name == "home":
            # Reset state when navigating back to the home page
            st.session_state.selected_feeling = None
            st.session_state.selected_category = None
            st.session_state.selected_emotion = None
        st.session_state.page = page_name
        for key, value in kwargs.items():
            st.session_state[key] = value

    # Home Page
    if st.session_state.page == "home":
        st.title("How are you feeling right now?")
        st.write("Select the category that best describes your current feeling.")

        st.button("Pleasant", on_click=navigate, args=("category",), kwargs={"selected_feeling": "Pleasant"}, key="pleasant_btn")
        st.button("Unpleasant", on_click=navigate, args=("category",), kwargs={"selected_feeling": "Unpleasant"}, key="unpleasant_btn")

    # Category Page
    elif st.session_state.page == "category":
        feeling = st.session_state.selected_feeling
        st.title(f"You feel {feeling.lower()}")
        st.markdown('Try to dig a little deeper...')
        for category in emotions_data[feeling]:
            st.button(category, on_click=navigate, args=("emotions",), kwargs={"selected_category": category}, key=f"{category}_btn")
        st.divider()
        st.button("Back to Home", on_click=navigate, args=("home",), key="back_to_home")

    # Emotions Page
    elif st.session_state.page == "emotions":
        category = st.session_state.selected_category
        feeling = st.session_state.selected_feeling
        st.title(f"{category.capitalize()} Emotions")

        emotions_list = emotions_data[feeling][category]
        col1, col2 = st.columns(2)

        with col1:
            selected_emotion = st.radio("Choose an emotion:", emotions_list, key="selected_emotion_radio")

        with col2:
            if selected_emotion:
                emotion_df = df[df["Emotion"] == selected_emotion].iloc[0]
                with st.expander('Definition and Synonyms'):
                    st.markdown(f"### {selected_emotion}")
                    definitions = emotion_df["Definitions"].split("; ")

                    st.markdown("**Definitions:**")
                    for definition in definitions:
                        if definition=='':
                            continue
                        st.markdown(f"- {definition}")

                    st.markdown(f"**Synonyms:** {emotion_df['Synonyms']}")
                    
                
        st.write(f"### Reflect on your feeling of **{selected_emotion}**:")
        #reflection = st.text_area("Write your thoughts here:")
      
        # Function to generate the copy to clipboard button
        def copy_to_clipboard(reflection_text):
            # JavaScript to copy text to clipboard
            st.markdown(f"""
            <script>
                function copyText() {{
                    const text = `{reflection_text}`;
                    navigator.clipboard.writeText(text).then(function() {{
                        console.log('Text successfully copied to clipboard');
                        alert('Your reflection has been copied to the clipboard!');
                    }}, function(err) {{
                        console.error('Error copying text: ', err);
                    }});
                }}
                copyText();
            </script>
            """, unsafe_allow_html=True)
      
  
        reflection_input = st.text_area("Write your reflection here:", height=100)
  
        # Button to trigger the copy functionality
        if st.button("Copy to Clipboard"):
            if reflection_input:  # Only trigger copy if there is text entered
                copy_to_clipboard(reflection_input)
            else:
                st.warning("Please write something in the reflection field before copying.")

    
        # Back buttons
        st.divider()
        st.button("Back to Categories", on_click=navigate, args=("category",), key="back_to_categories")
        st.button("Back to Home", on_click=navigate, args=("home",), key="back_to_home")


# Page 2: View Emotions List (If you want to show all emotions in a list)
elif page == "Emotions List":
    category_map = {
        "Pleasant": ["Courageous", "Energized", "Grateful", "Hopeful", "Introspective", "Joyful", "Kind", "Loving", "Surprised"],
        "Unpleasant": ["Afraid", "Angry", "Disconnected", "Dislike", "Embarrassed",  "Helpless", "Hurt", "Insecure", "Sadness", "Unkind"],
        }

    st.title("Emotions List")

    # Function to display emotions compactly in columns
    def display_emotions(category, emotions_data):
        # Loop through emotions data and match with category
        for feeling, sub_emotions in emotions_data[category].items():
            st.subheader(f"**{feeling}**")
            # Create columns to display emotions in a compact way
            columns = st.columns(3)  # 3 columns per row
            for i, emotion in enumerate(sub_emotions):
                col = columns[i % 3]  # Distribute emotions across columns
                col.markdown(f"- {emotion}")


    # Use Streamlit tabs for each category
    tab1, tab2 = st.tabs(["Pleasant", "Unpleasant"])
    
    with tab1:
        display_emotions("Pleasant", emotions_data)

    with tab2:
        display_emotions("Unpleasant", emotions_data)
