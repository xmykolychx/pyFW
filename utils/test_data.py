from faker import Faker

FAKE = Faker()

class TestData:
    username = FAKE.name()

    text_data = FAKE.pystr(min_chars=10, max_chars=100)

    first_name = FAKE.first_name()
    middle_name = FAKE.first_name_nonbinary()
    last_name = FAKE.last_name()

    employee_id = FAKE.pystr_format(string_format='######')
    other_id = FAKE.pystr_format(string_format='######')

    license_number = FAKE.pystr_format(string_format='######')

    street_one = FAKE.street_address()
    street_two = FAKE.street_address()
    city = FAKE.city()
    province = FAKE.city()
    postcode = FAKE.postcode()

    home_number = FAKE.phone_number()
    mobile_number = FAKE.phone_number()
    work_number = FAKE.phone_number()

    work_email = FAKE.email()
    other_email = FAKE.email()