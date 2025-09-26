pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        withPythonEnv('python3.8') { // Use pyenv to activate a specific version
                        sh 'pip install -r requirements.txt'
                        sh 'python my_script.py'
                    }
      }
    }
  }
}
