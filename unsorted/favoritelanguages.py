favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phill': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:
    print(f"\n{name.title()}")

"""language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")"""