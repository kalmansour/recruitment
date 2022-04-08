def get_skills():
    return ['coding', 'cooking', 'singing','dancing','laughing']


def show_skills(skills):
    skills = skills
    for listed_skills in enumerate(skills, 1):
        print (listed_skills)

    ...


def get_user_skills(skills):
    show_skills(skills)
    chosen_skill_1 = int(input("choose first skill:")) - 1
    chosen_skills = []
    chosen_skills.append(skills[chosen_skill_1])
    chosen_skill_2 = int(input("choose second skill:")) - 1
    chosen_skills.append(skills[chosen_skill_2])
    return chosen_skills
    ...
    


def get_user_cv(skills):
    cv = dict()
    name = input("What's your full name:")
    age = int(input("What's your age:"))
    experience = int(input("What's your experience:"))
    dict_1 = {'name':name,'age':age,'experience':experience,'skills': get_user_skills(skills)}
    cv.update(dict_1)
    return cv
    ...


def check_acceptance(cv, desired_skill):
    if 25 <= int(cv['age']) <=40 and int(cv['experience']) > 3 and desired_skill in cv['skills']:
        return True
    ...


def main():
    print("Welcome to this recruitment program!")
    skills = get_skills()
    cv = get_user_cv(skills)
    while True:
        if check_acceptance(cv, skills[2]) == True:
            print("Congratulations! You have been accepted")
        else:
            print("Sorry..You have been rejected")
        break
    ...


if __name__ == "__main__":
    main()
