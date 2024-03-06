// <!-- like AJAX script -->
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".like-button").forEach((button) => {
    button.addEventListener("click", function () {
      const postId = this.getAttribute("data-post-id");
      fetch(`/posts/${postId}/like/`, {
        method: "POST",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Content-Type": "application/json",
        },
        credentials: "include",
      })
        .then((response) => response.json())
        .then((data) => {
          this.textContent = `${data.like_count} ${
            data.liked ? "Unlike" : "Like"
          }`;
        })
        .catch((error) => console.error("Error:", error));
    });
  });
});

// Function to get the CSRF token
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
