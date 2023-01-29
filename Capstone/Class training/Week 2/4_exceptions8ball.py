import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://magic-eight-ball.azurewebsites.net/magic/JSON/{question}'

try:
    response = requests.get(magic_8_ball_url).json()
    answer = response['magic']['answer']
    print(f'The magic 8 ball says.... {answer}')
except Exception as e:
    print(e)
    print('Not working out, bud')