pipeline {
    agent {
        label "debian-python3"
    }

    environment {
        GIT_CREDENTIALS = 'itops-scm-git-token'

        BASELINE_REPO = 'https://git.ellucian.com/scm/ci/monthly-openstack-report.git'
        BASELINE_BRANCH = 'master'
        BASELINE_CMD = './vm-count-in-projects.py'
        OS_AUTH_URL = 'https://iadosvip01.ece.ellucian.com:5000'
        OS_PROJECT_ID = '7b9b3c86a8ab4a6e9a1cdc8bb07ae190'
        OS_PROJECT_NAME = 'IT Admin'
        OS_USER_DOMAIN_NAME = 'Corp'
        OS_PROJECT_DOMAIN_ID = '4fbe9bec195c4f4c85dbb68d7c529088'
        OS_REGION_NAME = 'iadprod'
        OS_INTERFACE = 'public'
        OS_IDENTITY_API_VERSION = '3'

    }

    stages {
        stage('Fetch Baseline Repo') {
            steps {
                /*
                 * Get the baseline code from the git repo.
                 * This will overwrite the current working
                 * directory contents.
                 */
                git branch: "${env.BASELINE_BRANCH}",
                credentialsId: "${env.GIT_CREDENTIALS}",
                url: "${env.BASELINE_REPO}"
            }
        }

       stage('Run OpenStack Report') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'openstack-autobot-integration', usernameVariable: 'OS_USERNAME', passwordVariable: 'OS_PASSWORD')]) {
                  sh "python3 vm-count-in-projects.py > report.txt"
                }
              }
       }
       stage('Send Email') {
            steps {
                emailext (
                    subject: "Monthly OpenStack Report",
                    body: "Attached is the monthly OpenStack instance report.",
                    to: "sunil.kathait@ellucian.com",
                    attachmentsPattern: "report.txt"
                )
            }
        }
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
    }    
}
