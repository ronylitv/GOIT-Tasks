from setuptools import setup, find_namespace_packages

setup(name='useful',
      version='1',
      description='Very useful code',
      url='https://github.com/ronylitv/GOIT-Tasks/module7/les2/useful',
      author='Rostyslav Lytvynets',
      author_email='rostislavlitvinets@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      install_requires=['markdown'],
      entry_points={'console_scripts': ['helloworld = useful.some_code:hello_world']}
      )
