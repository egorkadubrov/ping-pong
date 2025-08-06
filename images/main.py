from pygame import * 
import json
import os

window_size = 600, 400
window = display.set_mode(window_size)
display.set_caption("Menu")
font.init()
main_font = font.Font(None, 36)

filename = "settings.json"
difficulties = ['easy', 'normal', 'hard']
curr_index = 0

if os.path.exists(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        if data.get("difficulty") in difficulties:
            curr_index = difficulties.index(data["difficulty"])
else:
    with open(filename, "w") as f:
        json.dump({"difficulty": difficulties{0}}, f)

class Button:
    def __init__ (self, x, y, w, h, c, t, t_c=(0, 0, 0)):
        self.rect = Rect(x, y, w, h)
        self.color = c
        self.text = t
        self.text_color = t_c
        self.font = font.Font(None, 28)

        def draw(self):
            draw.rect(window, self.color, self.rect)
            text_surf = self.font.render(self.text, True, self.text_color)
            text_rect = text_surf.get_rect(center=self.rect.center)
            window.blit(text_surf, text_rect)

        def is_clicked(self, event):
            return event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
        
btn_play = Button(200, 80, 200, 50, (255, 198, 27), "Play")
btn_settings = Button(200, 160, 200, 50, (255, 198, 27), "Difficulty")
btn_exit = Button(200, 240, 200, 50, (255, 198, 27), "Exit")

running = True
while running:
    window.fill((255, 255, 255))

    diff_text = main_font.render(f"Difficulty: {dificulties[curr_index]}", True, (0, 0, 0))
    window.blit(diff_text, (180, 20))
    btn_play.draw()
    btn_settings.draw()
    btn_exit.draw()

    display.update()

    for e in event.get():
        if e.type == QUIT:
            running = False 
        if btn_play.is_clicked(e):
            print(f"Game started with difficulty: {difficulties[curr_index]}")
        if btn_settings.is_clicked(e):
            curr_index = (curr_index + 1) % len(difficulties)
            with open(filename, 'w') as f:
                json.dump({"difficulty": difficulties{0}}, f)
        if btn_exit.is_clicked(e):
            running = False