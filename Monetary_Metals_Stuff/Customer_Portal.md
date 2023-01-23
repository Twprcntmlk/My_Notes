Customer Portal Case Studies

Alice - New Customer Onboarding and Funding

Alice has heard about Monetary Metals and wants to put her capital to work. She goes to monetary-metals.com where “Open an Account” is prominently featured. She creates a login or uses her existing Apple, Amazon, or Google credentials. She is also asked to further secure her account through some secondary means (security questions, MFA, etc.). She then assents to various notices (Terms of Service, Privacy Policies, etc.). If she does not use a third party identity provider, she is required to verify her email address. She is only asked for the minimum necessary to create an online presence.

Alice is presented with her account summary page.

One section shows her balances (zero ounces of various metals). Since this is her first time logging in, based on the locale of her IP address, a conversion currency is selected for her. Her balances are also presented in terms of that conversion currency, which Alice can change and her changes will be remembered on subsequent logins.

Another section shows her positions, which shows no positions, but instead shows a sample rate she might expect to earn and a “Fund My Account” button. Yet another section shows her recent transactions, which is also empty.

“Statements and Documents” and “Deposit” links are available. “Statements and Documents” will take Alice to a separate page where she can view and download her statements or other documents. She currently has no statements, but a “Fund My Account” also appears on this page. Clicking on the “Deposit” link will take her to the same flow as clicking on any of the “Fund My Account” buttons.

Alice clicks on “Fund My Account” which allows her to enter an amount that satisfies the minimum account requirements. She can enter amounts in ounces of metal or her selected currency and a conversion will be updated as she types.

As she proceeds, she is presented with an overview of the on-boarding process, what she'll need, and how long she can expect it to take. She is prompted to verify her email address (if required and she has not yet done so), enter her residence address and sign a customer agreement covering a storage account and a yield account. She is directed to an ID verification provider who collects the requisite information.

Once complete, she is presented with wire instructions she can provide to her bank to find the account. The prominently display “Fund My Account” buttons no longer appear, but the “Deposit” link remains a standard part of the navigation.

Alternatives

Simplification: “Deposit” and “Fund My Account” go to a static page directing Alice to call MM. Onboarding and funding are performed as they are today.

Simplification: Recent transactions do not appear.

Simplification: No conversion currency.

Enhancement: List month’s, last year’s, or YTD interest could be displayed with balances.

Simplification: Skip “native” MFA for now. It will still be available via third party identification providers who offer it. We understand many of our existing customers may not wish to login via third party identification providers, especially those who have earned reputations for surveillance (e.g., Google, Facebook, Amazon, etc.).

Open Questions

Conditions under which we can delete an account? (We won’t build a mechanism to delete accounts at first, but we’ll want to signal to account holders that we retain the right to do so under certain circumstances.)

Conditions under which we can stop delivering historical documents (e.g., after ten years)?

Privacy policy

Data export functionality (i.e., GDPR, CCPA, etc.)? Do we need it? Will we soon?

Should the phone number of the customer’s RM be displayed in their account? How prominently?

Should a user be able to prohibit use of third party identity providers with an established account?

Use case: Alice uses alice-and-bob@gmail.com as her login, but wants to prohibit accessing the account via Google as a third party identity providers. She only wants to be able to access her MM account with her MM-native password.

Architectural Implications

User Registration

User Authentication w/ Logging/Auditing

Email verification

Alternative: Leverage the forgotten password flow?

“Native” MFA (i.e., implemented for our own logins and not those via a third party identification provider)

Simple (Single User) Authorization (i.e., single user has complete access)

Statement (and Other Document) Storage and Index (API)

Optional: Transaction Subsystem (API)

Optional: Integration w/ ID Verification Provider (API)

Optional: Agreement Signature Capture Mechanism (API)

Ambiguity: How will we deal with multiple identity providers mapping to the same account

Bob - Statement Notification and Download

Bob is an established depositor and expects that Monetary Metals will deliver statements of his account. After the current statement period comes to a close, a statement is generated and made available. Bob receives an email from Monetary Metals indicating that his statement is ready to be viewed or downloaded. No link appears in the email.

Bob navigates to “Statements and Documents”, which contains a list of his statements and other documents (tax documents, copies of signed agreements, notices, etc.). Each document can be downloaded as a PDF. The list can be sorted by document name, type, or date. The list can also be filtered by date range and document type.

Alternatives

Simplification: No filtering or sorting.

Architectural Implications

User Migration from Salesforce

User Authentication w/ Logging/Auditing

Simple (Single User) Authorization (i.e., single user has complete access)

Statement (and Other Document) Storage and Index (API)

Charlie - Existing Customer Establishing Login

Charlie has been a depositor for years and has enjoyed returns from many leases. He is accustomed to getting his statements via email and has a login to the MM WordPress site which he has used once or twice.

Monetary Metals creates Charlie’s login for him based on the email address we have on file in Salesforce. We migrate the information we have from Salesforce to Monetary Metals’ internal user management system and then remove as much personally identifying information as we can from Salesforce.

The next time Charlie’s statement is scheduled to be emailed to him, we instead send Charlie an email notifying him that his statement is now available via our portal. If Charlie has never logged into the portal, this email should contain instructions on how Charlie can finish provisioning his account, establish a new password, set up MFA, etc.

If Charlie has never logged into this account, and if we receive a bounce-back from one of these emails, we should reach out to him so that we can update his information.

Once established, Charlie’s experience mirrors Alices, except that he can browse all of his prior statements, tax documents, and client agreements. Charlie can see recent transactions, but a granular transaction history is not available prior to some date TBD.

Alternatives

Alternative: Migration of user data from SF to MM’s user subsystem can happen in stages over time. This should be treated with some urgency, but is not a strict requirement on delivering the customer portal. Careful attention should be paid to those systems getting out of sync. This may allow for an earlier launch with some downstream complications.

