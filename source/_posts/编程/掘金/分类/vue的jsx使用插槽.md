
---
title: 'vue的jsx使用插槽'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3462'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 01:16:47 GMT
thumbnail: 'https://picsum.photos/400/300?random=3462'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.csdn.net%2Fweixin_44423832%2Farticle%2Fdetails%2F106187043" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.csdn.net/weixin_44423832/article/details/106187043" ref="nofollow noopener noreferrer">参考</a></p>
<p>jsx文件：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">props</span>:&#123;
        <span class="hljs-attr">initData</span>: &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-function">()=></span>&#123;
                <span class="hljs-keyword">return</span> &#123;&#125;
            &#125;
        &#125;,
        <span class="hljs-attr">config</span>:  &#123;
            <span class="hljs-attr">type</span>: <span class="hljs-built_in">Object</span>,
            <span class="hljs-attr">default</span>: <span class="hljs-function">()=></span>&#123;
                <span class="hljs-keyword">return</span> &#123;&#125;
            &#125;
        &#125;
    &#125;,
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params">h</span>)</span>&#123;
        <span class="hljs-keyword">let</span> tagName = <span class="hljs-built_in">this</span>.config&&<span class="hljs-built_in">this</span>.config.type ? <span class="hljs-built_in">this</span>.config.type: <span class="hljs-string">'div'</span>
        <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"chart-box"</span>></span>
                    &#123;/* <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"chart-title"</span>></span>&#123;this.config.title&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span> */&#125;
                    <span class="hljs-tag"><<span class="hljs-name">header</span>></span>&#123;this.$slots.default&#125;<span class="hljs-tag"></<span class="hljs-name">header</span>></span>
                    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">'chart-main'</span>></span>
                        <span class="hljs-tag"><<span class="hljs-name">tagName</span> <span class="hljs-attr">initData</span>=<span class="hljs-string">&#123;this.initData&#125;</span> <span class="hljs-attr">config</span>=<span class="hljs-string">&#123;this.config&#125;</span> /></span>
                    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
               <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>xx.vue文件使用jsx</p>
<pre><code class="hljs language-vue copyable" lang="vue">可以直接像组件那样引入使用

<Comp>
    <p>插槽内容</p>
</Comp>

import Comp from 'xxx.js'
componnets: &#123;
Comp
&#125;


//全局使用
main.js:
import Comp from 'xxx.js'
Vue.component('Comp',Comp)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            