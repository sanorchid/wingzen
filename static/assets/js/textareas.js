tinyMCE.init({
    // 基本选项： 
    mode : "textareas",
    theme : "advanced",
	skin: "default",
	language : "ch",  //中文语言包
    plugins : "safari,pagebreak,style,table,save,advhr,advimage,advlink,emotions,inlinepopups,insertdatetime,preview,media,searchreplace,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,imagemanager,filemanager", 

    // 主题选项 (Theme options)
   theme_advanced_buttons1 : "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect",   //工具栏第二行的按钮,| 为按钮分隔符
   theme_advanced_buttons2 : "cut,copy,paste,pastetext,pasteword,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,code,|,insertdate,inserttime,preview,|,forecolor,backcolor", //工具栏第三行的按钮
   theme_advanced_buttons3 : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,media,advhr,|,ltr,rtl,|,fullscreen",    //工具栏第三行的按钮
   theme_advanced_toolbar_location : "top",   //工具按钮栏的位置，
   theme_advanced_toolbar_align : "left",   //工具按钮栏水平对齐方式
   theme_advanced_statusbar_location : "bottom",   //编辑器状态栏位置
   theme_advanced_resizing : true,  //设置是否可以改变编辑器大小
   theme_advanced_fonts: "宋体=宋体;黑体=黑体;仿宋=仿宋;楷体=楷体;隶书=隶书;幼圆=幼圆;Arial=arial,helvetica,sans-serif;Comic Sans MS=comic sans ms,sans-serif;Courier New=courier new,courier;Tahoma=tahoma,arial,helvetica,sans-serif;Times New Roman=times new roman,times;Verdana=verdana,geneva;Webdings=webdings;Wingdings=wingdings,zapf dingbats", //设置字体
   theme_advanced_resize_horizontal: true,   //设置是否允许水平方向上改变大小
   height:"200px",
   width:"960px"
});
