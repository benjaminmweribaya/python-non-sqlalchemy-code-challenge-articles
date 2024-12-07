class Article:
    _all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = new_author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, new_magazine):
        if not isinstance(new_magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        self._magazine = new_magazine

    @classmethod
    def all(cls):
        return cls._all
    
        
class Author:
    def __init__(self, name):
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = new_name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, article):
        self._articles.append(article)

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))
        

class Magazine:
    _all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    @classmethod
    def all(cls):
        return cls._all

    def articles(self):
        return [article for article in Article._all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_counts = {author: 0 for author in self.contributors()}
        for article in self.articles():
            author_counts[article.author] += 1
        return [author for author, count in author_counts.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        return max(cls._all, key=lambda magazine: len(magazine.articles()), default=None)