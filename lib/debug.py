#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Reset the lists to avoid conflicts
    Article._all = []
    Magazine._all = []

    # Create authors
    author1 = Author("Alice Walker")
    author2 = Author("James Baldwin")
    author3 = Author("Toni Morrison")

    # Create magazines
    mag1 = Magazine("Eco Weekly", "Environment")
    mag2 = Magazine("Tech Today", "Technology")
    mag3 = Magazine("Literary Digest", "Literature")

    # Add articles
    article1 = author1.add_article(mag1, "Saving Our Planet")
    article2 = author1.add_article(mag2, "AI and Humanity")
    article3 = author2.add_article(mag1, "Climate Change Facts")
    article4 = author2.add_article(mag2, "Future of Automation")
    article5 = author2.add_article(mag3, "The Art of Writing")
    article6 = author3.add_article(mag3, "Literature in the Modern Age")

    # Debugging - Check relationships
    print("Author 1 Articles:", author1.articles())
    print("Author 1 Magazines:", author1.magazines())
    print("Author 1 Topics:", author1.topic_areas())

    print("Magazine 1 Articles:", mag1.articles())
    print("Magazine 1 Contributors:", mag1.contributors())
    print("Magazine 1 Article Titles:", mag1.article_titles())
    print("Magazine 1 Top Publisher:", Magazine.top_publisher())

    # Test mutability of Magazine's name and category
    print("Original Magazine Name:", mag2.name)
    mag2.name = "Tech Innovations"
    print("Updated Magazine Name:", mag2.name)

    print("Original Magazine Category:", mag2.category)
    mag2.category = "Innovation"
    print("Updated Magazine Category:", mag2.category)

    # Test mutability of Article's author and magazine
    print("Original Article Author:", article1.author.name)
    article1.author = author3
    print("Updated Article Author:", article1.author.name)

    print("Original Article Magazine:", article1.magazine.name)
    article1.magazine = mag3
    print("Updated Article Magazine:", article1.magazine.name)

    # Test contributing authors for magazines with multiple articles
    print("Magazine 3 Contributing Authors:", mag3.contributing_authors())

    # Debugging - Test Article.all and Magazine.all
    print("All Articles:", Article.all())
    print("All Magazines:", Magazine.all())

    # don't remove this line, it's for debugging!
    ipdb.set_trace()
