def explain_error(error_text):
    return f"""
    You are a debugging expert.

    Explain this error:
    {error_text}

    Provide:
    - Meaning
    - Cause
    - Fix
    - Command to solve
    """