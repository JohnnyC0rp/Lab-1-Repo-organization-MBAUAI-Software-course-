# gpt.py
import json
from typing import Any, Dict

from openai import OpenAI

CATEGORIES = [
    "Meals",
    "Transport",
    "Lodging",
    "Office Supplies",
    "Entertainment",
    "Other",
]

def extract_receipt_info(image_b64):
    """Extract receipt fields from a base64-encoded image.

    Args:
        image_b64: Base64-encoded receipt image data.

    Returns:
        A dictionary with keys: date, amount, vendor, category.
    """
    client = OpenAI()
    prompt = f"""
You are an information extraction system.
Extract ONLY the following fields from the receipt image:

date: the receipt date as a string
amount: the total amount paid as it appears on the receipt
vendor: the merchant or vendor name
category: one of [{", ".join(CATEGORIES)}]

Return EXACTLY one JSON object with these four keys and NOTHING ELSE.
Do not include explanations, comments, or formatting.
Do not wrap the JSON in markdown.
If a field cannot be determined, use null.

The output must be valid JSON.
"""
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        seed=43,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_b64}"
                        }
                    }
                ]
            }
        ]
    )
    return json.loads(response.choices[0].message.content)


def normalize_amount(receipt_info: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize the amount field in a receipt info dictionary.

    This removes a leading "$" if present, strips separators, converts the
    value to float, and replaces the original entry when conversion succeeds.

    Args:
        receipt_info: Receipt data with an "amount" field.

    Returns:
        The updated receipt_info dictionary.
    """
    if not isinstance(receipt_info, dict):
        return receipt_info

    amount = receipt_info.get("amount")
    if amount is None:
        return receipt_info

    if isinstance(amount, (int, float)):
        receipt_info["amount"] = float(amount)
        return receipt_info

    if isinstance(amount, str):
        cleaned = amount.replace("$", "").replace(",", "").strip()
        try:
            receipt_info["amount"] = float(cleaned)
        except ValueError:
            pass

    return receipt_info
