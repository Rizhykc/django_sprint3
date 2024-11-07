# Blogicum


WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
----------------------- Проверка flake8 пройдена -----------------------

============================= test session starts ==============================
platform linux -- Python 3.9.16, pytest-7.1.3, pluggy-0.13.1 -- /usr/local/bin/python
django: settings: blogicum.settings (from env)
rootdir: /app, configfile: pytest.ini, testpaths: tests/
plugins: django-4.5.2, Faker-12.0.1
collecting ... collected 82 items

tests/test_category_page_views.py::test_category_page ERROR              [  1%]
tests/test_category_page_views.py::test_category_page_check_context_keys[title] ERROR [  2%]
tests/test_category_page_views.py::test_category_page_check_context_keys[key1] ERROR [  3%]
tests/test_category_page_views.py::test_category_page_check_context_keys[key2] ERROR [  4%]
tests/test_category_page_views.py::test_category_page_check_context_keys[key3] ERROR [  6%]
tests/test_category_page_views.py::test_category_page_category_unpublished ERROR [  7%]
tests/test_category_page_views.py::test_category_page_posts_unpublished ERROR [  8%]
tests/test_category_page_views.py::test_category_page_pub_date_later_today ERROR [  9%]
tests/test_category_page_views.py::test_category_page_posts_with_location ERROR [ 10%]
tests/test_category_page_views.py::test_category_page_posts_with_unpublished_locations ERROR [ 12%]
tests/test_category_page_views.py::test_many_posts_on_category_page ERROR [ 13%]
tests/test_category_page_views.py::test_no_other_posts_on_category_page ERROR [ 14%]
tests/test_pageapp_views.py::test_pageapp_views[about] FAILED            [ 15%]
tests/test_pageapp_views.py::test_pageapp_views[rules] FAILED            [ 17%]
tests/test_post_detail_views.py::test_posts_page_pk_published_location ERROR [ 18%]
tests/test_post_detail_views.py::test_posts_page_pk_unpublished_location ERROR [ 19%]
tests/test_post_detail_views.py::test_posts_page_pk_post_doesnt_exists FAILED [ 20%]
tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[title] ERROR [ 21%]
tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[text] ERROR [ 23%]
tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key2] ERROR [ 24%]
tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key3] ERROR [ 25%]
tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key4] ERROR [ 26%]
tests/test_post_detail_views.py::test_posts_page_pk_unpublished_post FAILED [ 28%]
tests/test_post_detail_views.py::test_posts_page_pk_pub_date_later_today FAILED [ 29%]
tests/test_post_detail_views.py::test_posts_page_pk_category_unpublished FAILED [ 30%]
tests/test_post_detail_views.py::test_posts_page_pk_post_with_published_location_and_category ERROR [ 31%]

tests/test_posts_page_views.py::test_all_unpublished ERROR               [ 45%]
tests/test_posts_page_views.py::test_mixed_published ERROR               [ 46%]
tests/test_posts_page_views.py::test_check_context_keys[title] ERROR     [ 47%]
tests/test_posts_page_views.py::test_check_context_keys[key1] ERROR      [ 48%]
tests/test_posts_page_views.py::test_check_context_keys[key2] ERROR      [ 50%]
tests/test_posts_page_views.py::test_check_context_keys[key3] ERROR      [ 51%]
tests/test_posts_page_views.py::test_category_unpublished ERROR          [ 52%]
tests/test_posts_page_views.py::test_pub_date_later_today ERROR          [ 53%]
tests/test_posts_page_views.py::test_posts_with_published_location ERROR [ 54%]
tests/test_posts_page_views.py::test_posts_with_unpublished_locations ERROR [ 56%]
tests/test_posts_page_views.py::test_many_posts_on_main_page ERROR       [ 57%]


==================================== ERRORS ====================================
_____________________ ERROR at setup of test_category_page _____________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stdout setup -----------------------------
Operations to perform:
  Synchronize unmigrated apps: blog, debug_toolbar, messages, pages, staticfiles
  Apply all migrations: admin, auth, contenttypes, sessions
