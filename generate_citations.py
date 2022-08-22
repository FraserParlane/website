from dataclasses import dataclass
from typing import Optional, List
import json
import os
import re

# Shared first author
shared_pubs = [
    'Self-driving laboratory for accelerated discovery of thin-film materials'
]


@dataclass
class Author:
    last: str
    first_initials: List[str]


@dataclass
class Paper:
    title: str
    journal: str
    year: int
    volume: Optional[str]
    issue: Optional[str]
    authors: List[Author]

    def __lt__(self, other):
        return self.year < other.year

    def get_author_string(self) -> str:
        """
        Generate HTML string for authors
        :return: string
        """

        auth_str = ''
        for author in self.authors:
            auth_str.append(author.last)
        return auth_str


    def get_paper_string(self) -> str:
        """
        Generate HTML string for paper
        :return: string
        """
        return self.title

def make_pub_objects() -> List[Paper]:
    """
    Process the metadata files from crossref into Python objects
    :return: List of papers
    """
    #

    # data to return
    papers = []

    # For each file
    path = os.path.join(os.getcwd(), 'crossref_metadata')
    for file_name in os.listdir(path):
        if file_name.endswith('.json'):

            # Open
            with open(os.path.join(path, file_name), 'rb') as f:
                j = json.load(f)

                # Extract information from JSON
                title = j['message']['title'][0]
                journal = j['message']['short-container-title'][0]
                url = j['message']['link'][0]['URL']
                year = int(j['message']['published']['date-parts'][0][0])
                issue = None
                volume = None
                if j['message'].get('journal-issue') is not None:
                    issue = int(j['message']['journal-issue']['issue'])
                else:
                    volume = int(j['message']['volume'])
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
                    issue=issue,
                    volume=volume,
                    authors=authors,
                )
                papers.append(paper)

    # Sort
    papers = sorted(papers)
    return papers


def generate_php():
    """
    Generate PHP to include for publications.
    :return: None
    """

    # Data
    php = ''
    papers = make_pub_objects()

    # Iterate through papers
    for paper in papers:
        php += '<tr><td>'
        php += paper.get_paper_string()
        php += '</td></tr>\n'

    # Save to disk
    with open('publications.php', 'w') as f:
        f.write(php)


if __name__ == '__main__':
    generate_php()
