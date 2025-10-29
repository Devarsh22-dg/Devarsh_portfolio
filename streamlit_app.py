# Create downloadable app.py file for user

app_content = """import streamlit as st

st.set_page_config(page_title="Devarsh Gandhi — Portfolio", page_icon="📋", layout="wide")

sections = {
    "About": {
        "content": \"\"\"Experienced Business Analyst and aspiring Project Manager with a proven record of leading complex projects, performing gap analyses, and implementing strategic solutions to enhance system functionalities. Skilled in translating business requirements into actionable deliverables and fostering stakeholder engagement through regular meetings. Adept at using tools like JIRA, ALM, and process flow diagrams to optimize performance and drive continuous improvements.\"\"\"
    },
    "Experience": {
        "content": [
            {
                "role": "Project Manager / Business Analyst",
                "company": "Spruce Technology (NYC DOHMH)",
                "range": "Oct 2021 – Present",
                "tasks": [
                    "Led end-to-end project lifecycle, from requirements gathering to deployment.",
                    "Managed cross-functional team of 8 members.",
                    "Executed projects using Azure DevOps for backlog and sprint tracking.",
                    "Conducted stakeholder interviews, BRDs, FRDs, and process flow documentation.",
                    "Improved efficiency by 20% through process optimization."
                ]
            },
            {
                "role": "Business Analyst",
                "company": "Systech Corporation",
                "range": "Jul 2021 – Oct 2021",
                "tasks": [
                    "Performed gap analyses and streamlined operations.",
                    "Developed 8 detailed user manuals improving adoption.",
                    "Resolved 500+ UAT issues for quality improvement."
                ]
            },
            {
                "role": "Business Analyst",
                "company": "COLSH CONSULTANTS LLC",
                "range": "Mar 2021 – Jul 2021",
                "tasks": [
                    "Improved business processes using UML diagrams.",
                    "Collaborated cross-functionally to enhance decision-making."
                ]
            },
            {
                "role": "Junior Business Analyst",
                "company": "DIGIP",
                "range": "Jan 2018 – Apr 2019",
                "tasks": [
                    "Supported requirements gathering and UAT.",
                    "Maintained JIRA backlog and client communication."
                ]
            }
        ]
    },
    "Projects": {
        "content": [
            {
                "title": "NYC DOHMH Modernization",
                "description": "Managed full lifecycle of digital modernization projects for NYC DOHMH.",
                "tags": ["Project Management", "Azure DevOps", "Integration"]
            },
            {
                "title": "Market Research for iRobot",
                "description": "Performed user research, built personas, and presented data-driven insights.",
                "tags": ["Market Research", "Data Analysis", "UX"]
            },
            {
                "title": "UX Research — Blizzard Entertainment",
                "description": "Led UX research for mobile gaming platform migration.",
                "tags": ["UX", "Gaming", "Data Visualization"]
            }
        ]
    },
    "Education": {
        "content": [
            {
                "degree": "MS in Marketing",
                "school": "Suffolk University, Boston",
                "range": "Sept 2019 – May 2020"
            },
            {
                "degree": "BBA in Business Administration",
                "school": "PDPU, India",
                "range": "Jul 2015 – May 2019"
            }
        ]
    },
    "Skills": {
        "content": [
            "Project Management", "Business Analysis", "Azure DevOps", "JIRA",
            "Salesforce", "SQL", "Python", "Power BI", "LucidChart",
            "Market Research", "SPSS", "Qualtrics", "Lean Six Sigma Green Belt"
        ]
    }
}

# Sidebar
st.sidebar.image("profile.png", width=120)
st.sidebar.title("Devarsh Gandhi")
st.sidebar.markdown("**Project Manager | Business Analyst**")
st.sidebar.markdown("📍 New Jersey, USA")
st.sidebar.markdown("📧 Devarsh.22.dg@gmail.com")
st.sidebar.markdown("📞 (813) 606-2192")
st.sidebar.markdown("[LinkedIn](https://linkedin.com/in/devarsh-gandhi)")
st.sidebar.markdown("---")

active_section = st.sidebar.radio("Navigate", list(sections.keys()))

# Main
st.title(f"📋 {active_section}")

if active_section == "About":
    st.write(sections["About"]["content"])

elif active_section == "Experience":
    for exp in sections["Experience"]["content"]:
        with st.expander(f"💼 {exp['role']} — {exp['company']} ({exp['range']})", expanded=False):
            for t in exp["tasks"]:
                st.markdown(f"- {t}")

elif active_section == "Projects":
    cols = st.columns(3)
    for i, proj in enumerate(sections["Projects"]["content"]):
        with cols[i % 3]:
            st.subheader(f"🧩 {proj['title']}")
            st.write(proj["description"])
            st.caption(" • ".join(proj["tags"]))

elif active_section == "Education":
    for edu in sections["Education"]["content"]:
        st.markdown(f"🎓 **{edu['degree']}**, {edu['school']} ({edu['range']})")

elif active_section == "Skills":
    st.markdown("### 🧠 Skills & Certifications")
    st.write(", ".join(sections["Skills"]["content"]))

st.markdown("---")
st.caption("© 2025 Devarsh Gandhi — Interactive Portfolio (JIRA Theme)")
"""

# Save file to disk for download
file_path = "/mnt/data/devarsh_portfolio_app.py"
with open(file_path, "w") as f:
    f.write(app_content)

file_path
