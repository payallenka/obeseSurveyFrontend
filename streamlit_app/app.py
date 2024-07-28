import streamlit as st
import requests



st.title('Obesity and Fitness Solutions Survey')

with st.form(key='my_form'):
    # Demographic Information
    st.subheader("Demographic Information")
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female", "Non-binary", "Prefer not to say"])
    location = st.text_input("Location")
    occupation = st.text_input("Occupation")

    # Observational Questions
    st.subheader("Observational Questions")
    encounter_obese = st.radio("Do you encounter individuals who are obese in your daily life?", ["Yes", "No"])
    
    # Show profession_of_obese only if encounter_obese is "Yes"
    if encounter_obese == "Yes":
        profession_of_obese = st.selectbox("What profession do these individuals typically have?", 
                                           ["Healthcare", "Education", "Technology", "Retail", "Service Industry", "Other"])
    else:
        profession_of_obese = "Not applicable"  # Or another appropriate value

    # Perceptions of Obesity
    st.subheader("Perceptions of Obesity")
    causes_of_obesity = st.selectbox("In your opinion, what is the primary cause of obesity?", 
                                     ["Genetics", "Lack of physical activity", "Poor dietary choices", "Psychological factors", "Socioeconomic factors", "Environmental factors", "Other"])
    junk_food_main_cause = st.radio("Do you believe that junk food is the main reason for obesity?", ["Yes", "No", "Unsure"])

    # Fitness Apps and Programs
    st.subheader("Fitness Apps and Programs")
    used_fitness_app = st.radio("Have you ever used a fitness app or program?", ["Yes", "No"])
    
    # Show fitness_apps_used only if used_fitness_app is "Yes"
    if used_fitness_app == "Yes":
        fitness_apps_used = st.selectbox("Which fitness app or program have you used?", 
                                         ["Don't Use","MyFitnessPal", "Fitbit", "Weight Watchers", "Nike Training Club", "Strava", "Other"])
    else:
        fitness_apps_used = "Not applicable"  # Or another appropriate value

    reasons_for_app_failure = st.selectbox("In your experience, why do you think some fitness apps or programs fail to help people achieve their fitness goals?", 
                                           ["Lack of personalization", "User interface issues", "Inadequate support or motivation", "High cost", "Poor integration with other tools", "Other"])

    # Needs and Preferences
    st.subheader("Needs and Preferences")
    effective_features = st.selectbox("What feature do you believe would make a fitness app or program more effective for individuals with obesity?", 
                                      ["Personalized workout plans", "Dietary recommendations", "Regular progress tracking", "Community support and motivation", "Professional guidance (e.g., nutritionists, trainers)", "Integration with wearable devices", "Other"])
    barriers_to_adherence = st.selectbox("What barrier do you think prevents people from adhering to fitness and diet programs?", 
                                         ["Lack of time", "High cost of programs or healthy food", "Lack of motivation", "Social pressures", "Inadequate knowledge or resources", "Other"])

    # Additional Comments
    st.subheader("Additional Comments")
    additional_comments = st.text_area("Please provide any additional comments or suggestions on how to improve fitness solutions for individuals with obesity:", value= "Null")

    submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        # Validation
        if not location or not occupation:
            st.error("Please fill in all the required fields.")
        else:
            payload = {
                'age': age,
                'gender': gender,
                'location': location,
                'occupation': occupation,
                'encounter_obese': encounter_obese,
                'profession_of_obese': profession_of_obese,
                'primary_causes_of_obesity': causes_of_obesity,
                'junk_food_main_cause': junk_food_main_cause,
                'used_fitness_app': used_fitness_app,
                'fitness_apps_used': fitness_apps_used,
                'reasons_for_app_failure': reasons_for_app_failure,
                'effective_features': effective_features,
                'barriers_to_adherence': barriers_to_adherence,
                'additional_comments': additional_comments
            }

            # Debugging output
            #st.write("Sending payload:", payload)

            response = requests.post('https://obeseSurveyProject.onrender.com/api/formdata/', json=payload)
            
            
            # Debugging output
            #st.write("Response status code:", response.status_code)
            #st.write("Response content:", response.text)

            if response.status_code == 201:
                st.success('Data submitted successfully!')
            else:
                st.error(f'Error: {response.status_code} - {response.text}')
