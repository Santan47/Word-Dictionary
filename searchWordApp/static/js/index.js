$(document).ready(function () {
    searchWordAppModel = new searchApp();
    searchWordAppModel.init();
});


function searchApp() {

    // var fnAjaxRequest = function (ajaxURL, ajaxReqMethod, ajaxReqHeader, ajaxReqData, onSucess, onError) {
    //     $.ajax({
    //         type: ajaxReqMethod,
    //         url: ajaxURL,
    //         headers: ajaxReqHeader,
    //         data: ajaxReqData,
    //         success: onSucess,
    //         error: onError
    //     });
    // };

    function playAudio(url) {
        new Audio(url).play();
    }
    (function () {
        //  change nav tab
        $('body').off('click', '#wordSound').on('click', '#wordSound', function (e) {
            e.preventDefault();
            e.stopPropagation();
            playAudio(e.target.getAttribute("data-id"));
        });

    })();

    return {
        init: function () {
            var initialize = 1;
        }
    }
}