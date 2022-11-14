def check_term(weeks : int) -> str:
    if(weeks < 37):
        return "Pre-Term"
    elif(weeks > 42):
        return "Post-Term"
    else:
        return "Term"