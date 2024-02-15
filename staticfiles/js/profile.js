// JavaScript class to handle profile form submission
class ProfileFormHandler {
	constructor() {
		this.submitButton = document.getElementById("submitButton");
		this.profileForm = document.getElementById("ProfileForm");
		this.textArea = document.getElementById("id_bio");
		this.profileBio = document.querySelector("[data-profile-bio]").dataset.profileBio;

		this.handleSubmit();
		this.updateBioContent();
	}
	
	handleSubmit() {
		this.submitButton.addEventListener("click", (e) => {
			this.bioSubmission(e);
		});
	}

	bioSubmission(e) {
		e.preventDefault();
		const userId = this.submitButton.dataset.userId;
		const profileId = this.submitButton.dataset.profileId;
		this.profileForm.setAttribute("action", `/profile/${userId}/bio_edit/${profileId}`);
		this.profileForm.submit();
	}

	updateBioContent() {
		document.addEventListener("DOMContentLoaded", () => {
			this.textArea.innerHTML = this.profileBio;
		});
	}
}

// Initialize the profile form handler
const profileFormHandler = new ProfileFormHandler();