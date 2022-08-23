from dataclasses import dataclass
from typing import Optional, List
import json
import os
import re

# Shared first author
shared_pubs = [
    'Self-driving laboratory for accelerated discovery of thin-film materials',
    'A self-driving laboratory advances the Pareto front for material properties',
    'Flexible automation for self-driving laboratories',
]
priorities = []


@dataclass
class Author:
    last: str
    first_initials: List[str]

    def __post_init__(self):
        self.me = True if self.last == 'Parlane' else False


@dataclass
class Paper:
    title: str
    journal: str
    year: int
    url: str
    page: str
    volume: Optional[str]
    issue: Optional[str]
    authors: List[Author]
    priority: bool

    def __post_init__(self):
        self.shared = True if self.title in shared_pubs else False
        self.num_authors = len(self.authors)
        if self.title[-1] == '.':
            self.title = self.title[:-1]

    def __lt__(self, other):
        return self.year < other.year

    def get_author_string(self) -> str:
        """
        Generate HTML string for authors
        :return: string
        """

        php = ''
        for i, author in enumerate(self.authors):
            if author.me:
                php += '<b>'

            # Names
            php += author.last + ', '
            php += '. '.join(author.first_initials) + '.'

            # Formatting
            if i < 2 and self.shared:
                php += '*'
            if author.me:
                php += '</b>'

            # Final ampersand
            if i + 1 != self.num_authors:
                php += ', '
            if i + 2 == self.num_authors:
                php += '& '
        return php

    def get_paper_string(self) -> str:
        """
        Generate HTML string for paper
        :return: string
        """

        php = ''
        php += self.get_author_string()
        php += ' '
        php += f'<a href="{self.url}" target="_blank">{self.title}.</a> '
        php += f'<i>{self.journal}</i> '
        b_str = self.issue if self.issue is not None else self.volume
        php += f'<b>{b_str}</b>, {self.page} ({self.year}).'

        return php


def make_pub_objects() -> List[Paper]:
    """
    Process the metadata files from crossref into Python objects
    :return: List of papers
    """
    #

    # data to return
    papers = []

    # For each file
    path = os.path.join(os.getcwd(), '../crossref_metadata')
    for file_name in os.listdir(path):
        if file_name.endswith('.json'):

            # Open
            with open(os.path.join(path, file_name), 'rb') as f:
                j = json.load(f)

                # Extract information from JSON
                title = j['message']['title'][0]
                if j['message'].get('short-container-title'):
                    journal = j['message']['short-container-title'][0]
                else:
                    journal = j['message']['container-title'][0]
                    journal += ' (' + j['message']['publisher'] + ')'
                url = j['message']['resource']['primary']['URL']
                year = int(j['message']['published']['date-parts'][0][0])
                issue = None
                volume = None
                priority = True if title in priorities else False
                if j['message'].get('page') is not None:
                    page = j['message']['page']
                elif j.get('published') is not None:
                    if j['published'].get('article-number') is not None:
                        page = j['published']['article-number']
                if j['message'].get('journal-issue') is not None:
                    issue = int(j['message']['journal-issue']['issue'])
                elif j['message'].get('volume') is not None:
                    volume = int(j['message']['volume'])
                else:
                    print('a')
                shared = True if title in shared_pubs else False

                # Make the authors
                authors = []

                # For each author
                for ia, a in enumerate(j['message']['author']):

                    last = a['family']
                    first_split = re.split(', |,| ', a['given'])
                    first_inits = [fsplit[0] for fsplit in first_split]

                    # Make, store
                    author = Author(
                        last=last,
                        first_initials=first_inits,
                    )
                    authors.append(author)

                # Store metadata
                paper = Paper(
                    title=title,
                    journal=journal,
                    year=year,
                    page=page,
                    issue=issue,
                    url=url,
                    volume=volume,
                    authors=authors,
                    priority=priority
                )
                papers.append(paper)

    # Sort
    papers = sorted(papers, reverse=True)
    return papers


def generate_php():
    """
    Generate PHP to include for publications.
    :return: None
    """

    # Data
    php = ''
    papers = make_pub_objects()

    # Add temporary MRS reference
    with open('../php/temp_references.php') as f:
        php += f.read()

    # Iterate through papers
    for paper in papers:
        php += '<tr><td>'

        # Generate paper string
        php += ' '
        php += paper.get_paper_string()
        php += '</td></tr>\n'

    # Save to disk
    with open('../php/publications.php', 'w') as f:
        f.write(php)


if __name__ == '__main__':
    generate_php()
