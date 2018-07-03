"""
Configures access to Adwords API and where to store results
"""
from datetime import date
from mara_config import declare_config

@declare_config()
def data_dir() -> str:
    """The directory where result data is written to"""
    return '/tmp/adwords'


@declare_config()
def first_date() -> str:
    """The first day for which data is downloaded"""
    return '2015-01-01'


@declare_config()
def client_customer_id() -> str:
    """The id of the manager account (MCC) that contains all the accounts for which data should be downloaded"""
    return '123-456-7890'


@declare_config()
def developer_token() -> str:
    """The developer token that is used to access the Adwords API"""
    return 'ABCDEFEGHIJKL'


@declare_config()
def oauth2_client_id() -> str:
    """The Oauth client id obtained from the Adwords API center"""
    return '123456789-abcdefghijklmnopqrstuvwxyz.apps.googleusercontent.com'


@declare_config()
def oauth2_client_secret() -> str:
    """The Oauth client secret obtained from the Adwords API center"""
    return 'aBcDeFg'


@declare_config()
def oauth2_refresh_token() -> str:
    """The Oauth refresh token returned from the adwords-downloader-refresh-oauth2-token script"""
    return '1/acbd-efghijklmnopqrstuvwxyz'


@declare_config()
def api_version() -> str:
    """Which Adwords API version should be called"""
    return 'v201802'


@declare_config()
def redownload_window() -> str:
    """The number of days for which the performance data will be redownloaded"""
    return '30'


@declare_config()
def output_file_version() -> str:
    """A suffix that is added to output files, denoting a version of the data format"""
    return 'v3'


@declare_config()
def max_retries() -> int:
    """How often try retry at max in case of 500 errors"""
    return 5


@declare_config()
def retry_backoff_factor() -> int:
    """How many seconds to wait between retries (is multiplied with retry count)"""
    return 5
