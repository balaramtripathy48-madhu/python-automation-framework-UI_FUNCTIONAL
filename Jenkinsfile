pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/balaramtripathy48-madhu/python-automation-framework-UI_FUNCTIONAL.git'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 --version || true
                pip3 install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                pytest -v
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
    }
}