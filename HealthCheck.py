# a basic health check in python language:

def main():
    print("Welcome to the Health Diagnosis App!")
    print("Please answer the following questions to help us understand your symptoms.\n")

    symptoms = []

    # Ask questions about symptoms
    print("Do you have a fever? (yes/no)")
    fever = input().lower()
    if fever == "yes":
        symptoms.append("fever")

    print("Do you have a cough? (yes/no)")
    cough = input().lower()
    if cough == "yes":
        symptoms.append("cough")

    print("Do you have difficulty breathing? (yes/no)")
    breathing_difficulty = input().lower()
    if breathing_difficulty == "yes":
        symptoms.append("breathing difficulty")

    print("Do you have body aches? (yes/no)")
    body_aches = input().lower()
    if body_aches == "yes":
        symptoms.append("body aches")

    print("Do you have a sore throat? (yes/no)")
    sore_throat = input().lower()
    if sore_throat == "yes":
        symptoms.append("sore throat")

    print("Do you have fatigue? (yes/no)")
    fatigue = input().lower()
    if fatigue == "yes":
        symptoms.append("fatigue")

    # Provide diagnosis based on symptoms
    print("\nBased on your symptoms, you may have the following conditions:")
    if len(symptoms) == 0:
        print("No specific condition identified. Please consult a healthcare professional for further evaluation.")
    else:
        for symptom in symptoms:
            if symptom == "fever" and "cough" in symptoms and "breathing difficulty" in symptoms:
                print("- You may have symptoms of COVID-19. It is recommended to get tested and consult a doctor.")
                print("  Tips: Self-isolate, rest, and hydrate. Monitor your symptoms closely.")
                break
            elif symptom == "fever" and "cough" in symptoms:
                print("- You may have symptoms of flu. Rest and hydrate, and consider seeing a doctor if symptoms worsen.")
                print("  Tips: Stay hydrated, get plenty of rest, and consider over-the-counter flu medications.")
                break
            elif symptom == "fever":
                print("- You may have a fever. Monitor your temperature and consider taking fever-reducing medication.")
                print("  Tips: Get plenty of rest, drink fluids, and take fever-reducing medication if necessary.")
                break
            elif symptom == "cough":
                print("- You may have a common cold. Rest and hydrate, and consider over-the-counter cough medicine.")
                print("  Tips: Drink warm liquids, use a humidifier, and get plenty of rest.")
                break
            elif symptom == "breathing difficulty":
                print("- You may be experiencing breathing difficulties. Seek medical attention immediately.")
                print("  Tips: Call emergency services or visit the nearest emergency room for immediate evaluation.")
                break
            elif symptom == "sore throat":
                print("- You may have a sore throat. Gargle with warm salt water and rest your voice.")
                print("  Tips: Drink warm liquids, suck on throat lozenges, and avoid irritants like smoke and pollution.")
                break
            elif symptom == "fatigue":
                print("- You may be experiencing fatigue. Get plenty of rest and try to reduce stress.")
                print("  Tips: Establish a regular sleep schedule, engage in light exercise, and eat a balanced diet.")
                break
        else:
            print("No specific condition identified. Please consult a healthcare professional for further evaluation.")

if __name__ == "__main__":
    main()
