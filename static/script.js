const dropArea = document.querySelector(".drag-area"),
    dragText = dropArea.querySelector("header");
    button = dropArea.querySelector("button");
    input = dropArea.querySelector("input");
    icon = dropArea.querySelector("i");
    numOfFiles = dropArea.querySelector(".num-of-files");

let file; //this is a global variable and we'll use it inside multiple functions

button.onclick = ()=>{
    input.click(); // button을 누르면 input 태그도 함께 눌러진다.
}

input.addEventListener("change", function () {
    // 가장 먼저 골라진 단일 파일만을 저장
    file = this.files[0];
    valid_images();
    dropArea.classList.add("active");
})



// 유저가 파일을 Drop할 위치에 파일을 Over 있는 시간 표시
dropArea.addEventListener("dragover", (event) => {
    event.preventDefault(); // preventing from default behaviour
    dropArea.classList.add("active");
    dragText.textContent = "파일을 여기 끌어다 놓으세요.";
    icon.className = "fas fa-cloud-upload-alt"
});

// 유저가 파일을 Drop할 위치를 벗어났음을 표시
dropArea.addEventListener("dragleave", () => {
    dropArea.classList.remove("active");
    dragText.textContent = "파일을 여기 끌어다 놓으세요.";
    icon.className = "fas fa-cloud-upload-alt"
});

// 유저가 파일을 Drop할 위치에 파일을 Drop
dropArea.addEventListener("drop", (event) => {
    event.preventDefault(); // preventing from default behaviour
    // 가장 먼저 골라진 단일 파일만을 저장
    file = event.dataTransfer.files[0];
    valid_images()
});

function valid_images(){
    let fileType = file.type;
    let validExtensions = ["image/jpeg", "image/jpg", "image/png"];

    if (validExtensions.includes(fileType)) {
        icon.className = "fas fa-image"
        numOfFiles.textContent = `${input.files.length} / 150`;
        // let fileReader = new FileReader(); // creating new FileReader object
        // fileReader.onload = () => {
        //     let fileURL = fileReader.result; // passing user file source in fileURL variable
        //     console.log(fileURL);
        //     let imgTag = `<img src="${fileURL}" alt="">`; // creating an img tag and passing user selected file source inside src attribute
        //     dropArea.innerHTML = imgTag; // 이미지 정보를 통해 화면에 이미지를 출력해주는 것
        // }
        // fileReader.readAsDataURL(file);
    } else {
        alert("지원하지 않는 Image File 형식입니다!");
        dropArea.classList.remove("active");
    }
}

