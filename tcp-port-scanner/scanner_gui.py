# Interface gráfica
import pygame
import threading
from scanner.tcp_scanner import scan_ports

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
RED = (200, 0, 0)
DARK_RED = (150, 0, 0)
GRAY = (220, 220, 220)

WIDTH, HEIGHT = 700, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TCP port scanner")

font = pygame.font.SysFont(None, 28)

host_input = ''
start_port_input = ''
end_port_input = ''
scanning = False
results = []
input_active = [False, False, False]

scan_pressed = False
close_pressed = False

def draw_text(text, x, y, color=BLACK):
    txt_surface = font.render(text, True, color)
    screen.blit(txt_surface, (x, y))

def scan_ports_thread(host, start, end):
    global scanning, results
    ports_found = scan_ports(host, start, end)

    if not ports_found:
        results = ["No open ports found."]
    else:
        results = ports_found

    scanning = False

def run_gui():
    global host_input, start_port_input, end_port_input, scanning, results, input_active
    global scan_pressed, close_pressed

    clock = pygame.time.Clock()
    running = True

    input_rects = [
        pygame.Rect(180, 25, 300, 40),
        pygame.Rect(180, 85, 300, 40),
        pygame.Rect(180, 145, 300, 40)
    ]

    scan_button = pygame.Rect(WIDTH//2 - 160, HEIGHT - 170, 120, 50)
    close_button = pygame.Rect(WIDTH//2 + 40, HEIGHT - 170, 120, 50)

    blink = True
    blink_timer = 0

    while running:
        screen.fill(GRAY)

        draw_text("Host/IP:", 20, 30)
        draw_text("Home port:", 20, 90)
        draw_text("Final port:", 20, 150)

        mouse_pos = pygame.mouse.get_pos()
        cursor_set = False

        inputs = [host_input, start_port_input, end_port_input]
        for i, rect in enumerate(input_rects):
            pygame.draw.rect(screen, WHITE, rect, border_radius=8)
            pygame.draw.rect(screen, BLACK, rect, 2, border_radius=8)

            draw_text(inputs[i], rect.x + 10, rect.y + 8)

            if input_active[i] and blink:
                cursor_x = rect.x + 10 + font.size(inputs[i])[0] + 2
                pygame.draw.line(screen, BLACK, (cursor_x, rect.y + 8), (cursor_x, rect.y + 32), 2)

            if rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
                cursor_set = True

        draw_text("Results:", 20, 210)
        y_offset = 250

        if scanning:
            draw_text("Port scan in progress...", 20, y_offset)
        else:
            for res in results[-8:]:
                draw_text(res, 20, y_offset)
                y_offset += 30

        pygame.draw.rect(screen, DARK_GREEN if scan_pressed else GREEN, scan_button, border_radius=8)
        pygame.draw.rect(screen, DARK_RED if close_pressed else RED, close_button, border_radius=8)

        draw_text("Scan", scan_button.centerx - 25, scan_button.centery - 10, WHITE)
        draw_text("Close", close_button.centerx - 35, close_button.centery - 10, WHITE)

        if not cursor_set:
            if scan_button.collidepoint(mouse_pos) or close_button.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                cursor_set = True

        if not cursor_set:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if scan_button.collidepoint(x, y):
                    scan_pressed = True
                if close_button.collidepoint(x, y):
                    close_pressed = True

                for i, rect in enumerate(input_rects):
                    if rect.collidepoint(x, y):
                        input_active = [False, False, False]
                        input_active[i] = True
                        break
                else:
                    input_active = [False, False, False]

            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if scan_button.collidepoint(x, y) and scan_pressed:
                    if not scanning and host_input and start_port_input.isdigit() and end_port_input.isdigit():
                        results = []
                        scanning = True
                        thread = threading.Thread(
                            target=scan_ports_thread,
                            args=(host_input, int(start_port_input), int(end_port_input))
                        )
                        thread.start()
                if close_button.collidepoint(x, y) and close_pressed:
                    running = False

                scan_pressed = False
                close_pressed = False

            elif event.type == pygame.KEYDOWN:
                if input_active[0]:
                    if event.key == pygame.K_BACKSPACE:
                        host_input = host_input[:-1]
                    else:
                        host_input += event.unicode
                elif input_active[1]:
                    if event.key == pygame.K_BACKSPACE:
                        start_port_input = start_port_input[:-1]
                    elif event.unicode.isdigit():
                        start_port_input += event.unicode
                elif input_active[2]:
                    if event.key == pygame.K_BACKSPACE:
                        end_port_input = end_port_input[:-1]
                    elif event.unicode.isdigit():
                        end_port_input += event.unicode

        blink_timer += clock.get_time()
        if blink_timer >= 500:
            blink = not blink
            blink_timer = 0

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()