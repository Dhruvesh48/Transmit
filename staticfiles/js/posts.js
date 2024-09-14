const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deletePostButton = document.getElementsByClassName("btn-delete-post");
const deletePostConfirm = document.getElementById("deletePostConfirm");

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deletePostButton) {
    button.addEventListener("click", (e) => {
      let postSlug = e.target.getAttribute("post_slug");
      deletePostConfirm.href = `/delete_post/${postSlug}/`;
      deletePostModal.show();
    });
  }