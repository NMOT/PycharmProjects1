## importação do  turtle para se poder desenhar
import turtle


## função a ser utilizada
def quadrado(lado, posicao, angulo):
    ## preparação
    turtle.up()
    turtle.goto(posicao)
    turtle.setheading(angulo)
    turtle.down()
    turtle.shape('turtle')

    ## desenhar o quadrado
    for conta in range(4):
        turtle.forward(lado)
        turtle.right(90)

    turtle.hideturtle()
    turtle.exitonclick()


if __name__ == '__main__':
    quadrado(100,(300,300),0)

