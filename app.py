from flask import Flask
from github import Github
import sys,yaml,json

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Hello from Dockerized Flask App!!"

@app.route('/v1/<fileName>')
def git_read(fileName):
    print fileName
    g = Github("madhuribharathula@gmail.com","Gp2254131")
    repoPaths = sys.argv[1].split("/")
    gitRepo = repoPaths[len(repoPaths) - 1]
    user = g.get_user()
    repo = user.get_repo(gitRepo)
    fileNameList = fileName.split(".")
    if fileNameList[len(fileNameList) -1] == "yml":
        try:
            fileYml = repo.get_file_contents(fileName)
            return yaml.dump(yaml.load(fileYml.decoded_content))
        except:
            fileYml = repo.get_file_contents(fileNameList[0]+".json")
            return yaml.dump(yaml.load(fileYml.decoded_content))
    elif fileNameList[len(fileNameList) -1] == "json":
        try:
            fileJson = repo.get_file_contents(fileName)
            return json.dumps(yaml.load(fileJson.decoded_content), sort_keys=True, indent=2)
        except:
            fileJson = repo.get_file_contents(fileNameList[0]+".yml")
            return json.dumps(yaml.load(fileJson.decoded_content),sort_keys=True, indent=2)
    else:
        return "Must provide yml or json extension"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')