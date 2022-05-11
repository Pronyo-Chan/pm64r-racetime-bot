from setuptools import find_packages, setup


setup(
    name='pm64r-randobot',
    description='racetime.gg bot for generating PM64R seeds.',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'GNU GENERAL PUBLIC LICENSE',
        'Programming Language :: Python :: 3.10',
    ],
    url='https://racetime.gg/pm64r',
    project_urls={
        'Source': 'https://github.com/Pronyo-Chan/pm64r-racetime-bot',
    },
    version='0.1.0',
    install_requires=[
        'racetime_bot>=1.5.0,<2.0',
        'google-cloud-secret-manager>=2.10.0',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'randobot=randobot:main',
        ],
    },
)