require(['../libs/zepto-1.1.6-min', '../libs/baidu.tongji', ], function() {
    var article_id = $("#article_detail").data('id');
    //_hmt.push(['_trackEvent', categoray, action, opt_label, opt_value]);
    _hmt.push(['_trackEvent', 'article_detail', 'overview', 'article_id', article_id]);
});
