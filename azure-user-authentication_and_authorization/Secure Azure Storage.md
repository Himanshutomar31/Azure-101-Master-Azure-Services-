Securing Azure Storage:

1. Management Plane: RBAC(Role-based access control)
   -> Security principal: Securing principal is somebody or something you want to grant access to.
   Example: User, group of users can also be security principals, service principal, or a managed identity.
   at the end of the day security principals is like a user/passwords but it is intended to work like an
   automated headless process that can run behind the scenes.
   -> Role Definition: It defines what a certain set of permision is. when we are assigning a role we can futher limit the actions using scopes.
   -> Scopes: Management group, subscriptions, resource group, resource

   Role Assignment: Attach role definitions to a security principal on a scope.
   Example: Sahil(security principal) is attached "Storage account contributor(role definition)"
   to "storage account sahilstorage123"(scope)

   Multiple role assignments are additive
   Deny assignments can block access

2. Data Plane:
   -> Keys: when you provision a new storage account, azure will generate two 512-bit storage account access keys. These are basically long strings
   that an application can use to access azure storage.
   In some cases you do need to take some steps to protect access to these access keys because they are equivalent to root passwords to your
   storage account.Infact you should not be embedding these keys directly in your applications that you distribute to all your clients.
   plus, you should have the ability to rotate keys. you can do that manually, or you can use Key Vault to do that automatically.
   and you should prefer to use products like shared access signature or Azure AD for authentication.
   -> Shared Access Signature: Shared access signature is basically like a least-privilege mechanism when compared to Azure Sttorage Keys.
   but they allow you to trim things down and allow you to access something without sharing access keys. and you can still
   rotate the storage key to invalidate these shared access signature.
   There are 3 types of SAS: 1. User delegation SAS 2. Service SAS 3. Account SAS
   another way to categories SAS is ad-hoc and service SAS with stored access policy.
   -> Azure AD: Azure Active Directory is a premier part of the Microsoft Identity platform. and when you access azure storage using Azure AD, you can
   access it using openID connect mechanisms. Here you use access token, the duration of which is customizable, but its one hour by default.
   Storage account access key: on creation of storage account we are going to get two keys. They reason they give you two is if you want to rotate
   one, you can use the other one for continuity purposes. These are root-level access we shouldn't be using them
   directly.
   Microsoft recommends Key Vault to manage access to ur keys, and then you should regularly rotate and
   regenerate your keys.
