# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name, greeting='Hello, <name>!'):
    template = greeting.replace('<name>', name)
    return template


print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))


boddies = {
    'sun': 274,
    'jupiter': 24.9,
    'neptune': 11.6,
    'saturn': 10.4,
    'earth': 9.8,
    'uranus': 8.9,
    'venus': 8.9,
    'mars': 3.7,
    'mercury': 3.7,
    'moon': 1.6,
    'pluto': 0.6
}


def force(mass, body='earth'):
    force = mass * boddies[body]
    return force


def pull(m1, m2, d):
    gravity = 6.674*10**-11
    force = gravity*((m1*m2)/d**2)
    return force
