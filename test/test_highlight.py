from highlight import find_phone_pattern, find_dob_pattern


def test_find_phone_pattern():
    phone_number_with_dash = "The phone number is 123-456-7890, Please reach out to me with questions."
    phone_number_with_parentheses = "TEL: (123) 456-7890, Please reach out to me with questions."
    start_with_phone_number = "777 888 1111, Please reach out"
    end_with_phone_number = "Please reach out me at 555.876.1212"

    match = find_phone_pattern(phone_number_with_dash)
    result = [phone_number_with_dash[start: end] for start, end in match]
    assert " 123-456-7890" in result

    match = find_phone_pattern(phone_number_with_parentheses)
    result = [phone_number_with_parentheses[start: end] for start, end in match]
    assert " (123) 456-7890" in result

    match = find_phone_pattern(start_with_phone_number)
    result = [start_with_phone_number[start: end] for start, end in match]
    assert "777 888 1111" in result

    match = find_phone_pattern(end_with_phone_number)
    result = [end_with_phone_number[start: end] for start, end in match]
    assert " 555.876.1212" in result
