import re

# Rule-based responses for common medical questions
def get_medical_response(user_input):
    user_input = user_input.lower()

    if re.search(r"(headache|migraine)", user_input):
        return "Headaches can be caused by stress, dehydration, or various medical conditions. Make sure to stay hydrated and consider seeing a healthcare provider if the problem persists."

    elif re.search(r"(fever|temperature)", user_input):
        return "A fever is usually a sign that your body is fighting an infection. Rest, drink plenty of fluids, and consult a doctor if the fever is high or lasts for more than a few days."

    elif re.search(r"(cold|flu|cough)", user_input):
        return "For common colds or flu, rest and hydration are essential. Over-the-counter medicines can help relieve symptoms, but consult a doctor if symptoms worsen."

    elif re.search(r"(diabetes|blood sugar)", user_input):
        return "Diabetes is a chronic condition that affects how your body processes sugar. It's important to manage your blood sugar levels with a healthy diet, exercise, and possibly medication."

    elif re.search(r"(heart|chest pain)", user_input):
        return "Chest pain could be a serious symptom of heart disease. Please seek medical attention immediately if you experience chest pain."

    elif re.search(r"(pregnancy|pregnant)", user_input):
        return "Pregnancy involves significant changes in your body. Make sure to consult with a healthcare provider for proper prenatal care and advice."

    else:
        return "I'm sorry, I don't have information on that topic. Please consult a healthcare professional for more accurate guidance."

def chatbot():
    print("Medical Chatbot: How can I assist you today? (Type 'exit' to quit)")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Medical Chatbot: Take care and stay healthy!")
            break
        
        response = get_medical_response(user_input)
        print(f"Medical Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
