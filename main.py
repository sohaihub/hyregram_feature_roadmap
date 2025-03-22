import streamlit as st

# Page Config
st.set_page_config(page_title="Hyregram feature roadmap release", layout="wide")

# Custom CSS for Auto Light/Dark Mode Detection
theme_css = """
    <style>
        body { font-family: 'Arial', sans-serif; }
        .title { font-size: 36px; font-weight: bold; text-align: center; padding: 10px 0; }
        .subtitle { font-size: 22px; text-align: center; font-weight: 500; margin-bottom: 15px; }
        .highlight-box { padding: 15px; border-radius: 12px; margin-bottom: 15px; box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.2); }
        .section-title { font-size: 30px; font-weight: bold; margin: 10px 0; }
        .feature-list { font-size: 18px; padding: 5px; margin-left: 15px; }
        .divider { border-top: 2px solid #FFD700; margin: 20px 0; }
        
        /* Auto Detect Light/Dark Mode */
        @media (prefers-color-scheme: light) {
            body { background-color: #F8F9FA; color: #000; }
            .highlight-box { background: #FFF; color: #000; }
        }
        @media (prefers-color-scheme: dark) {
            body { background-color: #1E1E2E; color: #F8F9FA; }
            .highlight-box { background: #27293D; color: #F8F9FA; }
        }
    </style>
"""

st.markdown(theme_css, unsafe_allow_html=True)

# Title & Introduction
st.markdown("<div class='title'>🚀Hyregram feature roadmap release</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>From AI-agent powered Hiring to Predictive Analytics – Explore Our Evolution</div>", unsafe_allow_html=True)

# Featured Highlights
st.markdown("### 🌟 **Key Highlights**")
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("<div class='highlight-box'><b>✅ AI-agent powered Hiring</b><br>AI Agents, Skill gap analysis, Proctored process, Resume Matchmaking, </div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='highlight-box'><b>✅ Next-Gen Assessments</b><br>Coding Challenges, Hackathons, MCQs, Proctoring & Voice Agents</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='highlight-box'><b>✅ Job Intelligence</b><br>Jobs Aggregator - Faang, Mango, Big 7, Career Roadmap, AI Chatbot</div>", unsafe_allow_html=True)

st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

# Roadmap Data (Without ** formatting)
phases = {
    "🚀 Phase 1 (Now - Feb) - Ready to be deployed": [
        "Resume Builder AI - Smart CV generator",
        "Resume Analyzer AI - Skill gap analysis",
        "Job Description Generator AI",
        "MatchMaker AI - JD vs Resume Matching",
        "Coding Assessment IDE - Python, C, C++ problems",
        "Applicant Tracking System (ATS)",
        "Proctoring Features: Face Detection, Object Detection, Multi-person Detection, Eye Tracking, Tab Switch Detection, Fullscreen Monitoring"
    ],
    "🚀 Phase 2 (Feb - April) - In progress": [
        "Round 1: AI & Custom MCQs (Critical Thinking, Logic, Psychometrics)",
        "Round 2: MERN Stack Coding Assessments",
        "Round 3: AI-Human Video Interviews + Speech-to-Text",
        "Proctoring Option - custom for new rounds",
        "Job Intelligence: FAANG, Big 7 Job Aggregator, Career Path Guide",
        "Jobs trending dashboard - job based approach",
        "Job Route Map - user can select a role to see how to reach the spot - check roadmap.ch",
        "Proctoring System: Custom AI Proctoring for Assessments",
        "Resume Matchmaker AI & GDPR/SOC Compliance",
        "One-Click Interview Invites & Multi-Format Report Downloads",
        "SOC II Type 2 Compliance",
        "Multi Factor Authentication "
    ],
    "🔥 Phase 3 (April - July)": [
        "Round 1: Advanced Tech Assessments (Cloud, AIML, DSA) - In progress ",
        "Round 2: AI-Driven Coding Tests & Mock Interviews - In progress",
        "Round 3: AI Video Interview Bot",
        "Online Hackathon Platform - Fully Automated Hackathons",
        "AI Voice Agents - Candidate Screening & Scheduling - In progress ",
        "ATS - adding more features - Tech discovery",
        "Online Hackathon Platform - Fully Online Hackathon and Ideathon Platform",
        "User Social Profiling - Personality Types, social media handles, coding handles, auto resume update and download etc",
        "Ai Agents build/conversion (resume builder, matchmaker, etc) - Tech discovery",
        "One-Click Reach:  Send personalized interview invites or offers directly to candidates through the platform. Streamline communication and reduce back-and-forth with automated scheduling tools - Tech discovery",
        "Online Chatbot - interact with Dashboard - L2 - Tech discovery ",
        "Reports Download - multi format - Tech discovery ",
        "Coding Mock Test environment: Practise background, skill and coding interviews - Tech discovery",
        "Pre-Screened Talent Pool: Access a vetted database of candidates who've completed skill assessments & video interviews. Skip initial screening rounds and fast-track to final interviews or offers. - In progress",
        "Plagiarism checker"
    ],
    "⚡ Phase 4 (July - Sept)": [
        "Game-Based Hiring Assessments for Fun & Insightful Hiring",
        "Campus Hiring Tools - AI-Driven University Recruitment",
        "Candidate Personalisation - Level 1",
        "Voice Agents to conduct intial candidate screening, scheduling, conducting",
        "Ai Agents build/conversion (resume builder, matchmaker, etc)",
        "Seamless ATS Integration: Integrate with popular ATS systems to streamline the end-to-end hiring process.",
        "Predictive Analytics - AI to Forecast Candidate Success",
        "Mobile Optimization - Enhanced UX for Mobile Assessments",
        "Full PostgreSQL & Next.js Migration for Scalability"
    ]
}

# Display Roadmap with Collapsible Sections
for phase, features in phases.items():
    with st.expander(phase, expanded=False):
        for feature in features:
            st.markdown(f"<div class='feature-list'>• {feature}</div>", unsafe_allow_html=True)
    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)