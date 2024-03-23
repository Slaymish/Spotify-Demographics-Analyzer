def analyze_demographics(artist_demographics):
    gender_count = {"male": 0, "female": 0, "undefined": 0}
    total_age = 0
    age_count = 0
    location_count = {}

    for artist, demographics in artist_demographics.items():
        # Gender analysis
        if 'gender' in demographics:
            if isinstance(demographics['gender'], list):
                for gender in demographics['gender']:
                    if gender.lower() in gender_count:
                        gender_count[gender.lower()] += 1
            elif isinstance(demographics['gender'], dict):
                for person, gender in demographics['gender'].items():
                    gender = gender.lower()
                    gender_count[gender] = gender_count.get(gender, 0) + 1

        # Age analysis
        if 'age' in demographics and isinstance(demographics['age'], dict):
            for person, age in demographics['age'].items():
                if age:
                    if isinstance(age, str) and age.isdigit():
                        age = int(age)
                    if isinstance(age, int):
                        total_age += age
                        age_count += 1

        # Location analysis
        if 'location' in demographics:
            if isinstance(demographics['location'], dict):
                for person, location in demographics['location'].items():
                    location_count[location] = location_count.get(location, 0) + 1
            elif isinstance(demographics['location'], str):
                location_count[demographics['location']] = location_count.get(demographics['location'], 0) + 1

    # Calculate average age as a float for precise comparison
    average_age = float(total_age) / age_count if age_count else 0.0

    analysis_result = {
        "gender": gender_count,
        "average_age": average_age,  # Keep as a float for precise average
        "location": location_count
    }

    return analysis_result
