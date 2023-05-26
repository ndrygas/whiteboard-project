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

    shareBtn.addEventListener('click', (evt) => {
        evt.preventDefault();
        const userId = document.querySelector('#shared-user').value;

        const formInputs = {
          id: noteId,
          user: userId
          // title: document.querySelector(`#n-title${noteId}`).value,
          // body: document.querySelector(`#n-body${noteId}`).value,
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
            // location.reload();
            console.log(responseJson.status);
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