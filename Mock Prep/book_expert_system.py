def recommend_books(user_profile, books_db):
    recommendations = []

    for book in books_db:
        if not book["available"]:
            continue

        if book["domain"].lower() != user_profile["domain"].lower():
            continue
        if book["level"].lower() != user_profile["level"].lower():
            continue

        if book["language"].lower() != user_profile["preferred_language"].lower():
            continue

        if "project_type" in user_profile:
            project_keywords = [
                user_profile["project_type"].lower(),
                "project",
                "research",
                "development",
            ]
            description_lower = book["description"].lower()
            if not any(keyword in description_lower for keyword in project_keywords):
                recommendations.append(book)
                continue

        if "time_available" in user_profile:
            if book["length"].lower() != user_profile["time_available"].lower():
                recommendations.append(book)
                continue

        if not set(book["prerequisites"]).issubset(set(user_profile["skills"])):
            recommendations.append(book)
            continue

        if (
            "format" in user_profile
            and book["format"].lower() != user_profile["format"].lower()
        ):
            recommendations.append(book)
            continue

        if user_profile.get("recent_only", False) and book["publication_year"] < 2021:
            continue

        recommendations.append(book)

    return recommendations


books = [
    {
        "title": "Hands-On Machine Learning with Scikit-Learn",
        "author": "Aurélien Géron",
        "description": "Intermediate ML book using Python",
        "domain": "Machine Learning",
        "level": "Intermediate",
        "language": "Python",
        "format": "eBook",
        "length": "long",
        "publication_year": 2022,
        "rating": 4.7,
        "prerequisites": ["Python", "Linear Algebra"],
        "available": True,
    },
    {
        "title": "Flask Web Development",
        "author": "Miguel Grinberg",
        "description": "Web App projects using Python and Flask",
        "domain": "Web Development",
        "level": "Beginner",
        "language": "Python",
        "format": "PDF",
        "length": "medium",
        "publication_year": 2018,
        "rating": 4.5,
        "prerequisites": ["Python"],
        "available": True,
    },
    {
        "title": "Data Science from Scratch",
        "author": "Joel Grus",
        "description": "Introduction to data science and machine learning with Python",
        "domain": "Data Science",
        "level": "Beginner",
        "language": "Python",
        "format": "eBook",
        "length": "long",
        "publication_year": 2021,
        "rating": 4.8,
        "prerequisites": ["Python"],
        "available": True,
    },
    {
        "title": "Deep Learning with Python",
        "author": "François Chollet",
        "description": "A comprehensive guide to deep learning",
        "domain": "Machine Learning",
        "level": "Intermediate",
        "language": "Python",
        "format": "PDF",
        "length": "long",
        "publication_year": 2020,
        "rating": 4.6,
        "prerequisites": ["Python", "Linear Algebra"],
        "available": True,
    },
    {
        "title": "Building Web Apps with Flask",
        "author": "Matthew Makai",
        "description": "Learn Flask by building web applications",
        "domain": "Web Development",
        "level": "Intermediate",
        "language": "Python",
        "format": "eBook",
        "length": "medium",
        "publication_year": 2021,
        "rating": 4.3,
        "prerequisites": ["Python", "Flask"],
        "available": True,
    },
    {
        "title": "Python Machine Learning",
        "author": "Sebastian Raschka",
        "description": "Master machine learning with Python",
        "domain": "Machine Learning",
        "level": "Advanced",
        "language": "Python",
        "format": "eBook",
        "length": "long",
        "publication_year": 2021,
        "rating": 4.9,
        "prerequisites": ["Python", "Linear Algebra", "Statistics"],
        "available": True,
    },
]

user = {
    "domain": "Machine Learning",
    "level": "Intermediate",
    "preferred_language": "Python",
    "project_type": "Research",
    "time_available": "long",
    "skills": ["Python", "Linear Algebra"],
    "format": "eBook",
    "recent_only": True,
}

recommended_books = recommend_books(user, books)
print("\nRecommendations:")
for book in recommended_books:
    print(f"\t{book['title']} by {book['author']}")

user1 = {
    "domain": "Web Development",
    "level": "Intermediate",
    "preferred_language": "Python",
    "project_type": "Development",
    "time_available": "medium",
    "skills": ["Python", "Flask"],
    "format": "eBook",
    "recent_only": False,
}


recommended_books = recommend_books(user1, books)
print("\nRecommendations:")
for book in recommended_books:
    print(f"\t{book['title']} by {book['author']}")
