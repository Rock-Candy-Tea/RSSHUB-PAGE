
---
title: 'Element-UI 源码简析——Radio单选框（下）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c2836d0b7347f1af59ce2524ac5c9d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
author: 掘金
comments: false
date: Thu, 05 Aug 2021 23:46:36 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c2836d0b7347f1af59ce2524ac5c9d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c7c2836d0b7347f1af59ce2524ac5c9d~tplv-k3u1fbpfcp-zoom-in-crop-mark:1956:0:0:0.image" alt="26d8116a7588ac4a91a8398280e436fe.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">序言</h2>
<p>这篇的话，来分享一下Radio剩下的两个组件，radio-group、radio-button. 这两个组件的大致看了一下很多的地方和上一篇radio 90%以上是超不多的，radio和radio-button他俩最主要的区别还是样式上的不一样，还有一个原因就是，radio-button是和radio-group配合起来用的，所以这里就主要的讲一下radio-group的东西吧😁😁。</p>
<h2 data-id="heading-1">结构分析</h2>
<p>老样子还是根据三个角度来分析，Dom、数据属性、事件</p>
<h3 data-id="heading-2">Dom</h3>
<pre><code class="hljs language-js copyable" lang="js">     <component is=_elTag <span class="hljs-class"><span class="hljs-keyword">class</span></span>=el-radio-group role=radiogroup @keydown=handleKeydown>
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">slot</span>></span><span class="hljs-tag"></<span class="hljs-name">slot</span>></span></span>
    </component>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>radio-group的dom结构还是非常的少的，便于理解和参考,</p>
