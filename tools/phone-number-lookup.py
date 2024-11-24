import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from pystyle import Colors, Colorate
import os
from datetime import datetime

def fade(text: str) -> str:
    return Colorate.Horizontal(Colors.purple_to_blue, text, 1)

def lookup(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)

        is_valid = phonenumbers.is_valid_number(parsed_number)

        formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
        country_code = f"+{parsed_number.country_code}"
        country = geocoder.country_name_for_number(parsed_number, "en")
        region = geocoder.description_for_number(parsed_number, "fr")
        timezones = timezone.time_zones_for_number(parsed_number)
        operator = carrier.name_for_number(parsed_number, "en")
        number_type = phonenumbers.number_type(parsed_number)

        number_type_map = {
            phonenumbers.PhoneNumberType.MOBILE: "Mobile",
            phonenumbers.PhoneNumberType.FIXED_LINE: "Fixed Line",
            phonenumbers.PhoneNumberType.FIXED_LINE_OR_MOBILE: "Fixed Line or Mobile",
            phonenumbers.PhoneNumberType.TOLL_FREE: "Toll-Free",
            phonenumbers.PhoneNumberType.PREMIUM_RATE: "Premium Rate",
            phonenumbers.PhoneNumberType.VOIP: "VoIP",
            phonenumbers.PhoneNumberType.UNKNOWN: "Unknown",
        }
        number_type_str = number_type_map.get(number_type, "Unknown")

        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Formatted    : {formatted_number}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Status       : {'Valid' if is_valid else 'Invalid'}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Country Code : {country_code}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Country      : {country}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Region       : {region}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Timezone     : {', '.join(timezones)}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Operator     : {operator}")
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Type Number  : {number_type_str}")

    except phonenumbers.NumberParseException as e:
        time = datetime.now().strftime("%H:%M:%S")
        print(f"{fade("[")}{time}{fade("]")} Error parsing phone number: {e}")

if __name__ == "__main__":
    time = datetime.now().strftime("%H:%M:%S")
    phone_number = input(f"\n{fade("[")}{time}{fade("]")} > Enter Phone Number: ")

    lookup(phone_number)

    time = datetime.now().strftime("%H:%M:%S")
    input(f"{fade("[")}{time}{fade("]")} Press any key to go back.")
    os.system("python master.py")
