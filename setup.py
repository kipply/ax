import setuptools
setuptools.setup(
    name='ax',
    version='0.1',
    scripts=['src/ax'],
    author='Carol Chen',
    description='Connect your running processes to Spotify!',
    install_requires=[
        'setuptools',
        'spotipy >= 2.13.0'
    ],
    python_requires='>=3.5'
)
