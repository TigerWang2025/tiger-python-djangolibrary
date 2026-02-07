# tiger-python-djangolibrary

第一步： 如果是直接创建的项目，没有使用 venv，则需要先创建虚拟环境venv，命令： python -m venv .venv
		此时，项目中会多一个文件夹。
		启动venv虚拟环境，windows 的启动命令： cd .\venv\Script  然后执行： .\activate
						  MacOS   的启动命令： source venv/bin/activate

第二步：安装Django，命令： pip install django
		安装完成后，可以使用命令查看安装结果： pip list
第三步：创建项目，命令： django-admin startproject {project_name}  .   # 后边加 “.”，表示在当前目录下直接创建项目，不会在多生成一层。
		会在项目目录下，创建{project_name}的目录名，包括对应的项目文件
第四步：启动项目，进入{project_name}的目录下，命令： cd {project_name}
		启动项目总配置文件，命令： python manage.py runserver
		在控制台中，可以看到启动后的访问路径： http://127.0.0.1:8000/，直接点击即可。
		可通过通过ctrl+c，退出启动应用
第五步：在退出的目录，即{project_name}目录下，创建其它应用，比如main_app，使用命令： django-admin startapp main_app
		可以看到在项目目录下，新多出一个main_app目录
		
第六步：涉及上传图片，需要使用pillow的包，须提前安装： pip install pillow



优化后台管理台页面样式，使用平台  pypi.org ，搜索  simpleui ，
具体使用：
第一步 ： 安装，命令：  pip install django-simpleui


根据Model.py 生成数据
生成数据集： python manage.py makemigrations
生成数据： python manage.py migrate

如果使用的mysql数据库，需要安装 mysqlclient，命令： pip install mysqlclient



添加管理员账户：
python manage.py createsuperuser
