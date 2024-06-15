import os
import json
import traceback
from text_utils import read_file, get_table_data
import streamlit as st
from openai_utils import generate_evaluate_chain

# Loading the JSON file
with open(r"C:\Users\Hp\Desktop\MCQ_GEN\Response.json") as file:
    RESPONSE_JSON = json.load(file)

# Function to generate questions and handle user interactions
def generate_questions(text, mcq_count, quiz_data):
    try:
        # Generate questions
        response = generate_evaluate_chain({
            "text": text,
            "number": mcq_count,
            "Response_json": json.dumps(quiz_data)
        })
    except Exception as e:
        st.error("Error generating questions.")
        st.write(e)
        return None

    return json.loads(response.get("quiz", "[]")) if isinstance(response, dict) else None

# Main Streamlit app
def main():
    # Create the title for the app
    st.title("MCQ Application with LangChain")

    # Create form using st.form
    with st.form("user-inputs"):
        uploaded_file = st.file_uploader("Upload PDF file or txt file")
        mcq_count = st.number_input("No of MCQs", min_value=3, max_value=20)
        button = st.form_submit_button("Generate Questions")

    # Check if form is submitted and all fields have input
    if button and uploaded_file is not None and mcq_count:
        with st.spinner("Loading...."):
            try:
                text = read_file(uploaded_file)
                quiz = generate_questions(text, mcq_count, RESPONSE_JSON)

                if quiz is not None:
                    for idx, question in enumerate(quiz):
                        st.write(f"**Question {idx + 1}: {question['mcq']}**")
                        for option_idx, option in enumerate(question["options"], start=1):
                            st.write(f"{option_idx}. {option}")

                        # Display the correct answer in a different style
                        st.markdown(f"**Correct Answer:** <span style='color:green;'>{question['correct']}</span>", unsafe_allow_html=True)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error generating or displaying questions.")

# Run the app
if __name__ == "__main__":
    main()

