const editDraftModal = new bootstrap.Modal(document.getElementById("editDraftModal"));
const editDraftButtons = document.getElementsByClassName("btn-edit-draft");
const editDraftForm = document.getElementById("editDraftForm");
const draftTitleInput = document.getElementById("editDraftTitle");
const draftContentInput = document.getElementById("editDraftContent");

/**
 * Initializes editing functionality for the provided edit buttons.
 * 
 * For each button in the `editDraftButtons` collection:
 * - Retrieves the associated draft's data (slug, title, and content) upon click.
 * - Populates the `editDraftForm` inputs with the draft's existing values.
 * - Updates the `editDraftForm` action URL to point to the draft's specific edit endpoint (using the slug).
 * - Displays a modal (`editDraftModal`) to allow the user to edit the draft.
 */
for (let button of editDraftButtons) {
    button.addEventListener("click", (e) => {
        // Get draft details from the button's data attributes
        let draftSlug = e.target.getAttribute("draft_slug");
        let draftTitle = e.target.getAttribute("draft_title");
        let draftContent = e.target.getAttribute("draft_content");
        
        // Update form inputs with the existing draft data
        draftTitleInput.value = draftTitle;
        draftContentInput.value = draftContent;
        
        // Update the form action to point to the draft's edit endpoint using the slug
        editDraftForm.action = `/edit_draft/${draftSlug}/`;
        
        // Show the edit modal
        editDraftModal.show();
    });
}