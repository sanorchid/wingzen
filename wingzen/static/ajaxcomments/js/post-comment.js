$(document).ready(function() {
    previewed = false;
    
    commentBusy = false;
});

function ajaxComment(args) {
    // TODO: if the media variable ends in a forward slash, remove it.
    var media = args.media;
    
    $('div.comment-error').remove();
    
    if (commentBusy) {
        $('div.comment-form form').before('\
            <div class="comment-error">\
                正在上传数据...\
            </div>\
        ');
        $('div.comment-error').fadeOut(2000);
        
        return false;
    }
    
    comment = $('div.comment-form form').serialize();
   
    // Add a wait animation
    $('input.submit-post').after('\
        <img src="' + media + '/img/ajax-wait.gif" alt="请等待..."\
            class="ajax-loader" />\
    ');
    
    // Indicate that the comment is being posted
    $('p.submit').after('\
        <div class="comment-waiting" style="display: none;">\
            正在提交...请稍等...\
        </div>\
    ');
    $('div.comment-waiting').fadeIn(1000);
    
    commentBusy = true;
    
    url = $('div.comment-form form').attr('action');
    
    // Use AJAX to post the comment.
    $.ajax({
        type: 'POST',
        url: url,
        data: comment,
        success: function(data) {
            commentBusy = false;
        
            removeWaitAnimation()
        
            if (data.success == true) {
                commentSuccess(data);
            } else {
                commentFailure(data);
            }
        },
        error: function(data) {
            commentBusy = false;
            
            removeWaitAnimation()
            
            $('div.comment-form form').unbind('submit');
            $('div.comment-form form').submit();
        },
        dataType: 'json'
    });
    
    return false;
}

function commentSuccess(data) {
    email = $('#id_email').val();
    comment = $('#id_comment').val();
    name = $('#id_name').val();
    url = $('#id_url').val();
    
    if ($('div.meta').children().length == 1) {
        $('div.meta').prepend(
            '    <span class="comments">已有1个脚印</span>'
        )
    }
   $('div.comment-form form textarea')[0].value = "";

    $('#id_comment').val('');
    
    $('#comments').append(data['html']);
    $('div.comment:last').show('slow');
    
    $('p.submit').after('\
        <div class="comment-thanks">\
            谢谢你的回复！\
        </div>\
    ');
    $('div.comment-thanks').fadeOut(4000);
}

function commentFailure(data) {
    $('div.comment-form ul.errorlist').each(function() {
	    this.parentNode.removeChild(this);
        });

    for (var error in data.errors) {
        $('#id_' + error).parent().before(data.errors[error])
    }
}

function removeWaitAnimation() {
    // Remove the wait animation and message
    $('.ajax-loader').remove();
    $('div.comment-waiting').stop().remove();
}
