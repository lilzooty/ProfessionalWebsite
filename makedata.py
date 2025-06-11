import django
from website.models import Project
from django.contrib.auth.models import User



def initialize_data():
    
    User.objects.create_superuser(username="nicholaskroop", email="nickkroop@gmail.com", password="12345",
                                  first_name="Nick", last_name="Kroop",)

    Project.objects.create(title="QT Simon Game", thumbnail=None, exeDownload=None, githubLink=None, description=
                           """
                           <p></p>
                           """)
    Project.objects.create(title="Circuitect", thumbnail=None, exeDownload=None, githubLink=None, description=
                           """
                           <p></p>
                           """)
    Project.objects.create(title="PrimordialGPT", thumbnail=None, exeDownload=None, githubLink=None, description=
                           """
                           <p></p>
                           """)
    Project.objects.create(title="Lights Out Game", thumbnail=None, exeDownload=None, githubLink=None, description=
                           """
                           <p></p>
                           """)
    Project.object.create(title="ProfessionalWebsite", thumbnail=None, exeDownload=None, githubLink=None, description=
                          """
                          <p></p>
                          """)
    Project.object.create(title="Lt. Glip Glop's World Tour", thumbnail=None, exeDownload=None, githubLink=None, description=
                          """
                          <p>You are a lone alien commando who has flown far from his home tasked with one purpose: To weaken the United States of Earth as preparation 
                          for the Crustacean Empire's invasion. Pilot a top of the line starfighter and let loose on human civilization! Featuring 6DOF movement,
                          Model Destruction Physics, in an Open World Sandbox environment.</p>
                          """ )






def check_has_data():
    return Project.objects.all().count() or User.objects.all.count()




if __name__ == "__main__":
    if check_has_data():
        print(
        """It looks you've already run the makedata.py script.
        If you've changed the model and want to rerun the script, run:
        
        python3 manage.py makemigrations
        rm db.sqlite3
        python3 manage.py migrate
        python3 makedata.py
        """)
        exit(1)
    initialize_data()

