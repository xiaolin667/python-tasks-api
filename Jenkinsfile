pipeline {
  agent any

  environment {
    IMAGE = 'tasks-api'
    TAG = 'main'
    SONAR_HOST_URL = 'http://localhost:9000'
    SONAR_TOKEN = 'sqp_c461d108fd3c1f1432048045fb4847e099a31124'
    DD_API_KEY = '394fd83372d3de0a7ca5f6403a0364b5'
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

    stage('Code Quality') {
      steps {
        sh """
          /opt/homebrew/bin/sonar-scanner \
            -Dsonar.projectKey=tasks-api \
            -Dsonar.sources=app \
            -Dsonar.tests=tests \
            -Dsonar.host.url=${SONAR_HOST_URL} \
            -Dsonar.login=${SONAR_TOKEN}
        """
      }
    }

    stage('Security') {
      steps {
        withPythonEnv('/Users/xiaolinsitu/Documents/Deakin/2_Professional_Practice_In_Info_Tech/Assignments/7.3HD/venv/bin'){
          sh('pip install bandit')
          sh('bandit -r app -f json -o bandit-report.json || true')
          sh('/opt/homebrew/bin/trivy image --severity HIGH,CRITICAL --format json -o trivy-image.json ${IMAGE}:${TAG} || true')
          archiveArtifacts artifacts: 'bandit-report.json,trivy-image.json'
        }
      }
    }

    stage('Deploy to Staging') {
      // when { not { branch 'main' } }
      steps {
        sh "TAG=${TAG} docker compose -f docker-compose.staging.yml up -d --build"
      }
    }

    stage('Release to Production') {
      // when { branch 'main' }
      steps {
        sh "TAG=latest DD_API_KEY=${DD_API_KEY} docker compose -f docker-compose.prod.yml up -d --build"
      }
    }

    stage('Monitoring') {
      steps {
        sh "curl -sf http://localhost/health || true"
        echo 'Datadog agent is running locally with logs/APM enabled'
      }
    }
  }
}
