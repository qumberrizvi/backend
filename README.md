# backend
The backend google cloud project. It includes the backend apart from the main website


1. artist_bid: Inserts Artist Bid form's data into Firestore. Triggered by Integromat.

2. artist_signup: Inserts Artist Signup form's data into Firestore. Triggered by Integromat.

3. Pipebot: Allocated the deals in round-robin to deal owners. Also sends a welcome SMS and email to the client after verifying the email address and slack notification to the deal owner and #starbot1. Triggered by Pipedrive.

4. pyr_firestore: Inserts PYR form's data into Firestore. Triggered by PYR get-quote.js .

5. reopen_deal: Reopens the Pipedrive deal. Triggered by the client from the email. (currently not in production)
