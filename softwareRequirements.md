## Software Requirements for Linkedin

### User Personas (At least 2)

#### What is Linkedin?
LinkedIn users are professionals and job seekers who utilize the platform for networking, career development, and knowledge sharing.   

**User Personas on Linkedin**
1. Knowledge Miner / Content Creator.
2. General User / Normal User.
3. The Recruiter.
4. Business Professional

### User Stories (as granular as possible)   

1. **General user** like job hunters, Quiet Listener  

   1. As a User, ISBAT login.
   2. As a User, ISBAT Sign in.
   3. As a User, ISBAT create a post.
   4. As a User, ISBAT edit my post.
   5. As a User, ISBAT delete my post.
   6. As a User, ISBAT like a post.
   7. As a User, ISBAT comment on a post.
   8. As a User, ISBAT view my profile.
   9. As a User, ISBAT edit my profile.
   10. As a User, ISBAT add eductional details.
   11. As a User, ISBAT add cerifcates.
   12. As a User, ISBAT add profile photo.
   13. As a User, ISBAT see other person profile.
   14. As a User, ISBAT search any user.  
   15. As a User, ISBAT send connection requests to another user. 
   16. As a User, ISBAT accept or reject connection requests from another user. 

   Advance implementations for Users:  

   17. As a User, ISBAT send message to other user.
   18. As a User, ISBAT block another user.
   19. As a User, ISBAT report inappropriate content.
   20. As a User, ISBAT view notifications.  
   
2. **Knowledge Miner**- someone who post eductional content
   1. As a Creator, ISBAT write longer post.
   2. As a Creator, ISBAT add video content along the text post.
   3. As a Creator, ISBAT access basic analytics to see the performance metrics of my recent posts.
   4. As a Creator, ISBAT add tags or keywords to my posts.
   5. As a Creator, ISBAT enable comments moderation on my posts.
   6. As a Creator, ISBAT pin a specific post to the top of my profile for increased visibility.
   7.  As a Creator, ISBAT receive notifications when my post reaches a certain number of likes or comments.
   
   Advance implementations for creator:   
   
   8.   As a Creator, ISBAT enable monetization features to generate revenue from my content.
   9.   As a Creator, ISBAT utilize audience engagement tools such as polls, Q&A sessions, and live broadcasts.
   10.  As a Creator, ISBAT promote my content through sponsored posts and advertising options.

### Database Design
1. User:
   - userId (primary key)
   - name
   - email
   - password
   - profile photo
   - creation data
   - last login data
   - isBlocked
   - isDeleted  

2. Post:
    - Postid (pk)
    - UserIdc(fk)
    - Content
    - PostDate
    - LikeCount
    - CommentsCount
    - isDeleted    

3. EducationalDetails:
   - EduId (pk)
   - UserID (fk)
   - Degree
   - CollegeName
   - StartDate
   - EndDate
  
4. Certificate:
   - CertId (pk)
   - userId(fk)
   - certificateName
   - IssueBy
   - IssueDate
   - ExpireDate
  
5. Connection:
   - ConnectionId (pk)
   - SenderUserId (fk)
   - ReceiverUserId (fk)
   - Status

6. Message:
    - messageId (pk)
    - senderUserId (fk)
    - receiverUserId (fk)
    - messageContent
    - sendDate