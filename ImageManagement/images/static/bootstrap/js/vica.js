
$(function () {
    if ($("#id_date_start_day")[0] != undefined) {
        $("#id_date_start_day")[0].setAttribute('disabled', 'disabled');
    }
    if ($("#id_date_start_month")[0] != undefined) {
        $("#id_date_start_month")[0].setAttribute('disabled', 'disabled');
    }
    if ($("#id_date_start_year")[0] != undefined) {
        $("#id_date_start_year")[0].setAttribute('disabled', 'disabled');
    }
    if ($("#id_date_end_day")[0] != undefined) {
        $("#id_date_end_day")[0].setAttribute('disabled', 'disabled');
    }
    if ($("#id_date_end_month")[0] != undefined) {
        $("#id_date_end_month")[0].setAttribute('disabled', 'disabled');
    }
    if ($("#id_date_end_year")[0] != undefined) {
        $("#id_date_end_year")[0].setAttribute('disabled', 'disabled');
    }
    $("#id_blur")[0].setAttribute('disabled', 'disabled');
    $("#id_rescale")[0].setAttribute('disabled', 'disabled');
    $("#id_rotate")[0].setAttribute('disabled', 'disabled');
});
$("#id_between_date").click(function () {
        if($("#id_between_date")[0].checked == false) {
            $("#id_date_start_day")[0].setAttribute('disabled', 'disabled');
            $("#id_date_end_day")[0].setAttribute('disabled', 'disabled');
            $("#id_date_start_month")[0].setAttribute('disabled', 'disabled');
            $("#id_date_end_month")[0].setAttribute('disabled', 'disabled');
            $("#id_date_start_year")[0].setAttribute('disabled', 'disabled');
            $("#id_date_end_year")[0].setAttribute('disabled', 'disabled');
        }
        else {
            $("#id_date_start_day")[0].removeAttribute('disabled');
            $("#id_date_end_day")[0].removeAttribute('disabled');
            $("#id_date_start_month")[0].removeAttribute('disabled');
            $("#id_date_end_month")[0].removeAttribute('disabled');
            $("#id_date_start_year")[0].removeAttribute('disabled');
            $("#id_date_end_year")[0].removeAttribute('disabled');
        }
    })
$("#id_to_blur").click(function () {
        if($("#id_to_blur")[0].checked == false) {
            $("#id_blur")[0].setAttribute('disabled', 'disabled');
        }
        else {
            $("#id_blur")[0].removeAttribute('disabled');
        }
    })
$("#id_to_rescale").click(function () {
        if($("#id_to_rescale")[0].checked == false) {
            $("#id_rescale")[0].setAttribute('disabled', 'disabled');
        }
        else {
            $("#id_rescale")[0].removeAttribute('disabled');
        }
    })
$("#id_to_rotate").click(function () {
        if($("#id_to_rotate")[0].checked == false) {
            $("#id_rotate")[0].setAttribute('disabled', 'disabled');
        }
        else {
            $("#id_rotate")[0].removeAttribute('disabled');
        }
    })