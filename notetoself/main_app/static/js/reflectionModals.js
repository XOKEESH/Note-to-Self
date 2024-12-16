// const promptObj = [
//     {
//       header: "Get specific! Describe in great detail what you are grateful for!",
//       body: "3 things I am grateful for...",
//       placeholder: "Write your gratitude here...",
//     },
//     {
//       header: "What would make today great?",
//       body: "Keep these small and achievable so you actually go out and complete them.",
//       placeholder: "Write your ideas here...",
//     },
//     {
//       header: "Daily Affirmation",
//       body: "Choose powerful words and phrases to imprint on your subconscious mind.",
//       placeholder: "Write your affirmation here...",
//     },
//   ]
  
//   let count = 0
//   let userResponses = []
  
//   const modal = document.getElementById("morning-reflection-modal")
//   const openModalBtn = document.getElementById("morning-reflection-btn")
//   const closeModalBtn = document.getElementById("close-modal")
//   const nextBtn = document.getElementById("next-question")
//   const header = document.getElementById("modal-header")
//   const body = document.getElementById("modal-body")
//   const textBox = document.getElementById("text-box")
//   const progressBarContainer = document.getElementById("progress-bar-container")
//   const progressBar = document.getElementById("progress-bar")
  
//   // Open Modal
//   openModalBtn.addEventListener("click", () => {
//     modal.style.display = "flex"
//     count = 0
//     resetModal()
//   })
  
//   // Close Modal
//   closeModalBtn.addEventListener("click", () => {
//     modal.style.display = "none"
//   })
  
//   // Reset Modal
//   function resetModal() {
//     header.innerText = "Welcome to Your Morning Reflection"
//     body.innerText = "Click next to start your morning reflection."
//     textBox.value = ""
//     textBox.placeholder = "Your response..."
//     progressBarContainer.style.display = "none"
//     progressBar.style.width = "0%"
//   }
  
//   // Handle Next Button
//   nextBtn.addEventListener("click", () => {
//     if (count < promptObj.length) {
//       if (count === 0) {
//         progressBarContainer.style.display = "block"
//       }
  
//       // Save user response
//       userResponses.push({
//         question: promptObj[count].body,
//         response: textBox.value,
//       })
  
//       // Update progress bar
//       const progress = ((count + 1) / promptObj.length) * 100
//       progressBar.style.width = `${progress}%`
  
//       // Load next question
//       textBox.value = ""
//       header.innerText = promptObj[count].header
//       body.innerText = promptObj[count].body
//       textBox.placeholder = promptObj[count].placeholder
//       count++
//     } else {
//       // Final Screen
//       header.innerText = `What a great start to your day! See you back this evening.`
//       body.innerText = ""
//       progressBarContainer.style.display = "none"
//       textBox.style.display = "none"
//       nextBtn.innerText = "Done"
//       nextBtn.addEventListener("click", () => {
//         modal.style.display = "none"
//         resetModal()
//       })
//     }
//   })


// // Evening Reflection
// const eveningPromptObj = [
//     {
//       header: "Highlights of the day...",
//       body: "What were the highlights from your day?",
//       placeholder: "Reflect on your highlights here...",
//     },
//     {
//       header: "What did I learn today?",
//       body: "If you could magically go back in time and change something, what would it be?",
//       placeholder: "",
//     }
//   ]

// const eveningModal = document.getElementById("evening-reflection-modal")
// const eveningOpenModalBtn = document.getElementById("evening-reflection-btn")
// const eveningCloseModalBtn = document.getElementById("close-evening-modal")
// const eveningNextBtn = document.getElementById("next-evening-question")
// const eveningHeader = document.getElementById("evening-modal-header")
// const eveningBody = document.getElementById("evening-modal-body")
// const eveningTextBox = document.getElementById("evening-text-box")
// const eveningProgressBarContainer = document.getElementById("evening-progress-bar-container")
// const eveningProgressBar = document.getElementById("evening-progress-bar")

