from setuptools import setup
from pathlib import Path
directory = Path(__file__).parent
long_description = (directory / "README.md").read_text()

setup(
  name = 'bookish',         
  packages = ['bookish'],   
  version = '1.2',      
  license='MIT',       
  description = 'Word count for text',   
  author = 'Irati Garitano, Javier Ortega',                 
  author_email = 'irati.garitano@alumni.mondragon.edu, javier.ortega@alumni.mondragon.edu',    
  url = 'https://github.com/iratigaritano/bookish',  
  download_url = 'https://github.com/iratigaritano/bookish/archive/refs/tags/v_12.tar.gz',    
  keywords = ['WORD', 'COUNT', 'BOOK'],  
  
  long_description=long_description,
  long_description_content_type="text/markdown",
  
  install_requires=[            
          'epub_conversion',
          'mobi',
          'xml_cleaner',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
