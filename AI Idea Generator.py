def generate_idea():
    print("Welcome to the AI-powered Idea Generator!")
    
    while True:
        print("\nLet's generate a creative idea for you.")
        
        # Gathering inputs
        idea_type = input("What type of idea do you need? (business/art/app or 'exit' to quit): ").strip().lower()
        
        if idea_type == 'exit':
            print("Thank you for using the AI-powered Idea Generator. Goodbye!")
            break
        
        interest = input("What are your interests or passions? (e.g., technology, environment, education): ").strip().lower()
        target_audience = input("Who is your target audience? (e.g., children, professionals, seniors): ").strip().lower()
        budget = input("What's your budget? (low/medium/high): ").strip().lower()
        
        # Generating ideas based on inputs
        if idea_type == "business":
            if interest == "technology" and target_audience == "professionals" and budget == "high":
                print("Idea: A high-end co-working space with state-of-the-art technology for tech professionals.")
            elif interest == "environment" and target_audience == "children" and budget == "low":
                print("Idea: An eco-friendly toy line made from recycled materials.")
            # Add more conditions here for other combinations
            else:
                print("Idea: A general business consulting service tailored to your specified interests.")
        
        elif idea_type == "art":
            if interest == "education" and target_audience == "children" and budget == "medium":
                print("Idea: An interactive art exhibition that teaches kids about history through augmented reality.")
            elif interest == "technology" and target_audience == "seniors" and budget == "low":
                print("Idea: A digital art workshop for seniors to create and share their digital paintings.")
            # Add more conditions here for other combinations
            else:
                print("Idea: A unique art project exploring your specified interests.")
        
        elif idea_type == "app":
            if interest == "education" and target_audience == "professionals" and budget == "medium":
                print("Idea: An app that offers bite-sized professional development courses.")
            elif interest == "environment" and target_audience == "children" and budget == "high":
                print("Idea: An educational game app teaching kids about sustainability and the environment.")
            # Add more conditions here for other combinations
            else:
                print("Idea: A versatile app concept based on your specified interests.")
        
        else:
            print("Sorry, I didn't understand that type of idea. Please try again.")

# Run the idea generator
generate_idea()
