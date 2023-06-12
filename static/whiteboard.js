'use strict';

// Selectors for save button and all notes displayed on page.
const saveNotes = document.querySelector("#save-notes");
const allNotes = document.querySelectorAll("#note-forms .form-group");

saveNotes.addEventListener("click", (evt) => {
    /* Update note information in database when "Save" button is clicked. */
    evt.preventDefault();

    for (const noteForm of allNotes) {
      const noteId = noteForm.id;
      console.log(noteId);

          const formInputs = {
          id: noteId,
          title: document.querySelector(`#n-title${noteId}`).value,
          body: document.querySelector(`#n-body${noteId}`).value,
        };
        console.log(formInputs);
      
        fetch('/save-notes', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((responseJson) => {
            console.log(responseJson.status);
          });
      }
          alert("Notes Saved")    
    });
    


for (const noteForm of allNotes) {
    /* Adds share and delete functionality buttons to relevant notes.  */

    console.log(noteForm)
    const noteId = noteForm.id;
    console.log(noteId);
    const shareBtn = document.querySelector(`#share-note${noteId}`);
    const delBtn = document.querySelector(`#delete-note${noteId}`);

    console.log(shareBtn)
    console.log(delBtn)

    shareBtn.addEventListener('click', (evt) => {
      /* Connects share buttons to share-notes route. */

      evt.preventDefault();
      const userId = document.querySelector(`#shared-user${noteId}`).value;

      const formInputs = {
        id: noteId,
        user: userId
      };
      console.log(formInputs)
    
      fetch('/share-note', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then((response) => response.json())
        .then((responseJson) => {
          location.reload();
          alert(responseJson.status);
        });
    });

      delBtn.addEventListener('click', (evt) => {
        /* Connects delete buttons to delete-notes route */

        evt.preventDefault();
    
        const formInputs = {id: noteId};
        console.log(formInputs)
      
        fetch('/delete-note', {
          method: 'POST',
          body: JSON.stringify(formInputs),
          headers: {
            'Content-Type': 'application/json',
          },
        })
          .then((response) => response.json())
          .then((responseJson) => {
            location.reload();
            console.log(responseJson.status);
          });
      });
}

//Selector for shared notes displayed on page
const sharedNotes = document.querySelectorAll("#shared-notes form")

for (const sharedForm of sharedNotes) {

  const noteId = sharedForm.id;
  const removeBtn = document.querySelector(`#remove-note${noteId}`);

  removeBtn.addEventListener('click', (evt) => {
    /* Connects remove button to remove-note route */

    evt.preventDefault();
  
    const formInputs = {id: noteId};
    console.log(formInputs)
  
    fetch('/remove-note', {
      method: 'POST',
      body: JSON.stringify(formInputs),
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => response.json())
      .then((responseJson) => {
        location.reload();
        console.log(responseJson.status);
      });
  });

}
