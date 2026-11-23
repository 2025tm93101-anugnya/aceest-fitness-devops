pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "anugnya2711/aceest-fitness"
        APP_VERSION = "1.0.${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${APP_VERSION} -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Run Pytest Inside Container') {
            steps {
                sh "docker run --rm ${DOCKER_IMAGE}:${APP_VERSION} pytest"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}:${APP_VERSION}"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }
}
