"""
Vaccination Tracker - PROG211 Object-Oriented Programming 1
Domain: Health
DPG: open-source, simple/accessible, privacy-respecting (no sensitive data), modular
"""

# ---------- Tuple (optional, extra marks): vaccines the program accepts ----------
ALLOWED_VACCINES = ("Polio", "Measles", "BCG", "Yellow Fever", "COVID-19")


# ---------- CLASS 1: Vaccine ----------
class Vaccine:
    """One vaccine dose given to a patient."""

    def __init__(self, name, date_given):
        self.name = name              # attribute
        self.date_given = date_given  # attribute

    def display_info(self):           # method
        return f"{self.name} (given on {self.date_given})"


# ---------- CLASS 2: Patient ----------
class Patient:
    """A patient. Only a code ID, first name and age are stored (privacy)."""

    total_patients = 0  # class attribute shared by ALL patients

    def __init__(self, patient_id, first_name, age):
        self.patient_id = patient_id
        self.first_name = first_name
        self.age = age
        self.vaccines = []            # will hold Vaccine objects
        Patient.total_patients += 1

    # ----- Instance method: works on ONE patient -----
    def add_vaccine(self, vaccine):
        if vaccine.name not in ALLOWED_VACCINES:
            print(f"  '{vaccine.name}' is not a valid vaccine.")
            return
        self.vaccines.append(vaccine)  # objects interacting

    def display_info(self):
        print(f"ID: {self.patient_id} | Name: {self.first_name} | Age: {self.age}")
        if not self.vaccines:
            print("  No vaccines recorded yet.")
        for v in self.vaccines:
            print("  -", v.display_info())

    # ----- Class method: works on the whole class -----
    @classmethod
    def get_total_patients(cls):
        return cls.total_patients

    # ----- Static method: needs no object or class data -----
    @staticmethod
    def is_child(age):
        return age < 18


# ---------- DICTIONARY: stores patients using their ID as the key ----------
patients = {}


def add_patient(patient):
    """Add a patient record to the dictionary."""
    patients[patient.patient_id] = patient


def display_all_patients():
    """Show every patient record."""
    print("\n===== ALL PATIENT RECORDS =====")
    for patient in patients.values():
        patient.display_info()
        print()


# ---------- MAIN PROGRAM ----------
if __name__ == "__main__":
    # 1. Create objects
    p1 = Patient("P001", "Aminata", 5)
    p2 = Patient("P002", "Mohamed", 30)

    # 2. Create vaccine objects and link them to patients
    p1.add_vaccine(Vaccine("Polio", "2026-09-01"))
    p1.add_vaccine(Vaccine("Measles", "2026-09-15"))
    p2.add_vaccine(Vaccine("Yellow Fever", "2026-10-02"))
    p2.add_vaccine(Vaccine("Malaria", "2026-10-03"))  # invalid -> rejected

    # 3. Store in the dictionary
    add_patient(p1)
    add_patient(p2)

    # 4. Display everything
    display_all_patients()

    # 5. Use class method and static method
    print("Total patients:", Patient.get_total_patients())
    print("Is Aminata a child?", Patient.is_child(p1.age))
    print("Is Mohamed a child?", Patient.is_child(p2.age))

    # 6. Look up one patient quickly by ID (dictionary benefit)
    print("\nLookup P002:")
    patients["P002"].display_info()S