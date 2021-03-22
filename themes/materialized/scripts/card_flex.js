//通用注入器
//name 注入插件名称
//item_comfig 注入插件的配置名
//temple_html_text 注入插件的挂载html模板(带有用户自定义的html/js/css)
//js_text 注入js
//css_text 注入css

function common_injector(name, item_comfig, temple_html_text, js_text, css_text) {
    if (item_comfig.enable) {
        if (temple_html_text !== '') {
            var layout_name;
            var layout_type;
            var layout_index = 0;
            if (item_comfig.layout_id) {
                layout_name = item_comfig.layout_id;
                layout_type = 'id';
            } else {
                layout_name = item_comfig.layout.name;
                layout_type = item_comfig.layout.type;
                layout_index = item_comfig.layout.index;
            }
            var get_layout
            if (layout_type === 'class') {
                get_layout = `document.getElementsByClassName('${layout_name}')[${layout_index}]`
            } else if (layout_type === 'id') {
                get_layout = `document.getElementById('${layout_name}')`
            } else {
                get_layout = `document.getElementById('${layout_name}')`
            }
            var user_info_js = `<script data-pjax>function ${name}_injector_config(){
                var parent_div_git = ${get_layout};
                var item_html = '${temple_html_text}';
                console.log('已挂载${name}')
                // parent_div_git.innerHTML=item_html+parent_div_git.innerHTML // 无报错，但不影响使用(支持pjax跳转)
                parent_div_git.insertAdjacentHTML("afterbegin",item_html) // 有报错，但不影响使用(支持pjax跳转)
            }if( ${get_layout} && (location.pathname ==='${item_comfig.enable_page}'|| '${item_comfig.enable_page}' ==='all')){

            ${name}_injector_config()
        } </script>`
        }
        hexo.extend.injector.register('body_end', user_info_js, "default");
        if (js_text !== '') {
            hexo.extend.injector.register('body_end', js_text, "default");
        }
        if (css_text !== '') {
            hexo.extend.injector.register('head_end', css_text, "home");
            hexo.extend.injector.register('head_end', css_text, "tag");
            hexo.extend.injector.register('head_end', css_text, "category");
            hexo.extend.injector.register('head_end', css_text, "archive");
        }
    }
}

hexo.extend.filter.register('after_generate',function() {
    if(hexo.config.card_flex.enable){
        var card_flex = hexo.config.card_flex;
        var css_text =``;
var css_plus =`
<style>

</style>
`
        var js_text =``
        common_injector('card_flex', card_flex,'',js_text,css_text)
        hexo.extend.injector.register('head_end', css_plus, "default");

    }


})