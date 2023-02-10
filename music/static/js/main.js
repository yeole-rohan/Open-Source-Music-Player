var $ = jQuery.noConflict();
$(document).ready((function () {
     $(document).on("click", ".play-button svg", function (params) {
        params.preventDefault()
        const allPuasebtns = document.querySelectorAll(".pause-btn")
        for (let index = 0; index < allPuasebtns.length; index++) {
         const element = allPuasebtns[index];
         element.classList.remove("pause-btn")
         element.classList.add("play-button")
         element.parentElement.querySelector(".audio-file audio").pause()
         element.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-play-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z"/></svg>'
        }
        
        const audioFile = this.parentElement.parentElement.querySelector(".audio-file audio")
        const playButton = this.parentElement.parentElement.querySelector(".play-button")
        playButton.classList.remove("play-button")
        playButton.classList.add("pause-btn")
        playButton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-pause-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M5 6.25a1.25 1.25 0 1 1 2.5 0v3.5a1.25 1.25 0 1 1-2.5 0v-3.5zm3.5 0a1.25 1.25 0 1 1 2.5 0v3.5a1.25 1.25 0 1 1-2.5 0v-3.5z"/></svg>'
        audioFile.play()
     })

     $(document).on("click", ".pause-btn svg", function (params) {
         params.preventDefault()
         const audioFile = this.parentElement.parentElement.querySelector(".audio-file audio")
         const pauseButton = this.parentElement
         pauseButton.classList.remove("pause-btn")
         pauseButton.classList.add("play-button")
         pauseButton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="35" height="35" fill="currentColor" class="bi bi-play-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z"/></svg>'
         audioFile.pause()
     })
  })(jQuery)
);
