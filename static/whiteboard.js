'use strict';

const saveNotes = document.querySelector("#save-notes");
const allNotes = document.querySelectorAll("#note-forms form");

saveNotes.addEventListener("click", (evt) => {
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
      }});
    


for (const noteForm of allNotes) {
    
    const noteId = noteForm.id;
    console.log(noteId);
    const shareBtn = document.querySelector(`#share-note${noteId}`);
    const delBtn = document.querySelector(`#delete-note${noteId}`);
    const removeBtn = document.querySelector(`#remove-note${noteId}`);

    shareBtn.addEventListener('click', (evt) => {
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
            alert(responseJson.status);
          });
      });

      delBtn.addEventListener('click', (evt) => {
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

const sharedNotes = document.querySelectorAll("#shared-notes form")

for (const sharedForm of sharedNotes) {

  const noteId = sharedFrom.id;
  const removeBtn = document.querySelector(`#remove-note${noteId}`);

  removeBtn.addEventListener('click', (evt) => {
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
