import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

from modules.pdf_extractor import extract_text_from_pdf
from modules.preprocess import preprocess_text
from modules.skill_extractor import extract_skills
from modules.ats_calculator import calculate_ats_score

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(to right,#0f172a,#1e293b);
}

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}

.hero{
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:35px;
    border-radius:25px;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.4);
}

.hero h1{
    color:white;
    font-size:55px;
}

.hero p{
    color:#e2e8f0;
    font-size:18px;
}

.metric-card{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:20px;
    padding:25px;
    text-align:center;
    color:white;
    box-shadow:0px 4px 20px rgba(0,0,0,0.3);
}

.section-box{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:20px;
    padding:25px;
    margin-top:20px;
}

.skill-match{
    display:inline-block;
    background:#16a34a;
    color:white;
    padding:8px 14px;
    margin:5px;
    border-radius:20px;
    font-weight:bold;
}

.skill-miss{
    display:inline-block;
    background:#dc2626;
    color:white;
    padding:8px 14px;
    margin:5px;
    border-radius:20px;
    font-weight:bold;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    border:none;
    background:linear-gradient(90deg,#22c55e,#16a34a);
    color:white;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{
    transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.title("🤖 AI Resume Analyzer")

    st.markdown("---")

    st.markdown("""
### Features

✅ ATS Compatibility Score

✅ Skill Extraction

✅ Keyword Matching

✅ Missing Skills Detection

✅ Resume Strength Analysis

✅ AI Suggestions
""")

    st.markdown("---")

    st.info(
        "Built using Python, NLP, Scikit-Learn and Streamlit."
    )

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class='hero'>

<h1>🤖 AI Resume Analyzer</h1>

<p>
Analyze your Resume against Job Description and
boost your ATS score instantly.
</p>

</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# INPUT AREA
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:
    resume_file = st.file_uploader(
        "📤 Upload Resume PDF",
        type=["pdf"]
    )

with col2:
    jd_text = st.text_area(
        "📝 Paste Job Description",
        height=250
    )

# --------------------------------------------------
# ANALYSIS
# --------------------------------------------------

if st.button("🚀 Analyze Resume"):

    if resume_file and jd_text:

        with st.spinner("Analyzing Resume..."):

            # Extract Text
            resume_text = extract_text_from_pdf(
                resume_file
            )

            # Clean Text
            resume_clean = preprocess_text(
                resume_text
            )

            jd_clean = preprocess_text(
                jd_text
            )

            # Skills
            resume_skills = extract_skills(
                resume_clean
            )

            jd_skills = extract_skills(
                jd_clean
            )

            matched = list(
                set(resume_skills) &
                set(jd_skills)
            )

            missing = list(
                set(jd_skills) -
                set(resume_skills)
            )

            # Similarity
            similarity_score = calculate_ats_score(
                resume_clean,
                jd_clean
            )

            # Skill Score

            if len(jd_skills) > 0:
                skill_score = (
                    len(matched) /
                    len(jd_skills)
                ) * 100
            else:
                skill_score = 0

            # Final Score
            final_score = round(
                (0.3 * similarity_score) +
                (0.7 * skill_score),
                2
            )

        st.toast("🎉 Resume Analysis Completed Successfully!", icon="✅")
        # --------------------------------------------------
        # METRICS
        # --------------------------------------------------

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>🎯 ATS Score</h3>
            <h1>{final_score}%</h1>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>✅ Matched Skills</h3>
            <h1>{len(matched)}</h1>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown(f"""
            <div class='metric-card'>
            <h3>❌ Missing Skills</h3>
            <h1>{len(missing)}</h1>
            </div>
            """, unsafe_allow_html=True)

        # --------------------------------------------------
        # TABS
        # --------------------------------------------------

        tab1, tab2, tab3 = st.tabs([
            "📊 Dashboard",
            "🛠 Skills Analysis",
            "💡 Suggestions"
        ])

        # --------------------------------------------------
        # DASHBOARD TAB
        # --------------------------------------------------

        with tab1:

            g1, g2 = st.columns(2)

            with g1:

                gauge = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=final_score,
                    title={
                        'text': "ATS Compatibility Score"
                    },

                    gauge={
                        'axis': {'range': [0, 100]},

                        'bar': {
                            'color': "#22c55e"
                        },

                        'steps': [

                            {
                                'range': [0, 40],
                                'color': "#ef4444"
                            },

                            {
                                'range': [40, 70],
                                'color': "#f59e0b"
                            },

                            {
                                'range': [70, 100],
                                'color': "#22c55e"
                            }
                        ]
                    }
                ))

                gauge.update_layout(
                    paper_bgcolor="#1e293b",
                    font={'color': "white"},
                    height=400
                )

                st.plotly_chart(
                    gauge,
                    use_container_width=True
                )

            with g2:

                pie = px.pie(
                    names=["Matched", "Missing"],
                    values=[
                        len(matched),
                        len(missing)
                    ],
                    title="Keyword Distribution"
                )

                pie.update_layout(
                    paper_bgcolor="#1e293b",
                    font_color="white"
                )

                st.plotly_chart(
                    pie,
                    use_container_width=True
                )

                st.subheader("📈 Resume Strength")

                st.progress(int(final_score))

                if final_score >= 85:
                    st.success(
                        "⭐⭐⭐⭐⭐ Excellent Resume"
                    )

                elif final_score >= 70:
                    st.success(
                        "⭐⭐⭐⭐ Strong Resume"
                    )

                elif final_score >= 50:
                    st.warning(
                        "⭐⭐⭐ Average Resume"
                    )

                else:
                    st.error(
                        "⭐⭐ Needs Improvement"
                    )

        # --------------------------------------------------
        # SKILLS TAB
        # --------------------------------------------------

        with tab2:

            st.subheader("✅ Matched Skills")

            if matched:

                html = ""

                for skill in matched:
                    html += f"""
                    <span class='skill-match'>
                    {skill}
                    </span>
                    """

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )

            else:
                st.warning(
                    "No skills matched."
                )

            st.markdown("---")

            st.subheader("❌ Missing Skills")

            if missing:

                html = ""

                for skill in missing:
                    html += f"""
                    <span class='skill-miss'>
                    {skill}
                    </span>
                    """

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )

            else:
                st.success(
                    "No important skills missing."
                )

        # --------------------------------------------------
        # SUGGESTION TAB
        # --------------------------------------------------

        with tab3:

            st.subheader("💡 AI Suggestions")

            if missing:

                st.warning(
                    "Add these keywords to improve ATS:\n\n"
                    + ", ".join(missing)
                )

            else:
                st.success(
                    "Excellent! Resume is highly optimized."
                )

            st.markdown("---")

            st.subheader("📋 Final Verdict")

            if final_score >= 85:

                st.success("""
Your resume is highly ATS friendly.

Strong chances of clearing the initial screening process.
""")

            elif final_score >= 70:

                st.info("""
Your resume is good.

Add a few missing keywords for better performance.
""")

            elif final_score >= 50:

                st.warning("""
Your resume needs some improvements.

Try adding more relevant technical skills.
""")

            else:

                st.error("""
Your resume needs significant improvements.

Add missing keywords and project details.
""")

    else:
        st.warning(
            "Please upload Resume PDF and paste Job Description."
        )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown("""
<div style='text-align:center;
color:gray;
padding:20px;'>

Made with by DeepKumar Kacha

AI Resume Analyzer | NLP + Streamlit

</div>
""", unsafe_allow_html=True)