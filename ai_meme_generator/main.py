import os
from PIL import Image, ImageDraw, ImageFont

# Constants
TEMPLATE_PATH = "templates/temp2.jpg"
OUTPUT_DIR = "output"
FONT_PATH = "latha.ttf"
CAPTION = "Love panradhu easy da... but unaku teriyanum!"

def wrap_text(text, font, max_width, draw):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and draw.textlength(line + words[0], font=font) < max_width:
            line += words.pop(0) + ' '
        lines.append(line.strip())
    return lines

def generate_meme():
    # Load image
    img = Image.open(TEMPLATE_PATH)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Fit font to image height
    font_size = 50
    while font_size > 10:
        font = ImageFont.truetype(FONT_PATH, font_size)
        lines = wrap_text(CAPTION, font, width - 40, draw)
        text_height = sum([draw.textbbox((0, 0), line, font=font)[3] for line in lines])
        if text_height < height // 3:
            break
        font_size -= 2

    # Draw text
    y = height - text_height - 30
    for line in lines:
        text_width = draw.textlength(line, font=font)
        x = (width - text_width) // 2
        draw.text((x, y), line, font=font, fill="white", stroke_width=2, stroke_fill="black")
        y += draw.textbbox((0, 0), line, font=font)[3]

    # Save output
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, "tamil_meme.png")
    img.save(output_path)
    print(f"Meme saved to {output_path}")

if __name__ == "__main__":
    generate_meme()
