from flask import Flask, render_template, request

app = Flask(__name__)

# Room descriptions
ROOM_DESCRIPTIONS = {
    'Library1': 'The main reading area of the CIT College Library offers a spacious and well-lit environment for students to study and research. With comfortable seating arrangements and a peaceful atmosphere, it provides an ideal setting for academic focus and intellectual exploration.',
    'Library2': 'This section of the CIT College Library houses an extensive collection of academic resources, including textbooks, reference materials, and journals. The well-organized shelving system makes it easy for students to locate materials related to their field of study.',
    'Library3': 'The quiet study zone in the CIT College Library is designed for individual study and deep concentration. This area maintains a strict noise policy to ensure students can work without distractions, making it perfect for exam preparation and focused research.',
    'E Learning Center': 'The E-Learning Center within the CIT College Library is equipped with modern computers and digital resources. This technology-enabled space allows students to access online databases, e-journals, and digital learning materials to supplement their traditional learning.',
    'Librarian Desk': 'The Librarian\'s Desk serves as the central point for library assistance. Here, students can seek help with locating resources, checking out books, and getting guidance on research methodologies from knowledgeable library staff.',
    'Librarian Desks': 'The administration area features multiple librarian workstations where the library staff manages the catalog system, assists with inter-library loans, and coordinates library services. This area is essential for the efficient operation of the library\'s resources and services.'
}

@app.route('/')
def index():
    return render_template('index.html', room_descriptions=ROOM_DESCRIPTIONS)

@app.route('/vr-view')
def vr_view():
    room = request.args.get('room', '')
    res = request.args.get('res', 'low')
    description = ROOM_DESCRIPTIONS.get(room, 'No description available for this area.')
    return render_template('vr-view.html', room=room, res=res, description=description)

if __name__ == '__main__':
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))