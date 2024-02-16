from math import radians, sin, cos, tan
angulo = float(input("Dígite um ângulo: "))
radius = radians(angulo)
print(f"O seno do ângulo {angulo} é {sin(radius):.2f}")
print(f"O cosseno do ângulo {angulo} é {cos(radius):.2f}")
print(f"A tangente do ângulo {angulo} é {tan(radius):.2f}")
