import sys

class Respondent:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class AgeGroup:
    def __init__(self, min_age, max_age):
        self.min_age = min_age
        self.max_age = max_age
    def contains(self, age):
        if self.max_age is None:
            return age >= self.min_age
        return self.min_age <= age <= self.max_age
    def get_label(self):
        if self.max_age is None:
            return f"{self.min_age}+"
        return f"{self.min_age}-{self.max_age}"


class SurveyGrouper:
    def __init__(self, boundaries):
        if not boundaries:
            raise ValueError("Необходимо указать границы")
        if any(b < 0 or b > 123 for b in boundaries):
            raise ValueError("Границы должны быть от 0 до 123")
        if boundaries != sorted(set(boundaries)):
            raise ValueError("Границы должны строго возрастать")
        self.groups = self.create_groups(boundaries)

    def create_groups(self, boundaries):
        groups = []
        previous = 0
        for boundary in boundaries:
            groups.append(AgeGroup(previous, boundary))
            previous = boundary + 1
        groups.append(AgeGroup(previous, None))

        return groups

    def find_group(self, age):
        if not 0 <= age <= 123:
            raise ValueError("Возраст должен быть от 0 до 123")
        for group in self.groups:
            if group.contains(age):
                return group
        return None

    def group_respondents(self, respondents):
        result = {}
        for person in respondents:
            group = self.find_group(person.age)
            if group not in result:
                result[group] = []
            result[group].append(person)
        return result

    def sort_respondents(self, grouped):
        for group in grouped:
            grouped[group].sort(
                key=lambda person: (
                    -person.age,
                    person.name
                )
            )
        return grouped

    def format_result(self, grouped):
        result = []
        for group in reversed(self.groups):
            if group not in grouped:
                continue
            people = []
            for person in grouped[group]:
                people.append(
                    f"{person.name} ({person.age})"
                )
            result.append(
                f"{group.get_label()}: {', '.join(people)}"
            )
        return "\n".join(result)


    def process(self, respondents):
        grouped = self.group_respondents(respondents)
        self.sort_respondents(grouped)
        return self.format_result(grouped)


def read_respondents():
    respondents = []
    while True:
        line = input().strip()
        if line == "END":
            break
        if not line:
            continue
        if "," not in line:
            raise ValueError("Неверный формат строки")
        name, age = line.rsplit(",", 1)
        name = name.strip()
        age = int(age.strip())
        if not name:
            raise ValueError("ФИО не может быть пустым")
        if not 0 <= age <= 123:
            raise ValueError("Возраст должен быть от 0 до 123")
        respondents.append(
            Respondent(name, age)
        )
    return respondents


def main():
    try:
        boundaries = list(map(int, sys.argv[1:]))
        grouper = SurveyGrouper(boundaries)
        respondents = read_respondents()
        result = grouper.process(respondents)
        if result:
            print(result)
    except ValueError as error:
        print(f"Ошибка: {error}", file=sys.stderr)


if __name__ == "__main__":
    main()
