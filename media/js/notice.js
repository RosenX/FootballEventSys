$(document).on('click', '#notice-save', function(){
    form = $("#notice-add-form").serialize(true);
    Dajaxice.notice.addNotice(addNotice_callback, {"form":form});
});

function addNotice_callback(data){
    if(data['statu'] == 1){
        $(".notice-table").html(data["html"]);
        $("#id_title").val("");
        $("#id_content").val("");
    }else{
        alert("Something wrong!");
    }
}

$(document).on('click', '.notice-delete-btn', function(){
    notice_id = $(this).attr("iid");
    if(confirm("确定删除吗？")){
        Dajaxice.notice.deleteNotice(deleteNotice_callback, {'notice_id':notice_id});
    }
});

function deleteNotice_callback(data){
    if(data['statu'] == 1){
        alert("成功删除");
        $(".notice-table").html(data['html']);
    }else{
        alert("Someting wrong!");
    }
}
