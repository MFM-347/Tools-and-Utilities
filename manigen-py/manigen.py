import json
import uuid
import argparse
import sys
from colorama import init, Fore, Style

init(autoreset=True)

print(f"{Fore.YELLOW}Welcome to the ManiGen (Minecraft BE Resource Pack Manifest Generator){Style.RESET_ALL}")

def generate_uuid():
    return str(uuid.uuid4())
    
def get_user_input(prompt, default_value=None):
    user_input = input(f"{Fore.CYAN}{prompt} [{default_value}]: {Style.RESET_ALL}")
    return user_input if user_input else default_value

def parse_version(version_str):
    try:
        return [int(x) for x in version_str.split('.')]
    except ValueError:
        print(f"{Fore.RED}Invalid version format. Using default [1, 0, 0].{Style.RESET_ALL}")
        return [1, 0, 0]

def generate_manifest(pack_name, description, version, min_engine_version):
    header_uuid = generate_uuid()
    module_uuid = generate_uuid()

    manifest = {
        "format_version": 2,
        "header": {
            "description": description,
            "name": pack_name,
            "uuid": header_uuid,
            "version": version,
            "min_engine_version": min_engine_version
        },
        "modules": [
            {
                "description": description,
                "type": "resources",
                "uuid": module_uuid,
                "version": version
            }
        ]
    }
    
    print(f"\n{Fore.GREEN}Generated manifest.json:{Style.RESET_ALL}")
    print(json.dumps(manifest, indent=2))
    
    with open("manifest.json", "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\n{Fore.GREEN}Manifest file 'manifest.json' has been created successfully!{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="Minecraft Resource Pack Manifest Generator")
    parser.add_argument('command', choices=['init', 'template'], help="Command to run: 'init' for user input, 'template' for default values")
    
    args = parser.parse_args()

    if args.command == 'init':
        pack_name = get_user_input("Enter the resource pack name", "My Resource Pack")
        description = get_user_input("Enter the resource pack description", "A custom resource pack")
        
        major_version = int(get_user_input("Enter major version", "1"))
        minor_version = int(get_user_input("Enter minor version", "0"))
        patch_version = int(get_user_input("Enter patch version", "0"))
        version = [major_version, minor_version, patch_version]
        
        min_engine_version_str = get_user_input("Enter min engine version", "1.21.30")
        min_engine_version = parse_version(min_engine_version_str)
        
        generate_manifest(pack_name, description, version, min_engine_version)

    elif args.command == 'template':
        pack_name = "My Resource Pack"
        description = "A custom resource pack"
        version = [1, 0, 0]
        min_engine_version = [1, 21, 30]
        
        generate_manifest(pack_name, description, version, min_engine_version)

if __name__ == "__main__":
    main()