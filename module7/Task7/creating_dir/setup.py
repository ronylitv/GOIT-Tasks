from setuptools import setup, find_namespace_packages


setup(name='creating_new_fold_for_work',
      version='1',
      description='Very useful code',
      author='Rostyslav Lytvynets',
      author_email='rostislavlitvinets@gmail.com',
      packages=find_namespace_packages(),
      install_requires=['pathlib'],
      entry_points={'console_scripts': ['newfold = creating_dir.fold_creator:func']}
      )
