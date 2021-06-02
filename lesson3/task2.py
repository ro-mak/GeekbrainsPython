def print_user_info(
        second_name,
        first_name,
        date_of_birth,
        email,
        phone,
        city
): print(
    f"User {first_name} {second_name} born {date_of_birth} lives in {city} can be contacted via email {email} and phone {phone}"
)


print_user_info(
    first_name="Roma",
    second_name="Makuta",
    date_of_birth="1.01.0000",
    city="Jerusalem",
    email="python@yandex.ru",
    phone="+03413387687"
)
