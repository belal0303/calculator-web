pipeline {
    agent any

    tools {
        sonarRunner 'SonarScanner'
    }

    stages {
        stage('GitHub Checkout') {
            steps {
                checkout scm
                echo 'Code downloaded from GitHub'
            }
        }

        stage('Python Test') {
            steps {
                sh 'python3 -m py_compile app.py'
                echo 'Python test successful'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=calculator-web \
                          -Dsonar.projectName="Calculator Web" \
                          -Dsonar.sources=. \
                          -Dsonar.exclusions=venv/**,__pycache__/**
                    '''
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t calculator-app:${BUILD_NUMBER} .'
            }
        }

        stage('Docker Deploy') {
            steps {
                sh '''
                    docker rm -f calculator-container calculator-containers || true
                    docker run -d \
                      --name calculator-container \
                      -p 5000:5000 \
                      calculator-app:${BUILD_NUMBER}
                '''
            }
        }

        stage('Application Verification') {
            steps {
                sh '''
                    curl --retry 10 \
                         --retry-all-errors \
                         --retry-delay 2 \
                         --retry-max-time 30 \
                         -fsS -o /dev/null \
                         http://localhost:5000/
                '''
                echo 'Application deployed successfully!'
            }
        }
    }
}