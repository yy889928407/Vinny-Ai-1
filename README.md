# GreenHarvest Spaces Africa

Empowering youth. Restoring ecosystems. Securing food systems.

## Project Structure

```
.
├── front-ai/              # Frontend application
│   ├── index.html         # Static homepage
│   └── style.css          # Frontend styling
│
├── back-ai/               # Backend application
│   ├── app.py             # Flask server
│   ├── templates/         # Jinja2 templates
│   │   └── index.html
│   └── static/            # Static assets
│       └── style.css
│
├── web/                   # GitHub Pages static site
│   ├── index.html
│   └── style.css
│
└── README.md              # This file
```

## Frontend (front-ai/)

Static frontend files optimized for GitHub Pages.
- **index.html** - Homepage markup
- **style.css** - Styling

## Backend (back-ai/)

Flask-based backend application.
- **app.py** - Main Flask server
- **templates/** - Dynamic HTML templates with Jinja2
- **static/** - Static assets served by Flask

## GitHub Pages (web/)

Static website hosted on GitHub Pages.
- Access at: `https://yy889928407.github.io/vinny-ai1/web/`

## Running the Project

### Frontend (Static)
Open `front-ai/index.html` in a browser or serve with:
```bash
python -m http.server 8000
```

### Backend (Flask)
From the `back-ai/` directory:
```bash
python app.py
```

## License

© 2026 GreenHarvest Spaces Africa 💚
