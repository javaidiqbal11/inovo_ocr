import gradio as gr
import base64
import requests
import json
from io import BytesIO
from PIL import Image
import fitz  # PyMuPDF

# Define the extract_text function
def extract_text_from_image(image, temperature=0.2):
    api_key = "OPENAI_API_KEY"
    def encode_image(image):
        buffered = BytesIO()
        image.save(buffered, format="PNG")  # Save image to buffer as PNG
        return base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    base64_image = encode_image(image)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """Please convert the following receipt information for english and french language (place comma where there is comma and fullstop where is fullstop) into a structured JSON format matching this class definition:
                        The structure should include the following classes and fields:

                        - `Subcategory`: with a `value` field.
                        - `Category`: with `value` and `subcategory` fields, where `subcategory` is optional and of type `Subcategory`.
                        - `DocumentType`: with a `value` field.
                        - `ReceiptNumber`: with a `value` field.
                        - `Date`: with a `value` field.
                        - `Time`: with a `value` field.
                        - `Locale`: with `country`, `language`, `currency`, and `value` fields.
                        - `SupplierCompanyRegistration`: with `type` and `value` fields.
                        - `Supplier`: with `name`, `address`, `phone_number`, and `company_registrations` fields, where `company_registrations` is a list of `SupplierCompanyRegistration`.
                        - `Tax`: with `code`, `rate`, `base`, and `value` fields.
                        - `TotalTax`: with a `value` field.
                        - `TipGratuity`: with a `value` field.
                        - `TotalAmount`: with a `value` field.
                        - `TotalNet`: with a `value` field.
                        - `LineItem`: with `description`, `quantity`, `unit_price`, and `total_amount` fields.
                        - `Receipt`: with fields for `category` (of type `Category`), `document_type`, `receipt_number`, `date`, `time`, `locale`, `orientation`, `supplier` (of type `Supplier`), `taxes` (a list of `Tax`), `total_tax`, `tip_gratuity`, `total_amount`, `total_net`, and `line_items` (a list of `LineItem`).

                        Only include the information that can be directly extracted from the receipt image. Do not add any extra information or fields not present in the receipt, and omit any information that is not provided. The output should be returned in JSON format."
                        receipt image, without adding any unnecessary or unavailable details.\n
                        always return in json format and don't duplicate items."""
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                            }
                    }
                ]
            }
        ],
        "max_tokens": 4000,
        "temperature": temperature
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.status_code, "message": response.text}
    

def clean_json_response(response_content):
    # Remove the ```json from the beginning and ``` from the end
    if response_content.startswith("```json"):
        response_content = response_content[7:]
    if response_content.endswith("```"):
        response_content = response_content[:-3]
    
    # Parse the JSON string to a Python dictionary
    return json.loads(response_content)


# Function to convert the first page of PDF to an image
def convert_pdf_to_image(pdf_filepath):
    doc = fitz.open(pdf_filepath)  # Open the PDF file by path
    page = doc.load_page(0)  # Load the first page
    pix = page.get_pixmap()  # Render page to an image
    
    # Convert Pixmap to PIL Image
    image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    return image


# Gradio interface function
def gradio_interface(pdf_file):
    if pdf_file is None:
        return None, "Error: No PDF file uploaded. Please upload a PDF file before clicking submit."
    
    # Convert the uploaded PDF to an image
    image = convert_pdf_to_image(pdf_file.name)
    
    # Extract text from the image
    result = extract_text_from_image(image)
    
    if result is not None and 'choices' in result:
        raw_json_content = result['choices'][0]['message']['content']
        #response = clean_json_response(raw_json_content)
    else:
        raw_json_content = "Error: No choices found in the response."

    return image, raw_json_content



# Define Gradio inputs and outputs
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):  # Fix the size of the left column
            pdf_input = gr.File(type="filepath", label="Upload PDF")
            extracted_image = gr.Image(label="Extracted Image", interactive=False)
        with gr.Column(scale=1):  # Keep the size of the right column for the JSON response
            extracted_json = gr.Textbox(label="Extracted JSON")

    submit_button = gr.Button("Submit")
    
    submit_button.click(gradio_interface, inputs=pdf_input, outputs=[extracted_image, extracted_json])

demo.launch(share=True)



# Please convert the following receipt information for english and french language (place comma where there is comma and fullstop where is fullstop) into a structured JSON format matching this class definition:
#                         The structure should include the following classes and fields:

#                         - `Subcategory`: with a `value` field.
#                         - `Category`: with `value` and `subcategory` fields, where `subcategory` is optional and of type `Subcategory`.
#                         - `DocumentType`: with a `value` field.
#                         - `ReceiptNumber`: with a `value` field.
#                         - `Date`: with a `value` field.
#                         - `Time`: with a `value` field.
#                         - `Locale`: with `country`, `language`, `currency`, and `value` fields.
#                         - `SupplierCompanyRegistration`: with `type` and `value` fields.
#                         - `Supplier`: with `name`, `address`, `phone_number`, and `company_registrations` fields, where `company_registrations` is a list of `SupplierCompanyRegistration`.
#                         - `Tax`: with `code`, `rate`, `base`, and `value` fields.
#                         - `TotalTax`: with a `value` field.
#                         - `TipGratuity`: with a `value` field.
#                         - `TotalAmount`: with a `value` field.
#                         - `TotalNet`: with a `value` field.
#                         - `LineItem`: with `description`, `quantity`, `unit_price`, and `total_amount` fields.
#                         - `Receipt`: with fields for `category` (of type `Category`), `document_type`, `receipt_number`, `date`, `time`, `locale`, `orientation`, `supplier` (of type `Supplier`), `taxes` (a list of `Tax`), `total_tax`, `tip_gratuity`, `total_amount`, `total_net`, and `line_items` (a list of `LineItem`).

#                         Only include the information that can be directly extracted from the receipt image. Do not add any extra information or fields not present in the receipt, and omit any information that is not provided. The output should be returned in JSON format."
#                         receipt image, without adding any unnecessary or unavailable details.
