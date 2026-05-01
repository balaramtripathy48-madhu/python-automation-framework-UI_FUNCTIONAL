pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/balaramtripathy48-madhu/python-automation-framework-UI_FUNCTIONAL.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t pytest-image .'
            }
        }

        stage('Test') {
            steps {
                sh 'docker run --rm pytest-image'
            }
        }
    }
}