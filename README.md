# Flask FitFile Viewer

## Overview

The Flask FitFile Viewer is a web application built with Flask that allows users to upload `.fit` files, commonly used in fitness tracking devices, and parses them to extract structured data. It provides a simple interface to view parsed data such as file IDs, records, events, sessions, and activities in JSON format.

## Description

This project aims to simplify the process of analyzing fitness data stored in `.fit` files. By leveraging Flask and `fitparse`, it offers a straightforward solution for users to upload their files and quickly retrieve parsed data for further analysis or integration into other systems.

## Image

![Flask FitFile Viewer](https://github.com/smdedar/laravel-backend-api/assets/30989286/b49e18ec-0a48-4fd1-9753-14039a1f9d6a)

## How it Works

1. **Upload**: Users upload `.fit` files through a web interface.
2. **Parsing**: The application uses `fitparse` to parse uploaded files.
3. **Data Extraction**: Extracts and presents structured data such as file IDs, records, events, sessions, and activities.
4. **Display**: Displays parsed data in JSON format on the user interface for easy viewing and integration.

## Features

- **File Upload**: Supports uploading `.fit` files.
- **Data Parsing**: Uses `fitparse` to extract structured data.
- **Data Presentation**: Displays parsed data (file ID, records, events, sessions, activities) in JSON format.
- **Error Handling**: Provides clear error messages for invalid file types or parsing failures.
- **User Interface**: Simple and intuitive web interface for ease of use.

## Technologies Used

- **Flask**: Web framework for Python.
- **Werkzeug**: Utilities for building web applications with Flask.
- **fitparse**: Python library for parsing `.fit` files.