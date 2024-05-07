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
                    docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo 'Username is $dockerhubid.USR'
                script {
                    docker.withRegistry('https://hub.docker.com/', DOCKER_CREDENTIALS_ID) {
                        docker.image(DOCKER_IMAGE_NAME).push('latest')
                    }
                }
            }
        }
    }
}
