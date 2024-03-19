from PIL import Image, ImageDraw, ImageFont

# Open the ticket template


template_path = "boleto.png"
template = Image.open(template_path)
draw = ImageDraw.Draw(template)

# Define font and starting number
font = ImageFont.truetype("Montserrat-ExtraBold.ttf", size=100)
starting_number = 95

# Number of tickets you want to generate
num_tickets = 10

# Define the position where you want to place the number
x_position = 90
y_position = 220

# Loop through each ticket
for i in range(num_tickets):
    # Draw the number on the ticket
    draw.text((x_position, y_position), str(starting_number + i), fill="white", font=font)
    
    # Save the ticket with the number
    ticket_path = f"ticket_{starting_number + i}.png"
    template.save(ticket_path)
    
    # Open the template again for the next iteration
    template = Image.open(template_path)
    draw = ImageDraw.Draw(template)

print(f"{num_tickets} tickets generated.")