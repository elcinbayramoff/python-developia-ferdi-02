# a = 3
# b = 5

# a = b # 5 5
# b = 3

# print(a, b)

# A = (1, 2, 3, 4, 5)
# # print(A[1:3])
# A[0] = 5
# print(A)

# A = list('Hello')
# A = (1, 2, 3, 4, 5)
# A = list(A)
# A[2] = 100
# A = tuple(A)
# print(A)


# a1 = A[0]
# a2 = A[1]
# a3 = A[2]
# A = (1, 2, 3)
# a1, a2, a3 = (1, 2, 3)
# print(a1, a2, a3)

# a1, a2, *a3 = (1, 2, 3, 4)
# print(a1, a2, a3)

# *a1, a2, a3 = (1, 2, 3, 4, 5)
# print(a1, a2, a3)

# a1, *a2, a3 = (1, 2, 3, 4, 5)
# print(a1, a2, a3)
# a = 3
# b = 5

# a, b = b, a
# print(a, b)

# a = 'a' * 10
# print(a)

# a = [1] * 10
# print(a)

# a = 1 * 10
# print(a)

# a = (1,) * 10
# print(a)

# a = 100
# dollar = a * 0.59
# print(dollar)

# a = 2
# b = 3

# a1 = a
# a = b
# b = a1

# a,b,*c = (1,2,3,4)

# print(a,b,c)
# a = 2
# b = 3
# a, b = b, a #a = 3, b = 2
# print(a, b)

# a, *b, c, d = (1,2,3,4,5,6,7)
# print(a, b, c)

# a = [5]
# a = '5'
# a = (5)
# print(type(a))

# a = (2,)
# print(type(a))

# a = (1, 2, 2, 3, 4, 2)

# print(a.count(2))
# print(len(a))

# a = (1,2,3)
# print(a.index(2))
# print((1,2,3).index(2))

