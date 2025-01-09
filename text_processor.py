import re

def preprocess_text(text):
    # Remove special characters and extra whitespace
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def extract_sections(text):
    # Simple section extraction based on common resume headings
    sections = {}
    current_section = "general"
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip().lower()
        if line in ["education", "experience", "skills", "projects"]:
            current_section = line
            sections[current_section] = []
        else:
            if current_section in sections:
                sections[current_section].append(line)
            else:
                sections[current_section] = [line]
    
    return sections

# # Test the text processor
# if __name__ == "__main__":
#     sample_text = """
#     John Doe
#     john.doe@email.com

#     Education
#     Bachelor of Science in Computer Science

#     Experience
#     Software Engineer at XYZ Company

#     Skills
#     Python, Java, Machine Learning
#     """

#     preprocessed_text = preprocess_text(sample_text)
#     sections = extract_sections(preprocessed_text)
#     print(sections)