def classify_number(s):
    """
    Classifies a number string into one of six categories based on its digits.
    """
    n = len(s)
    if n <= 1:
        # A number with one digit is always a Repdrome.
        return "Repdrome"

    # --- Initialize flags to check the number's properties ---
    is_ascending = True
    is_descending = True
    has_duplicates = False
    
    # --- Check for Repdrome (all digits are the same) ---
    first_digit = s[0]
    is_repdrome = True
    for i in range(1, n):
        if s[i] != first_digit:
            is_repdrome = False
            break
    if is_repdrome:
        return "Repdrome"

    # --- Check for any duplicates in the entire number ---
    # We do this by checking every digit against every other digit that follows it.
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                has_duplicates = True
                break
        if has_duplicates:
            break

    # --- Check for ascending or descending order ---
    # We loop up to the second-to-last digit to compare it with the next one.
    for i in range(n - 1):
        # If a digit is greater than the next one, it can't be ascending.
        if s[i] > s[i+1]:
            is_ascending = False
        # If a digit is less than the next one, it can't be descending.
        if s[i] < s[i+1]:
            is_descending = False

    # --- Final classification based on the flags ---
    if is_ascending:
        if has_duplicates:
            return "Plaindrome"  # Ascending with duplicates
        else:
            return "Metadrome"   # Strictly ascending, no duplicates
    elif is_descending:
        if has_duplicates:
            return "Nialpdrome"  # Descending with duplicates
        else:
            return "Katadrome"   # Strictly descending, no duplicates
    else:
        # If it's neither ascending nor descending, it's a Nondrome.
        return "Nondrome"

# --- Main execution block ---
input_str = input("Enter Input : ")
result = classify_number(input_str)
print(result)
