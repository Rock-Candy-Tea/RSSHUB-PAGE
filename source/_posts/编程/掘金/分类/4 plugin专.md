
---
title: '4. plugin专'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2245'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 00:01:22 GMT
thumbnail: 'https://picsum.photos/400/300?random=2245'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">文件列表插件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">/*
最终结果
## 文件名    资源大小
- bundle.js    32157
- bundle.js.map    30826
- index.html    317
*/</span>

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">FileListPlugin</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">&#123;filename&#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.filename = filename;
    &#125;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
        compiler.hooks.emit.tap(<span class="hljs-string">"FileListPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation, cb</span>) =></span> &#123;
            <span class="hljs-comment">// 所有的资源都挂在compilation.assets属性上， 可以在属性上再加一个文件 这样就会被打包生成出来</span>
            <span class="hljs-keyword">let</span> assets = compilation.assets;
            <span class="hljs-keyword">let</span> content = <span class="hljs-string">`## 文件名    资源大小\r\n`</span>;
            <span class="hljs-built_in">Object</span>.entries(assets).forEach(<span class="hljs-function"><span class="hljs-params">element</span> =></span> &#123;
                <span class="hljs-keyword">let</span> [filename, statObj] = element;
                content += <span class="hljs-string">`- <span class="hljs-subst">$&#123;filename&#125;</span>    <span class="hljs-subst">$&#123;statObj.size()&#125;</span>\r\n`</span>
            &#125;)
            assets[<span class="hljs-built_in">this</span>.filename] = &#123;
                <span class="hljs-function"><span class="hljs-title">source</span>(<span class="hljs-params"></span>)</span>&#123;
                    <span class="hljs-keyword">return</span> content;
                &#125;,
                <span class="hljs-function"><span class="hljs-title">size</span>(<span class="hljs-params"></span>)</span> &#123;
                    <span class="hljs-keyword">return</span> content.length;
                &#125;
            &#125;
        &#125;)
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = FileListPlugin;

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">内联webpack插件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 将外链标签变成内联</span>
<span class="hljs-keyword">const</span> HtmlWebpackPlugin = <span class="hljs-built_in">require</span>(<span class="hljs-string">"html-webpack-plugin"</span>);
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InlineSourcePlugin</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">&#123;match&#125;</span>)</span> &#123;
        <span class="hljs-built_in">this</span>.reg = match;  <span class="hljs-comment">// 正则</span>
    &#125;
    <span class="hljs-function"><span class="hljs-title">apply</span>(<span class="hljs-params">compiler</span>)</span> &#123;
        <span class="hljs-comment">// 要通过htmlwebpackplugin实现这个功能</span>
        compiler.hooks.compilation.tap(<span class="hljs-string">"InlineSourcePlugin"</span>, <span class="hljs-function">(<span class="hljs-params">compilation</span>) =></span> &#123;
            HtmlWebpackPlugin.getHooks(compilation).alterAssetTagGroups.tapAsync(<span class="hljs-string">"alterPlugin"</span>, <span class="hljs-function">(<span class="hljs-params">data,cb</span>) =></span> &#123;
                data = <span class="hljs-built_in">this</span>.processTags(data, compilation); <span class="hljs-comment">// 因为资源内容都放在compilation.assets上</span>
                cb(<span class="hljs-literal">null</span>,data);
            &#125;)
        &#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">processTags</span>(<span class="hljs-params">data, compilation</span>)</span> &#123; <span class="hljs-comment">// 处理引入标签的数据</span>
        <span class="hljs-keyword">let</span> headTags = [];
        <span class="hljs-keyword">let</span> bodyTags = [];
        data.headTags.forEach(<span class="hljs-function"><span class="hljs-params">headTag</span> =></span> &#123;
            headTags.push(<span class="hljs-built_in">this</span>.processTag(headTag, compilation))
        &#125;)
        data.bodyTags.forEach(<span class="hljs-function"><span class="hljs-params">bodyTag</span> =></span> &#123;
            bodyTags.push(<span class="hljs-built_in">this</span>.processTag(bodyTag, compilation))
        &#125;)
        <span class="hljs-keyword">return</span> &#123;...data, headTags, bodyTags&#125;;
    &#125;

    <span class="hljs-function"><span class="hljs-title">processTag</span>(<span class="hljs-params">tag, compilation</span>)</span> &#123; <span class="hljs-comment">// 处理某一个标签</span>
        <span class="hljs-keyword">let</span> newTag, url;
        <span class="hljs-keyword">if</span>(tag.tagName === <span class="hljs-string">"link"</span> && <span class="hljs-built_in">this</span>.reg.test(tag.attributes.href))&#123;
            newTag = &#123;
                <span class="hljs-attr">tagName</span>: <span class="hljs-string">"style"</span>,
                <span class="hljs-attr">attributes</span>:&#123;<span class="hljs-attr">type</span>:<span class="hljs-string">"text/css"</span>&#125;
            &#125;;
            url = tag.attributes.href;
        &#125;
        <span class="hljs-keyword">if</span>(tag.tagName === <span class="hljs-string">"script"</span> && <span class="hljs-built_in">this</span>.reg.test(tag.attributes.src))&#123;
            newTag = &#123;
                <span class="hljs-attr">tagName</span>: <span class="hljs-string">"script"</span>,
                <span class="hljs-attr">attributes</span>:&#123;<span class="hljs-attr">type</span>:<span class="hljs-string">"application/javascript"</span>&#125;
            &#125;
            url = tag.attributes.src;
        &#125;
        <span class="hljs-keyword">if</span>(url) &#123;
            newTag.innerHTML = compilation.assets[url].source(); <span class="hljs-comment">// 文件的内容 放到innerHTML属性上</span>
            <span class="hljs-keyword">delete</span> compilation.assets[url]; <span class="hljs-comment">// 删除掉原资源 否则还是会被单独打包生成文件</span>
            <span class="hljs-keyword">return</span> newTag;
        &#125;
        <span class="hljs-keyword">return</span> tag;
    &#125;
&#125;
<span class="hljs-built_in">module</span>.exports = InlineSourcePlugin;



<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            