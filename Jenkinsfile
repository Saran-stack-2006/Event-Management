pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Saran-stack-2006/event-management.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step started'
                bat 'echo Build completed'
            }
        }

        stage('Test') {
            steps {
                echo 'Test step started'
                bat 'echo No automated tests added yet'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
