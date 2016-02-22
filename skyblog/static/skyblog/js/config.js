require.config({
    baseUrl: '/skyblog/static/js/',
    paths: {
        zepto: 'libs/zepto-1.1.6-min',
        tmpl: 'libs/tmpl-2.5.4-min',
        fastclick: 'libs/fastclick-1.0.3-min'
    },
    shim: {
        'zepto': {
            exports: '$'
        },
        'tmpl': {
            exports: 'tmpl'
        }
    }
});
