#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:34:42 2018

@author: carol
"""

from __future__ import print_function

import re
import unidecode

from datetime import datetime
from requests import exceptions as requests_errors

import sys

from googleapiclient import sample_tools
from google.auth.exceptions import RefreshError
from google.oauth2.credentials import Credentials
from social_django.utils import load_strategy

from django.shortcuts import redirect

from .constants import ACCESORIES, SKINCARE, NAILPOLISH, MAKEUP, PARFUM
from .constants import GENERIC_LIST, ACCESORIES_LIST, SKINCARE_LIST, \
    NAILPOLISH_LIST, MAKEUP_LIST, PARFUM_LIST, PROJECTPAN_LIST


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')

    try:

        # users = service.users()

        # Retrieve this user's profile information
        # thisuser = users.get(userId='self').execute()

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()

        posts = service.posts()

        # List the posts for each blog this user has
        for blog in thisusersblogs['items']:
                print('The posts for %s:' % blog['name'])
                request = posts.list(blogId=blog['id'])
                while request is not None:
                    posts_doc = request.execute()
                    if 'items' in posts_doc and not (
                            posts_doc['items'] is None):
                        for post in posts_doc['items']:
                            print('  %s (%s)' % (post['title'], post['url']))
                            request = posts.list_next(request, posts_doc)

    except RefreshError:
        print('The credentials have been revoked or expired, please re-run \
              the application to re-authorize')


if __name__ == '__main__':
    main(sys.argv)


class Credentials(Credentials):
    """Google auth credentials using python social auth under the hood"""

    def _parse_expiry(self, data):
        """
        Parses the expiry field from a data into a datetime.

        Args:
             data (Mapping): extra_data from UserSocialAuth model
        Returns:
             datetime: The expiration
        """
        return datetime.fromtimestamp(data['auth_time'] + data['expires'])

    def __init__(self, usa):
        """
        Args:
            usa (UserSocialAuth): UserSocialAuth google-oauth2 object
        """
        backend = usa.get_backend_instance(load_strategy())
        data = usa.extra_data
        token = data['access_token']
        refresh_token = data['refresh_token']
        # refresh_token = None
        token_uri = backend.refresh_token_url()
        client_id, client_secret = backend.get_key_and_secret()
        scopes = backend.get_scope()
        # id_token is not provided with GoogleOAuth2 backend
        super().__init__(
                token,
                refresh_token=refresh_token,
                id_token=None,
                token_uri=token_uri,
                client_id=client_id,
                client_secret=client_secret,
                scopes=scopes
                )
        self.usa = usa
        # Needed for self.expired() check
        self.expiry = self._parse_expiry(data)

    def refresh(self, request):
        """Refreshes the access token.

        Args:
            request (google.auth.transport.Request): The object used to make
                HTTP requests.

        Raises:
            google.auth.exceptions.RefreshError: If the credentials could
                not be refreshed.
        """
        usa = self.usa
        try:
            usa.refresh_token(load_strategy())
        except requests_errors.HTTPError as e:
            raise RefreshError(e)
        data = usa.extra_data
        self.token = data['access_token']
        self._refresh_token = data['refresh_token']
        self.expiry = self._parse_expiry(data)


def get_user_profile(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')
    try:
        users = service.users()
        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()
        return thisuser
    except RefreshError:
        print('The credentials have been revoked or expired, please re-run \
              the application to re-authorize')


def get_user_blogs(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')
    try:
        # Retrieve the list of Blogs this user has write privileges on
        blogs = service.blogs()
        thisusersblogs = blogs.listByUser(userId='self').execute()
        return thisusersblogs
    except RefreshError:
        print('The credentials have been revoked or expired, please re-run \
              the application to re-authorize')


def get_blog_id(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')
    try:
        # Retrieve the list of Blogs this user has write privileges on
        blogs = service.blogs()
        blog_id = blogs.getByUrl('https://bordeauxnouvelle.blogspot.com')
        return blog_id
    except RefreshError:
        print('The credentials have been revoked or expired, please re-run \
              the application to re-authorize')


def get_blog_posts(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')

    try:
        posts = service.posts()
        request = posts.list(blogId=get_blog_id(argv))
        while request is not None:
            posts_doc = request.execute()
            if 'items' in posts_doc and not (
                    posts_doc['items'] is None):
                for post in posts_doc['items']:
                    print('  %s (%s)' % (post['title'], post['url']))
                    request = posts.list_next(request, posts_doc)

    except RefreshError:
        print('The credentials have been revoked or expired, please re-run \
              the application to re-authorize')


def generate_hashtags(product):
    brand = ' #' + unidecode.unidecode(re.sub("[' ]", "", product.brand.lower()))
    category = ' #' + product.category
    if product.category in ACCESORIES:
        words = ' #'.join(ACCESORIES_LIST)
    elif product.category in SKINCARE:
        words = ' #'.join(SKINCARE_LIST)
    elif product.category in NAILPOLISH:
        words = ' #'.join(NAILPOLISH_LIST)
    elif product.category in MAKEUP:
        words = ' #' + ' #'.join(MAKEUP_LIST)
    elif product.category in PARFUM:
        words = ' #'.join(PARFUM_LIST)
    else:
        words = ''
    hashtags_list = brand + category + GENERIC_LIST + words
    product.status = 1
    product.save()
    return hashtags_list


def redirect_if_no_refresh_token(backend, response, social, *args, **kwargs):
    if backend.name == 'google-oauth2' and social and \
       response.get('refresh_token') is None and \
       social.extra_data.get('refresh_token') is None:
        return redirect('/login/google-oauth2?approval_prompt=force')




