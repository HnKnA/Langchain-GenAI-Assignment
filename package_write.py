import importlib.metadata
import subprocess

# Get the list of packages from pip freeze
def get_pip_freeze():
    result = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE, text=True)
    return result.stdout.strip().splitlines()

# Get the installed packages from pip freeze
pip_packages = get_pip_freeze()

# Create a set of pip packages for quick lookup, excluding those with '@ file'
pip_packages_set = {pkg.split('==')[0].split('@')[0].strip().lower(): pkg for pkg in pip_packages}

# Collect package names and versions
packages = []
for package in importlib.metadata.distributions():
    package_name = package.metadata['Name'].lower()  # Normalize to lowercase for comparison
    # Only include packages that are in the pip freeze list
    if package_name in pip_packages_set:
        packages.append(f"{package.metadata['Name']}=={package.version}")  # Get the original line from pip freeze

# Sort the packages alphabetically
packages.sort()

# Write to the requirements file
with open('requirements.txt', 'w') as f:
    for pkg in packages:
        f.write(f"{pkg}\n")
