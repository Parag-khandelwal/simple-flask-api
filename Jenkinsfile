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
                    
                    bat 'docker run -d -p 5000:5000 --name flask-api flask-api'
                }
            }
        }
        stage('Stop and Remove Docker Container'){
            steps{
                script{
                    bat '''
                    docker stop flask-api || exit 0
                    docker rm flask-api || exit 0
                    '''
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
