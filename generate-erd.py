from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1000, 700
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

try:
    font = ImageFont.truetype("arial.ttf", 14)
    title_font = ImageFont.truetype("arial.ttf", 18)
    bold_font = ImageFont.truetype("arialbd.ttf", 14)
except:
    font = ImageFont.load_default()
    title_font = font
    bold_font = font

def draw_box(x, y, w, h, title, fields):
    draw.rectangle([x, y, x + w, y + h], outline="black", width=2)
    h_title = 28
    draw.rectangle([x, y, x + w, y + h_title], fill="#4472C4", outline="black", width=2)
    draw.text((x + 8, y + 6), title, fill="white", font=bold_font)
    cy = y + h_title + 4
    for f in fields:
        draw.text((x + 8, cy), f, fill="black", font=font)
        cy += 18

def draw_crow_foot(x1, y1, x2, y2, many=True):
    draw.line([(x1, y1), (x2, y2)], fill="black", width=2)
    if many:
        size = 8
        angle = math.radians(30)
        for sign in (-1, 1):
            dx = sign * size * math.cos(angle)
            dy = size * math.sin(angle)
            draw.line([(x2, y2), (x2 + dx, y2 + dy)], fill="black", width=2)
        draw.line([(x2 - size * math.cos(angle), y2), (x2 + size * math.cos(angle), y2)], fill="black", width=2)
    else:
        draw.line([(x2, y2 - 6), (x2, y2 + 6)], fill="black", width=2)
        draw.line([(x2 - 6, y2), (x2 + 6, y2)], fill="black", width=2)

draw.text((W // 2 - 80, 20), "Chama ERD", fill="black", font=title_font)

chamas_box = (100, 80, 260, 220)
members_box = (420, 80, 580, 220)
cycles_box = (100, 340, 260, 480)
contributions_box = (420, 340, 580, 480)
fines_box = (740, 340, 900, 480)

draw_box(*chamas_box, "chamas", ["id UUID PK", "name TEXT", "contribution_amount_cents INT", "cycle_length_days INT", "created_at TIMESTAMPTZ"])
draw_box(*members_box, "members", ["id UUID PK", "chama_id UUID FK", "name TEXT", "phone TEXT", "position INT", "created_at TIMESTAMPTZ"])
draw_box(*cycles_box, "cycles", ["id UUID PK", "chama_id UUID FK", "number INT", "recipient_id UUID FK", "starts_at DATE", "ends_at DATE", "status TEXT", "created_at TIMESTAMPTZ"])
draw_box(*contributions_box, "contributions", ["id UUID PK", "cycle_id UUID FK", "member_id UUID FK", "amount_cents INT", "mpesa_reference TEXT", "status TEXT", "paid_at TIMESTAMPTZ"])
draw_box(*fines_box, "fines", ["id UUID PK", "cycle_id UUID FK", "member_id UUID FK", "amount_cents INT", "reason TEXT", "created_at TIMESTAMPTZ"])

draw_crow_foot(chamas_box[2], chamas_box[1] + 80, members_box[0], members_box[1] + 80)
draw.text((members_box[0] + 20, members_box[1] + 70), "chamas --< members", fill="red", font=font)

draw_crow_foot(chamas_box[2], chamas_box[1] + 120, cycles_box[0], cycles_box[1] + 60)
draw.text((cycles_box[0] + 20, cycles_box[1] + 50), "chamas --< cycles", fill="red", font=font)

draw_crow_foot(cycles_box[2], cycles_box[1] + 80, contributions_box[0], contributions_box[1] + 80)
draw.text((contributions_box[0] + 20, contributions_box[1] + 70), "cycles --< contributions", fill="red", font=font)

draw_crow_foot(members_box[2], members_box[1] + 80, contributions_box[0], contributions_box[1] + 120)
draw.text((contributions_box[0] + 20, contributions_box[1] + 110), "members --< contributions", fill="red", font=font)

draw_crow_foot(cycles_box[2], cycles_box[1] + 120, fines_box[0], fines_box[1] + 80)
draw.text((fines_box[0] + 20, fines_box[1] + 70), "cycles --< fines", fill="red", font=font)

img.save(r"C:\Users\Admin\OneDrive\Desktop\Week22\day 1\docs\chama-erd.png")
print("Saved docs/chama-erd.png")
