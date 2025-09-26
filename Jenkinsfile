pipeline {
  agent any

  environment {
    IMAGE = 'tasks-api'
    TAG = 'main'
  }

  stages {
    stage('Build') {
      steps {
        withPythonEnv('/Users/xiaolinsitu/Documents/Deakin/2_Professional_Practice_In_Info_Tech/Assignments/7.3HD/venv/bin'){
                // sh('Make install')
                sh('Make build')
                sh('echo $PATH')
                sh('docker version')
                // sh "docker build -t ${IMAGE}:${TAG} ."
                echo 'Building the code...'
        }         
      }
    }
  }
}