<p>首先引入眼帘的就是咱们的 component 这个组件了,这个就是vue自带的组件了,还有一个就是slot。</p>
<p>Vue自带的标签有component,transition,transition-group,keep-alive,slot。</p>
<p>component标签它是Vue内置的标签,它的用途是可以动态绑定我们的组件,根据数据不同更换不同的组件，详细的可以看看官网的描述了，这里就不做很详细的描述了。</p>
<p>role ： 这个属性在上一篇我提过 无障碍网页应用属性 大家也可以去参考看一看，这里也不多介绍了。</p>
<p>keydown：键盘按下事件</p>
<h2 data-id="heading-3">数据属性</h2>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-keyword">const</span> keyCode = <span class="hljs-built_in">Object</span>.freeze(&#123;
        LEFT <span class="hljs-number">37</span>,
        UP <span class="hljs-number">38</span>,
        RIGHT <span class="hljs-number">39</span>,
        DOWN <span class="hljs-number">40</span>,
    &#125;);
    <span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
        name ElRadioGroup,
        componentName ElRadioGroup,
        inject &#123;
            elFormItem &#123;
                <span class="hljs-keyword">default</span> ,
            &#125;,
        &#125;,
        mixins [Emitter],
        props &#123;
            value &#123;&#125;,
            size <span class="hljs-built_in">String</span>,
            textColor <span class="hljs-built_in">String</span>,
            disabled <span class="hljs-built_in">Boolean</span>,
        &#125;,
        computed &#123;
            <span class="hljs-function"><span class="hljs-title">_elFormItemSize</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.elFormItem  &#123;&#125;).elFormItemSize;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">_elTag</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> (<span class="hljs-built_in">this</span>.$vnode.data  &#123;&#125;).tag  div;
            &#125;,
            <span class="hljs-function"><span class="hljs-title">radioGroupSize</span>(<span class="hljs-params"></span>)</span> &#123;
                <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.size  <span class="hljs-built_in">this</span>._elFormItemSize  (<span class="hljs-built_in">this</span>.$ELEMENT  &#123;&#125;).size;
            &#125;,
        &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>属性这块的话，大部分也是之前分析过的，大家也可以参考之前的，但是这样有一个属性，大家可能平时可能用的比较少</p>
<p>Object.freeze： （冻结一个对象）一个被冻结的对象再也不能被修改；冻结了一个对象则不能向这个对象添加新的属性，不能删除已有属性，不能修改该对象已有属性的可枚举性、可配置性、可写性，以及不能修改已有属性的值。此外，冻结一个对象后该对象的原型也不能被修改。<code>freeze()</code> 返回和传入的参数相同的对象。</p>
<h4 data-id="heading-4">computed</h4>
<p>_elFormItemSize：用来判断当前from的</p>
<p>_elTag： 这个就是用来区分 按钮的组件和普通的组件了</p>
<p>radioGroupSize：Group的大小</p>
<h3 data-id="heading-5">事件</h3>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-function"><span class="hljs-title">created</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.$on(handleChange, (value) = &#123;
            <span class="hljs-built_in">this</span>.$emit(change, value);
        &#125;);
    &#125;,
    <span class="hljs-function"><span class="hljs-title">mounted</span>(<span class="hljs-params"></span>)</span> &#123;
         当radioGroup没有默认选项时，第一个可以选中Tab导航
        <span class="hljs-keyword">const</span> radios = <span class="hljs-built_in">this</span>.$el.querySelectorAll([type=radio]);
        <span class="hljs-keyword">const</span> firstLabel = <span class="hljs-built_in">this</span>.$el.querySelectorAll([role=radio])[<span class="hljs-number">0</span>];
        <span class="hljs-keyword">if</span> (![].some.call(radios, (radio) = radio.checked) && firstLabel) &#123;
            firstLabel.tabIndex = <span class="hljs-number">0</span>;
        &#125;
    &#125;,
    methods &#123;
            左右上下按键 可以在radio组内切换不同选项
        <span class="hljs-function"><span class="hljs-title">handleKeydown</span>(<span class="hljs-params">e</span>)</span> &#123;
            <span class="hljs-keyword">const</span> target = e.target;
             当前按下元素的事件对象
            <span class="hljs-keyword">const</span> className = target.nodeName === INPUT  [type=radio]  [role=radio];
             判断当前的元素是否是对应的INPUT,然后再来选择对应的input或者label
            <span class="hljs-keyword">const</span> radios = <span class="hljs-built_in">this</span>.$el.querySelectorAll(className);
             获取所有的className
            <span class="hljs-keyword">const</span> length = radios.length;
            <span class="hljs-keyword">const</span> index = [].indexOf.call(radios, target);
             在<span class="hljs-built_in">this</span>.$el.querySelectorAll的集合中查找evevt.target当前的下标
            <span class="hljs-keyword">const</span> roleRadios = <span class="hljs-built_in">this</span>.$el.querySelectorAll([role=radio]);
             获取所有的 label标签
            <span class="hljs-keyword">switch</span> (e.keyCode) &#123;
                  左 
                <span class="hljs-keyword">case</span> keyCode.LEFT
                 上
                <span class="hljs-keyword">case</span> keyCode.UP
                    e.stopPropagation();
                    e.preventDefault();
                    <span class="hljs-keyword">if</span> (index === <span class="hljs-number">0</span>) &#123;
                        roleRadios[length - <span class="hljs-number">1</span>].click();
                        roleRadios[length - <span class="hljs-number">1</span>].focus();
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        roleRadios[index - <span class="hljs-number">1</span>].click();
                        roleRadios[index - <span class="hljs-number">1</span>].focus();
                    &#125;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">case</span> keyCode.RIGHT
                 右
                <span class="hljs-keyword">case</span> keyCode.DOWN
                 下
                    <span class="hljs-keyword">if</span> (index === length - <span class="hljs-number">1</span>) &#123;
                        e.stopPropagation();
                        e.preventDefault();
                        roleRadios[<span class="hljs-number">0</span>].click();
                        roleRadios[<span class="hljs-number">0</span>].focus();
                    &#125; <span class="hljs-keyword">else</span> &#123;
                        roleRadios[index + <span class="hljs-number">1</span>].click();
                        roleRadios[index + <span class="hljs-number">1</span>].focus();
                    &#125;
                    <span class="hljs-keyword">break</span>;
                <span class="hljs-keyword">default</span>
                    <span class="hljs-keyword">break</span>;
            &#125;
        &#125;,
    &#125;,
<span class="copy-code-btn">复制代码</span></code></pre>
<p>created ： 主要是来监听子组件的handleChange，并且把这个事件抛出来。</p>
<p>handleKeydown：这个方法主要的作用就是左右上下按键 可以在radio组内切换不同选项，详细的看上方注释</p>
<h2 data-id="heading-6">末</h2>
<pre><code class="copyable">    树大招风风撼树，人为高名名丧人 ——————无奖竞猜
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            