from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Sample data for the portfolio
portfolio_data = {
    'name': 'Your Name',
    'title': 'Full Stack Developer',
    'description': 'I create beautiful and functional web experiences that bring ideas to life.',
    'email': 'your.email@example.com',
    'phone': '+1 (555) 123-4567',
    'location': 'Your City, Country',
    'about': {
        'text': '''I'm a passionate developer with 3+ years of experience in creating digital solutions 
                   that make a difference. I love turning complex problems into simple, beautiful designs.
                   
                   When I'm not coding, you can find me exploring new technologies, contributing to 
                   open-source projects, or enjoying a good cup of coffee while reading tech blogs.''',
        'stats': [
            {'number': '50+', 'label': 'Projects Completed'},
            {'number': '25+', 'label': 'Happy Clients'},
            {'number': '3+', 'label': 'Years Experience'}
        ]
    },
    'skills': [
        {
            'category': 'Frontend',
            'items': ['HTML5', 'CSS3', 'JavaScript', 'React', 'Vue.js', 'TypeScript']
        },
        {
            'category': 'Backend',
            'items': ['Python', 'Flask', 'Django', 'Node.js', 'Express', 'FastAPI']
        },
        {
            'category': 'Database & Tools',
            'items': ['PostgreSQL', 'MongoDB', 'Git', 'Docker', 'AWS', 'Redis']
        }
    ],
    'projects': [
        {
            'title': 'E-commerce Platform',
            'description': 'A full-stack e-commerce solution with user authentication, payment integration, and admin dashboard.',
            'technologies': ['Flask', 'PostgreSQL', 'Bootstrap'],
            'github': '#',
            'demo': '#',
            'image': 'project1.jpg'
        },
        {
            'title': 'Task Management App',
            'description': 'A collaborative task management application with real-time updates and team collaboration features.',
            'technologies': ['Django', 'WebSockets', 'React'],
            'github': '#',
            'demo': '#',
            'image': 'project2.jpg'
        },
        {
            'title': 'Weather Dashboard',
            'description': 'A responsive weather application with location-based forecasts and interactive charts.',
            'technologies': ['Python', 'Flask', 'Chart.js'],
            'github': '#',
            'demo': '#',
            'image': 'project3.jpg'
        }
    ],
    'social': {
        'github': 'https://github.com/yourusername',
        'linkedin': 'https://linkedin.com/in/yourusername',
        'twitter': 'https://twitter.com/yourusername',
        'email': 'mailto:your.email@example.com'
    }
}

@app.route('/')
def home():
    return render_template('home.html', data=portfolio_data)

@app.route('/about')
def about():
    return render_template('about.html', data=portfolio_data)

@app.route('/projects')
def projects():
    return render_template('projects.html', data=portfolio_data)

@app.route('/contact')
def contact():
    return render_template('contact.html', data=portfolio_data)

@app.route('/contact', methods=['POST'])
def contact_post():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')
    
    # Here you would typically send an email or save to database
    # For now, we'll just flash a success message
    flash(f'Thank you {name}! Your message has been sent successfully.', 'success')
    return redirect(url_for('contact'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)