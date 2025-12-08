# IAM Exercise 4

## Steps
- 1.      On the        Home         tab, go to         Manage Users.
- 2.      Click     Refresh         . Locate         Alice Smith.              Click the arrow to the right of the name and click                                           Change         .
- 3.      Change the              Last name, Full name, Preferred user ID, and email address                                                                   attributes to reflect her
- 4.      Refresh          the user list to confirm the name change.
- 5.      Click the          arrow       to the right of Alice Smyth and click                                    Accounts            . Click      Refresh          . For the account on
- 1.      On the        Home         tab, you go to             Manage Users.
- 2.      Locate        Alice Smyth              . Click the arrow to the right of the name and click                                           Change          .
- 3.      Click the         Business Information tab.
- 4.      In the       Manager            field, click         Search         and locate             Sue Thomas                . Select Sue as the manager and Click
- 5.      Click      Submit Now                to update the entry. Click                       Close       .
- 1.      On the        Home          tab, go to         Manage Users.
- 2.      Search          the user list and locate the entry for                               Sue Thomas.
- 3.      Select        the Sue Thomas entry and click                                Transfer         .
- 4.      Search for the               Finance          organizational unit. Select                        Finance           and click         OK     .
- 5.      Click      Transfer         . Click      Close       .
- 6.      Return to the              Manage           Users        tab.     Refresh          the user list to verify that                    Sue      Thomas            is transferred.
- 7.      Repeat steps 1 through 6 to transfer                                      Bob       Smith        to the        WW       location           in   Sales       . Also, transfer              John
- 8.      When you are done, the user list should look like this:
- 1.      On the        Home          tab, click        Manage           Roles       .
- 2.      Click      Create         to add a new role.
- 3.      Complete the                Create         Role       form with the following information:

## Fields and Values
| Field | Value |
|---|---|
| Role Type | Static |
| Role Classification | [Leave blank] |
| Business unit | JK Enterprises |
| Role Name | JKE System Admin |
| Description | Organizational Role for System Administrators |
| Access Information | [Leave as is] |
| Assignment Attributes | [none] |
| Role Membership | Erica Carr |
| 4. | Click |
| 5. | Repeat steps 2 through 4 to create 5 more static roles |
| initially) | : |
| a) | System Account Owner |
| b) | Finance Employees |
| c) | Asset Handling |
| Check the | Enable access for this role |
| access | check box. These settings allow users to request membership in the roles as an access. |
| d) | Booking and Ledgers |
| Check the | Enable access for this role |
| access | check box. |
| e) | Comparison and Review |
| Check the | Enable access for this role |
| access | check box. |
| Page | 42 |
| 1. | Create another role, this time choose the |
| 2. | Complete the |
| Role Type | Dynamic |
| Role Classification | [Leave blank] |
| Business unit | JK Enterprises |
| Make role applicable to | This business unit and its subunits |
| Role Name | JKE Managers |
| Description | Organizational Role for JKE Managers |
| Access Information | [Leave as is] |
| Definition (Rule) | (title=*Manager*) |
| 3. | Click |
| 4. | On the |
| 5. | Click the arrow to the right of the |
| 6. | Verify that the users in this dynamic role have |
| 7. | Create another Dynamic role |
| 8. | Complete the form with the following information: |
| Page | 43 |
| Role Type | Dynamic |
| Role Classification | [Leave blank] |
| Business unit | TechSupport |
| Make role applicable to | This business unit and its subunits |
| Role Name | Help Desk |
| Description | TechSupport help desk |
| Access Information | [Leave as is] |
| Definition (Rule) | (cn=*) |
| Note | :  The role scope is relative to the position of the role in the organization tree. A dynamic role |
| 4.4 | Exercise 4 – Creating child role assignments |
| 1. | On the |
| 2. | In the |
| 3. | Click |
| 4. | Click the |
| 5. | Search |
| 6. | Select the three finance child roles: |
|  | Asset Handling and Disposition |
|  | Booking and Ledgers |
|  | Comparison and Review |
| 7. | Click |
| 8. | Select the |
| Page | 44 |
| 4.5 | Exercise 5 – Creating a separation of duty policy |
| these roles: | A  sset Handling and Disposition, |
| 1. | On the |
| 2. | Click |
| 3. | Create the policy with the following information: |
| Policy Name | ABCs of Finance |
| Description | Finance rules to maintain separation of duties |
| Business Unit | Finance |
| 4. | In the Policy Rules section, click |
| Description of separation | Finance department ABCs |
| 5. | Click |
| 6. | Search for roles in the |
|  | Asset Handling and Disposition |
|  | Booking and Ledgers |
|  | Comparison and Review |
| 7. | After you select the |
| one | role. |
| 8. | Click |
| 9. | Under |
| Sue Thomas , | select |
| Sue, as the | manager |
| 10. | Click |
| 11. | Log out |
| 4.6 | Exercise 6 – Approving a separation of duty policy violation |
| Page | 45 |
| 1. | Restart |
| https://isim.test:9443/itim/ui/Login.jsp | or click the bookmark |
| 2. | Log on as Alice Smyth ( |
| 3. | Click |
| role and Click | Next. |
| 4. | Click on |
| 5. | Click the |
| 6. | Click |
| Finance | and Click |
| 7. | Log out |
| 8. | Now, log in to the Identity Service Center as |
| exception. | Log back |
| 9. | Click on |
| 10. | Provide Justification – |
| 11. | Log out |
| Page | 46 |

