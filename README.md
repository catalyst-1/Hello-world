# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask and Bootstrap. Features a clean design with smooth animations and a working contact form.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional design with smooth animations
- **Template-based**: Easy to customize content through Flask templates
- **Contact Form**: Working contact form with form validation
- **Social Media Integration**: Links to your social profiles
- **SEO Friendly**: Proper meta tags and semantic HTML structure

## Pages

- **Home**: Hero section with introduction and featured projects preview
- **About**: Detailed about section with skills and achievements
- **Projects**: Showcase of your work with project details
- **Contact**: Contact form and contact information

## Tech Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5 + Custom CSS
- **Icons**: Font Awesome
- **Animations**: CSS animations and JavaScript interactions

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Application

```bash
python app.py
```

The website will be available at `http://localhost:5000`

### 3. Customize Your Content

Edit the `portfolio_data` dictionary in `app.py` to customize:

- Personal information (name, title, contact details)
- About section text and statistics
- Skills and technologies
- Project details
- Social media links

## Project Structure

```
portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html         # Base template
│   ├── home.html         # Home page
│   ├── about.html        # About page
│   ├── projects.html     # Projects page
│   └── contact.html      # Contact page
└── static/              # Static files
    ├── css/
    │   └── style.css     # Custom styles
    ├── js/
    │   └── main.js       # JavaScript functionality
    └── images/           # Image assets
```

## Customization

### Adding Your Profile Image

1. Add your profile image to `static/images/profile.jpg`
2. Update the image path in the templates if needed

### Adding Project Images

1. Add project images to `static/images/`
2. Update the image names in the `portfolio_data` dictionary in `app.py`

### Modifying Styles

- Edit `static/css/style.css` for custom styling
- The design uses Bootstrap 5 for responsive layout
- Custom animations and effects are included

### Contact Form

The contact form currently shows a success message. To make it functional:

1. Set up email sending (using Flask-Mail or similar)
2. Add database storage for messages
3. Update the `contact_post` route in `app.py`

## Deployment

### Local Development

```bash
python app.py
```

### Production Deployment

For production deployment, consider:

1. **Heroku**: Easy deployment with git
2. **DigitalOcean**: VPS hosting
3. **AWS/GCP**: Cloud hosting
4. **Vercel/Netlify**: For static deployment (requires build process)

Remember to:
- Set `debug=False` in production
- Use environment variables for sensitive data
- Set up proper domain and SSL certificate

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you have any questions or need help customizing the portfolio, feel free to reach out!