
---
title: '11-JS-WEB-API 事件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8873'
author: 掘金
comments: false
date: Sun, 04 Jul 2021 03:04:26 GMT
thumbnail: 'https://picsum.photos/400/300?random=8873'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">事件绑定和事件冒泡</h2>
<h3 data-id="heading-1">题目</h3>
<pre><code class="copyable">- 编写一个通用的事件监听函数
- 描述事件冒泡的流程
- 无限下拉的图片列表，如何监听每个图片的点击？
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>编写一个通用的事件监听函数</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,selector,fn</span>)</span>&#123;
    <span class="hljs-keyword">if</span>(fn == <span class="hljs-literal">null</span>)&#123;<span class="hljs-comment">//传三个参数和四个参数的处理</span>
        fn = selector;
        selector = <span class="hljs-literal">null</span>;
    &#125;
    elem.addEventListener(type, <span class="hljs-function"><span class="hljs-params">event</span>=></span>&#123;
        <span class="hljs-keyword">let</span> target;
        <span class="hljs-keyword">if</span>(selector)&#123;
            <span class="hljs-comment">//需要代理</span>
            target = event.target;
            <span class="hljs-keyword">if</span>(target.matches(selector))&#123;
                fn.call(target,event)
            &#125;<span class="hljs-keyword">else</span>&#123;
                <span class="hljs-comment">//不需要代理</span>
                fn.call(target,event)
            &#125;            
        &#125;
    &#125;)
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>描述事件冒泡的流程
<ul>
<li>基于DOM树形结构</li>
<li>事件会顺着触发元素往上冒泡</li>
<li>应用场景：代理</li>
</ul>
</li>
<li>无限下拉的图片列表，如何监听每个图片的点击？
<ul>
<li>
<p>事件代理</p>
</li>
<li>
<p>用e.target获取触发元素</p>
</li>
<li>
<p>用matches来判断是否是触发元素</p>
</li>
</ul>
</li>
</ul>
<h3 data-id="heading-2">知识点</h3>
<ul>
<li>事件绑定</li>
<li>事件冒泡</li>
<li>事件代理</li>
</ul>
<h3 data-id="heading-3">事件绑定</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> btn = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn1'</span>)
btn.addEventListener(<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">event</span> =></span>&#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">'clicked'</span>)
&#125;)


<span class="hljs-comment">//通用的绑定函数</span>
<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,fn</span>)</span>&#123;
    elem.addEventListener(type,fn)
&#125;

