from setuptools import setup, find_packages

setup(
        name = "nash_equilibrium",
        version = "1.0",
        description = "Nash equilibrium",
        long_description = "Solve the matrix game using simplex method free",
        license = "MIT",
        packages = find_packages(),
        classifiers = [
                "Programming language :: Python :: 3",
                "License :: OSI approved :: MIT License",
        ],
        python_required = "=> 3.6",
)
