from dataclasses import dataclass
from enum import Enum
from typing import List

class ExperienceLevel(Enum):
    ADVANCED = 'Advanced'
    MEDIUM = 'Medium'
    BEGINNER = 'Beginner'

@dataclass
class LanguageExperience:
    language: str
    experience: ExperienceLevel

    def __str__(self):
        return "%s - %s" % (self.language, self.experience)

@dataclass
class CV:
    personal: str
    experience: List[LanguageExperience]
    education: str

    def __str__(self):
        return "\n Personal: %s \n Experience: %s \n Education: %s \n" % (self.personal, '\n\t'+'\n\t'.join(map(str, self.experience)), self.education)

def _get_experience() -> List[LanguageExperience]:
    experience: List[LanguageExperience] = []
    experience.append(LanguageExperience("C++", ExperienceLevel.ADVANCED.value))
    experience.append(LanguageExperience("C", ExperienceLevel.MEDIUM.value))
    experience.append(LanguageExperience("Python", ExperienceLevel.MEDIUM.value))
    experience.append(LanguageExperience("HTML/CSS/JS/TS/React", ExperienceLevel.MEDIUM.value))
    experience.append(LanguageExperience("C#", ExperienceLevel.BEGINNER.value))
    return experience

cv_alex_oprinca = CV(personal="\n\t Email: %s \n\t Phone: %s" % ("oprincaalexandru@gmail.com", "0758510974"), experience=_get_experience(), education="Bachelor's Degree in Computer Science at Babes Bolyiai University")
