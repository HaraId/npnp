# NP (New Project) - Project Template Generator

## Overview
A command-line tool for quickly generating C++ project templates with various build systems and configurations.

## Features
- Multiple template types (CMake, Makefile, Conan, etc.)
- Simple command-line interface
- Easy to extend with new templates
- Preserves original project files while creating symlinks

## Installation

### Prerequisites
- Python 3.x
- Bash

### Steps
1. Clone or download the repository:
```bash
git clone git@github.com:HaraId/npnp.git
cd np
```

2. Run the installer:

```bash
chmod +x install.sh
sudo ./install.sh
```

3. Verify installation:

```bash
np --version
```

4. Usage

```bash
> np
usage: np [-h] [name] [type]

Create new project template

positional arguments:
  name        Project folder name
  type        Project type (see available templates below)

options:
  -h, --help  show this help message and exit

Examples:
  np my_project cmake
  np new_app qt-cmake

Available project templates:
  - cmake1 : simple cmake project
  - cpp    : just main.cpp
  - make   : No description available
```

5. Project structure

```bash
np/
├── np.py               # Main script
├── templates/          # Project templates
│   ├── cmake/          # Example template
│   │   ├── CMakeLists.txt
│   │   ├── main.cpp
│   │   └── template_description.txt
│   └── ...             # Other templates
└── install.sh          # Installation script
```

6. Adding New Templates

```bash
Adding New Templates
Create a new folder in templates/

Add your template files

Include a template_description.txt file
```

7. Uninstallation

```bash
sudo rm /usr/local/bin/np
```