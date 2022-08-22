from dataclasses import dataclass
from typing import Optional
import json
import os

# Shared first author
shared = [
    'Self-driving laboratory for accelerated discovery of thin-film materials'
]


@dataclass
class Author:
    last: str
    first_initials: str


@dataclass
class Paper:
    title: str
    journal: str
    year: int
    volume: Optional[str]
    issue: Optional[str]


def process_metadata():
    # Process the metadata files from crossref into an HTML table.

    # data
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

                # Store metadata
                paper = Paper(
                    title=title,
                    journal=journal,
                    year=year,
                    issue=issue,
                    volume=volume,
                )


                # Store
                papers.append(paper)



                # # Authors
                # d['authors'] = ''
                # ca = len(j['message']['author'])
                # sa = ''
                # for ia, a in enumerate(j['message']['author']):
                #     sa += a['family'] + ', '
                #     g = a['given'].split(' ')
                #     sa += g[0][0] + '.'
                #     if len(g) > 1:
                #         sa += ''.join(g[1:])
                #     if ia < 2 and d['title'] in shared:
                #         sa += '*'
                #     if ca > 3 and ia + 2 < ca:
                #         sa += ', '
                #     elif ca > 3 and ia + 2 == ca:
                #         sa += ' & '
                # d['authors'] += sa
                # print(d['authors'])
if __name__ == '__main__':
    process_metadata()