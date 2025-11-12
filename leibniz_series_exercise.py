
def approximate_pi(n_terms):
    total = 0  # נשתמש במשתנה זה כדי לצבור את סכום הסדרה
    for n in range(n_terms):
        term = (-1) ** n / (2 * n + 1)  # הנוסחה של לייבניץ
        total += term
    pi_approx = 4 * total  # נכפיל ב-4 כדי לקבל את קירוב π
    return pi_approx


