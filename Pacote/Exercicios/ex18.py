import math
ang = float(input('Digite o ângulo que você deseja: '))
print('O angulo de {} tem o seno de {:.2f} \n'.format(ang, math.sin(math.radians(ang))),
      'O ângulo de {} tem o cosceno de {:.2f} \n'.format(ang, math.cos(math.radians(ang))),
      'O ângulo de {} tem a tangente de {:.2f} \n'.format(ang, math.tan(math.radians(ang))))
