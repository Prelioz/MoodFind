import streamlit as st
from src.predict import predict_sentiment

# 1. Page Configuration (Must be the very first Streamlit command)
st.set_page_config(
    page_title="MoodFind // Premium Sentiment Analysis",
    page_icon="🎬",
    layout="wide"  # Wide layout gives us more room for a clean grid layout
)

# 2. Injecting Custom Luxury Cinema CSS (Classic Gold & Velvet Theme)
st.markdown("""
    <style>
    /* Main background and font styling */
    .stApp {
        background: radial-gradient(circle, #140d14 0%, #050205 100%);
        color: #f5f0f2;
    }

    /* Customizing Sidebar */
    [data-testid="stSidebar"] {
        background-color: #0d0611 !important;
        border-right: 2px solid #800020; /* Deep Burgundy border */
    }
    
    /* Customizing buttons to look like premium vintage movie tickets */
    .stButton>button {
        background: linear-gradient(180deg, #ffcc00 0%, #cc9900 100%) !important;
        color: #140d14 !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
        border-radius: 6px !important;
        border: 1px solid #ffcc00 !important;
        transition: all 0.2s ease;
        width: 100%;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        background: #ffcc00 !important;
        color: #000000 !important;
        box-shadow: 0 4px 15px rgba(255, 204, 0, 0.4);
    }
    
    /* Box containers for results */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 8px;
        border: 1px solid rgba(255, 204, 0, 0.2);
        margin-top: 20px;
    }
    
    /* Custom Metric Styling to completely bypass native st.metric theme collision */
    .custom-metric-box {
        background: rgba(0, 0, 0, 0.4);
        border: 1px solid rgba(255, 204, 0, 0.3);
        border-radius: 6px;
        padding: 15px;
        margin-top: 15px;
    }
    .custom-metric-label {
        font-family: 'Arial', sans-serif;
        text-transform: uppercase;
        font-size: 0.85rem;
        color: #a3969e;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }
    .custom-metric-value {
        font-family: 'Impact', 'Arial Black', sans-serif;
        font-size: 2.2rem;
        color: #ffffff;
        line-height: 1;
    }
    .custom-metric-delta {
        font-size: 0.95rem;
        font-weight: bold;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BACKSTAGE PASS ---
st.sidebar.markdown("<h2 style='color: #ffcc00; text-align: center;'>BACKSTAGE INFO</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

st.sidebar.markdown("""
<div style="background: rgba(255,255,255,0.02); padding: 15px; border-radius: 6px; border: 1px solid rgba(255,204,0,0.2);">
    <h4 style="color: #ffcc00; margin-top:0; letter-spacing: 1px;">THE ENGINE</h4>
    <p style="font-size: 0.95rem; color: #e0d5db;">MoodFind scans the emotional framework of movie reviews using an NLP pipeline trained on the IMDb archive.</p>
    <b style="color: #ffcc00;"> Architecture:</b>
    <ul style="color: #e0d5db; padding-left: 20px; margin-top: 5px;">
        <li>TF-IDF Vectorizer</li>
        <li>Logistic Regression</li>
    </ul>
    <b style="color: #ffcc00;"> Stack:</b> <span style="color: #e0d5db;">Python, Scikit-Learn, Streamlit</span>
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.subheader("🎭 Review Benchmarks")

with st.sidebar.expander("✨ Positive Review Example"):
    st.code("This movie was an absolute cinematic masterpiece! The cinematography was breathtaking.")

with st.sidebar.expander("🍿 Neutral Review Example"):
    st.code("The movie was okay. Great acting, but the pacing felt a bit too slow in the second act.")

with st.sidebar.expander("🍅 Negative Review Example"):
    st.code("Worst movie ever. A complete waste of time and money. The plot made zero sense.")


# --- MAIN INTERACTION ZONE: OPTION 2 ART DECO FILM STRIP ---
st.markdown("""
    <div style="
        text-align: center; 
        border-top: 3px double #ffcc00; 
        border-bottom: 3px double #ffcc00; 
        padding: 20px 0; 
        margin-top: -15px;
        margin-bottom: 45px;
        background: rgba(255, 204, 0, 0.02);
    ">
        <h1 style="
            font-family: 'Georgia', serif;
            font-size: 4.5rem;
            font-weight: bold;
            font-style: italic;
            color: #ffcc00;
            letter-spacing: 8px;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        ">
            🎬 MOODFIND
        </h1>
    </div>
""", unsafe_allow_html=True)

# Layout Split: Left for Input, Right for Cinematic Results
col1, col2 = st.columns([5, 4], gap="large")

with col1:
    st.markdown("### 📽️ Feed the Critic")
    review = st.text_area(
        "Paste your raw, unfiltered movie review below:",
        height=180,
        placeholder="Type here... (e.g., 'An absolute cinematic masterpiece!')"
    )
    
    # Elegant prediction trigger button
    predict_clicked = st.button("RUN SENTIMENT ANALYSIS")

with col2:
    st.markdown("### 📊 Box Office Verdict")
    
    if predict_clicked:
        if review.strip() == "":
            st.error("🚨 The projector is empty! Please enter a valid review before analyzing.")
        else:
            # Run prediction pipeline
            sentiment, confidence, cleaned_review = predict_sentiment(review)
            confidence_pct = confidence * 100
            
            # Custom styled container for results
            with st.container():
                # Define sentiment specific traits
                if sentiment == "Positive":
                    border_color = "#4caf50"
                    title_icon = "🤩"
                    delta_text = "Certified Fresh "
                    delta_color = "#4caf50"
                elif sentiment == "Negative":
                    border_color = "#f44336"
                    title_icon = "🍅"
                    delta_text = "Rotten "
                    delta_color = "#f44336"
                else:
                    border_color = "#ff9800"
                    title_icon = "😐"
                    delta_text = "Mixed Reviews "
                    delta_color = "#ff9800"

                # Render HTML Bounded Result Card with explicitly handled text colors
                st.markdown(f"""
                <div class='result-card' style='border-left: 6px solid {border_color};'>
                    <h2 style='color: {border_color}; margin-top:0; font-family: "Impact", sans-serif; letter-spacing: 1px;'>
                        {title_icon} VERDICT: {sentiment.upper()}
                    </h2>
                    <div class='custom-metric-box'>
                        <div class='custom-metric-label'>Confidence Score</div>
                        <div class='custom-metric-value'>{confidence_pct:.2f}%</div>
                        <div class='custom-metric-delta' style='color: {delta_color};'>{delta_text}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                st.write("") # Spacing element
                
                # Show Text Preprocessing Breakdown
                with st.expander("🔍 Behind the Scenes (Preprocessed Text)"):
                    st.info("This is how the model interprets your text after removing punctuation, capitalization, and standard stop words:")
                    st.code(cleaned_review, language="text")
    else:
        # Placeholder state before user clicks predict
        st.info(" Awaiting input... Enter a movie review on the left and click the analyze button to generate a report.")