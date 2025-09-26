pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        withPythonEnv('python3.11') { // Use pyenv to activate a specific version
                        sh 'pip install -r requirements.txt'
                        sh 'Make build'
                    }
      }
    }
  }
}
