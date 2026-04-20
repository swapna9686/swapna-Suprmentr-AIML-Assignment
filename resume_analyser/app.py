import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import preprocess
from PyPDF2 import PdfReader

st.set_page_config(page_title="RESUME ANALYSER", layout="centered")

st.title("👩‍💻 AI Resume Analyser")

# ✅ Correct file uploader
resume_file = st.file_uploader("Upload Resume (.pdf)", type=["pdf"])
job_desc = st.text_area("Enter the Job Description:")

# ✅ Function to extract text from PDF
def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""   # avoid None error
    return text

# ✅ Main logic
if resume_file and job_desc:

    try:
        # ✅ Extract text from PDF
        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text.strip():
            st.error("❌ Could not extract text from PDF")
        else:
            # Preprocess
            resume_clean = preprocess(resume_text)
            job_clean = preprocess(job_desc)

            # Vectorization
            vectorizer = TfidfVectorizer()
            vectors = vectorizer.fit_transform([resume_clean, job_clean])

            # Similarity
            similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            score = round(similarity * 100, 2)

            # Display score
            st.subheader(f"Match Score: {score}%")

            if score > 70:
                st.success("✅ Strong Match")
            elif score > 40:
                st.warning("⚠️ Moderate Match")
            else:
                st.error("❌ Low Match")

            # Keywords
            st.subheader("Top Keywords")
            feature_names = vectorizer.get_feature_names_out()
            st.write(feature_names[:20])

    except Exception as e:
        st.error(f"❌ Error reading PDF: {e}")