pipeline {
  agent any

  environment {
    IMAGE = 'tasks-api'
    TAG = 'main'
    SONAR_HOST_URL = 'http://localhost:9000'
    SONAR_TOKEN = credentials('squ_d1fac25b1450c20e973ce467fc792e6d47609e80')   // create in Jenkins
    DD_API_KEY = credentials('394fd83372d3de0a7ca5f6403a0364b5')    // create in Jenkins
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
