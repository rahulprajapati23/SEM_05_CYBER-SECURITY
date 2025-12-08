# ISIM Part 1

## Steps
- 1.     Create 2 IBM SDS instances
- 2.     Import the sample data using LDIF.
- 3.     Configure Master – Master replication within IBM Security Directory Servers.
- 1.      Operating System – CentOS 7.7 installed on a VMware Workstation VM.
- 2.      IBM Security Directory Server – version 6.4.0.20 x64 Linux.  IBM Security Directory Server 6.4.0.20
- 2. DB2  - /opt/ibm/db2/V11.1/
- 3. WAS - /opt/IBM/WebSphere/AppServer/
- 1.    Open     Terminal      from   Desktop       and navigate to the SDS folder as below
- 2.    Create two new users            idsldap1      and    idsldap2      as the owner of two new instances using :
- 3.    Similarly, add the second user              idsldap2
- 4.    Create the instance for the idsldap1 user using                     idsicrt    command as below :
- 5.   Similarly, create the instance for the       idsldap2    user using idsicrt command as below :
- 6.    Now you can check the instance details using the below command in terminal and check the new
- 7.    Once the instances are created we will configure the DB2 database for the SDS instance, the DB2
- 8.    Similarly, configure database for the second instance idsldap2 with below command
- 9.    Minimize the           Terminal         window,        Double-click           the    Home       icon from        Desktop         . Click    Other Locations               in
- 10.   Double-click            idsldap1 directory and you can see                              idsslapd-idsldap1                folder which have all instance
- 11.   Minimize          the   Files     window and go back to                     Terminal        window. Create admin user (                       cn=root       ) who can
- 12.   Similarly, for        idsldap2         instance create the admin user cn=root as below:
- 13.   Close      Terminal        .
- 1.     Open     Terminal        from Desktop.
- 2.     Start    the newly created SDS instance                      idsldap1        using below command:
- 3.     Similary, start the         idsldap2        instance using :
- 4.     To  stop     the instance idsldap1 enter the below command :
- 5.     Similarly, to      stop     the idsldap2 instance enter below command:
- 6.     Start    both the instances again :
- 1.     Open the Firefox browser from the task bar and enter the below URL or Click the                                                   Web Admin Tool
- 2.     Click on     Login to Console admin                    . Enter the credentials as               superadmin           using the password              secret     .
- 3.     Click on     Manage Console Servers.
- 4.      Click on         Add.
- 5.      Click on         Add.
- 6.      Click on         Logout           in the left pane and then on next screen press on                                                   here.
- 7.      Now we will get the LDAP Server Name. Select idsldap1 and enter the credential cn=                                                                                         root/P@ssw0rd
- 8.      Click      Manage Entries                    in the Content Management Section . There are few default entries created by
- 9.      Press        Logout          in Left Pane and login with                            idsldap2           with Userid             cn=root/P@ssw0rd
- 10.   Click    Manage Entrie           s as above steps and similar data will be shown as idsldap1.
- 1.    To add the suffix         stop     both the SDS instances. Open                    terminal      and enter command:
- 2.    Since we will be loading data into the directory servers, it is necessary to                                     add    the   base suffix        into the
- 3.    Start the IBM SDS instances using below commands:
- 4.    Now that the suffix information has been added, and the directory server instances have been started
- 5.    In the    terminal      enter below command for                  idsldap1      ,
- 6.     Similarly, for idsldap2 add the o=jke entry as organization, we use 2389 port to imply the idsldap2
- 7.     Minimize        Terminal        . Open       Firefox        and click       Web Admin Tool Bookmark                            . Login to        idsldap       using
- 8.     Click    Manage Entries                from Content Management section on Homepage. You can see the
- 9.     Login to       idsldap2         using       cn=root/P@ssw0rd                    and you can see similar entries in idsldap2 instance.
- 10.    Logout       . Close      Firefox       .
- 1.     We will import user data into the organization                               “o=jke”        using LDIF file. Open                Terminal       . Navigate to
- 2.     Create the file          User1.ldif       in this folder. Use           gedit    to open
- 3.     Copy or type the below ldif entries into the file:
- 4.     Save     the file and       Close     .
- 5.     In the terminal enter the idsldapadd command as below for idsldap1 :
- 6.     Verify if the users are added into the                           idsldap1         instance of SDS using WAT. Open                              Firefox     . Click     Web
- 7.     Login to       idsldap1         using      cn=root/P@ssw0rd.
- 8.     Click     Manage Entries                in Content Management section. Click the plus (+) sign near o=jke and you can
- 9.     You can         click     cn=joe and see some extra details. Click                                 Cancel       and then Close. Click                   Logout        in left
- 10.    Open the           Terminal        window and repeat the above step of                                  idsldap2         using the port             2389     . Enter the
- 11.    Similar output window will be shown, now open                                       Firefox       and login to          idsldap2         into (Web Admin Tool)
- 12.    We will import user data into the organization “o=jke”  using LDIF file. Open Terminal. Navigate to
- 13.    Create the file            User2.ldif        in this folder. Use            gedit      to open
- 14.    Copy or type the below ldif entries into the file:
- 15.     Open        LDAP          Browser            by double-click on LDAP Browser of                                        Desktop           .
- 16.     To add new connection of idsldap1 instance Click                                                    New       .
- 17.     Enter name :               IDSLDAP1               . Click the          Connection                tab.
- 18.     Enter the details as below

