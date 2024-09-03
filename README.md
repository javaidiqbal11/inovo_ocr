# Receipt Text Extractor

This is a Gradio-powered web application that extracts structured data from receipt images or pdf using an API (such as OpenAI's GPT-4). The extracted information is returned in a structured JSON format that follows the provided class definitions for `Tax`, `LineItem`, `Supplier`, and `Receipt`.

## Features
- Upload a pdf soft copy or. 
- Upload a receipt image (PNG format).
- The application sends the image to the API for processing.
- The API extracts receipt details, such as total price, supplier, and line items, and structures them into a JSON format.
- The structured JSON is displayed as the output.

## Requirements

- Python 3.7 or higher
- `gradio`
- `requests`
- An API key for the GPT model (e.g., OpenAI's API)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/username/repository-name.git
```

2. Navigate to the project directory:

```bash
cd repository-name
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Replace the placeholder API key in the `extract_text_from_image` function with your actual API key.

2. Run the application:

```bash
python app.py
```

3. Access the Gradio interface via the provided link in the terminal.

4. Upload a receipt image and receive structured data in JSON format.

## Example Class Definitions

The structured JSON follows the format of the following Python class definitions:

```python
class Tax(BaseModel):
    rate: float
    value: float
    currency: str

class LineItem(BaseModel): 
    description: str
    quantity: int
    unit_price: float
    total_price: float
    currency: str

class Supplier(BaseModel):
    name: str
    address: str
    phone_number: str

class Receipt(BaseModel):
    name: str
    type: str
    locale: str
    total_incl: dict
    total_excl: dict
    tax: list[Tax]
    supplier: Supplier
    date: str
    time: str
    line_items: list[LineItem]
```


```

This `README.md` should give users a clear overview of your project and instructions for setting it up and running it.
