import re
import spacy

class ResumeParser:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_name(self, text):
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        return ""

    def extract_email(self, text):
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(email_regex, text)
        return match.group() if match else ""

    def extract_phone(self, text):
        phone_regex = r'\b(?:\+\d{1,2}\s?)?(?:$$\d{3}$$|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}\b'
        match = re.search(phone_regex, text)
        return match.group() if match else ""

    def extract_skills(self, text):
        skills = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL", "Machine Learning", "Data Analysis"]
        doc = self.nlp(text.lower())
        found_skills = [skill for skill in skills if skill.lower() in doc.text]
        return found_skills

    def extract_education(self, text):
        education_keywords = ["bachelor", "master", "phd", "degree", "university", "college"]
        doc = self.nlp(text.lower())
        education_sentences = [sent.text for sent in doc.sents if any(keyword in sent.text.lower() for keyword in education_keywords)]
        return education_sentences

    def parse_resume(self, text):
        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "education": self.extract_education(text)
        }

# # Test the parser
# if __name__ == "__main__":
#     sample_resume = """
#     John Doe
#     john.doe@email.com
#     (123) 456-7890

#     Experienced software engineer with expertise in Python and Machine Learning.

#     Education:
#     Bachelor of Science in Computer Science, XYZ University
#     Master of Science in Artificial Intelligence, ABC College

#     Skills:
#     Python, Java, SQL, Machine Learning, Data Analysis
#     """

#     parser = ResumeParser()
#     result = parser.parse_resume(sample_resume)
#     print(result)