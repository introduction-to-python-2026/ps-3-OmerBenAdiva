def approximate_pi(n_terms):
     leibniz_series = []

    # מוסיפים לרשימה את כל האיברים לפי הנוסחה
    for n in range(n_terms):
        term = ((-1) ** n) / (2 * n + 1)
        leibniz_series.append(term)

    # מחשבים את סכום כל האיברים
    total = sum(leibniz_series)

    # נכפיל ב-4 כדי לקבל קירוב לערך של π
    pi_approx = 4 * total

    # נחזיר את התוצאה
    return pi_approx

