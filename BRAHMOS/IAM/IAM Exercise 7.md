# IAM Exercise 7

## Steps
- 1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with
- 2.      In the      Home         tab, go to         Manage           Users        .
- 3.      Edit the        Alice      Smyth          entry.
- 4.      In the      Personal           Information              tab    , add the         JKE System Admin                        organizational              role    .
- 5.      Click      Submit         Now       . Click     Close.
- 6.      Repeat steps 1-5 for                    Douglas           Adams           and     Edwin         Abbott        .
- 7.      Add user          Linux System-Accounts                              to role      System Accounts Owner.
- 1.      On the         Home         tab, you go to              Manage Policies > Manage Provisioning Policies.
- 2.      Click      Refresh         . Click the policy named                        Default Provisioning Policy for service Linux Service.
- 3.      Modify the provisioning policy to match the following information:

## Fields and Values
| Field | Value |
|---|---|
| Policy name | Admin Linux Accounts |
| Policy Status | Enable |
| Priority | 100 |
| Members (Section) | Select : |
| Add organizational role | JKE System Admin |
| Entitlements (Section) | Select check box for |
| Provisioning options: | Automatic |
| Target type: | Specific Service |
| Service Name: | Linux Service |
| Workflow: | [Leave blank, click clear button if populated] |
| Entitlement parameters(Section) | Select check box for |
| click | Create |
| Select | UNIX shell |
| Enforcement type | default |
| Change UNIX shell value to | /bin/bash |
| 4. | Click |
| policy. Click | Continue |
| 5. | Click the |
| enforcement action is set to | Mark |
| Manager regarding these violations. If you set the enforcement action to | Correct |
| Page | 67 |
| 6. | Close |
| 7.3 | Exercise 3 – Verifying account provisioning |
| 1. | On the |
| 2. | Click |
| 3. | Click the link under the column |
| Clicking the plus sign (+) and you can see | 4  new |
| 4. | In a terminal window, view |
| of  /bin/bash | : |
| 7.4 | Exercise 4 – Verifying the password policy |
| 1. | On the |
| 2. | Click |
| 3. | Click the small |
| Page | 68 |
| 4. | Enter a password of |
| Linux Service | because the password is too short. |
| 5. | Read the error message on the screen. |
| 6. | Click the small triangle to the left of |
| length for a password is four characters. Click | Cancel. |
| 7.5 | Exercise 5 – Creating a provisioning policy for the JKE managers role |
| 1. | On the |
| 2. | Click |
| 3. | Create |
| Note | :  This provisioning policy takes precedence over Admin Linux Accounts because it has a |
| Policy name | Manager Linux Accounts |
| Policy Status | Enable |
| Priority | 50 |
| Members (Section) | Select : |
| Add organizational role | JKE Managers |
| Entitlements (Section) | Select |
| Provisioning options: | Automatic |
| Target type: | Specific Service |
| Service Name: | Linux Service |
| Workflow: | [Leave blank, click clear button if populated] |
| Entitlement parameters(Section) | Select check box for |
| click | Create |
| Select | UNIX shell |
| Enforcement type | mandatory |
| Change UNIX shell value to | /bin/ksh |
| Page | 69 |
| 4. | Preview |
| 5. | Close |
| 6. | Submit |
| 7.6 | Exercise 6 – Verifying that the manager policy takes priority |
| 1. | On the |
| 2. | Click the small triangle to the right of |
| 3. | Click |
| 4. | Click the non-compliant warning icon in the |
| 5. | The warning should indicate that the shell is not compliant. |
| Recall that you left the policy enforcement setting on the Linux Service service at the default of | Mark |
| not | Correct |
| 6. | Click |
| Page | 70 |
| 7.7 | Exercise 7 – Creating a provisioning policy for system accounts |
| use ownership type | system |
| 1. | On the |
| 2. | Create |
| Policy name | System Linux Accounts |
| Policy Status | Enable |
| Priority | 10000 |
| Business unit | JK Enterprises |
| Members (Section) | Select : |
| Add organizational role | System Account Owner |
| Entitlements (Section) | Select |
| Provisioning options: | Manual |
| Ownership type: | System |
| Target type: | Specific Service |
| Service Name: | Linux Service |
| Workflow: | [Leave blank, click clear button if populated] |
| Entitlement parameters(Section) | [none set] |
| 3. | Click |
| 4. | On the |
| 5. | Click the small arrow to the right of |
| Now you change the account ownership for all the accounts that | Linux System-Accounts |
| assign | to user function to change the ownership type. |
| Page | 71 |
| 6. | Filter the list of accounts to show only the accounts that Linux System-Accounts owns by completing |
| 7. | Click |
| 8. | Choose the check box at the top of the select column to |
| 9. | Find and choose user |
| 10. | On the confirmation screen, click |
| 11. | Click |
| 12. | The accounts show ownership type |
| Hint | :  If you don’t see any accounts, ensure that your Search settings specify ownership type |
| 7.8 | Exercise 8 – Modifying the default join directive for an attribute |
| 1. | On the |
| 2. | Click the |
| 3. | Select |
| Page | 72  of  119 |
| 4. | Create |
| the | adm |
| 5. | Create |
| and add the | dialout |
| Note | :  You add the dialout and video groups because those groups are assigned to new users by default |
| 6. | Submit |
| 7. | Repeat steps 1 through 6 for the |
| printadmin | as a |
| secondary groups. | Do not add games. |
| 8. | Submit |
| 9. | On the |
| Page | 73 |
| 10. | On the |
| 11. | Click |
| User | Data |
| Uma Join | Last Name: |
| Full Name: | Uma Join |
| Preferred user ID: | ujoin |
| First Name: | Uma |
| Organizational Role: | JKE System Admin |
| Title: | Manager |
| E-mail address: | ujoin@ |
| Password | : P@ssw0rd |
| Note | :  Be sure to specify Uma’s first name, even though the information is optional. You create |
| 12. | Submit |
| 13. | As |
|  | printadmin |
|  | adm |
| 14. | On the Home tab, go to |
| using Java Webstart(default). Click | OK |
| Click | Run |
| 15. | Select the |
| attribute | erposixsecondgroup |
| 16. | Select Intersection as the join type |
| Page | 74 |
| 17. | Click |
| 18. | Restart |
| command | : |
| Note | :  There is an option in |
| provisioning.policy.join.overridingCacheTimeout | that controls how often the join directives are refreshed |
| 19. | On the |
| 20. | Click |
| User | Data |
| Ima Join | Last Name: |
| Full Name: | Ima Join |
| Preferred user ID: | ijoin |
| First Name: | Ima |
| Organizational Role: | JKE System Admin |
| Title: | Manager |
| E-mail address: | ijoin@jke.test |
| Password | : P@ssw0rd |
| 21. | Submit |
| 22. | As |
| groups | Ima |
|  | printadmin |
| to  union | . |
| 23. | On the Home tab, you go to |
| using Java Webstart(default). Click | OK |
| Click | Run |
| 24. | Select the |
| attribute | erposixsecondgroup |
| Page | 75 |
| 25. | Select |
| 26. | Click |
| 27. | Click |
| 28. | Restart |
| command | : |
| 7.9 | Exercise 9 – De-provisioning an account |
| 1. | On the |
| 2. | Click |
| 3. | Click the small |
| 4. | Click the small |
| Explain why the operation was | successful or not successful. |
| 7.10 | Exercise 10 – Creating a service selection policy |
| In this exercise, you create a service selection policy to provision a Linux account to users whose | last name |
| begins with the | letters M through Z. |
| 1. | On the Home tab, go to |
| 2. | Create |
| Name | Linux Service based on last name |
| Business unit | JK Enterprises |
| Make policy | This business unit and its subunits |
| Page | 76  of  119 |
| Service Type (Section) | POSIX Linux Profile |
| Service | var service = null; |
| Selection Script (Section) | var serviceArray = |
| 3. | Click |
| 7.11 | Exercise 11 – Creating a provisioning policy using the service |
| 1. | On the Home tab, go to |
| 2. | Create |
| Policy Name | M-Z Linux Accounts |
| Make policy | This business unit and its subunits |
| Priority | 1000 |
| Business unit | JK Enterprises |
| Members | All users in the organization |
| Entitlements | Click |
| Provisioning options: | Automatic |
| Target type: | Service Selection Policy |
| Service type: | POSIX Linux profile |
| Governing service selection policy name: | Linux Service based on |
| Workflow: | [Leave blank] |
| Entitlement Parameters | [none set] |
| Page | 77 |
| 3. | Preview |
| names starting with M through Z. Click | Close. |
| 4. | Submit |
| 5. | Click |
| 7.12 | Exercise 12 – Enforcing policy compliance |
| 1. | On the |
| 2. | Click the small |
| 3. | Click the |
| 4. | Click the small yellow warning icon to see the non-compliant attributes. |
| 5. | On the |
| 6. | Click the small |
| 7. | Set the enforcement action to |
| 8. | Submit |
| Page | 78 |
| Important | :  Be careful when setting enforcement to Correct because disallowed accounts will be |
| 9. | Click |
| detail to see which user’s Linux accounts are modified. | Refresh |
| Accounts | Tab to confirm all accounts are now compliant. |
| In order to prevent unintended account changes or deletions, you set the policy enforcement back to | Mark |
| 10. | Return to |
| 11. | Click the small |
| 12. | Set the enforcement action to |
| 13. | Click |
| 7.13 | Exercise 13 – Provisioning access on Linux |
| 1. | On the |
| 2. | Click the small arrow to the right of |
| 3. | Click the group name |
| 4. | On the |
| 5. | Select |
| Application | . Select a workflow of |
| 6. | Click |
| 7. | Click |
| Page | 79 |
| 8. | Open Firefox. Enter the URL - |
| 9. | Log in as user |
| 10. | Click |
| Note | : |
| 11. | Click |
| 12. | To confirm successful provisioning, open a |
| 13. | Log out |
| 14. | Click |
| John is | not a member |
| 15. | Logout |
| 7.14 | Exercise 14 – Provisioning shared folder access on TechSupport |
| 1. | Log in to the IBM Security Identity Manager Administrative Console as the system administrator with |
| the user ID | itim manager. |
| 2. | On the |
| 3. | Click the policy named |
| Page | 80 |
| 4. | Modify the provisioning policy to match the following information. |
| Policy name | Help Desk LDAP Accounts |
| Policy Status | Enable |
| Priority | 1000 |
| Members(Section) | Add organizational role |
| Entitlements(Section) | Click on |
| Provisioning options: | Manual |
| Target type: | Specific Service |
| Service Name: | TechSupport LDAP |
| Page | 81 |
| Workflow: | [Leave blank, click Clear button if populated] |
| Entitlement Parameters(Section) | Select check box for |
| Create | button. |
| Select | Group |
| Enforcement type | Allowed |
| Group value | JKENetworkShare |
| click | Create button. |
| Select | Full Name |
| Parameter type | Javascript |
| Enforcement type | Mandatory |
| Value | return subject.getProperty("cn"); |
| click | Create button. |
| Select | Last Name |
| Parameter type | Javascript |
| Enforcement type | Mandatory |
| Value | return subject.getProperty("sn"); |
| click | Create button. |
| Select | UserID |
| Parameter type | Javascript |
| Enforcement type | Mandatory |
| Value | return subject.getProperty("uid"); |
| 5. | Click |
| Click | Continue |
| Page | 82  of  119 |
| 6. | Close |
| and | refresh |
| 7. | On the |
| Service and click | Manage Groups. |
| 8. | Click the group name |
| 9. | On the |
| 10. | Select |
| access type | Shared folder. |
| In access description put | Shared Directory Access for TechSupport Employees only |
| workflow of | No Approval Required. |
| 11. | Click |
| 12. | Click |
| 13. | Close |
| In this task, you request access to the | TechSupport Shared Directory |
| 14. | Enter the URL for the Self Service console in New Firefox Window: |
| 15. | Log in as John Davis, with user ID |
| 16. | Click |
| 17. | Enter the justification – |
| TechSupport LDAP | Service. Click |
| 18. | Return to the home page using the |
| 19. | Confirm that John receives the access by reviewing |
| You can open the | LDAP Browser |
| expand | ou=TechSuppEmployees. |
| also if you click | cn |
| Page | 83 |

