pipeline {
  agent any

  environment {
    IMAGE = 'tasks-api'
    TAG = 'main'
    SONAR_HOST_URL = 'http://localhost:9000'
  }

  stages {
    stage('Build') {
      steps {
        withPythonEnv('/Users/xiaolinsitu/Documents/Deakin/2_Professional_Practice_In_Info_Tech/Assignments/7.3HD/venv/bin'){
                // sh('Make install')
                sh('Make build')                
                sh "docker build -t ${IMAGE}:${TAG} ."
                echo 'Building the code...'
        }         
      }
    }

    stage('Test') {
      steps {
        withPythonEnv('/Users/xiaolinsitu/Documents/Deakin/2_Professional_Practice_In_Info_Tech/Assignments/7.3HD/venv/bin'){
              sh('pip install -r requirements.txt')
              sh('pytest --junitxml=pytest-report.xml')
              junit 'pytest-report.xml'
        }
      }
    }
  }
}
