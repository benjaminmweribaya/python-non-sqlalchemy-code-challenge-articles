#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Create authors
    author1 = Author("Alice Walker")
    author2 = Author("James Baldwin")

    # Create magazines
    mag1 = Magazine("Eco Weekly", "Environment")
    mag2 = Magazine("Tech Today", "Technology")

    # Add articles
    article1 = author1.add_article(mag1, "Saving Our Planet")
    article2 = author1.add_article(mag2, "AI and Humanity")
    article3 = author2.add_article(mag1, "Climate Change Facts")
    article4 = author2.add_article(mag2, "Future of Automation")

    # Debugging - Check relationships
    print("Author 1 Articles:", author1.articles())
    print("Author 1 Magazines:", author1.magazines())
    print("Author 1 Topics:", author1.topic_areas())

    print("Magazine 1 Articles:", mag1.articles())
    print("Magazine 1 Contributors:", mag1.contributors())
    print("Magazine 1 Article Titles:", mag1.article_titles())
    print("Magazine 1 Top Publisher:", Magazine.top_publisher())

    # Debugging - Test contributing authors
    print("Magazine 2 Contributing Authors:", mag2.contributing_authors())

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