{'environ': {'REDIS_URL': 'redis://redis:6379/0', 'FRONTEND_URL': 'https://dev.dmpservice.org', 'DJANGO_AWS_MEDIA_FILES_BUCKET_NAME': 'dmp-dev-media', 'PYTHONUNBUFFERED': '1', 'POSTGRES_HOST': 'contract_new_db', 'DATABASE_URL': 'postgres://debug:debug@contract_new_db:5432/contract_service', 'DJANGO_S3_URL': 'https://cdnlocal.dmpservice.org:8443/', 'HOSTNAME': '02b9c833b0f1', 'PYTHON_VERSION': '3.11.6', 'DJANGO_AWS_ACCESS_KEY_ID': 'IrfF42jkuKlSwdPT5KNQ', 'POSTGRES_PASSWORD': 'debug', 'USER_DATA_CACHE_EXPIRED_AFTER_SECONDS': '604800', 'SERVICE_PRIVATE_KEY': 'tywjpr8F.yClSTDivGVHDLxgg5CQnovQTTOtiysFy', 'PWD': '/app', 'PYTHON_SETUPTOOLS_VERSION': '65.5.1', 'IPYTHONDIR': '/app/.ipython', 'HOME': '/root', 'LANG': 'C.UTF-8', 'USE_DOCKER': 'yes', 'GPG_KEY': 'A035C8C19219BA821ECEA86B64E628F8D684696D', 'DJANGO_AWS_STATIC_FILES_BUCKET_NAME': 'dmp-dev-static', 'EXTERNAL_PB_MACRO_URL': 'http://localhost/integration_service/api/v1/pricebook_download/bp/', 'KAFKA_CONFIG_FILE_PATH': '/app/pyproject.toml', 'BUILD_ENV': 'local', 'PROFILING': 'True', 'POSTGRES_PORT': '5432', 'SHLVL': '0', 'POSTGRES_USER': 'debug', 'PYTHON_PIP_VERSION': '23.2.1', 'PYTHONDONTWRITEBYTECODE': '1', 'CURRENCY_API_KEY': 'A6wwiW97Z76ZWQLKMkyxT0iIAg3yT2y7', 'PYTHON_GET_PIP_SHA256': '9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6', 'PYTHON_GET_PIP_URL': 'https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py', 'DJANGO_AWS_STORAGE_BUCKET_NAME': 'dmp-dev-static', 'PATH': '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'DJANGO_AWS_SECRET_ACCESS_KEY': 'yDdKOSFduz2SHrVfDFSEvtUbuQUYV1gxI3VazmDa', 'POSTGRES_DB': 'contract_service', 'DJANGO_SETTINGS_MODULE': 'config.settings.local', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': '02b9c833b0f1', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '36', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/contract_new/api/v1/pricebooks/drafts/create_request/', 'QUERY_STRING': 'is_marketplace=false', 'REMOTE_ADDR': '172.18.0.1', 'CONTENT_TYPE': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTMzNzI5OTIsInVzZXIiOnsiaWQiOjQ0NywibmFtZSI6IkVsY2hpbiBCYXlyYW1saSBTdXBwbGllciIsImZpcnN0X25hbWUiOiJFbGNoaW4iLCJsYXN0X25hbWUiOiJCYXlyYW1saSBTdXBwbGllciIsImVtYWlsIjoiZWxjaGluYitzdXBwbGllckBkbXBzZXJ2aWNlLm9yZyIsImlzX3N0YWZmIjp0cnVlLCJyb2xlcyI6WyJzdXBwbGllciIsInN1cHBsaWVyX2FkbWluIl0sImlzX2N1c3RvbWVyIjpmYWxzZSwiaXNfc3VwcGxpZXIiOnRydWUsImNvbXBhbnlfaWQiOjQ2fX0.sEQ8Hdv7yEg1xWF6EDif_mA0o4Dy3XIQBrk3eubUkA1rL5tOvD6UCUYc-e5eTXLFhv1U1_g6y2NHuQm85lQGv8PHk0m56Uo2cX6E4rYMHW8KbExZVS7NEMBecEl9zUf6l3MDc-nddQVchhYUA8ChlQ61awWM2Ba9T25H2e8UjoBusx6wt0BD79RRrgBgiUStgQLcpQ0rHesPIQoWyWgUGvbpClCh2Suqn5wfylIumc38HRK1rU-yNLkjM0KC73bepdoKhTA0Q8qGda8gGwRfU1Rb2m4kpEFf-xFapSsAe7QkucSo-5MHzwJ9-4L86KvWVRrvLrN24pSWwB6Xa9qsw3SJNXcpFL-n0YjDliKNq_lIXm3OCxn1JIaCafQCaC8ZeNAJYKvPhmx2bSveY5uWhZWGiFiuLpx1h7XYxAdBEb1RNzeWUn3W8rcRvVTXdtOcXI8_MCwfR0oIhksOBPwPe-uYrt_lBkfA5nQ7STsb7ZM1p1stjuXAcv5USDzDox9LCgEaOkIhTo3hcgNYGU2p0HD0DhhoCnF13jLJ5Q5Mqcy7pmyArX71jZHi3FpkIq6fCe7jzYs8tlb_jnewn3jCm0LJY2HqpqMqLC9A_4kK-HzPvqtXqN0q29FKtwH8i3gogP5Xey5pt1a3QVuZJHiGhwIInDdMoV-9I-G303e6aks', 'HTTP_CONNECTION': 'upgrade', 'HTTP_HOST': 'contract', 'HTTP_SEC_CH_UA_PLATFORM': '"Linux"', 'HTTP_X_CSRFTOKEN': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36', 'HTTP_ACCEPT': 'application/json, text/plain, */*', 'HTTP_SEC_CH_UA': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_ORIGIN': 'http://localhost', 'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_SEC_FETCH_MODE': 'cors', 'HTTP_SEC_FETCH_DEST': 'empty', 'HTTP_REFERER': 'http://localhost/app/contract/pricebooks/17/drafts', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br, zstd', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9', 'HTTP_COOKIE': 'marketingconsentcookie=true; SESSION=815eee15-c073-4b16-82d1-9282e9c945cd; auth_token=89550c6d70515b61040108d4b5a704c122b3dd54; csrftoken=t7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x7a6137df2610>, 'wsgi.errors': <colorama.ansitowin32.StreamWrapper object at 0x7a618835ee90>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A'}, 'path_info': '/contract_new/api/v1/pricebooks/drafts/create_request/', 'path': '/contract_new/api/v1/pricebooks/drafts/create_request/', 'META': {'REDIS_URL': 'redis://redis:6379/0', 'FRONTEND_URL': 'https://dev.dmpservice.org', 'DJANGO_AWS_MEDIA_FILES_BUCKET_NAME': 'dmp-dev-media', 'PYTHONUNBUFFERED': '1', 'POSTGRES_HOST': 'contract_new_db', 'DATABASE_URL': 'postgres://debug:debug@contract_new_db:5432/contract_service', 'DJANGO_S3_URL': 'https://cdnlocal.dmpservice.org:8443/', 'HOSTNAME': '02b9c833b0f1', 'PYTHON_VERSION': '3.11.6', 'DJANGO_AWS_ACCESS_KEY_ID': 'IrfF42jkuKlSwdPT5KNQ', 'POSTGRES_PASSWORD': 'debug', 'USER_DATA_CACHE_EXPIRED_AFTER_SECONDS': '604800', 'SERVICE_PRIVATE_KEY': 'tywjpr8F.yClSTDivGVHDLxgg5CQnovQTTOtiysFy', 'PWD': '/app', 'PYTHON_SETUPTOOLS_VERSION': '65.5.1', 'IPYTHONDIR': '/app/.ipython', 'HOME': '/root', 'LANG': 'C.UTF-8', 'USE_DOCKER': 'yes', 'GPG_KEY': 'A035C8C19219BA821ECEA86B64E628F8D684696D', 'DJANGO_AWS_STATIC_FILES_BUCKET_NAME': 'dmp-dev-static', 'EXTERNAL_PB_MACRO_URL': 'http://localhost/integration_service/api/v1/pricebook_download/bp/', 'KAFKA_CONFIG_FILE_PATH': '/app/pyproject.toml', 'BUILD_ENV': 'local', 'PROFILING': 'True', 'POSTGRES_PORT': '5432', 'SHLVL': '0', 'POSTGRES_USER': 'debug', 'PYTHON_PIP_VERSION': '23.2.1', 'PYTHONDONTWRITEBYTECODE': '1', 'CURRENCY_API_KEY': 'A6wwiW97Z76ZWQLKMkyxT0iIAg3yT2y7', 'PYTHON_GET_PIP_SHA256': '9cc01665956d22b3bf057ae8287b035827bfd895da235bcea200ab3b811790b6', 'PYTHON_GET_PIP_URL': 'https://github.com/pypa/get-pip/raw/4cfa4081d27285bda1220a62a5ebf5b4bd749cdb/public/get-pip.py', 'DJANGO_AWS_STORAGE_BUCKET_NAME': 'dmp-dev-static', 'PATH': '/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin', 'DJANGO_AWS_SECRET_ACCESS_KEY': 'yDdKOSFduz2SHrVfDFSEvtUbuQUYV1gxI3VazmDa', 'POSTGRES_DB': 'contract_service', 'DJANGO_SETTINGS_MODULE': 'config.settings.local', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': '02b9c833b0f1', 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8000', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '36', 'SCRIPT_NAME': '', 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'POST', 'PATH_INFO': '/contract_new/api/v1/pricebooks/drafts/create_request/', 'QUERY_STRING': 'is_marketplace=false', 'REMOTE_ADDR': '172.18.0.1', 'CONTENT_TYPE': 'application/json', 'HTTP_AUTHORIZATION': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTMzNzI5OTIsInVzZXIiOnsiaWQiOjQ0NywibmFtZSI6IkVsY2hpbiBCYXlyYW1saSBTdXBwbGllciIsImZpcnN0X25hbWUiOiJFbGNoaW4iLCJsYXN0X25hbWUiOiJCYXlyYW1saSBTdXBwbGllciIsImVtYWlsIjoiZWxjaGluYitzdXBwbGllckBkbXBzZXJ2aWNlLm9yZyIsImlzX3N0YWZmIjp0cnVlLCJyb2xlcyI6WyJzdXBwbGllciIsInN1cHBsaWVyX2FkbWluIl0sImlzX2N1c3RvbWVyIjpmYWxzZSwiaXNfc3VwcGxpZXIiOnRydWUsImNvbXBhbnlfaWQiOjQ2fX0.sEQ8Hdv7yEg1xWF6EDif_mA0o4Dy3XIQBrk3eubUkA1rL5tOvD6UCUYc-e5eTXLFhv1U1_g6y2NHuQm85lQGv8PHk0m56Uo2cX6E4rYMHW8KbExZVS7NEMBecEl9zUf6l3MDc-nddQVchhYUA8ChlQ61awWM2Ba9T25H2e8UjoBusx6wt0BD79RRrgBgiUStgQLcpQ0rHesPIQoWyWgUGvbpClCh2Suqn5wfylIumc38HRK1rU-yNLkjM0KC73bepdoKhTA0Q8qGda8gGwRfU1Rb2m4kpEFf-xFapSsAe7QkucSo-5MHzwJ9-4L86KvWVRrvLrN24pSWwB6Xa9qsw3SJNXcpFL-n0YjDliKNq_lIXm3OCxn1JIaCafQCaC8ZeNAJYKvPhmx2bSveY5uWhZWGiFiuLpx1h7XYxAdBEb1RNzeWUn3W8rcRvVTXdtOcXI8_MCwfR0oIhksOBPwPe-uYrt_lBkfA5nQ7STsb7ZM1p1stjuXAcv5USDzDox9LCgEaOkIhTo3hcgNYGU2p0HD0DhhoCnF13jLJ5Q5Mqcy7pmyArX71jZHi3FpkIq6fCe7jzYs8tlb_jnewn3jCm0LJY2HqpqMqLC9A_4kK-HzPvqtXqN0q29FKtwH8i3gogP5Xey5pt1a3QVuZJHiGhwIInDdMoV-9I-G303e6aks', 'HTTP_CONNECTION': 'upgrade', 'HTTP_HOST': 'contract', 'HTTP_SEC_CH_UA_PLATFORM': '"Linux"', 'HTTP_X_CSRFTOKEN': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A', 'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36', 'HTTP_ACCEPT': 'application/json, text/plain, */*', 'HTTP_SEC_CH_UA': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_ORIGIN': 'http://localhost', 'HTTP_SEC_FETCH_SITE': 'same-origin', 'HTTP_SEC_FETCH_MODE': 'cors', 'HTTP_SEC_FETCH_DEST': 'empty', 'HTTP_REFERER': 'http://localhost/app/contract/pricebooks/17/drafts', 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br, zstd', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9', 'HTTP_COOKIE': 'marketingconsentcookie=true; SESSION=815eee15-c073-4b16-82d1-9282e9c945cd; auth_token=89550c6d70515b61040108d4b5a704c122b3dd54; csrftoken=t7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x7a6137df2610>, 'wsgi.errors': <colorama.ansitowin32.StreamWrapper object at 0x7a618835ee90>, 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False, 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A'}, 'method': 'POST', 'content_type': 'application/json', 'content_params': {}, '_stream': <_io.BytesIO object at 0x7a6137425850>, '_read_started': True, 'resolver_match': ResolverMatch(func=contract.pricebooks.api.pricebook_product_request_create_view.PricebookProductRequestCreateView, args=(), kwargs={}, url_name='create_product_request_view', app_names=[], namespaces=[], route='contract_new/api/v1/pricebooks/drafts/create_request/'), 'prometheus_before_middleware_event': 48167.927812528, '_cors_enabled': False, 'user': <SimpleLazyObject: RemoteUser(id=447, first_name=Elchin, last_name=Bayramli Supplier, email=elchinb+supplier@dmpservice.org, is_staff=True, roles=['supplier', 'supplier_admin'], company_id=46, is_customer=False, is_supplier=True)>, 'h_user': <SimpleLazyObject: RemoteUser(id=447, first_name=Elchin, last_name=Bayramli Supplier, email=elchinb+supplier@dmpservice.org, is_staff=True, roles=['supplier', 'supplier_admin'], company_id=46, is_customer=False, is_supplier=True)>, 'COOKIES': {'marketingconsentcookie': 'true', 'SESSION': '815eee15-c073-4b16-82d1-9282e9c945cd', 'auth_token': '89550c6d70515b61040108d4b5a704c122b3dd54', 'csrftoken': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A'}, 'GET': <QueryDict: {'is_marketplace': ['false']}>, 'headers': {'Content-Length': '36', 'Content-Type': 'application/json', 'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTMzNzI5OTIsInVzZXIiOnsiaWQiOjQ0NywibmFtZSI6IkVsY2hpbiBCYXlyYW1saSBTdXBwbGllciIsImZpcnN0X25hbWUiOiJFbGNoaW4iLCJsYXN0X25hbWUiOiJCYXlyYW1saSBTdXBwbGllciIsImVtYWlsIjoiZWxjaGluYitzdXBwbGllckBkbXBzZXJ2aWNlLm9yZyIsImlzX3N0YWZmIjp0cnVlLCJyb2xlcyI6WyJzdXBwbGllciIsInN1cHBsaWVyX2FkbWluIl0sImlzX2N1c3RvbWVyIjpmYWxzZSwiaXNfc3VwcGxpZXIiOnRydWUsImNvbXBhbnlfaWQiOjQ2fX0.sEQ8Hdv7yEg1xWF6EDif_mA0o4Dy3XIQBrk3eubUkA1rL5tOvD6UCUYc-e5eTXLFhv1U1_g6y2NHuQm85lQGv8PHk0m56Uo2cX6E4rYMHW8KbExZVS7NEMBecEl9zUf6l3MDc-nddQVchhYUA8ChlQ61awWM2Ba9T25H2e8UjoBusx6wt0BD79RRrgBgiUStgQLcpQ0rHesPIQoWyWgUGvbpClCh2Suqn5wfylIumc38HRK1rU-yNLkjM0KC73bepdoKhTA0Q8qGda8gGwRfU1Rb2m4kpEFf-xFapSsAe7QkucSo-5MHzwJ9-4L86KvWVRrvLrN24pSWwB6Xa9qsw3SJNXcpFL-n0YjDliKNq_lIXm3OCxn1JIaCafQCaC8ZeNAJYKvPhmx2bSveY5uWhZWGiFiuLpx1h7XYxAdBEb1RNzeWUn3W8rcRvVTXdtOcXI8_MCwfR0oIhksOBPwPe-uYrt_lBkfA5nQ7STsb7ZM1p1stjuXAcv5USDzDox9LCgEaOkIhTo3hcgNYGU2p0HD0DhhoCnF13jLJ5Q5Mqcy7pmyArX71jZHi3FpkIq6fCe7jzYs8tlb_jnewn3jCm0LJY2HqpqMqLC9A_4kK-HzPvqtXqN0q29FKtwH8i3gogP5Xey5pt1a3QVuZJHiGhwIInDdMoV-9I-G303e6aks', 'Connection': 'upgrade', 'Host': 'contract', 'Sec-Ch-Ua-Platform': '"Linux"', 'X-Csrftoken': 't7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36', 'Accept': 'application/json, text/plain, */*', 'Sec-Ch-Ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"', 'Sec-Ch-Ua-Mobile': '?0', 'Origin': 'http://localhost', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Dest': 'empty', 'Referer': 'http://localhost/app/contract/pricebooks/17/drafts', 'Accept-Encoding': 'gzip, deflate, br, zstd', 'Accept-Language': 'en-US,en;q=0.9', 'Cookie': 'marketingconsentcookie=true; SESSION=815eee15-c073-4b16-82d1-9282e9c945cd; auth_token=89550c6d70515b61040108d4b5a704c122b3dd54; csrftoken=t7epemcaNYK8wjiPWlzfNkK8pyVkt53qmiUxl0JuPKGr6mDXdcDhHlggrLgR5f3A'}, '_post': <QueryDict: {}>, '_files': <MultiValueDict: {}>, 'session': <django.contrib.sessions.backends.db.SessionStore object at 0x7a6137df09d0>, 'silk_is_intercepted': True, '_body': b'{"draft_ids":[21],"pricebook_id":17}', 'auth': None} 