// // Open Modal
// eveningOpenModalBtn.addEventListener("click", () => {
//   eveningModal.style.display = "flex"
//   count = 0
//   resetEveningModal()
// })

// // Close Modal
// eveningCloseModalBtn.addEventListener("click", () => {
//   eveningModal.style.display = "none"
// })

// // Reset Modal
// function resetEveningModal() {
//   eveningHeader.innerText = "Welcome to Your Evening Reflection"
//   eveningBody.innerText = "Click next to start your evening reflection."
//   eveningTextBox.value = ""
//   eveningTextBox.placeholder = "Your response..."
//   eveningProgressBarContainer.style.display = "none"
//   eveningProgressBar.style.width = "0%"
// }

// // Next Button for Evening Reflection
// eveningNextBtn.addEventListener("click", () => {
//   if (count < eveningPromptObj.length) {
//     if (count === 0) {
//       eveningProgressBarContainer.style.display = "block"
//     }

//     // Save user response
//     userResponses.push({
//       question: eveningPromptObj[count].body,
//       response: eveningTextBox.value,
//     })

//     // Update progress bar
//     const progress = ((count + 1) / eveningPromptObj.length) * 100
//     eveningProgressBar.style.width = `${progress}%`

//     // Load next question
//     eveningTextBox.value = ""
//     eveningHeader.innerText = eveningPromptObj[count].header
//     eveningBody.innerText = eveningPromptObj[count].body
//     eveningTextBox.placeholder = eveningPromptObj[count].placeholder
//     count++
//   } else {
//     // Final Screen
//     eveningHeader.innerText = "Goodnight! You've completed your evening reflection."
//     eveningBody.innerText = ""
//     eveningProgressBarContainer.style.display = "none"
//     eveningTextBox.style.display = "none"
//     eveningNextBtn.innerText = "Done"
//     eveningNextBtn.addEventListener("click", () => {
//       eveningModal.style.display = "none"
//       resetEveningModal()
//     })
//   }
// })
  
// // Best Case Scenario Section - 
// const bcsModal = document.getElementById("bcs-modal")
// const bcsBtn = document.getElementById("bcs-btn")
// const bcsClose = document.getElementById("close-bcs-modal")
// const bcsSkipIntro = document.getElementById("bcs-skip-intro")
// const bcsNext = document.getElementById("bcs-next")
// const bcsSubmit = document.getElementById("bcs-submit")
// const bcsCloseBtn = document.getElementById("bcs-close")

// const bcsIntro = document.getElementById("bcs-intro")
// const bcsPrompt = document.getElementById("bcs-prompt")
// const bcsConfirmation = document.getElementById("bcs-confirmation")

// // Open Modal
// bcsBtn.addEventListener("click", () => {
//   bcsModal.style.display = "flex"
//   bcsIntro.style.display = "block"
//   bcsPrompt.style.display = "none"
//   bcsConfirmation.style.display = "none"
// })

// // Close Modal
// bcsClose.addEventListener("click", () => {
//   bcsModal.style.display = "none"
// })

// // Skip Intro Button
// bcsSkipIntro.addEventListener("click", () => {
//   bcsIntro.style.display = "none"
//   bcsPrompt.style.display = "block"
// })

// // Next Button from Intro to Prompt
// bcsNext.addEventListener("click", () => {
//   bcsIntro.style.display = "none"
//   bcsPrompt.style.display = "block"
// })

// // Submit Response
// bcsSubmit.addEventListener("click", () => {
//   const response = document.getElementById("bcs-text-box").value
//   console.log("User Response:", response) 

//   bcsPrompt.style.display = "none"
//   bcsConfirmation.style.display = "block"
// })

// // Close Confirmation
// bcsCloseBtn.addEventListener("click", () => {
//   bcsModal.style.display = "none"
// })
