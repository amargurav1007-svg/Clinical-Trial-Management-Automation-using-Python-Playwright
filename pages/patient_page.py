class PatientPage:
    def __init__(self, page):
        self.page = page

    def open_form(self):
        self.page.goto("https://demoqa.com/text-box")

    def add_patient(self, name, age, gender, study_protocol):
        self.page.fill("#userName", name)
        self.page.fill("#userEmail", study_protocol + "@study.com")
        self.page.fill("#currentAddress", f"Age: {age}, Gender: {gender}")
        self.page.click("#submit")


