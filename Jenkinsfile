pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Lance-Fernandes/Jenkins-Pipeline-Demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Test Script') {
            steps {
                browserstack(credentialsId: "3003f1af-e7f7-470a-aa5e-65f59d19b529") {
                    sh '''
                        browserstack-sdk python3 script.py
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}