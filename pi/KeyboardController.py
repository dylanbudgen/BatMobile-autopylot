import pigpio
import pygame
import time
import CarController

ENABLE_SPEED_PIN = 4
SPEED_PIN_1 = 10
SPEED_PIN_2 = 17

ENABLE_DIRECTION_PIN = 5
DIRECTION_PIN_1 = 13
DIRECTION_PIN_2 = 26

CAR_SPEED = 255

pi = pigpio.pi()

pi = pi

if not pi.connected:
    print('Pi not connected. Exiting...')
    exit()

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Control the car')

car = CarController.CarModule(pi, ENABLE_SPEED_PIN, SPEED_PIN_1, SPEED_PIN_2,
                        ENABLE_DIRECTION_PIN, DIRECTION_PIN_1, DIRECTION_PIN_2, CAR_SPEED)

while True:
    try :
        events = pygame.event.get()
        for event in events:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    car.forward()
                elif event.key == pygame.K_DOWN:
                    car.backward()
                elif event.key == pygame.K_RIGHT:
                    car.right_turn()
                elif event.key == pygame.K_LEFT:
                    car.left_turn()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    car.stop()
                elif event.key == pygame.K_DOWN:
                    car.stop()
                elif event.key == pygame.K_RIGHT:
                    car.straight_turn()
                elif event.key == pygame.K_LEFT:
                    car.straight_turn()

    except KeyboardInterrupt:
        break

pi.stop()