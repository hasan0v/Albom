# Album Project

## Overview

The Album project is a web application built using Django, designed to manage and display a collection of photos. Users can view a gallery of photos, see individual photos in detail, and add new photos with descriptions.

## Features

- **Photo Gallery:** Displays all photos in the collection.
- **Photo Details:** View individual photos with their descriptions.
- **Add Photo:** Allows users to upload new photos and provide descriptions.

## File Structure

- **views.py:** Contains the main logic for handling requests and rendering templates.
- **models.py:** Defines the `Photo` model.
- **templates:** Contains HTML files for the gallery, photo detail, and add photo pages.

## Dependencies

- **Django:** A high-level Python web framework.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the gallery at `http://localhost:8000/gallery`.
2. View individual photos by clicking on them.
3. Add new photos at `http://localhost:8000/add`.

## Views

### Gallery View

Displays all photos. The photos can be filtered by category (commented out in the code).

### View Photo

Displays a single photo based on its primary key (`pk`).

### Add Photo

Handles the form for adding new photos. If the request method is POST, it saves the new photo and redirects to the gallery.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- Thanks to the Django community for their support and resources.

---

For more details, visit the [Album GitHub Repository](https://github.com/hasan0v/Enactus).
