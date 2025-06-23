pipeline {
  agent any

  environment {
    XRAY_TOKEN = credentials('xray-api-token')  
  }

  stages {
    stage('Checkout') {
      steps {
        git url: 'https://github.com/marius-kengne/tavern-api-tests.git', branch: 'main'
      }
    }

    stage('Install Dependencies') {
      steps {
        sh '''
          python3 -m venv venv
          source venv/bin/activate
          pip install --upgrade pip
          pip install pytest pytest-tavern tavern 
        '''
      }
    }

    stage('Run Tavern Tests') {
      steps {
        sh '''
          source venv/bin/activate
          tavern-ci tests/quotes/*.tavern.yaml --junitxml=results.xml
        '''
      }
    }

    stage('Upload to Xray') {
      steps {
        withCredentials([string(credentialsId: 'xray-api-token', variable: 'XRAY_TOKEN')]) {
          sh '''
            curl -H "Content-Type: application/json" \
                 -H "Authorization: Bearer $XRAY_TOKEN" \
                 --data @results.xml \
                 https://eu.xray.cloud.getxray.app/api/v2/import/execution/junit?projectKey=${PROJECT_KEY} 
          '''
        }
      }
    }
  }
}