Simplification: Do not make available signed agreements in the document download section. Only statements and tax documents.

Open Questions

What specific fields can/should we migrate/delete from SF?

Do we need to be prepared to mail physical statements where we cannot establish contact with a client?

Architectural Implications

User Migration from Salesforce

Migration, storage, and access of prior documents (statements, tax documents, etc.)

Dan - Account Email Address/Password Change

Dan wants to change the email address associated with his login. He logs into his MM account and navigates to the “Account” section, where he can update his email address or password. He is asked to log in again to initiate the change. If he has changed his email address, he is required to verify it before the change can be completed. Until this happens, Dan’s login remains his prior one.

Alternatives

Alternative: Email address changes can be required to go through RMs, assuming we have a reasonable way to update the customer account.

Open Questions

What gets display in the “Account” page before the new email is verified?

Do we need to support multiple email addresses per account?

Architectural Implications

Email verification

Alternative: Leverage the forgotten password flow?

Eve and Wally - Linked Accounts

Any depositor-facing invitation/user management flow is a difficult experience to get right while remaining secure. For now, we will avoid such a feature, and instead link accounts only upon request (and verification) through an internal tool. We will have to develop safeguards to protect against social engineering.

Linking will be limited to two users per account. Once linked, actions on the account will require approval by (or at least notification to) both users.

Open Questions

What happens when the person who controls one of the accounts becomes incapacitated?

What is the experience when one user (email) is attached to two accounts? Do we provide account switching? Or do we prohibit this? (I.E., supporting the same person with two different accounts requires a distinct email address on each account? I don’t particularly like this solution.)

This may impact our customer agreement with perma-offer (i.e., assent to the agreement requires two signatures, but we permit any single user to opt out of an upcoming lease without affirmation by the second).

Not sure what the security implications are. Can one user gather sufficient information from the account to social engineer or defeat protections against granting that user exclusive controlling access? How do we prevent this?

Architectural Implications

User admin tool



Frank - Forgotten Password

Frank remembers his account email address, and can still receive messages at that address, but has forgotten his password. Alongside the login interface, there is a “Forgot password?” link that Frank can follow to trigger a password reset, which is a special link sent to the account email. The “Forgot password?” link can be shown more prominently after a failed login attempt.

Alternatives

Simplification: Don’t show the “Forgot password?” link with more prominence under certain conditions.

Open Questions

How much of this can something like Cognito handle for us?

How does this interact with MFA?

Grace - Forgotten Password with No Access to Email

Poor Grace! She has forgotten her password, and maybe even her email. Or maybe she remembers the email she used, but no longer has access to it. Either way, the traditional forgotten password flow won’t help her.

TBD

Open Questions

Invite her to call?

Should she re-perform ID verification?

Can we automate this?

How much of this can something like Cognito handle for us?

What about an executor doing asset valuation, interim management, and intestate disposition?

Architectural Implications

User admin tool



Heidi - Opt-In Lease Preferences, New Lease

Heidi receives an email notification that there is an upcoming lease opportunity. The email directs her to log in. Upon log-in, she is presented with a “stream” of upcoming lease opportunities. She can drill into each one where she can find the pitch deck, schedule a call with her RM, and sign an offer.

Alternatives

We could avoid this experience altogether and maintain the one we have currently (i.e., entirely outside the customer portal). This is in anticipation of migrating (most) customers to opt-out lease involvement. This alternative is attractive, because if we field an experience for legacy (opt-in) leases, we’ll have to continue supporting it.

Open Questions

Should we have a “notifications” interface that is omnipresent (e.g., in the banner) where a user can see details on any email received?

We’ll still need a story for a period of time when opt-in and opt-out accounts can both participate in the same leases (which is hopefully short-lived).

Architectural Implications

Signing flow from link, which is unique to account

What happens with dual-signature accounts?

Notification subsystem

Contact mechanism preferences

Ivan - Opt-Out Lease Preferences, New Lease

Ivan receives an email notification that there is an upcoming lease opportunity. The email directs him to log in. Upon log-in, he is presented with a “stream” of upcoming lease opportunities. He can drill into each one where he can find the pitch deck, schedule a call with his RM, and toggle an opt-out setting.

Ivan can also see a “stream” of past leases that have already commenced. Each can be drilled into, where he can see the pitch deck and his position (if any). The opt-in setting is no longer toggle-able, but reflects Ivan’s choice at the time the lease commenced.

Open Questions

Should a depositor be able to opt into any in-flight lease at any time in the future (just like a new account holder could do when first signing up)?

Should we have a “notifications” interface that is omnipresent (e.g., in the banner) where a user can see details on any email received?

We’ll still need a story for a period of time when opt-in and opt-out accounts can both participate in the same leases (which is hopefully short-lived).

What happens with dual-signature accounts? Two toggle buttons (each only toggle-able by a specific user)?

Architectural Implications

Preference capture and feed into the (re)balancing calculator

Lease position API

Notification subsystem

Contact mechanism preferences

Judy - Opt-Out of In-Flight Leases for New Account

Judy has just signed up with MM and has opened a yield account. There are several in-flight leases that Judy can take part in to start earning a yield right away. She is prompted to traverse them and opt out of any she doesn’t want. It should be made clear that unless she opts out, she will participate in those leases after a certain amount of time.

Alternatives

Perhaps new clients are opted out of in-flight leases by default and can opt in at their discretion.

Architectural Implications

Preference capture and feed into the allocation calculator

Mike - Legacy Account that Opts in to “Opt-in” Leases

TBD

Nancy - Transfer Metal Between Accounts

TBD

Oscar - Transfer Metal Between Entities

TBD

Peggy - Withdraw Metal 
