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
                    sh 'docker build -t flask-api .'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh 'docker stop flask-api || true'
                    sh 'docker rm flask-api || true'
                    
                    sh 'docker run -d -p 5000:5000 --name flask-api flask-api'
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
