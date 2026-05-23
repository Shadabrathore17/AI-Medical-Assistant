import pandas as pd

from rapidfuzz import process
from rapidfuzz import fuzz

# Load CSV
data = pd.read_csv(

    "medicines.csv"
)

# AI Function
def medical_ai(user_input):

    try:

        text = user_input.lower()

        keywords = []

        # Store keywords
        for index, row in data.iterrows():

            keywords.append(

                str(row["Disease"])
            )

            keywords.append(

                str(row["Medicine"])
            )

        # Find Best Match
        best_match = process.extractOne(

            text,

            keywords,

            scorer=fuzz.partial_ratio
        )

        if not best_match:

            return """

No matching disease found.

Please consult a doctor.
"""

        matched_word = best_match[0]

        # Find Data
        for index, row in data.iterrows():

            disease = str(

                row["Disease"]
            ).lower()

            medicine = str(

                row["Medicine"]
            ).lower()

            if matched_word.lower() == disease or matched_word.lower() == medicine:

                return f"""

Possible Disease:
{row['Disease']}

Medicine:
{row['Medicine']}

How To Use:
{row['Usage']}

Symptoms:
{row['Symptoms']}

Precautions:
{row['Precautions']}

Side Effects:
{row['SideEffects']}

Warning:
Educational purposes only.
Please consult a doctor.
"""

        return """

No medical information found.
"""

    except Exception as e:

        return f"Error: {str(e)}"