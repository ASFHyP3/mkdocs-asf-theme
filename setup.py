from pathlib import Path

from setuptools import find_packages, setup

readme = Path(__file__).parent / 'README.md'

setup(
    name='mkdocs-asf-theme',
    use_scm_version=True,
    description='An extension of the MkDocs Material Theme for ASF',
    long_description=readme.read_text(),
    long_description_content_type='text/markdown',

    url='https://github.com/ASFHyP3/asf-mkdocs-theme',

    author='ASF APD/Tools Team',
    author_email='uaf-asf-apd@alaska.edu',

    license='BSD',
    include_package_data=True,

    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],

    python_requires='~=3.8',

    install_requires=[
        'mkdocs',
        'mkdocs-material',
    ],

    packages=find_packages(),

    entry_points={'mkdocs.themes': [
            'asf-theme = asf_theme',
        ]
    },

    zip_safe=False,
)
