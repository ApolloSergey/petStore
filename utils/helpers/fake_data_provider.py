from faker import Faker


class Fake:
    def __init__(self):
        self.fake = Faker()

    def word(self):
        return self.fake.word()

    def words_combination(self):
        return " ".join(self.fake.word() for _ in range(3))

    def number_n_digits(self, length=6):
        random_number = ""
        for _ in range(length):
            random_number += str(self.fake.random_digit())
        return random_number

    def number_n_letters(self, length=6):
        random_string = ""
        for _ in range(length):
            random_string += str(self.fake.random_letter())
        return random_string

    def word_with_number(self, number_amount=6):
        return "".join(self.fake.word() + "_" + self.number_n_digits(number_amount))

    def random_sentence(self, number_of_sentences=3):
        return self.fake.paragraph(nb_sentences=number_of_sentences)

    def random_host_name(self):
        return self.fake.hostname()

    def random_file_extension(self):
        return self.fake.file_extension()

    def random_file_name(self):
        return self.fake.file_name()

    def random_file_path(self):
        return self.fake.file_path()

    def street_address(self):
        return self.fake.street_address()

    def street_name(self):
        return self.fake.street_name()

    def city(self):
        return self.fake.city()

    def country(self):
        return self.fake.country()

    def country_code(self):
        return self.fake.country_code()

    def state(self):
        return self.fake.state()

    def zip(self):
        return self.fake.postcode()

    def email(self):
        return self.fake.ascii_safe_email()

    def phone_number(self):
        return self.fake.phone_number()

    def bank_account_iban(self):
        return self.fake.iban()

    def bank_swift(self):
        return self.fake.swift()


fake = Fake()
