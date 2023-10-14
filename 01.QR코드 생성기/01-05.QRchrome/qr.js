(function(){
    chrome.tabs.query({}, goTabs);

    const goTabs = () => {

    };

    const ajax = () => {
        const text = document.querySelector('#data').value.trim(); 
        let tag;
        httpRequest = new XMLHttpRequest();
        /* httpRequest의 readyState가 변화했을때 함수 실행 */
        httpRequest.onreadystatechange = () => {
            /* readyState가 Done이고 응답 값이 200일 때, 받아온 response로 name과 age를 그려줌 */
            if (httpRequest.readyState === XMLHttpRequest.DONE) {
                if (httpRequest.status === 200) {
                    var result = httpRequest.response;
                    console.log("response:{}", result)
                    const base64 = result.data;
                    const error = result.error;

                    if(error == "ok"){
                        tag = `<img src='data:image/png;base64, ${base64}'>`;
                        document.querySelector('#qrcode').innerHTML = tag;
                    }
                } else {
                    alert('Request Error!');
                }
            }
        };
        const url = "http://localhost:8999/make_qrcode";
        /* Get 방식으로 name 파라미터와 함께 요청 */
        httpRequest.open('POST', url, true);
        /* Response Type을 Json으로 사전 정의 */
        httpRequest.setRequestHeader('Content-Type', 'application/json');
        httpRequest.responseType = "json";
        /* 정의된 서버에 요청을 전송 */
        const data = {"text": text};
        console.log(data);
        httpRequest.send(JSON.stringify(data));
    }

})();



