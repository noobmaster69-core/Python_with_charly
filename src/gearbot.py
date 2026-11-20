left_wheel = Motor(Port.A) # Llanta izquierda
 right_wheel = Motor(Port.B) # Llanta derecha

def move(left_vel, right_vel, time_ms):
 """
 Esta función realiza el movimiento
 de mi llanta izquierda y derecha
 del robot.
 """
 left_wheel.run_time(left_vel, time_ms, wait=False)
 right_wheel.run_time(right_vel, time_ms, wait=True)

def move_forward(speed_robot, time_ms):
 """
 Esta función mueve el robot
 hacía adelante una velocidad - speed_robot
 a un tiempo time_ms
 """
 print("AVANZANDO")
 move(speed_robot, speed_robot, time_ms)

def move_backward(speed_robot, time_ms):
 """
 Esta función mueve el robot
 hacía atrás una velocidad - speed_robot
 a un tiempo time_ms
 """
 print("RETROCEDIENDO")
 move(-speed_robot, -speed_robot, time_ms)

def turn_right(speed_robot, time_ms):
 """
 Esta función hace que el robot
 gire sobre su propio eje a una velocidad - speed_robot
 en un tiempo time_ms, en el sentido de 
 las manecillas del reloj (sentido horario)
 """
 print("Girando a la derecha")
 move(speed_robot, -speed_robot, time_ms)

def turn_left(speed_robot, time_ms):
 """
 Esta función hace que el robot
 gire sobre su propio eje a una velocidad - speed_robot
 en un tiempo time_ms, en el sentido en contra de 
 las manecillas del reloj (sentido anti-horario)
 """
 print("Girando a la izquierda")
 move(-speed_robot, speed_robot, time_ms)

def stop_robot():
 """
 Esta función detiene a mi robot.
 """
 print("Robot detenido")
 left_wheel.stop()
 right_wheel.stop()
