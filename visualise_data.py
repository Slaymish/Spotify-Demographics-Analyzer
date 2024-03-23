import matplotlib.pyplot as plt
import seaborn as sns

def visualise_demographic_data(demographic_data: dict):
    """
    Visualise the demographic data in a human-readable format.
    
    {'gender': 
        {
            'male': 40, 
            'female': 11, 
            'other': 0, 
            'undefined': 8
        }, 
        'average_age': 38.65217391304348, 
        'location': 
            {
                'New York': 1, 
                'New York City': 1, 
                'undefined': 26, 
                'Sheffield': 5, 
                'Harlem, New York, United States': 1, 
                'United States': 4, 
                'Los Angeles': 4, 
                'United Kingdom': 1, 
                'Iceland': 1, 
                'England': 2, 
                'Seattle': 1}
            }
    """
    
    # Visual
    print("\nDemographic Data Analysis")
    print("----------------------------")

    # Gender analysis
    print("Gender Analysis")
    for gender, count in demographic_data['gender'].items():
        print(f"{gender.capitalize()}: {count}")

    # Average age
    print(f"\nAverage Age: {demographic_data['average_age']}")

    # Location analysis
    print("\nLocation Analysis")
    for location, count in demographic_data['location'].items():
        print(f"{location}: {count}")

    print("----------------------------")

    show_visualisation(demographic_data)

def show_visualisation(demographic_data: dict):
    # Sample demographic data
    # Set the style of seaborn for better visuals
    sns.set(style="whitegrid")

    # Gender analysis
    gender_data = demographic_data['gender']
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(gender_data.keys()), y=list(gender_data.values()))
    plt.title('Gender Analysis')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()

    # Average age
    print(f"\nAverage Age: {demographic_data['average_age']}")

    # Location analysis
    location_data = demographic_data['location']
    plt.figure(figsize=(10, 5))
    sns.barplot(x=list(location_data.keys()), y=list(location_data.values()))
    plt.title('Location Analysis')
    plt.xlabel('Location')
    plt.ylabel('Count')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility
    plt.show()

