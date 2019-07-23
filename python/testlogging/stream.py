import subprocess



recomd = subprocess.run("python D:\\Testfan\\study_notes\\testlogging\\testoutput.py",stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True,universal_newlines=True)
print(recomd.returncode)
print(recomd.stdout)
print(recomd.stderr)