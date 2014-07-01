
if (jQuery) (
function (jQuery) {
    jQuery.extend(jQuery.fn, {
        tablePaging: function (options) {
            jQuery(this).each(function () {
                settings = jQuery.extend({
                    id: jQuery(this).attr('id'), // The ID of the object being paging
                    pageSize: 10, // The size of one page
                    sorting: false,
                    sortDirection: 'asc', // asc & desc
                    sortSelector: '',
                    sortType: '', //number,string,date
                    onPaged: null // // Function to run after paged
                }, options);
            });
            $(this).each(function () {
                if (settings.sorting) {
                    jQuery(this).tableSort(settings.sortSelector, settings.sortType, settings.sortDirection);

                }
                var pageSize = parseInt(settings.pageSize);

                var trResult = jQuery('#' + jQuery(this).attr('id')).find('tbody:first tr');
                var trLen = trResult.length;
                var pageIndex = 0;
                if (!jQuery(this).data("pageindex")) {
                    jQuery(this).data("pageindex", "0");
                };
                pageIndex = parseInt(jQuery(this).data("pageindex"));
                if (pageIndex * pageSize == trLen && trLen != 0) {
                    pageIndex = pageIndex - 1; // make sure the last page will show right
                    jQuery(this).data("pageindex", pageIndex);
                }
                jQuery('#' + jQuery(this).attr('id')).find('tbody').each(function (i, element) {
                    var trs = $(this).find('tr');
                    var trsLen = trs.length;
                    trs.hide();
                    trs.slice(pageIndex * pageSize, (pageIndex + 1) * pageSize).show();
                });

                var allPage = Math.ceil(parseInt(trLen) / pageSize);
                if (allPage > 1) {
                    jQuery("#" + jQuery(this).attr('id') + "Paging").remove();
                    jQuery("#" + jQuery(this).attr('id')).after('<div id="' + jQuery(this).attr('id') + 'Paging" class="search-for"></div>');
                    queue = '#' + jQuery(this).attr('id') + 'Paging';
                    jQuery(queue).append('<p class="paging"><a id="prePage" tableid="' + jQuery(this).attr('id') + '" pageindex=' + (parseInt(jQuery(this).data("pageindex")) - 1) + ' href="#">前一页</a> | ' + (parseInt(jQuery(this).data("pageindex")) + 1) + '/' + allPage + ' | <a id="nextPage" tableid="' + jQuery(this).attr('id') + '" pageindex=' + (parseInt(jQuery(this).data("pageindex")) + 1) + ' href="#">后一页</a></p>');
                    jQuery("#" + jQuery(this).attr('id') + "Paging").find("#prePage").bind("click", settings, function (e) {
                        //                    var toPageIndex = settings.pageIndex - 1;
                        var toPageIndex = parseInt(jQuery(this).attr("pageindex"));
                        if (toPageIndex < 0) toPageIndex = allPage - 1;
                        jQuery("#" + jQuery(this).attr("tableid")).data("pageindex", toPageIndex);
                        jQuery("#" + jQuery(this).attr("tableid")).tablePaging(e.data);
                        e.preventDefault();
                    });
                    jQuery("#" + jQuery(this).attr('id') + "Paging").find("#nextPage").bind("click", settings, function (e) {
                        //var toPageIndex = settings.pageIndex + 1;
                        var toPageIndex = parseInt(jQuery(this).attr("pageindex"));
                        if (toPageIndex >= allPage) toPageIndex = 0;
                        jQuery("#" + jQuery(this).attr("tableid")).data("pageindex", toPageIndex);
                        jQuery("#" + jQuery(this).attr("tableid")).tablePaging(e.data);
                        e.preventDefault();
                    });
                }
                else {
                    jQuery("#" + jQuery(this).attr('id') + "Paging").remove();
                }

                if (jQuery.isFunction(settings.onPaged)) {
                    settings.onPaged();
                }
            });
        },
    })
})(jQuery);

function parseDate(date) {
    return Date.parse(convertDateFormat(date)); // from en-GB format to en-US format,must greater than 01/01/1970;
}

function convertDateFormat(value) {
    return value = value.toString().replace(/\-/g, '/').replace(/\./g, '/').replace(/\s/g, '/');
}