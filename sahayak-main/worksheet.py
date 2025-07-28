import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv 
import streamlit as st
import json
import re
from fpdf import FPDF
load_dotenv()
GEMINI_API_KEY=os.getenv('GEMINI_API_KEY')



def read_worksheet_from_json(json_path: str, key: str = "worksheet") -> str:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=15)
        self.add_page()
        self.set_font("Arial", size=12)

    def write_formatted_text(self, text: str):
        lines = text.split("\\n")
        for line in lines:
            parts = re.split(r'(\*\*.*?\*\*)', line)
            for part in parts:
                if part.startswith("**") and part.endswith("**"):
                    self.set_font("Arial", style='B', size=12)
                    self.multi_cell(0, 5, part[2:-2])  # removed ln argument
                else:
                    self.set_font("Arial", style='', size=12)
                    self.multi_cell(0, 5, part)        # removed ln argument
            self.ln()


def save_to_pdf(content: str, filename: str, folder: str = "worksheets"):
    os.makedirs(folder, exist_ok=True)
    pdf = PDF()
    pdf.write_formatted_text(content)
    output_path = os.path.join(folder, filename)
    pdf.output(output_path)
    print(f"✅ Worksheet PDF saved to: {output_path}")

try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    print("Error: The GEMINI_API_KEY environment variable is not set.")
    print("Please set your API key to run this script.")
    exit()

# --- Model Initialization ---
vision_model = genai.GenerativeModel('gemini-2.0-flash')
text_model = genai.GenerativeModel('gemini-2.5-pro')

def extract_text_from_image(image_path):
    """
    Extracts text from an image using the Gemini Pro Vision model.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The extracted text from the image, or None if an error occurs.
    """
    try:
        img = Image.open(image_path)
        response = vision_model.generate_content(["Extract the text from this textbook page.", img])
        return response.text
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during text extraction: {e}")
        return None

def generate_worksheet(text_content, grade_level):
    """
    Generates a worksheet for a specific grade level based on the provided text.

    Args:
        text_content (str): The source passage for the worksheet.
        grade_level (int): The grade level of the target students.

    Returns:
        str: The generated worksheet content, or a failure message.
    """
    prompt = f"""
You are an experienced educational content creator. Based on the following passage, create an engaging and age-appropriate worksheet for a Grade {grade_level} student.

**Instructions:**
- As the grade level increases, increase the complexity and depth of the questions.
- Avoid using generic phrases like "According to the text". Instead, refer to the actual topic or concept.
- Ensure all questions are clear, concise, and grammatically correct.
- Structure the worksheet professionally, and label each section properly.
- At the end, include a clearly marked **Answer Key** for teacher reference.
- at the beging of the worksheet, dont give instroctions, just give the title of the worksheet.

**Worksheet Format:**
1. **Multiple-Choice Questions** (3-10 questions based on grade level)
   - Each question should have 4 options (A–D) with only one correct answer.
   - dont give instructions for multiple choice questions, just give the question and options.
   - for grade 3, the questions should be simple and straightforward and number of question should be 3.
    - for grade 4, the questions should be slightly more complex and number of question should be 4.
    - for grade 5, the questions should be more analytical and number of question should be 5.
    - for grade 6, the questions should be more analytical and number of question should be 6.
    - for grade 7, the questions should be more analytical and number of question should be 7.
    - for grade 8, the questions should be more analytical and number of question should be 8.
    - for grade 9, the questions should be more analytical and number of question should be 9.
    - for grade 10, the questions should be more analytical and number of question should be 10.


2. **True or False Questions** (2 questions)
    - Each question should be a statement that the student must determine as true or false.
    - dont give instructions for multiple choice questions, just give the question and options.


3. **Short Answer Question** 
   - This should encourage critical thinking or personal reflection related to the topic.
   - The answer should be concise, typically one or two sentences and it should be blank in worksheet.
   - dont give instructions for multiple choice questions, just give the question and options.

**Source Text:**
---
{text_content}
---

**Begin the Worksheet Below:**
"""
    try:
        response = text_model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Failed to generate worksheet for grade {grade_level}. Error: {e}"


def main():
    """
    Main function to run the textbook to worksheet generation process.
    """
    image_path = input("Enter the path to the textbook page image: ")

    print("\nExtracting text from the image...")
    extracted_text = extract_text_from_image(image_path)

    if not extracted_text:
        print("Could not proceed without extracted text.")
        return

    print("Text extracted successfully!")
    print("-" * 30)

    grade = int(input("Enter the grade level which you want to generate the worksheet: "))

    # for grade in grade_levels:
    print(f"\nGenerating worksheet for Grade {grade}...")
    worksheet = generate_worksheet(extracted_text, grade)
    with open("syllabus_results.json", "w", encoding="utf-8") as f:
        json.dump(worksheet, f, indent=4, ensure_ascii=False)
    print(f"\n--- Grade {grade} Worksheet ---")
    print(worksheet)
    print("-" * 30)

        # === Main Execution ===
    json_file_path = "syllabus_results.json"  

    try:
        raw_content = read_worksheet_from_json(json_file_path)
        if raw_content:
            save_to_pdf(raw_content, f"Grade_{grade}_.pdf")
        else:
            print("❌ No worksheet content found in the JSON.")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()