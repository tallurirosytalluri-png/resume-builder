import streamlit as st
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="Resume Builder",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 Resume Builder")
st.write("Create your professional resume easily!")

# Two columns
left, right = st.columns(2)

# =========================
# INPUT SECTION
# =========================

with left:

    st.header("👤 Personal Information")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    location = st.text_input("Location")
    linkedin = st.text_input("LinkedIn")
    github = st.text_input("GitHub")

    st.header("🎯 Career Objective")

    objective = st.text_area(
        "Career Objective",
        height=100
    )

    st.header("🎓 Education")

    degree = st.text_input("Degree")
    college = st.text_input("College / University")
    education_year = st.text_input("Year of Graduation")
    cgpa = st.text_input("CGPA / Percentage")

    st.header("💻 Skills")

    skills = st.text_area(
        "Skills",
        placeholder="Python, C, Java, HTML, CSS, SQL"
    )

    st.header("🛠️ Project")

    project_name = st.text_input("Project Name")

    project_description = st.text_area(
        "Project Description",
        height=100
    )

    project_technologies = st.text_input(
        "Technologies Used"
    )

    st.header("💼 Internship / Experience")

    company = st.text_input("Company Name")
    role = st.text_input("Role")

    experience = st.text_area(
        "Experience Description",
        height=100
    )

    st.header("🏆 Certifications")

    certifications = st.text_area(
        "Certifications",
        placeholder="Python Certification\nWeb Development Certification"
    )

    st.header("🌐 Languages")

    languages = st.text_input(
        "Languages",
        placeholder="English, Telugu, Hindi"
    )


# =========================
# RESUME PREVIEW
# =========================

with right:

    st.header("📋 Resume Preview")

    if name:
        st.markdown(
            f"<h1 style='text-align:center;color:#2563EB'>{name}</h1>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h1 style='text-align:center;color:gray'>Your Name</h1>",
            unsafe_allow_html=True
        )

    contact = []

    if email:
        contact.append(email)

    if phone:
        contact.append(phone)

    if location:
        contact.append(location)

    if contact:
        st.markdown(
            "<p style='text-align:center'>"
            + " | ".join(contact)
            + "</p>",
            unsafe_allow_html=True
        )

    if linkedin or github:

        links = []

        if linkedin:
            links.append("LinkedIn: " + linkedin)

        if github:
            links.append("GitHub: " + github)

        st.markdown(
            "<p style='text-align:center'>"
            + " | ".join(links)
            + "</p>",
            unsafe_allow_html=True
        )

    st.divider()

    if objective:
        st.subheader("🎯 Career Objective")
        st.write(objective)

    if degree or college:

        st.subheader("🎓 Education")

        if degree:
            st.write("**" + degree + "**")

        if college:
            st.write(college)

        if education_year:
            st.write("Year:", education_year)

        if cgpa:
            st.write("CGPA / Percentage:", cgpa)

    if skills:

        st.subheader("💻 Skills")

        for skill in skills.split(","):
            if skill.strip():
                st.write("•", skill.strip())

    if project_name:

        st.subheader("🛠️ Project")

        st.write("**" + project_name + "**")

        if project_description:
            st.write(project_description)

        if project_technologies:
            st.write(
                "**Technologies:** "
                + project_technologies
            )

    if company or role:

        st.subheader("💼 Internship / Experience")

        if role:
            st.write("**" + role + "**")

        if company:
            st.write(company)

        if experience:
            st.write(experience)

    if certifications:

        st.subheader("🏆 Certifications")

        for certificate in certifications.split("\n"):
            if certificate.strip():
                st.write("•", certificate)

    if languages:

        st.subheader("🌐 Languages")

        st.write(languages)


# =========================
# PDF CREATION
# =========================

