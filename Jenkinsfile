pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'url_of_your_github_repo'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Test Script') {
            steps {
                browserstack(credentialsId: "jenkins_credential_id") {
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