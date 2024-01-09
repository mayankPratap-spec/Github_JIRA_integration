# Github_JIRA_integration

System Architecture:
1.	GitHub Repository:
•	Action Triggered:
  •	 A QA/Tester raises an issue on the GitHub repository.
2.	Developer Review:
•	Action Taken:
  •	The developer reviews the GitHub issue to determine its legitimacy.
3.	Comment for JIRA Ticket:
•	Action Taken:
  •	If the developer finds the issue genuine, they comment on the GitHub issue with "/JIRA". This action signals the intent to create a JIRA ticket.
4.	GitHub Webhook:
•	Action Triggered:
  •	GitHub Webhook is configured to trigger on new comments. It listens for comments that include "/JIRA".
5.	Flask API on EC2 Ubuntu Instance:
•	Action Triggered:
  •	The GitHub Webhook triggers a predefined Python Flask API hosted on an EC2 Ubuntu instance.
6.	Python Flask API Processing:
•	Action Taken:
  •	The Flask API receives the GitHub webhook payload and extracts relevant information, including the comment and issue details.
•	It verifies that the comment includes "/JIRA".
7.	Communication with JIRA API:
•	Action Taken:
  •	If the comment is valid ("/JIRA" present), the Python API communicates with the JIRA API to create a new ticket.
8.	JIRA Ticket Creation:
•	Action Taken:
  •	The JIRA API creates a new ticket with details provided by the GitHub issue and additional information as needed.
9.	Response to GitHub:
•	Action Taken:
  •	The Python Flask API responds to the GitHub Webhook with the result of the ticket creation process.
10.	Feedback on GitHub:
•	Action Taken:
  •	If the comment was valid and a JIRA ticket was created, relevant feedback is provided on the GitHub issue.
•	If the comment was invalid ("/JIRA" not present), a message is printed stating that the ticket will only be created if the comment includes "/JIRA".
