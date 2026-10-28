
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t notes-app:v2 .'
            }
        }

        stage('Verify Image') {
            steps {
                bat 'docker image inspect notes-app:v2'
            }
        }
    }
}
