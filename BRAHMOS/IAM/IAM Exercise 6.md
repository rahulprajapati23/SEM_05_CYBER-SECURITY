# IAM Exercise 6

## Steps
- 1.      Log in to the IBM Security Identity Manager Administrative Console as the system administrator with
- 2.      On the Home tab, navigate to                               Manage Services.
- 3.      Click      Create        .
- 4.      Wait for the list of services to appear. Ensure that Business unit is set to                                                                 JK Enterprises.
- 5.       Select        POSIX Linux profile                       and click         Next      .
- 6.      Use the information in the following table to complete the Create a Service form (Keep other settings

## Fields and Values
| Field | Value |
|---|---|
| Service name | Linux Service |
| Description | Linux Service on ISIM |
| Tivoli Directory Integrator location | rmi://isim.test:1099/ITDIDispatcher |
| Managed resource location | isim.test |
| Owner | Bob Smith |
| Service Prerequisite | [Leave blank] |
| Use Shadow File (Additional | Checked |
| Command used to query failed logins | pam_tally2 |
| Administrator name (Authentication | root |
| Page | 57 |
| Is Sudo User? (Authentication Section) | Checked |
| Password(Authentication Section) | P@ssw0rd |
| Configure Policy(Section) | Yes, create a policy for manually requesting account |
| Perform a supporting data | [Leave cleared] |
| Hint | : |
| section of the | Create Service |
| Integrator Adapter service is | running |
| 7. | Click |
| 8. | Verify that the Linux Service was added. |
| Page | 58 |
| 6.2 | Exercise 2 – Creating an identity policy |
| 1. | On the |
| 2. | Create |
| Name | Linux Identity Policy |
| Description | Identity Policy for Linux Service |
| Status | Enabled |
| User type | Person |
| Make policy available to | This business unit and its subunits |
| Business unit | JK Enterprises |
| Targets  (Section) | Click |
| 3. | In the Rule section, select the first attribute to be |
| 6 | and set Apply case to |
| 4. | Click |
| Hint | :  After creating a rule in |
| 5. | Click |
| Page | 59 |
| 6.3 | Exercise 3 – Creating a password policy |
| least | four |
| 1. | On the |
| 2. | Create a new password policy with the following information. |
| Name | Linux Password Policy |
| Description | Password policy for Linux Service |
| Business unit | JK Enterprises |
| Make policy available to | This business unit and its subunits |
| Status | Enabled |
| Targets (Section) | Click |
| Rules (Section) | Minimum length |
| 3. | Click |
| 6.4 | Exercise 4 – Running a reconciliation on Linux |
| 1. | On the |
| 2. | Click |
| 3. | A reconciliation schedule is automatically created by the |
| Reconciliation | Schedule |
| 4. | Modify the schedule for this reconciliation to run |
| 5. | Click |
| Page | 60  of  119 |
| 1. | Return to |
| 2. | Click the small |
| when prompted, and | submit |
| 3. | View the |
| 4. | Close |
| 1. | Return to |
| 2. | Click the small |
| 3. | Click |
| 4. | Close |
| 6.5 | Exercise 5 – Creating a system person |
| 1. | On the |
| 2. | Click |
| User | Data |
| Linux System-Accounts | Last Name: |
| Full Name: | Linux System-Accounts |
| Preferred user ID: | linuxsystemaccounts |
| First Name: | Linux |
| Password: | P@ssw0rd |
| 6.6 | Exercise 6 – Adopting accounts manually |
| 1. | Return to the |
| 2. | Click the small |
| 3. | Refresh |
| Assign nobody to the | Linux System-Accounts |
| Page | 61 |
| 4. | Refresh |
| Close | Manage Accounts Tab. |
| 6.7 | Exercise 7 – Adopting accounts automatically |
| 1. | On the |
| 2. | Create |
| Name | Linux Service Adoption Policy |
| Description | Adoption policy for Linux Service |
| Services (Section) | Linux Service (Change Service type to : |
| service type, | Click |
| Rule (Section) | Providing a script |
| Note: | There are system-defined JavaScript objects that you use in adoption rules. For more information, |
| refer to the on-line help. In this example, you are using the | searchByFilter |
| object. | The syntax is: |
| where | scope=1 |
| 3. | Click |
| Page | 62  of  119 |
| 4. | Return to the |
| click | Reconcile |
| 5. | Verify that the status of the reconciliation is |
| 6. | Return to the |
| click | Accounts |
| and | ntp |
| Note: | If you click one of these accounts to view the attributes, you might see the following warning |
| This error is occurring because | /sbin/nologin |
| form. You can safely | ignore |
| 6.8 | Exercise 8 – Creating an LDAP service |
| 1. | On the |
| 2. | Click |
| 3. | Wait for the list of services to appear. Ensure that Business unit is set to |
| 4. | Select |
| Page | 63 |
| 5. | Create a new service of type LDAP Profile with the information in the following table: |
| Service name | TechSupport LDAP |
| Description | TechSupport LDAP Service for ISIM |
| Tivoli Directory Integrator location | rmi://isim.test:1099/ITDIDispatcher |
| Directory Server Location | ldap://isim.test:389 |
| Administrator name | cn=root |
| Password | P@ssw0rd |
| Directory server name | IBM Directory Server |
| Owner | Bob Smith |
| 6. | Click |
| 7. | If the connection is |
| 8. | Complete the form the information in the below table : |
| User base DN | ou=TechSuppEmployees,dc=contractors |
| User RDN Attribute | UID |
| Group base DN | ou=TechSuppEmployees,dc=contractors |
| Group RDN attribute | CN |
| 9. | Keep other values as default and Click |
| Select | Yes, create a policy to automatically create accounts, and later enable the policy |
| Click | Finish |
| 10. | Return to |
| 11. | Click the small arrow to the right of |
| a query. | Submit |
| 12. | View the status of the reconciliation request. |
| Page | 64 |
| 13. | Return to Manage Services. Click the small arrow to the right of |
| Accounts | . |
| 14. | Click |
| 15. | The red X icon in the State column indicates that the account is not permitted. Click the red X for |
| allows the account on the service. Recall that when you created the | TechSupport |
| indicated you would | enable the provisioning policy later. |
| 16. | Close |
| Page | 65 |