def create_pdf():

    buffer = BytesIO()

    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    name_style = ParagraphStyle(
        "Name",
        parent=styles["Title"],
        fontSize=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#2563EB")
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.HexColor("#2563EB"),
        spaceBefore=12,
        spaceAfter=6
    )

    normal_style = ParagraphStyle(
        "Normal",
        parent=styles["Normal"],
        fontSize=10,
        leading=14
    )

    content = []

    # =========================
    # NAME
    # =========================

    content.append(
        Paragraph(
            name if name else "Your Name",
            name_style
        )
    )

    # =========================
    # CONTACT
    # =========================

    contact_details = []

    if email:
        contact_details.append(email)

    if phone:
        contact_details.append(phone)

    if location:
        contact_details.append(location)

    if contact_details:

        content.append(
            Paragraph(
                " | ".join(contact_details),
                normal_style
            )
        )

    content.append(Spacer(1, 10))

    # =========================
    # CAREER OBJECTIVE
    # =========================

    if objective:

        content.append(
            Paragraph(
                "CAREER OBJECTIVE",
                heading_style
            )
        )

        content.append(
            Paragraph(
                objective,
                normal_style
            )
        )

    # =========================
    # EDUCATION
    # =========================

    if degree or college:

        content.append(
            Paragraph(
                "EDUCATION",
                heading_style
            )
        )

        education_text = ""

        if degree:
            education_text += (
                "<b>" + degree + "</b><br/>"
            )

        if college:
            education_text += (
                college + "<br/>"
            )

        if education_year:
            education_text += (
                "Year: " + education_year + "<br/>"
            )

        if cgpa:
            education_text += (
                "CGPA / Percentage: " + cgpa
            )

        content.append(
            Paragraph(
                education_text,
                normal_style
            )
        )

    # =========================
    # SKILLS
    # =========================

    if skills:

        content.append(
            Paragraph(
                "SKILLS",
                heading_style
            )
        )

        content.append(
            Paragraph(
                skills,
                normal_style
            )
        )

    # =========================
    # PROJECT
    # =========================

    if project_name:

        content.append(
            Paragraph(
                "PROJECT",
                heading_style
            )
        )

        project_text = (
            "<b>" + project_name + "</b><br/>"
        )

        if project_description:
            project_text += (
                project_description + "<br/>"
            )

        if project_technologies:
            project_text += (
                "<b>Technologies:</b> "
                + project_technologies
            )

        content.append(
            Paragraph(
                project_text,
                normal_style
            )
        )

    # =========================
    # INTERNSHIP / EXPERIENCE
    # =========================

    if company or role:

        content.append(
            Paragraph(
                "INTERNSHIP / EXPERIENCE",
                heading_style
            )
        )

        experience_text = ""

        if role:
            experience_text += (
                "<b>" + role + "</b><br/>"
            )

        if company:
            experience_text += (
                company + "<br/>"
            )

        if experience:
            experience_text += experience

        content.append(
            Paragraph(
                experience_text,
                normal_style
            )
        )

    # =========================
    # CERTIFICATIONS
    # =========================

    if certifications:

        content.append(
            Paragraph(
                "CERTIFICATIONS",
                heading_style
            )
        )

        for certificate in certifications.split("\n"):

            if certificate.strip():

                content.append(
                    Paragraph(
                        "• " + certificate,
                        normal_style
                    )
                )

    # =========================
    # LANGUAGES
    # =========================

    if languages:

        content.append(
            Paragraph(
                "LANGUAGES",
                heading_style
            )
        )

        content.append(
            Paragraph(
                languages,
                normal_style
            )
        )

    # Create PDF
    pdf.build(content)

    buffer.seek(0)

    return buffer


# =========================
# DOWNLOAD PDF
# =========================

st.divider()

st.header("📥 Download Resume")

if name:

    pdf_file = create_pdf()

    st.download_button(
        label="⬇️ Download Resume as PDF",
        data=pdf_file,
        file_name=name + "_Resume.pdf",
        mime="application/pdf"
    )

else:

    st.info(
        "Please enter your name to download the resume."
    )