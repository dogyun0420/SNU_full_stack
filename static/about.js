// 페이지가 로드될 때 실행되는 함수
window.onload = function() {
    console.log("About page loaded");

    // 페이지 내 버튼 클릭 시 알림 메시지 표시
    const homeButton = document.querySelector('.button');
    // if (homeButton) {
    //     homeButton.addEventListener('click', function(event) {
    //         alert("You are going back to the homepage!");
    //     });
    // }
    if (homeButton) {
        homeButton.addEventListener('dblclick', function(event) {
            alert("You double-clicked to go back to the homepage!");
            console.log("dbdbdb");
        });
    }

    // 페이지 로드 후 2초 뒤에 안내 메시지 표시
    setTimeout(function() {
        alert("Welcome to the Netflix API About Page!");
    }, 2000);
}
