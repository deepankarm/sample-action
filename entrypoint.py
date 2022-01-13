import logging
import sys
from http import HTTPStatus

import requests


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def main(args):
    LOGGER = get_logger()
    repo, token, docsdir, index_pattern, readme, branch = args
    url = 'https://m702s4l4m9.execute-api.us-east-1.amazonaws.com/dev/projects'  # TODO
    body = {'repo': repo}
    if docsdir != 'docs':
        body['docsdir'] = docsdir
    if index_pattern != '**/*.md':
        body['index_pattern'] = index_pattern

    readme = True if readme == 'true' else False
    if readme:
        body['readme'] = True

    if branch != 'none':
        body['branch'] = branch
    headers = {'Authorization': token}
    print(body)
    print(headers)
    response = requests.post(url=url, json=body, headers=headers)
    print(response.json())
    if response.status_code == HTTPStatus.CREATED:
        LOGGER.info(
            f'Successfully registered `{repo}` with DocsQA. '
            f'You\'d receive an email with the details in a few minutes.'
        )
    elif response.status_code == HTTPStatus.OK:
        LOGGER.info(
            f'Successfully retriggered {repo} with DocsQA. '
            f'You\'d be alerted once reindexing is completed.'
        )
    elif response.status_code == HTTPStatus.UNAUTHORIZED:
        LOGGER.error('Couldn\'t trigger (Unauthorized)')
        sys.exit(-1)
    elif response.status_code == HTTPStatus.FORBIDDEN:
        LOGGER.error(f'Wrong token used, please create a PAT with user:email scope')
        sys.exit(-1)
    else:
        LOGGER.error(f'Failed with code {response.status_code}')
    assert response.status_code in [HTTPStatus.OK, HTTPStatus.CREATED]


if __name__ == '__main__':
    main(sys.argv[1:])
