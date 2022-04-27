import json

from behave import *
import requests

basic_application_url = {}
response_variable = {}
post_data = {}
patch_data = {}


@given(u'Set basic url "{base_url}"')
def basic_url(context, base_url):
    basic_application_url['base_url'] = base_url


@given(u'GET url with "{end_point}" end point')
def add_endpoint(context, end_point):
    basic_application_url['get_all_users'] = end_point


@when(u'make get request to url')
def make_getRequest(context):
    get_url = basic_application_url['base_url']
    get_url += basic_application_url['get_all_users']
    response_variable['all_users'] = requests.get(get_url)


@when(u'check status code')
def check_status(context):
    actual_status_code = response_variable['all_users'].status_code
    if actual_status_code == 200:
        users_data = response_variable['all_users'].json()
        print(json.dumps(users_data, indent=4))
        print("Data fetched Successfully")
    elif actual_status_code == 201:
        print(json.dumps(response_variable['all_users'].json(), indent=4))
        print("Data created Successfully")
    elif actual_status_code == 204:
        print("Data updated Successfully")
    else:
        print("Something went Wrong")


@given(u'basic user details as "{key}" and "{value}"')
def user_details(context, key, value):
    for row in context.table:
        temp_value = row['value']
        post_data[row['key']] = temp_value


@given(u'POST url with "{end_point}" end point')
def add_endpoint(context, end_point):
    basic_application_url['post_user'] = end_point


@when(u'make post request to url')
def make_postRequest(context):
    post_url = basic_application_url['base_url']
    post_url += basic_application_url['post_user']
    response_variable['all_users'] = requests.post(post_url, data=post_data)


@given(u'PATCH url with "{end_point}" end point')
def patch_endpoint(context, end_point):
    basic_application_url['patch_user'] = end_point


@when(u'modify body with title "{title}" and body "{body}"')
def modify_data(context, title, body):
    patch_data['title'] = title
    patch_data['body'] = body


@when(u'make patch request to url')
def make_patchRequest(context):
    patch_url = basic_application_url['base_url']
    patch_url += basic_application_url['patch_user']
    response_variable['all_users'] = requests.patch(patch_url, patch_data)


@given(u'DELETE url with "{end_point}" end point')
def delete_endpoint(context, end_point):
    basic_application_url['delete_user'] = end_point


@when(u'make delete request to url')
def make_deleteRequest(context):
    delete_url = basic_application_url['base_url']
    delete_url += basic_application_url['delete_user']
    response_variable['all_users'] = requests.delete(delete_url)