## Fields and Values
| Field | Value |
|---|---|
| Host | localhost |
| Port | 1389 |
| Version | 3 |
| Base DN (Click Fetch DN) | o=jke |
| Anonymous Bind | Uncheck |
| User DN | cn=root |
| Password | P@ssw0rd |
| 19. | Click |
| 20. | Click |
| 21. | Browse |
| Page | 18 |
| 22. | Click |
| 23. | You can see users |
| 24. | Repeat similar steps for IDSLDAP2. From |
| 25. | Menu bar→ File → Connect |
| 26. | Create connection for IDSLDAP2. Click |
| 27. | Enter name : |
| 28. | Enter the details as below |
| Host | localhost |
| Port | 2389 |
| Version | 3 |
| Base DN (Click Fetch DN) | o=jke |
| Anonymous Bind | Uncheck |
| User DN | cn=root |
| Password | P@ssw0rd |
| Page | 19 |
| 29. | Click |
| 30. | You will be able to see the entries in the |
| 31. | Close |
| 1.6 | Exercise 6 – Replication |
| 1. | Open |
| 2. | Login to LDAPServer |
| Note | : |
| open. In that case, clear the browser cache. | (Ctr+Shift+Del) Clear Data |
| 3. | Select |
| 4. | Click the |
| a. Select | o=jke |
| b. Check to ensure | ldap://localhost:1389 |
| 5. | Click the |
| 6. | In |
| a. | Select |
| b. Click the | Show Credentials |
| Page | 20 |
| 7. | Click the |
| 8. | Add the credential information |
| Credential Name – | cn=replicamanager |
| Authentication method – | Simple bind |
| 9. | Click the |
| 10. | Enter the Simple Bind information |
| Bind DN – | cn=replicamanager,o=jke |
| Bind password – | P@ssw0rd |
| Confirm password – | P@ssw0rd |
| 11. | Click the |
| 12. | On next screen click the |
| 13. | Now that the credentials are configured for the |
| topology | . |
| 14. | Under |
| 15. | With the |
| 16. | From the “Topology for the selected subtree” section, click on |
| Page | 21 |
| 17. | Click the |
| 18. | On the Add master screen enter the following information: |
| Server Hostname:port – Select | localhost:2389 |
| Enable SSL – | leave unchecked |
| Peer Master – | leave blank |
| Server ID – | click the Get server ID button |
| Description – | leave blank |
| 19. | Credential Object |
| 20. | In the Select Credential screen, select the |
| Credentials | button, |
| replicamanager | credential displayed, click the |
| 21. | Click the |
| 22. | The Add Replica – Additional screen allows the administrator to add further details about the replica |
| performance. | On this screen, the only change that will be made for this lab is to add the |
| 23. | Select the |
| Consumer admin DN – | cn=root |
| Consumer admin password – | P@ssw0rd |
| Page | 22  of  119 |
| 24. | Click the |
| 25. | Select O=JKE |
| 26. | Select the |
| Consumer admin DN – | cn=root |
| Consumer admin password – | P@ssw0rd |
| 27. | Following image shows the operation : |
| 28. | Click |
| Page | 23 |
| 29. | You will get the following message |
| 30. | Click |
| Note | : |
| 31. | In Replication Management go to |
| Radio | button |
| 32. | Click |
| 33. | The replication is now started from |
| 34. | Click |
| Note | : |
| IDSLDAP2 server. We just need to | start the queue |
| 35. | Login to |
| 36. | In Replication Management go to |
| 37. | The queue is in supended state, select the |
| 38. | Click |
| 39. | Replication from IDSLDAP2 to IDSLDAP1 is |
| 40. | Logout |
| 41. | In this we will check if replication works fine for modifications. n the SDS Web Administration Tool, |
| Login to | idsldap1 |
| 42. | Select |
| 43. | Select user |
| 44. | Modify the sn attribute to some new value , say “walter” to “ |
| Page | 24 |
| 45. | Logout |
| 46. | Login using |
| 47. | Select |
| 48. | Select user |
| 49. | Now you can see sn as |
| 50. | Press |
| Note | : |
| that we created previously. Also try to create the replication between the subtree | CN=IBMPOLICIES |
| Page | 25 |

