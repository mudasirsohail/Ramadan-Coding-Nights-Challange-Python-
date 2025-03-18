import streamlit as st
import random
import time 

st.title("Quiz Application")

questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
        "answer": "Pacific Ocean"
    },
    {
        "question": "How many continents are there on Earth?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7"
    },
    {
        "question": "Who was the first President of the United States?",
        "choices": ["Thomas Jefferson", "Abraham Lincoln", "George Washington", "John Adams"],
        "answer": "George Washington"
    },
    {
        "question": "What is the smallest country in the world?",
        "choices": ["Monaco", "Vatican City", "Liechtenstein", "San Marino"],
        "answer": "Vatican City"
    },
    {
        "question": "Which is the longest river in the world?",
        "choices": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
        "answer": "Nile River"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "choices": ["Gold", "Oxygen", "Silver", "Iron"],
        "answer": "Oxygen"
    },
    {
        "question": "Which is the largest desert in the world?",
        "choices": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "Who invented the light bulb?",
        "choices": ["Nikola Tesla", "Thomas Edison", "Alexander Graham Bell", "Albert Einstein"],
        "answer": "Thomas Edison"
    },
    {
        "question": "What is the national animal of China?",
        "choices": ["Panda", "Tiger", "Dragon", "Elephant"],
        "answer": "Panda"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "choices": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
        "answer": "Carbon Dioxide"
    },
    {
        "question": "Which country gifted the Statue of Liberty to the USA?",
        "choices": ["Germany", "France", "Italy", "Canada"],
        "answer": "France"
    },
    {
        "question": "Which is the highest mountain in the world?",
        "choices": ["K2", "Mount Everest", "Kilimanjaro", "Mount Fuji"],
        "answer": "Mount Everest"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["Gold", "Iron", "Diamond", "Quartz"],
        "answer": "Diamond"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"],
        "answer": "Albert Einstein"
    },
    {
        "question": "Which country is famous for the Great Wall?",
        "choices": ["India", "China", "Japan", "Russia"],
        "answer": "China"
    },
    {
        "question": "What is the national currency of Japan?",
        "choices": ["Dollar", "Euro", "Yen", "Won"],
        "answer": "Yen"
    },
    {
        "question": "What is the chemical formula of water?",
        "choices": ["CO2", "H2O", "O2", "CH4"],
        "answer": "H2O"
    }
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_options = st.radio("Choose your answer", question["choices"],key="answer")

if st.button("Submit Answer"):

    if selected_options == question["answer"]:

        st.success("Correct ✅")

    else:

        st.error("Incorrect ❌ The correct answer is" + question["answer"])

    time.sleep(3)

    st.session_state.current_question = random.choice(questions)

    st.rerun()
