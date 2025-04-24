from flask import Flask, render_template, request

app = Flask(__name__)

# Room descriptions
ROOM_DESCRIPTIONS = {
    'M302': 'The First Years Classroom (M302) is a spacious learning environment equipped with modern teaching facilities. This classroom serves as the primary learning space for first-year AI&DS students, featuring comfortable seating arrangements and advanced audio-visual systems to enhance the learning experience.',
    'IT109': 'The Second Years Classroom (IT109) is designed to support the specialized curriculum of second-year AI&DS students. With its ergonomic design and state-of-the-art teaching aids, this classroom provides an optimal environment for both theoretical learning and practical demonstrations.',
    'IT110': 'The Third Years Classroom (IT110) offers an advanced learning environment tailored to the complex subjects studied by third-year AI&DS students. Equipped with specialized software and hardware resources, this classroom facilitates both individual and group learning activities.',
    'IT315': 'The Final Years Classroom (IT315) is a premium learning space designed for the advanced coursework of final-year AI&DS students. This classroom features cutting-edge technology and flexible seating arrangements to support project-based learning and collaborative research activities.',
    'M114': 'Laboratory M114 is a specialized facility equipped with high-performance computing resources for AI&DS students. This lab provides access to advanced software tools and hardware necessary for data analysis, machine learning experiments, and AI model development.',
    'M139': 'Laboratory M139 serves as a dedicated space for hands-on experimentation in AI&DS. Equipped with specialized hardware and software, this lab supports students in developing and testing AI algorithms, working with large datasets, and implementing machine learning models.'
}

@app.route('/')
def index():
    return render_template('index.html', room_descriptions=ROOM_DESCRIPTIONS)

@app.route('/vr-view')
def vr_view():
    room = request.args.get('room', '')
    res = request.args.get('res', 'low')
    description = ROOM_DESCRIPTIONS.get(room, 'No description available for this room.')
    return render_template('vr-view.html', room=room, res=res, description=description)

if __name__ == '__main__':
    app.run(debug=True)