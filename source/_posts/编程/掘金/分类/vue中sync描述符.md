
---
title: 'vue中.sync描述符'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8311'
author: 掘金
comments: false
date: Sun, 25 Jul 2021 22:09:08 GMT
thumbnail: 'https://picsum.photos/400/300?random=8311'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>sync是语法糖 :title.sync 有两步 1  :title="title" 2 @update:title="val => title = val"</p>
<p><code>:title.sync="title"</code>会被扩展为<code>@update:title="val => title = val" :title="title"</code></p>
<p>方便子组件修改父组件的属性</p>
<pre><code class="hljs language-js copyable" lang="js">
<!DOCTYPE html>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">html</span>></span>

<span class="hljs-tag"><<span class="hljs-name">head</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">meta</span> <span class="hljs-attr">charset</span>=<span class="hljs-string">"utf-8"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">title</span>></span><span class="hljs-tag"></<span class="hljs-name">title</span>></span>
<span class="hljs-tag"></<span class="hljs-name">head</span>></span>

<span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"app"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">text-document</span> @<span class="hljs-attr">update:title</span>=<span class="hljs-string">"val => title = val"</span> <span class="hljs-attr">:title</span>=<span class="hljs-string">"title"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">text-document</span> <span class="hljs-attr">:title.sync</span>=<span class="hljs-string">"title"</span> /></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                &#123;&#123;title&#125;&#125;
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span> <span class="hljs-attr">src</span>=<span class="hljs-string">"./script/vue.js"</span>></span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
        Vue.component(<span class="hljs-string">'text-document'</span>, &#123;
            <span class="hljs-attr">props</span>: [<span class="hljs-string">'title'</span>],
            <span class="hljs-attr">template</span>: <span class="hljs-string">` <div>
            <div @click="setNewTitle">
                &#123;&#123;title&#125;&#125;
            </div>
        </div>`</span>,
            <span class="hljs-attr">methods</span>: &#123;
                <span class="hljs-attr">setNewTitle</span>: <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params"></span>) </span>&#123;
                    <span class="hljs-comment">//手动进行更新父组件中的值</span>
                    <span class="hljs-built_in">console</span>.log(<span class="hljs-number">121</span>)
                    <span class="hljs-built_in">this</span>.$emit(<span class="hljs-string">'update:title'</span>, <span class="hljs-string">'这步操作修改标题实现prop双向绑定'</span>)
                &#125;
            &#125;
        &#125;)
        <span class="hljs-keyword">var</span> vm = <span class="hljs-keyword">new</span> Vue(&#123;
            <span class="hljs-attr">el</span>: <span class="hljs-string">'#app'</span>,
            <span class="hljs-attr">data</span>: &#123;
                <span class="hljs-attr">title</span>: <span class="hljs-string">'对prop进行“双向绑定”'</span>
            &#125;,
        &#125;);
    </span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>

<span class="hljs-tag"></<span class="hljs-name">html</span>></span>
</span><span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            