from setuptools import setup, find_packages

setup(
    name="Testy",  # Name of the package
    version="0.1.0",  # Initial version
    description="A Jest-like Python testing framework",  # Short description
    author="Vagif Aghayev",
    author_email="your_email@example.com",  # Your email (optional)
    url="https://github.com/your-username/testy",  # GitHub repository URL
    packages=find_packages(),  # Automatically find packages in the current directory
    include_package_data=True,  # Include all package files listed in MANIFEST.in
    entry_points={  # Entry point for the CLI command
        "console_scripts": [
            "testy=testy.cli:run_cli",  # Create the `testy` command
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
    install_requires=[  # List all dependencies
        # Example dependencies, you can include your own requirements here
    ],
)
