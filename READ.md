# QsDjangok
# Let's make a try ~

![django](https://cf-assets2.tenlong.com.tw/products/images/000/123/927/original/413uHLT33KL.jpg?1536666201)

# To Check Python Engine

(1) add Path & check default path while installing Python Engine.

(2) to see env path in system.

(3) to see GUI Dirctory in system.

(4) to check Python version in Terminal | cmd.exe

# To Build a Virtual Env

<https://developer.mozilla.org/zh-TW/docs/Learn/Server-side/Django/development_environment>

open Terminal (在微軟稱為命令提示字元)

    $ cd c:\

    $ pip3 install virtualenv

> Successfully installed appdirs-1.4.3 distlib-0.3.0 filelock-3.0.12 virtualenv-20.0.3

    $virtualenv < virtual env name >

Question1 issued

C:\>virtualenv DjangoEnv
'virtualenv' 不是內部或外部命令、可執行的程式或批次檔 (Bug!!!) ?????

Question1 solved

    $pip3 install virtualenvwrapper-win (這可以執行ㄟ 讚!!!)

next step:

    $mkvirtualenv QsEnv

????? Question2 issued ?????

> 
C:\Users\109009>mkvirtualenv QsEnv
'mkvirtualenv' 不是內部或外部命令、可執行的程式或批次檔 。

# To Install the Django

    $pip3 install django

> add this path to 'PATH'
 'C:\Users\Queen\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.7_qbz5n2kfra8p0\LocalCache\local-packages\Python37\Scripts'

????? Question3 issued ?????
>
 C:\Users\109009>django-admin QsDjango
'django-admin' 不是內部或外部命令、可執行的程式或批次檔 。

check module version

    $python3 - m django --version

    $py -3 -m django --version

>3.0.3

# To set up the Env Path

if you use Mac OS , then edit it by opening ~./.profile, and use vim

if you use Windows, then open cmd.exe(命令提示字元), cmd it in bash like 

    $echo %path%

if the PATH is not on the path, then :

<https://support.microsoft.com/zh-tw/help/2542410>

if you use windows 10, and use 中文版本, then ->

    搜索(1)系統內容，點選(2)進階設定，

    按下(3)環境變數再行修改即可。

    (4)貼上環境值時，請去掉 ' ' quote symbol。

# Vir Env CLI

    deactivate — 退出當前的Python虛擬環境

    workon — 列出可用的虛擬環境

    workon name_of_environment — 激活指定的Python虛擬環境

    rmvirtualenv name_of_environment — 刪除指定的環境

    C:\Users\Queen\Envs\Queens> there are a Project called QsPy

# To Create a Project

    $cd < root dir >

    $django-admin startproject < project name >

    $cd < project name >

    C:\Users\Queen\Envs\Queens> there are a Project called QsPy

> C:\Users\109009\AppData\Local\Programs\Python\Python38-32\python.exe: No module named QsPy.__main__; 'QsPy' is a package and cannot be directly executed

# Django Project Structure

plz open th dir called QsPy

the structure is as following -> 


        QsPy (Folder name)  ---- manage.py
                            |
                            ---- QsPy (project name as root) |
                                                            ---- __init__.py
                                                            |
                                                            ---- asgi.py
                                                            |
                                                            ---- setting.py
                                                            |
                                                            ---- urls.py
                                                            |
                                                            ---- wsgi.py

code files:

    (1) manage.py import execute_command_line from django.core.management
                build app
                start server
                prompt shell

    (2) settings.py as config files 

    (3) urls.py as config files 

    (4) __init__.py (empty)

    (5) asgi.py

    (6) wsgi.py

# Start App

    cd <project folder>

    $python manage.py startapp <app name>

# Apps Structure

        (Top Level)/(App Name)
plz open QsPy/QueenPy

              QueenPy (app name) ----- migrations dir/
                                |
                                 ----- __init__.py
                                | 
                                 ----- admin.py
                                |
                                 ----- apps.py
                                |
                                 ----- models.py
                                |
                                 ----- tests.py
                                |
                                 ----- views.py

# ------------------------------------------------------------

<h1> Config Env

# ------------------------------------------------------------

# Add Html Templates & Static Folder

     cd .., from app folder to project folder

     $md templates 
     $md static

             Top Level   
             QsPy (Folder name)  ----- manage.py
                           |
                           |     Bottom Level
                            ----- QsPy (project name as root) 
                           |
                            ----- templates (new folder)
                           |
                            ----- static (new folder)
                           |
                            ----- QueenPy (App name)

# Make Migration (建立資料庫資料檔)

    cd .., from app folder to project folder

    $python manage.py makemigrations <app name>

             Top Level   
             QsPy (Folder name)  ----- manage.py
                           |
                           |     Bottom Level
                            ----- QsPy (project name as root) 
                           |
                            ----- templates 
                           |
                            ----- static 
                           |
                           |                       After Making Migartions
                            ----- QueenPy (app) ----- migrations (new folder)
                           |  
                           |
                           |   After Making Migartions
                            ----- db.sqlite3

倘若省略 <app name> 後方的參數，則如上指令會對專案中所有 app 進行 makemigrations， 接著會在個別 app 目錄下建立 migrations 目錄。

利用 migrate 可以根據 migration records sync this module to DB.

![migrations](https://www.novatec-gmbh.de/wp-content/uploads/2017/01/flyway-migration-1.png)

# Run Django Server

    $python manage.py runserver

> Watching for file changes with StatReloader
> Performing system checks...
> System check identified no issues(0 silenced).

> <time>
> Django version 3.0.3, using settings 'QsPy.settings'
> Start developing server at http:127.0.0.1:8000/

then go to browser to surf the URL: http://127.0.0.1:8000/
will see how successful you are!

![success](https://i1.wp.com/www.artsofthepamlico.org/wp-content/uploads/2019/09/bravo-1.png?w=372&ssl=1)

# see terminal | cmd.exe while surfing the django app

>[time] "GET / Http/ 1.1" 200 16351
>[time] "GET / favicon.ico http/1.1" 404 1970

# Quick Step to Run Django Server at local side

    $cd C:\<virtual env>

    $Scripts\activate

    $cd <project> #it hereby means Uplevel Project Folder

    $python manage.py runserver

# Set Up Env of Web App

plz open QsPy/QsPy/settings.py

add value '<app name>' in below Varibale called INSTALLED_APPS

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            '<app name>'
        ]

map k/v as 'DIRS':[os.path.join(BASE_DIR, 'templates')]  in Varibal called TEMPLATES

             # BASE_DIR 為 APP 應用程式目錄代稱

        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',

                'DIRS': [  ],

                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

![config](https://media.askvg.com/articles/images7/New_About_Config_Page_Main_UI_Mozilla_Firefox.png)

# Set Up Static Folder Path 

plz open QsPy/QsPy/settings.py

static (全小寫無複數s) 目錄儲存 local 的 image, CSS, JS files

ctrl+f to serach the STATIC_URL = '/static/' this phrase,

and add code line as below:

        STATICFILES_DIRS = [

            # BASE_DIR 為 APP 應用程式目錄代稱
            os.path.join(BASE_DIR, 'static'),

        ] # to add path

# Set up Timezone & Language

plz open QsPy/QsPy/settings.py

add value to the Variable called TIME_ZONE & LANGUAGE_CODE

such as 'zh-Hant' & 'Asia/Taipei'

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

# ------------------------------------------------------------

<h1> Web App

# Design URL Path, Route to Specific Method Called

plz go into bottom level project folder as QsPy/QsPy
and cd to urls.py

using tools called django.urls.path, it plays role as Router in Web app

        from django.contrib import admin
        from django.urls import path
        #from django.conf.urls import url # it seems deprecated
        from <app name>.views import <function name>
        from QueenPy.views import qsMethodCalled

        urlpatterns = [

            path('admin/', admin.site.urls), # to route url path to the function
            
            path('url_info_path', function_name)

            
            path( '', qsMethodCalled), #to use rex to show info_path in URL
            # to remove / slash to fix this router.


        ]

# Design UI, Render UI

go to <app folder>/views.py


        from django.shortcuts import render
        from django.http import HttpResponse

        def qsMethodCalled(request):

            return HttpResponse("haha, you must like cat as me. Miao~")

# Add Html File under templates Module

to render UI, there are many steps to do it, this the modified file in stucture =>


        Top Level Project Folder (root) ----- templates --- add a html file
                                        |
                                        |
                                        ----- static (may be add some image or css)
                                        |
                                        |
                                        ----- Bottom level Project Folder --- urls.py as Router('infopath', function_name)
                                        |
                                        |
                                        ----- App Folder --- views.py - to add functions
                                        

* 1. go to Upper Level Project Folder, and open templates folder, to add on a html file.

        <!DOCTYPE html>
        <html>

        <head>
            <meta charset='utf-8'>
            <title> PoupouCat </title>
        </head>

        <body>

            ...words hereby...

        </body>

        </html>

* 2. to add varibale in {{}} double object syntax embeded in html templates.

        member name: {{user_name}}

* 3. go to app folder/views.py, in this case will be Qspy(top level project)/QueenPy(app folder)/view.py

and using shortcuts.render() method instead of HttpResponse() method

    render(req, 'html.file', locals())

the 1st param means http request in GET | POST method

the 2nd param is a templates file name in string type.

the 3rd param is callback of locals() method, to pass local variables

    locals() 

///
        from django.shortcuts import render
        from django.http import HttpResponse

        def qsMethodCalled(request, user_name):
            time_now = datetime.now()
            #return HttpResponse("haha, you must like cat as me. Miao~")

        def renderMiao(request, user_name):
            return render(request, "miao.html", locals())

* 4. go to Bottom Level Project Folder/uls.py to add router there, so url req -> go to the sepecific method called mapping in ../App Folder/views.py

* 4-1. from <app module>.views import <function_name>

* 4-2. add code line to do router

        from QueenPy.views import qsMethodCalled, renderMiao # add methods

        urlpatterns = [

            path('admin/', admin.site.urls), # to route url path to the function

            path( '', function_name), #to use rex to show info_path in URL
            # to remove / slash to fix this router.

            path('infopath/(\w+)', renderMiao)
        ]


# Add Image & CSS File under static Module

to render UI, there are many steps to do it, this the modified file structure in stucture =>


        Top Level Project Folder (root) ----- templates --- add a html file
                                        |
                                        |
                                        ----- static --- css
                                        |            --- image (add on)
                                        |            --- js
                                        |
                                        ----- Bottom level Project Folder (urls.py as Router('infopath', function_name))
                                        |
                                        |
                                        ----- App Folder --- views.py (functions add on)
                                        
* 1. route URL to function in < down_level_project > / urls.py

        from django.urls import path
        from < app_name >.views import < function_name >

        urlpatterns = [

             path(r'infopath/', function_name),

        ]

* 2. add function to render html in < app_name > / views.py

        from django.shortcuts import render
        from django.http import HttpResponse

        def function_name(request):

            return render(request, "a_file_name_.html", locals())

* 3. add variable and local path in html

        < top level project > / templates / a_file_name_.html
    
          {% load static %} # instead of staticfiles

          <img src='{% static "image_name.png" %}'>

* 4. mapping local path and indirect path in project structure

          add image_name upnder < top level project > / static

* 5. check static path in project structure, open < Top Level Project > / settings.py

        STATIC_URL = '/static/'

        #BASE_DIR 為 APP 應用程式目錄代稱
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
        ] 
