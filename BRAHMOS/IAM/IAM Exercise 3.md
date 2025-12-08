# IAM Exercise 3

## Steps
- 1.       Log in to the IBM Security Identity Manager Administrative Console as the system administrator
- 2.      On the        Home         tab, you go to              Manage Organization Structure.
- 3.      Click the plus (+) sign to the left of the house icon to expand the selection. Click the small
- 4.      Complete the               Organizational Unit                      form with the following information:

## Fields and Values
| Field | Value |
|---|---|
| Organizational unit name | Sales |
| Description | Sales Organizational Unit |
| Supervisor | System Administrator |
| Page | 29 |
| Note5. | :  Click It is good practice to specify an organization supervisor. The system can notify the supervisor ofOK. You might have to refresh the Manage Organization Structure tab to see your new entry. |
| 6. | Repeat steps 3 through 5 to create the |
| Adding the locations unitsNote :  Be sure to add these entries under the | JK Enterprises entry, |
| The sales organization for JKE is divided into four regions: | WW, Americas, EMEA, and AP |
| 1. | Click the triangle to the right of |
| 2. | You complete the Location Details form with the following information. |
| Location Name | WW |
| Description | Worldwide Sales |
| Supervisor | System Administrator |
| 3. | Click |
| 4. | You repeat steps 1 through 3 for the remaining locations: |
|  | Americas |
|  | EMEA |
|  | AP |
| 1. | Click the arrow to the right of |
| 2. | Complete the Business Partner Unit form with the following information: |
| Page | 30 |
| Business partner name | TechSupport |
| Sponsor | System Administrator |
| 3. | Click |
| 3.2 | Exercise 2 – Creating users |
| 1. | On the |
| 2. | Click |
| Type | Person |
| Note | :  Title |
| section. On the password page Select | Allow me to type a password. |
| for a password, enter | P@ssw0rd. |
| User | Data |
| Sue Thomas | Last Name: |
| Full Name: | Sue |
| Page | 31 |
| Preferred user ID: | sthomas |
| First Name: | Sue |
| Title: | Manager |
| E-mail address: | sthomas@jke.test |
| Password: | P@ssw0rd |
| Bob Smith | Last Name: |
| Full Name: | Bob Smith |
| Preferred user ID: | bsmith |
| First Name: | Bob |
| Title: | [Leave blank] |
| E-mail address: | bsmith@jke.test |
| Erica Carr | Last Name: |
| Full Name: | Erica |
| Preferred user ID: | ecarr |
| First Name: | Erica |
| Title: | [Leave blank] |
| E-mail address: | ecarr@jke.test |
| John Davis | Last Name: |
| Full Name: | John |
| Preferred user ID: | jdavis |
| First Name: | John |
| Title: | [Leave blank] |
| E-mail address: | jdavis@jke.test |
| 3. | Add |
| On the | Home |
| Click | Create |
| Person | and Click |
| UserNote | :  Your previous users are added to the top of the organization chart. Make sure that you select theData |
| Finance | business unit when adding Alice. |
| Alice Smith | Last Name: |
| Full Name: | Alice Smith |
| Preferred user ID: | asmith |
| First Name: | Alice |
| Title: | [Leave blank] |
| E-mail address: | asmith@jke.test |
| When you are done, return to the | Manage Users |
| Page | 32 |
| 3.3 | Exercise 3 – Creating an Admin Domain |
| organization. To do this, you create an | Admin Domain |
| 1. | Return to the |
| 2. | Click the arrow to the right of |
| 3. | Complete the Admin Domain form with the following information: |
| Admin domain name | TechSupport Business Security |
| Description | Allows TechSupport to manage their Linux services |
| Administrator | John Davis |
| 4. | Click OK. Your organization tree should have the following hierarchical structure: |
| 3.4 | Exercise 4 – Adding a system administrator |
| you have used the | itim |
| Page | 33 |
| 1. | On the |
| 2. | Create |
| Business unit | JK Enterprises |
| Last Name | <Use your own last name> |
| Full name | <Use your own full name> |
| Preferred user ID | <First letter of first name plus last name> |
| First name | <Use your own first name> |
| Organizational roles | ITIM Administrators |
| E-mail address | <Your userid> |
| Password | P@ssw0rd |
| Note | :  For Organizational Role, Click |
| 3. | Submit |
| 4. | Now you add the new user to the System Administrator group for the ISIM system: |
| On the | Home |
| 5. | Click |
| System Administrator | group and click |
| 6. | Search |
| 7. | Submit |
| 8. | Log out |
| 9. | Log in to the IBM Security Identity Manager Administrative Console with |
| 10. | Verify that you have access to all operations. |
| Note | :  You can complete any of the administrative tasks in this course with this personal ID you |
| Page | 34 |
| 3.5 | Exercise 5 – Enabling automatic group membership |
| In the last exercise, you added your ID to the | System |
| IBM Security Identity Manager has a feature that automatically populates the | Manager |
| 1. | Log in to the IBM Security Identity Manager Administrative Console with |
| 2. | On the |
| 3. | In the Group Settings section, enable |
| 4. | Click |
| 3.6 | Exercise 6 – Navigating LDAP |
| The | basedn |
| search the entire organization, or | “ou=Sales,dc=com” |
| inetOrgPerson, use the filter | “objectclass=inetOrgPerson”. |
| returned. If you want the search to return a user’s email address, use | mail |
| 1. | Open a terminal window. |
| 2. | Change directory to |
| 3. | To find all the attributes for Bob Smith, type the following command: |
| Note | :  Some time the quote marks can give problems if copied from Windows machine to CentOS if the |
| command does not work just remove | quote marks |
| 4. | To find the email address for Sue Thomas, type the following command: |
| 5. | To find all the entries that are the children of the JKE organization, you type the following command: |
| Page | 35 |
| 6. | To find all the entries who have manager in their title, you type the following command: |
| Server. It is already installed and configured for you. LDAP Browser | simplifies viewing entries and |
| 1. | Double-click the |
| 2. | In the sessions panel of the interface, double-click |
| 3. | In the LDAP Browser panel, expand the |
| 4. | Right click |
| 5. | You set the filter to |
| 6. | The search result is the Sue Thomas entry. Right click on the result and click |
| Important | :  IBM Security Identity Manager stores data and configuration information in the sub tree under |
| ou=itim,dc=com and ou=ibm,dc=com | . You can browse these portions of the tree but |
| 1. | Open a web browser and open |
| Note | :  If Firefox gives certificate issue, Click |
| Page | 36  of  119 |
| 2. | Log in as user name |
| 1. | Click |
| 2. | Select |
| 3. | Use the following information to fill in the form: |
| Note | :  The drop-down for the below Attribute field might get delayed sometimes to open due to loading of |
| objectClass | top |
| Attribute | cn |
| Is equal to | Bob Smith |
| 4. | The completed form looks like : |
| 5. | Click |
| 6. | Select the entry and click |
| 7. | Click |
| Page | 37 |
| 1. | Select |
| 2. | Click |
| 3. | Use the following information to complete the form: |
| Attribute | objectClass |
| Comparison | Is equal to |
| Value | Person |
| Operator | AND |
| 4. | Click |
| 5. | Click |
| 6. | Use the following information to complete the form: |
| Attribute | title |
| Comparison | Is equal to |
| Value | *manager* |
| Operator | AND |
| 7. | Click |
| 8. | Click |
| 9. | View the attributes of an entry to verify that it contains a title of |
| 10. | Repeat steps 1 through 8, changing step 6 to search for title |
| 1. | Click |
| 2. | Select |
| 3. | Select |
| 4. | Select |
| 5. | Select |
| 6. | Select a role and click |
| Page | 38 |
| Note | :  For exercises that require browsing LDAP, you can use either LDAP Browser or |
| Page | 39 |

