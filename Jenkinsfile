pipeline {
    agent any

    stages {
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