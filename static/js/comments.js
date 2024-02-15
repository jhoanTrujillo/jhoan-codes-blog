// Turned code provide by Code Institute into JS clas
// made several edits, for modal functionality
class CommentsEditor {
  constructor(modalSelector) {
    this.editButtons = document.getElementsByClassName("edit-button") || {};
    this.commentText = document.getElementById("id_body");
    this.commentForm = document.getElementById("commentForm");
    this.submitButton = document.getElementById("submitButton");
    this.modal = document.querySelector(modalSelector);
    this.modalToggleButtons = document.querySelectorAll('[data-toggle-modal]');

    // Method trigger
    this.targetEditButtons();
    this.deleteWarning();
  }

  targetEditButtons() {
    for (let button of this.editButtons) {
      button.addEventListener("click", (e) => {
        this.editComment(e);
      });
    }
  }

  // Handles the click of a edit button
  editComment(e) {
    let commentId = e.target.getAttribute("comment_id");
    let commentContent = document.getElementById(`comment${commentId}`).innerText;
    this.commentText.value = commentContent;
    this.submitButton.innerText = "Update";
    this.commentForm.setAttribute("action", `edit_comment/${commentId}`);
  }

  deleteWarning() {
    // Open or close modal when clicking on modal open buttons
    this.modalToggleButtons.forEach(button => {
      button.addEventListener('click', (e) => {
        const button = e.target;
        this.deleteButtonSetup(button);
        this.toggleModal();
      });
    });
  }
  
  deleteButtonSetup(deleteButton) {
    // Passes the comment ID to the modal delete button
    const commentId = deleteButton.dataset.commentId;
    if (commentId !== "") {
      const deleteConfirmButton = document.querySelector("[data-inherit-id]");
      deleteConfirmButton.href = `delete_comment/${commentId}`;
    }
  }

  closeModal() {
    this.modal.classList.remove('is-active');
  }

  toggleModal() {
    this.modal.classList.toggle('is-active');
  }
}

const commentEditor = new CommentsEditor(".modal");