from bottle import route, run, response

def generate_mickey_svg():
    # SVG representation of Mickey Mouse with adjusted coordinates
    svg = '''<svg width="300" height="300" xmlns="http://www.w3.org/2000/svg">
        <!-- Face -->
        <circle cx="150" cy="150" r="80" fill="black"/>
        <!-- Left Ear -->
        <circle cx="80" cy="70" r="50" fill="black"/>
        <!-- Right Ear -->
        <circle cx="220" cy="70" r="50" fill="black"/>
    </svg>'''
    return svg

@route('/')
def show_mickey():
    response.content_type = 'image/svg+xml'
    return generate_mickey_svg()

run(host='localhost', port=8080)
