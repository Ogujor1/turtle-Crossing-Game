import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
screen.listen()
screen.onkey(player.move_up, "p")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # detect player collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.new_game()
            if score.response.lower() == 'yes':
                score.new_score()
                player.start_afresh()
            else:
                score.end_game()
                game_is_on = False

    # Detect a successful crossing
    if player.successful_cross():
        player.start_afresh()
        cars.increase_spead()
        score.increase_score()

screen.exitonclick()