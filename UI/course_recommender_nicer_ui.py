import pandas as pd
import streamlit as st
import requests

FASTAPI_URL = "http://localhost:8000"

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Course Recommender",
    page_icon="🎓",
    layout="wide",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600&family=DM+Sans:wght@300;400;500&display=swap');

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── App background ── */
.stApp {
    background: #F7F5F0;
}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #1A1A2E !important;
    border-right: none;
}

[data-testid="stSidebar"] * {
    color: #E8E4DC !important;
}

/* ── Sidebar title ── */
.sidebar-title {
    font-family: 'Playfair Display', serif;
    font-size: 1.45rem;
    font-weight: 600;
    color: #F5C842 !important;
    letter-spacing: -0.02em;
    line-height: 1.3;
    margin-bottom: 0.25rem;
}

.sidebar-subtitle {
    font-size: 0.75rem;
    color: #8888AA !important;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    margin-bottom: 2rem;
}

/* ── Pill selector label ── */
.pill-label {
    font-size: 0.7rem;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8888AA !important;
    margin-bottom: 0.6rem;
}

/* ── Radio → pill buttons ── */
[data-testid="stSidebar"] .stRadio > div {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

[data-testid="stSidebar"] .stRadio label {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 50px;
    padding: 0.55rem 1.1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.85rem;
    font-weight: 400;
    color: #C8C4BC !important;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(245, 200, 66, 0.12);
    border-color: rgba(245, 200, 66, 0.4);
    color: #F5C842 !important;
}

/* Selected pill */
[data-testid="stSidebar"] .stRadio label[data-checked="true"],
[data-testid="stSidebar"] .stRadio input:checked + div {
    background: #F5C842 !important;
    border-color: #F5C842 !important;
    color: #1A1A2E !important;
    font-weight: 500;
}

/* Hide the default radio circle */
[data-testid="stSidebar"] .stRadio input[type="radio"] {
    display: none;
}

/* ── Text inputs ── */
[data-testid="stSidebar"] .stTextInput > div > div > input {
    background: rgba(255,255,255,0.07) !important;
    border: 1px solid rgba(255,255,255,0.15) !important;
    border-radius: 10px !important;
    color: #E8E4DC !important;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    padding: 0.55rem 0.9rem;
    transition: border-color 0.2s;
}

[data-testid="stSidebar"] .stTextInput > div > div > input:focus {
    border-color: #F5C842 !important;
    box-shadow: 0 0 0 2px rgba(245,200,66,0.15) !important;
}

[data-testid="stSidebar"] .stTextInput label {
    font-size: 0.72rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #8888AA !important;
    font-weight: 500;
}

/* ── Fetch button ── */
[data-testid="stSidebar"] .stButton > button {
    background: #F5C842 !important;
    color: #1A1A2E !important;
    border: none !important;
    border-radius: 50px !important;
    font-family: 'DM Sans', sans-serif;
    font-weight: 500;
    font-size: 0.85rem;
    padding: 0.6rem 1.4rem;
    width: 100%;
    letter-spacing: 0.03em;
    transition: all 0.2s ease;
    margin-top: 0.5rem;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: #FFDA6B !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(245,200,66,0.35) !important;
}

[data-testid="stSidebar"] .stButton > button:active {
    transform: translateY(0px);
}

/* ── Divider ── */
.sidebar-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 1.5rem 0;
}

/* ── Main content area ── */
.main-header {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    font-weight: 600;
    color: #1A1A2E;
    letter-spacing: -0.03em;
    margin-bottom: 0.3rem;
}

.main-subtitle {
    font-size: 0.9rem;
    color: #888;
    font-weight: 300;
    letter-spacing: 0.05em;
    margin-bottom: 2.5rem;
}

.result-card {
    background: white;
    border-radius: 16px;
    padding: 1.8rem;
    box-shadow: 0 2px 20px rgba(0,0,0,0.06);
    border: 1px solid rgba(0,0,0,0.05);
}

.result-tag {
    display: inline-block;
    background: #EEF2FF;
    color: #4F46E5;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 0.3rem 0.8rem;
    border-radius: 50px;
    margin-bottom: 1rem;
}

/* ── Dataframe styling ── */
[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* ── Info/error boxes ── */
.stAlert {
    border-radius: 12px !important;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 4rem 2rem;
    color: #AAA;
}

.empty-state .icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.empty-state p {
    font-size: 0.95rem;
    font-weight: 300;
}
</style>
""", unsafe_allow_html=True)


# ── Data fetching ─────────────────────────────────────────────────────────────
def fetch_data(endpoint: str, params: dict, method: str = "get") -> pd.DataFrame:
    try:
        if method == "get":
            response = requests.get(f"{FASTAPI_URL}/{endpoint}", params=params)
        if response.status_code == 200:
            payload = response.json()
            rows = payload.get("data", [])
            return pd.DataFrame(rows)
        else:
            st.error(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        st.error(f"Could not connect to API: {e}")
        return None


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sidebar-title">🎓 Course Recommender</div>', unsafe_allow_html=True)
    st.markdown('<div class="sidebar-subtitle">Academic Planning Tool</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    st.markdown('<div class="pill-label">Select Functionality</div>', unsafe_allow_html=True)
    api_end_point = st.radio(
        label="functionality",
        options=["📋  Course Sections", "🔗  Prerequisites"],
        label_visibility="collapsed",
    )

    st.markdown('<hr class="sidebar-divider">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        subject_code = st.text_input("Subject Code", placeholder="e.g. CS")
    with col2:
        course_number = st.text_input("Course No.", placeholder="e.g. 101")

    fetch_clicked = st.button("Fetch Results →")


# ── Main content ──────────────────────────────────────────────────────────────
st.markdown('<div class="main-header">Course Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="main-subtitle">Search courses and prerequisites across all departments</div>', unsafe_allow_html=True)

if fetch_clicked:
    if not subject_code or not course_number:
        st.warning("Please enter both a subject code and course number.")
    else:
        params = {"subjectCode": subject_code.strip().upper(), "courseNumber": course_number.strip()}

        if "Sections" in api_end_point:
            endpoint = "get_course_sections_for_specified_course/"
            tag_label = "Course Sections"
            empty_msg = "No sections found for this course."
        else:
            endpoint = "get_course_prerequisites/"
            tag_label = "Prerequisites"
            empty_msg = "No prerequisites found for this course."

        with st.spinner("Fetching data…"):
            df = fetch_data(endpoint, params)

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(f'<div class="result-tag">{tag_label}</div>', unsafe_allow_html=True)
        st.markdown(f"**{subject_code.upper()} {course_number}**", )

        if df is not None and not df.empty:
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.markdown(f"""
            <div class="empty-state">
                <div class="icon">📭</div>
                <p>{empty_msg}</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="empty-state">
        <div class="icon">🔍</div>
        <p>Select a functionality and enter a course to get started.</p>
    </div>
    """, unsafe_allow_html=True)