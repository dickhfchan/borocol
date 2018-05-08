# borocol server

## important
in the server 52.76.*.*, app is in virtualenv not global. First, run source server/bin/activate


## run
require python3
``` bash
# important
# in the server 52.76.*.*, app is in virtualenv not global. First, run follow cmd to enter switch to the env
source server/bin/activate
# exit the env
deactivate

# install dependencies
pip install -r requirements.txt
# write dependencies to requirements.txt
pip freeze > requirements.txt

# development
python run.py
python run.py --remigrate
python run.py --seed
python run.py --remigrate --seed
```
## models and materialized view
models.py defined all models and materialized views. You can edit it to change data table structure. To apply the changes, run sync_tables_and_materialized_views.py
to recreate database and tables, run
remigrate.py

## timestamp
timestamp is int, unit is second

## api
/api/v1/

## fake attrs
['_Generator__config', '_Generator__format_token', '_Generator__random', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'add_provider', 'address', 'am_pm', 'ascii_company_email', 'ascii_email', 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 'boolean', 'bothify', 'bs', 'building_number', 'catch_phrase', 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color_name', 'company', 'company_email', 'company_suffix', 'country', 'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 'cryptocurrency_code', 'cryptocurrency_name', 'ctcd', 'currency', 'currency_code', 'currency_name', 'date', 'date_between', 'date_between_dates', 'date_object', 'date_this_century', 'date_this_decade', 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 'domain_name', 'domain_word', 'dt', 'ean', 'ean13', 'ean8', 'email', 'file_extension', 'file_name', 'file_path', 'firefox', 'first_name', 'first_name_female', 'first_name_male', 'format', 'free_email', 'free_email_domain', 'fstname', 'future_date', 'future_datetime', 'gender', 'geo_coordinate', 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'iban', 'image_url', 'img', 'imgs', 'internet_explorer', 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 'isbn13', 'iso8601', 'job', 'language_code', 'last_name', 'last_name_female', 'last_name_male', 'latitude', 'lexify', 'license_plate', 'linux_platform_token', 'linux_processor', 'locale', 'longitude', 'lstname', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'mdname', 'military_apo', 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name', 'msisdn', 'name', 'name_female', 'name_male', 'null_boolean', 'numerify', 'opera', 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 'phone', 'phone_number', 'postalcode', 'postalcode_plus4', 'postcode', 'prefix', 'prefix_female', 'prefix_male', 'profile', 'provider', 'providers', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystruct', 'pytuple', 'rand', 'random', 'random_digit', 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty', 'random_element', 'random_int', 'random_letter', 'random_lowercase_letter', 'random_number', 'random_sample', 'random_sample_unique', 'random_uppercase_letter', 'randomize_nb_elements', 'randstr', 'rgb_color', 'rgb_css_color', 'safari', 'safe_color_name', 'safe_email', 'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'sentence', 'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state', 'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female', 'suffix_male', 'text', 'time', 'time_delta', 'time_object', 'time_series', 'timezone', 'tld', 'ts', 'unix_device', 'unix_partition', 'unix_time', 'uri', 'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'windows_platform_token', 'word', 'words', 'year', 'zipcode', 'zipcode_plus4']
