pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/balaramtripathy48-madhu/python-automation-framework-UI_FUNCTIONAL.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t pytest-image .'
            }
        }

        stage('Test') {
            steps {
<<<<<<< HEAD
                sh '''
                docker run \
                -e PYTHONPATH=/app \
                pytest-image pytest -v
                '''
=======
                sh 'docker run pytest-image pytest -v'
>>>>>>> 4b6a25a34c554d335e6589e29bed7a278eea2108
            }
        }
    }
}
