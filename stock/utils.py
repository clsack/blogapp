#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:34:42 2018

@author: carol
"""

from __future__ import print_function

import sys

from oauth2client import client
from googleapiclient import sample_tools


def main(argv):
    # Authenticate and construct service.
    service, flags = sample_tools.init(
            argv, 'blogger', 'v3', __doc__, __file__,
            scope='https://www.googleapis.com/auth/blogger')

    try:

        users = service.users()

        # Retrieve this user's profile information
        thisuser = users.get(userId='self').execute()
        print('This user\'s display name is: %s' % thisuser['displayName'])

        blogs = service.blogs()

        # Retrieve the list of Blogs this user has write privileges on
        thisusersblogs = blogs.listByUser(userId='self').execute()
        for blog in thisusersblogs['items']:
                print('The blog named \'%s\' is at: %s' % (blog['name'],
                                                           blog['url']))

        posts = service.posts()

        # List the posts for each blog this user has
        for blog in thisusersblogs['items']:
                print('The posts for %s:' % blog['name'])
                request = posts.list(blogId=blog['id'])
                while request is not None:
                    posts_doc = request.execute()
                    if 'items' in posts_doc and not (posts_doc['items'] is None):
                        for post in posts_doc['items']:
                            print('  %s (%s)' % (post['title'], post['url']))
                            request = posts.list_next(request, posts_doc)

    except client.AccessTokenRefreshError:
        print ('The credentials have been revoked or expired, please re-run \
               the application to re-authorize')


if __name__ == '__main__':
    main(sys.argv)
