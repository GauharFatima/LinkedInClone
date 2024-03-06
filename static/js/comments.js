document.addEventListener('DOMContentLoaded', function () {
    // Toggle comment section
    document.querySelectorAll('.comment-toggle').forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            const commentSection = document.getElementById(`comment-submission-${postId}`);
            commentSection.style.display = commentSection.style.display === 'none' ? 'block' : 'none';
        });
    });

    // Submit comments
    document.querySelectorAll('.comment-form').forEach(form => {
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            const postId = this.getAttribute('data-post-id');
            const formData = new FormData(this);

            fetch(`/posts/${postId}/submit_comment/`, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('Comment posted successfully');
                    this.querySelector('textarea').value = ''; // Clear the textarea
                    // Optionally, append the new comment to the comments section
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    // loading previous comments 
    document.querySelectorAll('.load-comments').forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            const commentsSection = document.getElementById(`comments-display-${postId}`);
            // Assuming you start with page 1; you might need to keep track of the current page
            fetch(`/posts/${postId}/get_comments/?page=1`, {
                method: "GET",
                credentials: "include"
            })
            .then(response => response.json())
            .then(data => {
                data.comments.forEach(comment => {
                    const commentElement = document.createElement('div');
                    commentElement.classList.add('comment');
                    // Adjust how you create the comment element based on your comment data structure
                    commentElement.innerHTML = `<strong>${comment.profile__user__first_name}:</strong><p>${comment.content}</p>`;
                    commentsSection.appendChild(commentElement);
                });
                if (!data.has_next) {
                    button.remove(); // Remove the "Load Comments" button if there are no more comments to load
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    // Function to get the CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

// Placeholder for loading more comments
// You will need to implement the AJAX call to fetch and append more comments
