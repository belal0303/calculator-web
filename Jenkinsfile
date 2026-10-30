pipeline {
    agent any

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
                sh 'curl --retry 10 --retry-connrefused --retry-delay 2 -fsS http://localhost:5000/'
                echo 'Application deployed successfully!'
            }
        }
    }
}
