from distutils.core import setup
setup(
  name = 'bookish',         
  packages = ['bookish'],   
  version = '0.4',      
  license='MIT',       
  description = 'Word count for text',   
  author = 'Irati Garitano',                 
  author_email = 'irati.garitano@alumni.mondragon.edu',    
  url = 'https://github.com/iratigaritano/bookish',  
  download_url = 'https://github.com/iratigaritano/bookish/archive/refs/tags/v_04.tar.gz',    
  keywords = ['WORD', 'COUNT', 'BOOK'],  
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
