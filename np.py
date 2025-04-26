#!/usr/bin/env python3
import os
import sys
import argparse
from pathlib import Path

script_path = Path(__file__).resolve()
script_dir = script_path.parent

TEMPLATES_DIR = script_dir / "templates"
DESCRIPTION_FILE = "template_description.txt"

def get_template_description(template_path):
    """Read description from template_description.txt if exists"""
    desc_file = template_path / DESCRIPTION_FILE
    if desc_file.exists():
        return desc_file.read_text().strip()
    return "No description available"

def list_templates():
    """Display all available project templates with descriptions"""
    templates = [d for d in TEMPLATES_DIR.iterdir() if d.is_dir()]
    if not templates:
        print("No templates found in 'templates' directory!")
        return
    
    print("\nAvailable project templates:")
    max_name_len = max(len(t.name) for t in templates)
    
    for template in sorted(templates, key=lambda x: x.name):
        desc = get_template_description(template)
        print(f"  - {template.name.ljust(max_name_len)} : {desc}")
    print()

def create_project(project_name, project_type):
    template_path = TEMPLATES_DIR / project_type
    
    if not template_path.exists():
        print("\n❌ Error: Template '{}' not found!".format(project_type))
        list_templates()
        sys.exit(1)
    
    project_path = Path(project_name)
    project_path.mkdir(parents=True, exist_ok=False)
    
    for file in template_path.glob("*"):
        # Пропускаем файл описания
        if file.name == DESCRIPTION_FILE:
            continue
            
        dest = project_path / file.name
        if file.is_file():
            content = file.read_text()
            content = content.replace("{{project_name}}", project_name)
            dest.write_text(content)
    
    print(f"\n✅ Project '{project_name}' ({project_type}) created!")
    print(f"📁 Path: {project_path.absolute()}\n")

def main():
    parser = argparse.ArgumentParser(
        description="Create new project template",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  np my_project cmake\n"
               "  np new_app qt-cmake\n"
    )
    parser.add_argument(
        "name", 
        nargs="?", 
        help="Project folder name"
    )
    parser.add_argument(
        "type",
        nargs="?",
        help="Project type (see available templates below)"
    )

    if len(sys.argv) == 1:
        parser.print_help()
        list_templates()
        sys.exit(0)

    args = parser.parse_args()

    if not args.name or not args.type:
        print("\n❌ Error: You must specify both project name and type!")
        list_templates()
        sys.exit(1)

    try:
        create_project(args.name, args.type)
    except FileExistsError:
        print(f"\n❌ Error: Folder '{args.name}' already exists!")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
