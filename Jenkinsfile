pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = credentials('dockerhubid')
        DOCKER_IMAGE_NAME = 'anshoo/simple_crud'
        GIT_REPO_URL = 'https://github.com/anshoomishra/simple_crud.git'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'your-github-credentials-id', url: GIT_REPO_URL
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE_NAME}:${BUILD_NUMBER}")
                }
            }
        }

        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKER_CREDENTIALS_ID_PSW | docker login -u $DOCKER_CREDENTIALS_ID_USR --password-stdin'
            }
        }
        stage('push image') {
            steps{
                sh 'docker push $DOCKER_IMAGE_NAME:$BUILD_NUMBER'
            }
        }
    }
}
