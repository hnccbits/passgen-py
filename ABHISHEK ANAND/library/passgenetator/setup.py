from setuptools import setup
 
classifiers = [
  'Development Status :: Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PASSGENERATOR',
  version='0.0.1',
  description='A Password generator',
  long_description=open('readme.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Abhishek Anand',
  author_email='',
  license='MIT', 
  classifiers=classifiers,
  keywords='calculator', 
  packages=['passgenpackage'],
  install_requires=['pyperclip'] 
)
