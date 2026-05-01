
import re



def normalize_phone(phone_number):

    cleaned = re.sub(r'[^0-9+]', '',phone_number)

    if cleaned.startswith("+"):
        return cleaned

    if cleaned.startswith('380'):
        return "+" + cleaned

    return "+38" + cleaned


