from PIL import Image, ImageDraw, ImageFont

# Create image
width, height = 1024, 576
background_color = (173, 255, 47)  # Lime green
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# Try to load a good font, fallback to default
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
    label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
except:
    title_font = ImageFont.load_default()
    label_font = ImageFont.load_default()

# Draw rounded rectangle (simulated with larger shape)
box_left, box_top = 150, 150
box_right, box_bottom = 850, 420
box_color = (20, 50, 20)  # Dark green

# Draw filled box
draw.rectangle([box_left, box_top, box_right, box_bottom], fill=box_color, outline=box_color, width=3)

# Draw checkmark
check_x, check_y = 220, 220
check_size = 120
check_color = (173, 255, 47)  # Lime green
draw.ellipse([check_x - 20, check_y - 20, check_x + check_size, check_y + check_size], outline=check_color, width=8)
# Draw checkmark
draw.line([(check_x + 30, check_y + 50), (check_x + 60, check_y + 90)], fill=check_color, width=12)
draw.line([(check_x + 60, check_y + 90), (check_x + 110, check_y + 30)], fill=check_color, width=12)

# Draw text
text = "Deposit Found"
text_color = (255, 255, 255)  # White
# Get text size and center it
draw.text((400, 240), text, font=title_font, fill=text_color)

# Add @room label at top left
draw.text((30, 20), "@room", font=label_font, fill=(0, 0, 0))

image.save('/home/runner/workspace/deposit_found_image.jpg', 'JPEG', quality=95)
print("✅ Deposit Found image created")
