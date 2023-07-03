# Itheum GitHub Action to store output in a AWS S3 bucket

## Abstract

Data Providers are one of the most important stakeholders when it comes to the Data NFT ecosystem. The objective of this template is to help Play Station gamers fetch their own PSN data automatically and save their results in a "set it and forget it" way.

## Description

This project template aims to help PSN Data Providers run automated scripts that updates datasets daily under the same URL.

This is done by using a GitHub Action that runs the Data Provider's Python script periodically and uploads the output to a AWS S3 bucket.

## Pre-requisites

- A GitHub account; you can create one [here](https://github.com/signup)

- Available GitHub Actions usage minutes; in public repositories, you have unlimited minutes by default, but if you use a private repository, you have 2000 minutes for free; (if your script takes 1 minute to run, you can run it 2000 times per month; if your script takes less than 1 minute to run, the usage time will be rounded to 1 minute); if you need more minutes you can set up a custom billing plan, but if you run your scripts once a day it's hard to get there (note: GitHub action minutes are cumulative per account, so if you have multiple repositories, the minutes will be shared between them)

- An AWS account; you can create one [here](https://portal.aws.amazon.com/billing/signup#/start)

- A Play Station account

## How to use

### A. Creating an AWS S3 bucket

Note: You can jump over this step if you already have an AWS S3 bucket.

1. Go to [AWS S3](https://aws.amazon.com/) and click on "Sign in to the Console" on the top right corner of the page. If you are not logged in, you will be asked to log in with your AWS account.

2. Once logged in to the AWS Console, use the search bar to search for "S3" and click on the first result. Once on the S3 page, click on "Create bucket".

3. Select a name for your bucket and choose a preffered region for its hosting. For the "Object ownership" option choose ACLs enabled. For "Block Public Access settings for this bucket" make sure all the checkboxes are UNchecked (except for the one asking you to acknowledge that these settings might result in this bucket becoming public). You can let the other options as default. Click on "Create bucket". Note: AWS S3 is (at the time of writing this guide) offering a free tier that allows you to store up to 5GB of data for free for 12 months. If you need more storage, you can set up a custom billing plan. You can find out more about AWS Free Tier [here](https://aws.amazon.com/free/) and about AWS pricing [here](https://aws.amazon.com/s3/pricing/).

### B. Creating a GitHub repository & preparing it for usage

1. Go on GitHub and create a new repository under your desired account using this template (click on the green "Use this template" button on the top right corner of [this page](https://github.com/Itheum/auto-data-generation-action)). Select a name for your repository, decide whether you want your repository to be public or private and click on "Create repository from template". Wait a few seconds for your repository to be generated

2. Go back to your repository page on GitHub. Click on "Settings". Then, under the "Security" section, click on "Secrets and variables" and then on "Actions".

3. We will have to create three secrets that will be used inside of our GitHub Action. We are using them as secrets instead of directly in the code in order to keep these variables private from the public. Click on "New repository secret" and create the following secrets:

- Name: SC_BUCKET_NAME, Secret: the name of the AWS S3 bucket you created in the previous step (if you don't remember it, you can find it by going to your account's AWS S3 page)
- Name: SC_KEY_ID, Secret: the AWS Access Key ID of your AWS account. You can generate one by clicking on your account name on the right top corner in AWS and then clicking on security credentials. Then, go to access keys and click "Create access key". After accepting the prompt and click again on "Create access key", your key will be created. The characters under "Access key" is your key ID. You have a button that you can use to copy it. Don't close this page after that, we will also need the secret access key for the next secret.
- Name: SC_ACCESS_KEY, Secret: the Secret access key coresponding to your AWS Access Key ID. You can find it in the same page as the previous secret.

4. In your bucket's menu, go to permissions and scroll down until you see "Cross-origin resource sharing (CORS)". Click on "Edit" and paste the following text there:

```
[
    {
        "AllowedHeaders": [
            "*"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": [
            "Access-Control-Allow-Origin"
        ]
    }
]
```

### C. Getting your npsso and setting it up on GitHub

1. Login into your My PlayStation account [here](https://my.playstation.com/)

2. In another tab, go to https://ca.account.sony.com/api/v1/ssocookie

3. If you are logged in you should see a text similar to this:

```
    {"npsso":"<64 character npsso code>"}
```

Copy the 64 characters npsso code along with the " at the beginning and the end included.

4. The same way you created the three secrets above, you will create a new one:

- Name: NPSSO, Secret: the 64 character code along with the beginning " and the ending ".

### That's it! Your runs should be successful from now on. If the workflow run was successful you can now go to your AWS S3 and click on your bucket. You should be able to see your objects there. Clicking on your object will allow you to see a link that can be used to access that object (file). You can now use that link to create a Data NFT!

## Customization

You can customize by changing the update-data.yaml file inside of the .github/workflows folder. If you don't see the .github folder, make sure you enabled seeing hidden files inside your explorer. More about GitHub Actions [here](https://docs.github.com/en/actions)

Moreover, you can customize the main.py project code.

## Contributing

Feel free the contact the development team if you wish to contribute or if you have any questions. If you find any issues, please report them in the Issues sections of the repository. You can also create your own pull requests which will be analyzed by the team.