<span class="hljs-keyword">const</span> a = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'link1'</span>)
bindEvent(a,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
    <span class="hljs-built_in">console</span>.log(e.target) <span class="hljs-comment">//获取触发的元素</span>
    e.preventDefault()<span class="hljs-comment">//阻止默认行为</span>
    alert(<span class="hljs-string">'clicked'</span>)
&#125;)

<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">事件冒泡</h3>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">body</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div1"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p1"</span>></span>激活<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p2"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p3"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p4"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div2"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p5"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"p6"</span>></span>取消<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">body</span>></span>
<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">//通用的绑定函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,fn</span>)</span>&#123;
        elem.addEventListener(type,fn)
    &#125;
    
    <span class="hljs-keyword">const</span> p1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'p1'</span>)
    <span class="hljs-keyword">const</span> body = <span class="hljs-built_in">document</span>.body;
    binEvent(p1,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
        e.stopPropagation();<span class="hljs-comment">//阻止冒泡，注释掉这一行来体会事件冒泡</span>
        alert(<span class="hljs-string">'激活'</span>)
    &#125;)
    bindEvent(body,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">e</span>=></span>&#123;
        alert(<span class="hljs-string">'取消'</span>)
    &#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">事件代理</h2>
<p>事件代理是基于事件冒泡的,绑定父元素上通过子元素冒泡查看是否是想要的元素</p>
<p>特点：代码简洁，减少浏览器内存占用，但是不要滥用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">id</span>=<span class="hljs-string">"div3"</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>a1<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>a2<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>a3<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">a</span> <span class="hljs-attr">href</span>=<span class="hljs-string">"#"</span>></span>a4<span class="hljs-tag"></<span class="hljs-name">a</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">button</span>></span>加载更多<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"><<span class="hljs-name">button</span>></span>点击增加一个a标签<span class="hljs-tag"></<span class="hljs-name">button</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-comment">//通用的绑定函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,fn</span>)</span>&#123;
        elem.addEventListener(type,fn)
    &#125;

    <span class="hljs-keyword">const</span> div3 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div3'</span>)
    bindEvent(div3,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">event</span> =></span>&#123;
        event.preventDefault()<span class="hljs-comment">//阻止默认行为</span>
        <span class="hljs-keyword">const</span> target = event.target
        <span class="hljs-keyword">if</span>(target.nodeName === <span class="hljs-string">'A'</span>)&#123;
            alert(target.innerHTML)
        &#125;
    &#125;)
    <span class="hljs-comment">/*div3.addEventListener('click', e=>&#123;
        event.preventDefault()//阻止默认行为
        const target = e.target;
        if(e.nodeName === 'A')&#123;
            alert(target.innerHTML)
        &#125;
    &#125;)*/</span>
    
    

</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">通用的事件绑定函数</h2>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//通用的绑定函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,fn</span>)</span>&#123;
        elem.addEventListener(type,fn)
    &#125;
    
    <span class="hljs-comment">//普通事件绑定</span>
    <span class="hljs-keyword">const</span> btn1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn1'</span>);
    bindEvent(btn1,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">event</span> =></span>&#123;
        <span class="hljs-comment">//console.log(event.target) //获取触发的元素</span>
        enent.preventDefault() <span class="hljs-comment">//阻止默认行为</span>
        alert(<span class="hljs-string">'clicked'</span>)
    &#125;

    <span class="hljs-comment">//代理事件绑定</span>
    <span class="hljs-keyword">const</span> div3 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div3'</span>)
    bindEvent(div3,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-params">event</span> =></span>&#123;
        event.preventDefault()<span class="hljs-comment">//阻止默认行为</span>
        <span class="hljs-keyword">const</span> target = event.target
        <span class="hljs-keyword">if</span>(target.nodeName === <span class="hljs-string">'A'</span>)&#123;
            alert(target.innerHTML)
        &#125;
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>将上面通用函数改成下面的通用函数：</p>
<pre><code class="hljs language-js copyable" lang="js">    <span class="hljs-comment">//通用的绑定函数</span>
    <span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">bindEvent</span>(<span class="hljs-params">elem,type,selector,fn</span>)</span>&#123;
        <span class="hljs-keyword">if</span>(fn == <span class="hljs-literal">null</span>)&#123;<span class="hljs-comment">//传三个参数和四个参数的处理</span>
            fn = selector;
            selector = <span class="hljs-literal">null</span>;
        &#125;
        elem.addEventListener(type, <span class="hljs-function"><span class="hljs-params">event</span>=></span>&#123;
            <span class="hljs-keyword">let</span> target;
            <span class="hljs-keyword">if</span>(selector)&#123;
                <span class="hljs-comment">//需要代理</span>
                target = event.target;
                <span class="hljs-keyword">if</span>(target.matches(selector))&#123;
                    fn.call(target,event)
                &#125;<span class="hljs-keyword">else</span>&#123;
                    <span class="hljs-comment">//不需要代理</span>
                    fn.call(target,event)
                &#125;            
            &#125;
        &#125;)
    &#125;
    
    <span class="hljs-comment">//普通事件绑定</span>
    <span class="hljs-keyword">const</span> btn1 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'btn1'</span>);
    bindEvent(btn1,<span class="hljs-string">'click'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
        <span class="hljs-comment">//console.log(event.target) //获取触发的元素</span>
        enent.preventDefault() <span class="hljs-comment">//阻止默认行为</span>
        alert(<span class="hljs-built_in">this</span>.innerHTML)
        <span class="hljs-comment">//如果用箭头函数，则用下面语句</span>
        <span class="hljs-comment">//alert(btn1.innerHMTL)</span>
    &#125;

    <span class="hljs-comment">//代理事件绑定</span>
    <span class="hljs-keyword">const</span> div3 = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'div3'</span>)
    bindEvent(div3,<span class="hljs-string">'click'</span>,<span class="hljs-string">'a'</span>,<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">event</span>)</span>&#123;
        event.preventDefault()<span class="hljs-comment">//阻止默认行为</span>
        alert(<span class="hljs-built_in">this</span>.innerHTML)
        <span class="hljs-comment">//如果用箭头函数，则用下面语句</span>
        <span class="hljs-comment">//alert(event.target.innerHMTL)</span>
    &#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            