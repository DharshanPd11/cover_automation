import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import base64
from datetime import date
 

# Set page config at the beginning
st.set_page_config(page_title="Cover Letter Generator")

# Create a Streamlit app
st.title('Cover Letter Generator')

# Input Form
company_name = st.text_input('Company Name')
position = st.text_input('Position')
location = st.text_input('Location (Leave empty for default)')
today = date.today()


if st.button('Generate Cover Letter'):
    if location == '':
        location = ''
    
    # Create a PDF document
    pdf_file = f"{company_name}_cover.pdf"
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Define a paragraph style for justified text
    styles = getSampleStyleSheet()
    justified_style = styles["Normal"]
    justified_style.alignment = 4  # 4 stands for 'ALIGN_JUSTIFY'
    justified_style.fontSize = 12
    justified_style.fontName = 'Times-Roman'
    justified_style.leading = 14

    # Create a Story object to hold the text
    story = []

    # Your cover letter content here
    cover_content = f"""                                                
Dear Recruiter,                                                                 

I am writing to express my strong interest in {position} position at {company_name}. As a recent
graduate with a Bachelor's degree in Computer Science and valuable internship experience, I
am excited about the opportunity to contribute my skills and enthusiasm to your dynamic team.

Throughout my academic journey, I cultivated a strong foundation in Python, Data Analytics,
and in Machine Learning. My passion for AI and ML drove me to actively engage in Data
Science hackathons, where I applied these skills in real-world scenarios. My coursework and
practical projects were pivotal in honing my proficiency in Python and constructing resilient
Machine Learning models. Additionally, I augmented my Data Analytics expertise through the
Google Data Analytics Professional Course.

My internship at Zoho Corporation, Chennai, exposed me to industry-level software
development challenges, where I had the opportunity to apply my knowledge to develop web
app extensions using REST/APIs.

Key highlights of my qualifications include:

- Proficiency in Python and its libraries like pytorch, tensorflow, matplotlib, pandas,
flask, and sklearn.

- Familiarity with Machine Learning and Web application frameworks like Django and Flask.

- Proficiency with SQL and Spreadsheets.

- Data Analysis and problem-solving abilities.

- Excellent communication skills and the ability to translate technical findings into
nontechnical terms.

Moreover, I am eager to collaborate with the company’s talented team and leverage the
resources available at the {location} office to make meaningful contributions to ongoing
projects. I am confident that my passion for technology and dedication to pushing the
boundaries of knowledge make me a strong candidate for this opportunity.

Thank you for considering my application. I look forward to the possibility of contributing
to the company’s success. Please feel free to contact me if further information is required,
mobile: +918072111647 or via Email: priyadharshanraja@gmail.com.

Sincerely,

Priyadharshan Raja
"""
    date_ = f"{today}"
    date_line = date_.strip().split('\n\n')
    
    # Split the text into paragraphs and add each as a justified paragraph with spacing
    paragraphs = cover_content.strip().split('\n\n')
    for i, paragraph in enumerate(paragraphs):
        story.append(Paragraph(paragraph, justified_style))
        if i+1 < len(paragraphs) - 1:
            story.append(Spacer(1, 12))  # Adjust the second value for the desired spacing

    # Build and save the PDF document
    doc.build(story)

    with open(pdf_file, "rb") as f:
        pdf_bytes = f.read()
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            key="download_button",
            file_name=f"{company_name}_cover.pdf",
        )

