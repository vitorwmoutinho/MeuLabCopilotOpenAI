import openai
from PIL import Image
import pytesseract
import os

# Configuração da chave da API OpenAI
openai.api_key = "SUA_API_KEY"

def process_image(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

def save_text(output_path, text):
    with open(output_path, 'w') as f:
        f.write(text)

input_dir = "inputs"
output_dir = "output"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for image_file in os.listdir(input_dir):
    input_path = os.path.join(input_dir, image_file)
    output_path = os.path.join(output_dir, f"{os.path.splitext(image_file)[0]}.txt")

    recognized_text = process_image(input_path)
    save_text(output_path, recognized_text)
    print(f"Processado: {image_file}")
