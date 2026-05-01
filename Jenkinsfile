pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/balaramtripathy48-madhu/python-automation-framework-UI_FUNCTIONAL.git'
            }
        }

        stage('Install Python') {
            steps {
                sh '''
                apt update
                apt install -y python3 python3-pip
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
}