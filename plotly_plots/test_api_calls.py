import pytest
import requests

from mtg_card_data import url as mtg_url, headers as mtg_headers
from github_ai_repos import url as gh_ai_url, headers as gh_ai_headers
from popular_repo import url as gh_pop_repo_url, headers as gh_pop_headers
from hn_submissions import url as hn_subs_url
from hn_article import url as hn_art_url


@pytest.fixture() # need to visit this again for furthwer understadning does this get called every time we run pytest to 
# update the status codes
def api_calls():
    """Used as a means to set up all api calls for status testing. Should be 
    relativly simp[le since we can use the request lib and simply check the
    status code."""
    # assemble the needed urls and headers
    urls_headers = [(mtg_url, mtg_headers),
            (gh_ai_url, gh_ai_headers),
            (gh_pop_repo_url, gh_pop_headers),
            (hn_subs_url, None),
            (hn_art_url, None),
            ]
    return urls_headers

def test_status_codes_of_all_api_calls_from_requests(api_calls):
    """Used to chekl that all api calls are operating as we want them to."""
    response_status_codes = []

    for url, specific_header in api_calls:
        api_call = requests.get(url, headers=specific_header)# set to default?
        response_status_codes.append(api_call.status_code)
    
    for status_code in response_status_codes:
        assert status_code == 200


# why does this run 2 of our plotly scripts and open our browser???
# we learned a crucial thing here and that's upon import if we have code like
# fig.show() that's ran at the top level of the script outside of fujnctions or
# classes and this means that it executes upon import wwe fiux this with the 
# handy method of a conditional if statement to test if it's re