pipeline {
    agent any

    stages {
        stage('Pull Code') {
            steps {
                git 'https://github.com/Parag-khandelwal/simple-flask-api.git'  
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t flask-api .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    bat 'docker stop flask-api || true'
                    bat 'docker rm flask-api || true'
                    
                    bat 'docker run -d -p 5000:5000 --name flask-api flask-api'
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
