pipeline {
  agent any

  environment {
    IMAGE = 'tasks-api'
    TAG = "${env.BRANCH_NAME == 'main' ? 'latest' : env.BRANCH_NAME}"
    SONAR_HOST_URL = 'http://localhost:9000'
    SONAR_TOKEN = credentials('squ_d1fac25b1450c20e973ce467fc792e6d47609e80')   // create in Jenkins
    DD_API_KEY = credentials('394fd83372d3de0a7ca5f6403a0364b5')    // create in Jenkins
  }

  stages {
    stage('Build') {
      steps {
        sh 'make build'
        sh "docker build -t ${IMAGE}:${TAG} ."
      }
    }

//     stage('Test') {
//       steps {
//         sh 'pip install -r requirements.txt'
//         sh 'pytest --junitxml=pytest-report.xml'
//         junit 'pytest-report.xml'
//       }
//     }

//     stage('Code Quality') {
//       steps {
//         sh """
//           sonar-scanner \
//             -Dsonar.projectKey=python-tasks-api \
//             -Dsonar.sources=app \
//             -Dsonar.tests=tests \
//             -Dsonar.host.url=${SONAR_HOST_URL} \
//             -Dsonar.login=${SONAR_TOKEN}
//         """
//       }
//     }

//     stage('Security') {
//       steps {
//         sh 'pip install bandit'
//         sh 'bandit -r app -f json -o bandit-report.json || true'
//         sh 'trivy image --severity HIGH,CRITICAL --format json -o trivy-image.json ${IMAGE}:${TAG} || true'
//         archiveArtifacts artifacts: 'bandit-report.json,trivy-image.json'
//       }
//     }

//     stage('Deploy to Staging') {
//       when { not { branch 'main' } }
//       steps {
//         sh "TAG=${TAG} docker compose -f docker-compose.staging.yml up -d --build"
//       }
//     }

//     stage('Release to Production') {
//       when { branch 'main' }
//       steps {
//         sh "TAG=latest DD_API_KEY=${DD_API_KEY} docker compose -f docker-compose.prod.yml up -d --build"
//       }
//     }

//     stage('Monitoring') {
//       steps {
//         sh "curl -sf http://localhost/health || true"
//         echo 'Datadog agent is running locally with logs/APM enabled'
//       }
//     }
  }
}
