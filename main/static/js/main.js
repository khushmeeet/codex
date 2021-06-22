function new_note(id) {
    let note_hyperlink = document.getElementById(id)
    window.location.href = note_hyperlink.getAttribute('data-link');
}