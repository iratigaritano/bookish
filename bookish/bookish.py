from epub_conversion.utils import open_book, convert_epub_to_lines
import os
import operator
import re
import shutil
from mobi.kindleunpack import unpackBook

class counter: 

    """ Count the words of a file

    Parameters
    ----------
    book_file: txt, epub or mobi, required
        text to count
    file_directory: str, default current directory
        directory where the book is located
    language: str, default English
        language of the text   
    """
    def __init__(self,book_file, file_directory=os.getcwd(), language='English', link_words:bool=False):
        """
        initialise the attributes of the class  after checking that the format and language is correct
        """    

        __languages = ['English', 'Spanish']
        if language not in __languages:
            raise ValueError("Invalid Language. Expected one of: %s" % __languages)
        else:
            self.language=language

        __book_formats = ['txt', 'epub','mobi']
        if book_file.split('.')[-1] not in __book_formats:
            raise ValueError("Invalid Language. Expected one of: %s" % __book_formats)
        else:
            self.__book_format=book_file.split('.')[-1]   
            self.file_directory=file_directory
            self.book_file=book_file

        self.__eng=['above','across','along','around','against','at', 'behind','beside','below','beneath','between','by','in','of','inside','near','on','opposite','outside','over','under','underneath','upon',
        "at", "in", "to", "of",'and', "on", 'about', 'after','around', 'before', 'beyond', 'during','for','past','since','throughout','until','away','the', 'i','it','she','he','they','their','them', 'not','her','his','him',
        'down','from','into','off','onto','out','over','past','to', 'towards','under','up','ago','circa','per','from','with', 'a', 's', 't','as','you',
        'that', 'we','or','if','so','this','me','there','how','when','where','that','who','whose','what','my','but']

        self.__esp=['a','ante', 'bajo', 'cabe', 'con', 'contra', 'de', 'desde', 'durante', 'en', 'entre', 'hacia', 'hasta', 'mediante', 'para', 'por', 'segun', 'sin', 'so', 'sobre', 'tras', 'versus', 'via', 
        'el','la','lo','los','las','un','una','unos','unas','al','del', 'se', 'su', 'le','sus','e','este','esta','les','aquella', 'donde','tan', 'a',
        'y','ni','no','tambien','tanto','como','asi','que','pero','mas','empeoro','sino','mientras','o','u','ya','porque','como','pues','sin','aunque','cuando','por','si','luego', 'conque','mientras']

        self.link_words=link_words

    @property
    def link_words(self):
        return self.__link_words

    @link_words.setter
    def link_words(self, link_words):
        self.__link_words=link_words

    def read_book(self):
        """Reads the text
        Returns
        -------
        book: str
            String of all the text without line breaks
        """
        if self.__book_format=='txt':
            lines=open(f'{self.file_directory}/{self.book_file}', encoding='utf-8').readlines()
        elif self.__book_format=='epub':
            to_format_book = open_book(f'{self.file_directory}/{self.book_file}')
            lines = convert_epub_to_lines(to_format_book)
        elif self.__book_format=='mobi':
            current_dir=os.getcwd()
            original_dirs=next(os.walk('.'))[1]
            epub_book_file=self.book_file.replace('mobi','epub')
            unpackBook(f'{self.file_directory}/{self.book_file}', current_dir, epubver="A")
            shutil.move(f'{current_dir}/mobi8/{epub_book_file}',f'{self.file_directory}')
            new_dirs=next(os.walk('.'))[1]
            remove_dirs=list(set(new_dirs) -set(original_dirs))
            to_format_book=open_book(f'{current_dir}/{epub_book_file}')
            lines= convert_epub_to_lines(to_format_book)
            for pouvelle in remove_dirs:
                shutil.rmtree(f'{current_dir}/{pouvelle}', ignore_errors=False)
        else: 
            print('error')
        book=' '.join(lines)
        return book

    def cleanning(self) :
        """Cleans the text
        Parameters
        ----------
        link_words: bol, default False
            If articles, conjunctions and prepositions are omitted
        Returns
        -------
        book_div: list
            List of words cleanned 
        """

        book=self.read_book()
        book_cleaned=re.sub(r'[^\w]', ' ', book)
        book_div=list(filter(None, book_cleaned.lower().split(' ')))   
        book_div2=[]
        if self.__link_words==False:
            if self.language=='English':
                for word in book_div:  
                    if not word in self.__eng:
                        book_div2.append(word)
            if self.language=='Spanish':
                for word in book_div:  
                    if not word in self.__esp:
                        book_div2.append(word)
        else:
            book_div2=book_div
        return book_div2

    def count(self):
        """Counts the text
        Returns
        -------
        sorted_word_dict: dictionary
            Sorted dictionary of the counted words
        """
        clean_book=self.cleanning()
        word_list=[]
        word_dict={}
        for word in clean_book:
            if word not in word_list:
                word_list.append(word)
                word_dict[word]=clean_book.count(word)

        sorted_word_tuple = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
        sorted_word_dict = {k: v for k, v in sorted_word_tuple}
        return sorted_word_dict