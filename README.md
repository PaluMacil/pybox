# Pybox
Pybox is a modular CMS based on Flask with plugins and themes.

It's currently in **conceptual stages and not ready for use**. It's also important to note that I have a pretty untested setup script and won't be able to support that until I further basic functionality.

The reason for this project is my love of Python and rapidly growing interest in Flask. I find Flask to be a fantastic framework because of the light, modular nature of it, and I don't think that will ever change because that's what Flask is based around. In my opinion, that is why a lot of new developers start Python web dev here instead of Django. However, I'd like to see two primary goals fulfilled in this project.

PRIMARY GOALS:

1. Complete Technical Choices: Pybox will provide Flask with extension choices already made--user management (Flask-Login), orm (SQL Alchemy), even default plugins (in the form of blueprints) and themes (in the form of templates) distributed from Pybox.ninja (tentative--I might just use the main site) or pybox.io (also registered).

2. Modular design: First, the choices above will be minimized. Where I might start with one auth library, I might eventually be able to abstract is to two. I'd like to keep as close as possible to Flask's feel rather than Django's feel. Second, the "store" for adding plugins and themes in the admin user's web interface is important. I think the complexity of Django and lack of plugins is why Mezzanine and other Django CMS applications rock in large organizations but don't coax over the droves of Wordpress devs who would really love the beauty of Python but just can't do without the ease of a plugin/theme store and a framework they can learn from a very simple starting point.

RESOURCES:

1. Stock images from [Pexels](www.pexels.com) and [Free Favicon](www.freefavicon.com).
2. Inspiration, naming conventions, and some class structure are from [Miguel Grinberg's flasky](https://github.com/miguelgrinberg/flasky).
