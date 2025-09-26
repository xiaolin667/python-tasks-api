pipeline {
  agent any

  stages {
    stage('Build') {
      steps {
        withPythonEnv('/Users/xiaolinsitu/Documents/Deakin/2_Professional_Practice_In_Info_Tech/Assignments/7.3HD/venv/bin'){
                sh('Make create')
                sh('Make install')
                sh('Make build')
        }
      }
    }
  }
}
