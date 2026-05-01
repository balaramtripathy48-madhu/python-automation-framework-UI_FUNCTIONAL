pipeline {
    agent any

    environment {
        IMAGE_NAME = "pytest-image"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/balaramtripathy48-madhu/python-automation-framework-UI_FUNCTIONAL.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                sh '''
                docker run --rm \
                -v $(pwd):/app \
                -w /app \
                -e PYTHONPATH=/app \
                selenium/standalone-firefox \
                pytest -v
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed"
        }
        success {
            echo "Tests Passed ✅"
        }
        failure {
            echo "Tests Failed ❌"
        }
    }
}