Synchronizing apps without migrations:
  Creating tables...
    Creating table blog_category
    Creating table blog_location
    Creating table blog_post
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
---------------------------- Captured stderr setup -----------------------------
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_category_page_check_context_keys[title] ________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_category_page_check_context_keys[key1] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_category_page_check_context_keys[key2] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_category_page_check_context_keys[key3] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
__________ ERROR at setup of test_category_page_category_unpublished ___________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
____________ ERROR at setup of test_category_page_posts_unpublished ____________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
__________ ERROR at setup of test_category_page_pub_date_later_today ___________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
___________ ERROR at setup of test_category_page_posts_with_location ___________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
____ ERROR at setup of test_category_page_posts_with_unpublished_locations _____
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
______________ ERROR at setup of test_many_posts_on_category_page ______________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
____________ ERROR at setup of test_no_other_posts_on_category_page ____________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что страница категории существует и отображается в соответствии с заданием в случае, если категория существует и опубликована.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /category/None/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
___________ ERROR at setup of test_posts_page_pk_published_location ____________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
__________ ERROR at setup of test_posts_page_pk_unpublished_location ___________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/2/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/2/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_posts_page_pk_check_context_keys[title] ________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_posts_page_pk_check_context_keys[text] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_posts_page_pk_check_context_keys[key2] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_posts_page_pk_check_context_keys[key3] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________ ERROR at setup of test_posts_page_pk_check_context_keys[key4] _________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_ ERROR at setup of test_posts_page_pk_post_with_published_location_and_category _
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что страница публикации существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /posts/1/
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
____________________ ERROR at setup of test_all_unpublished ____________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
____________________ ERROR at setup of test_mixed_published ____________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_______________ ERROR at setup of test_check_context_keys[title] _______________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_______________ ERROR at setup of test_check_context_keys[key1] ________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_______________ ERROR at setup of test_check_context_keys[key2] ________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_______________ ERROR at setup of test_check_context_keys[key3] ________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_________________ ERROR at setup of test_category_unpublished __________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_________________ ERROR at setup of test_pub_date_later_today __________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
_____________ ERROR at setup of test_posts_with_published_location _____________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
___________ ERROR at setup of test_posts_with_unpublished_locations ____________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
________________ ERROR at setup of test_many_posts_on_main_page ________________
E   FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'

During handling of the above exception, another exception occurred:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.

The above exception was the direct cause of the following exception:
E   AssertionError: Убедитесь, что главная страница существует и отображается в соответствии с заданием.
---------------------------- Captured stderr setup -----------------------------
Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
------------------------------ Captured log setup ------------------------------
ERROR    django.request:log.py:224 Internal Server Error: /
Traceback (most recent call last):
  File "/usr/local/lib/python3.9/site-packages/django/core/handlers/exception.py", line 47, in inner
    response = get_response(request)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/middleware.py", line 92, in __call__
    panel.generate_stats(request, response)
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 128, in generate_stats
    "staticfiles_finders": self.get_staticfiles_finders(),
  File "/usr/local/lib/python3.9/site-packages/debug_toolbar/panels/staticfiles.py", line 140, in get_staticfiles_finders
    for path, finder_storage in finder.list([]):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/finders.py", line 130, in list
    for path in utils.get_files(storage, ignore_patterns):
  File "/usr/local/lib/python3.9/site-packages/django/contrib/staticfiles/utils.py", line 23, in get_files
    directories, files = storage.listdir(location)
  File "/usr/local/lib/python3.9/site-packages/django/core/files/storage.py", line 330, in listdir
    for entry in os.scandir(path):
FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
=================================== FAILURES ===================================
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
/usr/local/lib/python3.9/site-packages/django/core/files/storage.py:330: FileNotFoundError: [Errno 2] No such file or directory: '/app/blogicum/static'
=========================== short test summary info ============================
ERROR tests/test_category_page_views.py::test_category_page - AssertionError:...
ERROR tests/test_category_page_views.py::test_category_page_check_context_keys[title]
ERROR tests/test_category_page_views.py::test_category_page_check_context_keys[key1]
ERROR tests/test_category_page_views.py::test_category_page_check_context_keys[key2]
ERROR tests/test_category_page_views.py::test_category_page_check_context_keys[key3]
ERROR tests/test_category_page_views.py::test_category_page_category_unpublished
ERROR tests/test_category_page_views.py::test_category_page_posts_unpublished
ERROR tests/test_category_page_views.py::test_category_page_pub_date_later_today
ERROR tests/test_category_page_views.py::test_category_page_posts_with_location
ERROR tests/test_category_page_views.py::test_category_page_posts_with_unpublished_locations
ERROR tests/test_category_page_views.py::test_many_posts_on_category_page - A...
ERROR tests/test_category_page_views.py::test_no_other_posts_on_category_page
ERROR tests/test_post_detail_views.py::test_posts_page_pk_published_location
ERROR tests/test_post_detail_views.py::test_posts_page_pk_unpublished_location
ERROR tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[title]
ERROR tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[text]
ERROR tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key2]
ERROR tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key3]
ERROR tests/test_post_detail_views.py::test_posts_page_pk_check_context_keys[key4]
ERROR tests/test_post_detail_views.py::test_posts_page_pk_post_with_published_location_and_category
ERROR tests/test_posts_page_views.py::test_all_unpublished - AssertionError: ...
ERROR tests/test_posts_page_views.py::test_mixed_published - AssertionError: ...
ERROR tests/test_posts_page_views.py::test_check_context_keys[title] - Assert...
ERROR tests/test_posts_page_views.py::test_check_context_keys[key1] - Asserti...
ERROR tests/test_posts_page_views.py::test_check_context_keys[key2] - Asserti...
ERROR tests/test_posts_page_views.py::test_check_context_keys[key3] - Asserti...
ERROR tests/test_posts_page_views.py::test_category_unpublished - AssertionEr...
ERROR tests/test_posts_page_views.py::test_pub_date_later_today - AssertionEr...
ERROR tests/test_posts_page_views.py::test_posts_with_published_location - As...
ERROR tests/test_posts_page_views.py::test_posts_with_unpublished_locations
ERROR tests/test_posts_page_views.py::test_many_posts_on_main_page - Assertio...
============= 6 failed, 45 passed, 44 warnings, 31 errors in 3.76s =============