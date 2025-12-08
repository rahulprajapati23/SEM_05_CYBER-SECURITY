# IAM Exercise 5

## Steps
- 1.      Log in        to the IBM Security Identity Manager Administrative Console as the system administrator with
- 2.      On the        Home         tab, navigate to                Manage Services.
- 3.      Click      Create       .
- 4.      Confirm that the                 Finance business                        unit is selected or Click                        Search          in front of Business Unit and
- 5.      Select       Comma Separated File (CSV) identity feed                                                and click         Next      .
- 6.      Complete the Create a Service form with the following information:

## Fields and Values
| Field | Value |
|---|---|
| Service name | CSV Identity Feed |
| Description | CSV Feed for finance users |
| File name | /classfiles/data/newhires_finance.csv |
| Use workflow | [Cleared] |
| Evaluate separation of duty | [Cleared] |
| Person profile name | Person |
| Name attribute | uid |
| Placement rule | return "ou=Finance"; |
| 7. | Click |
| Page | 47  of  119 |
| 8. | If the connection is |
| 9. | When you see the message that you |
| 10. | From |
| 11. | Click the |
| 12. | When you see the message that you successfully submitted a reconciliation request, click |
| my request. | The reconciliation request should be the |
| 13. | If the status of the request shows it is |
| 14. | On the |
| Finance | business unit. |
| 15. | You can also review the contents of |
| correct. Open it in | Text Editor |
| 16. | Close |
| 5.2 | Exercise 2 – Creating a Directory Services Markup Language (DSML) |
| 1. | On the |
| 2. | Click |
| 3. | Select the |
| Development | . |
| 4. | Select |
| 5. | Complete the |
| Page | 48 |
| Service name | DSML Identity Feed |
| Description | Load Dev Team through DSML Feed |
| User ID | [Leave blank] |
| Password | [Leave blank] |
| File name | /classfiles/data/development.dsml |
| Use workflow | [Cleared] |
| Evaluate separation of duty | [Cleared] |
| Placement rule | return "ou=Development"; |
| 6. | Click |
| 7. | If the connection is |
| 8. | When you see the message that you |
| 9. | From |
| 10. | Click the |
| 11. | When you see the message that you successfully submitted a reconciliation request, click |
| my request. | The reconciliation request should be the top-most request in the list. |
| 12. | If the status of the request is pending(wait for a minute), click |
| 13. | On the |
| to the | Development |
| 14. | You can also review the contents of |
| in | Text Editor |
| 15. | Close all the tabs. |
| Page | 49 |
| 5.3 | Exercise 3 – Creating an LDAP InetOrgPerson identity feed |
| ou=sales,o=PDQ. | You can use |
| Open the | LDAP Browser |
| O=PDQ then Expand ou=sales. | Confirm there are five users in the PDQ organization to import with this |
| 1. | Log in to the IBM Security Identity Manager Administrative Console as the system administrator with |
| the user ID | itim manager. |
| 2. | On the |
| 3. | Click |
| 4. | Complete the |
| Page | 50 |
| Business unit | JK Enterprises |
| Service type | INetOrgPerson identity feed |
| Service name | LDAP inetOrgPerson Identity Feed |
| Description | LDAP Identity Feed |
| URL | ldap://isim.test:389 |
| User ID | cn=root |
| Password | P@ssw0rd |
| Naming context | ou=sales,o=pdq |
| Use workflow | [Cleared] |
| Evaluate separation of duty | [Cleared] |
| Person profile name | Person |
| Name attribute | uid |
| Placement rule | return "L=AP,ou=Sales"; |
| Note | :  The placement rule uses L=AP,ou=Sales to indicate that new users are placed in the AP |
| 5. | Click |
| 6. | If the connection is successful, click |
| 7. | When you see the message that you |
| 8. | From |
| Page | 51 |
| 9. | Click the small |
| 10. | When you see the message that you successfully submitted a reconciliation request, click |
| 11. | If the initial status of the request shows that it is in the pending state, click |
| 12. | On the |
| Notice that the users are imported but marked as | inactive |
| the users inactive because they do not have a | userPasssword |
| 13. | To activate each user, |
| 14. | Close the Reconcile Now tab. |
| 5.4 | Exercise 4 – Creating a IBM Security Directory Integrator identity feed |
| 1. | Launch the IBM Security Directory Integrator editor with the following command: Open the |
| 2. | If you are prompted to select a workspace, accept the default location and click |
| 3. | Import the pre-built configuration file by clicking |
| Integrator > Configuration | and click |
| 4. | Select |
| 5. | When prompted for the |
| 6. | In the Navigator panel, expand |
| Page | 52 |
| 7. | Double-click |
| 8. | Click |
| 9. | The mapping table has three columns. The |
| source CSV file. | The |
| Security Identity Manager. The | middle |
| 10. | Close |
| 11. | Double-Click |
| Page | 53 |
| 12. | The |
| IBM Security Identity Manager. If the request is for a | reconciliation |
| line calls the | CSVtoISIM |
| assembly line are collected and then | passed back |
| 13. | Click |
| 14. | The Assembly Line is running successfully when you see a message similar to the following: |
| on port | 8800 |
| Note | : Don’t close |
| exercise | 5.5 |
| 5.5 | Exercise 5 – Creating identities with a IBM Security Directory |
| 1. | Log in to the IBM Security Identity Manager Administrative Console as the system administrator with |
| 2. | On the |
| 3. | Click |
| 4. | Confirm that the Business unit is set to |
| Next | . |
| 5. | Use the following information to complete the Create a Service form: |
| Page | 54 |
| Service name | TDI feed |
| URL | http://isim.test:8800/ |
| Naming context | dc=IDIFeed |
| Use workflow | [Cleared] |
| Evaluate separation of duty | [Cleared] |
| Name attribute | uid |
| Placement rule | var deptNum = entry.departmentnumber[0]; |
| the file | /classfiles/scripts/ IDI_placementrule.js. |
| and you can copy the JavaScript and paste the into the | Placement Rule |
| 6. | Click |
| 7. | Assuming a successful connection test, click |
| 8. | Return to the |
| 9. | Click the small arrow to the right of |
| 10. | To verify that the feed is successful, click Manage Users to confirm the identities are added to |
| 11. | Return to the IBM Security Directory Integrator editor and click the red square icon( |
| Page | 55 |
| 12. | Exit |
| Page | 56 |

