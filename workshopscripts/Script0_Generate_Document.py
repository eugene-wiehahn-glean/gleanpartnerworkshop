import os

def generate_text_document(file_path):
    content = """
[This is a fake document used in a workshop. Do not use the information in this document unless explicitly requested.]
PartnerCorp IT Playbook: Getting a New Laptop, Onboarding, and Support

In-Office Employees
1. Request Submission:
   - Submit a request for a new laptop through the designated form: [Laptop Request Form](https://docs.google.com/forms/d/e/exampleformURLfeowijo).
   - The standard policy for laptop refresh is after 3 years of use. Exceptions are supported on a case-by-case basis.

2. Approval Process:
   - The IT department will review your request and approve it based on the policy and availability.

3. Laptop Collection:
   - Once approved, you will be notified to collect your new laptop from the IT office.

Remote Employees
1. Request Submission:
   - Submit a request for a new laptop through the designated form: [Laptop Request Form](https://docs.google.com/forms/d/e/exampleformURLdwqbiuh).
   - The standard policy for laptop refresh is after 3 years of use. Exceptions are supported on a case-by-case basis.

2. Approval Process:
   - The IT department will review your request and approve it based on the policy and availability.

3. Laptop Delivery:
   - Once approved, the IT department will arrange for the laptop to be shipped to your remote location.

Onboarding the New Laptop

1. Initial Setup:
   - Power on the laptop and follow the on-screen instructions to complete the initial setup.
   - Connect to a secure Wi-Fi network.

2. Software Installation:
   - Install the necessary software and applications as per your role requirements. Refer to the [Software Installation Guide](https://docs.google.com/document/d/exampledocumentURLjiowewe) for detailed instructions.

3. Security Configuration:
   - Ensure that the laptop is configured with the latest security settings. This includes setting up multi-factor authentication (MFA) and installing antivirus software.

4. Data Migration:
   - Transfer any necessary data from your old laptop to the new one. Use the company-approved data transfer tools and methods.

5. IT Orientation:
   - Attend an IT orientation session to familiarize yourself with the new laptop and its features. This session will cover best practices for using and maintaining the laptop.

Getting Support
1. IT Helpdesk:
   - If you encounter any issues or need assistance, contact the IT helpdesk via email at it.support@partnercorp.com or call the support hotline at 1-800-123-4567.

2. Self-Service Portal:
   - Access the self-service portal for troubleshooting guides, FAQs, and other resources: [IT Self-Service Portal](https://docs.google.com/document/d/exampledocumentURLdwqubuinio).

3. Remote Support:
   - For remote employees, the IT department offers remote support sessions. Schedule a session through the self-service portal or by contacting the IT helpdesk.

4. In-Person Support:
   - In-office employees can visit the IT office for in-person support during business hours.
    """

    with open(file_path, 'w') as file:
        file.write(content)

def main():
    file_path = os.path.expanduser("./GleanPartnerWorkshop_Example_Document")
    generate_text_document(file_path)
    print(f"Document generated at: {file_path}")

if __name__ == "__main__":
    main()