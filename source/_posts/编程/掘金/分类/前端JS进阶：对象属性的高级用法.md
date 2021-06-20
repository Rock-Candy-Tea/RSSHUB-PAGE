
---
title: '前端JS进阶：对象属性的高级用法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a8e2e9c0b84b128c18753a32a06b1f~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 00:07:00 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a8e2e9c0b84b128c18753a32a06b1f~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>“这是我参与更文挑战的第13天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a>”</p>
<p><strong>获取属性值用点’.’，多层级的，就用多个点</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-keyword">var</span> obj1 = &#123;
            <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
            <span class="hljs-attr">y</span>:&#123;
                <span class="hljs-attr">x</span>:<span class="hljs-number">2</span>,
                <span class="hljs-attr">y</span>:&#123;
                    <span class="hljs-attr">x</span>:<span class="hljs-number">3</span>,
                    <span class="hljs-attr">y</span>:<span class="hljs-number">4</span>,
                &#125;
            &#125;
        &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e7a8e2e9c0b84b128c18753a32a06b1f~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>属性的特性</strong>(除了属性名和属性值）<br>
1.可写：是否可以设置该属性的值 writable:true<br>
2.可枚举：for…in是否可以获取该属性值 enumerable:true<br>
3.可配置：是否可以删除，或修改属性的特性 configurable:true</p>
<p><strong>定义属性的特性：</strong><br>
Object.defineProperty(对象，属性名字符串，特性描述对象)<br>
Object.defineProperties(对象，多属性特性描述对象)</p>
<p><strong>单属性：</strong><br>
<strong>可写：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-keyword">var</span> obj1 = &#123;
            <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
            <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>,
        &#125;
        <span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
            <span class="hljs-attr">value</span>:<span class="hljs-number">3</span>,
            <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,
            <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
            <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f1d4733b2294f909c3d334290da2803~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
由于obj1的z是可配置的，所以，要想修改z值，将z的可写改成true即可</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">        <span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
            <span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
        &#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：z值可修改<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e930acaf17da4bb4a4fbdd7ee895a66c~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>可枚举：</strong><br>
可枚举时：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
    <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>,
&#125;
<span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
    <span class="hljs-attr">value</span>:<span class="hljs-number">3</span>,
    <span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> obj1)&#123;
    <span class="hljs-built_in">console</span>.log(i + <span class="hljs-string">' : '</span> + obj1[i]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d458372b33b744c5a0ff391de497258a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
不可枚举时：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
    <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>,
&#125;
<span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
    <span class="hljs-attr">value</span>:<span class="hljs-number">3</span>,
    <span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;)
<span class="hljs-keyword">for</span> (<span class="hljs-keyword">var</span> i <span class="hljs-keyword">in</span> obj1)&#123;
    <span class="hljs-built_in">console</span>.log(i + <span class="hljs-string">' : '</span> + obj1[i]);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4af5a560c664621902ebc9f66dcce04~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>可配置</strong><br>
不可配置之不能删除属性：delete返回false</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">var</span> obj1 = &#123;
    <span class="hljs-attr">x</span>:<span class="hljs-number">1</span>,
    <span class="hljs-attr">y</span>:<span class="hljs-number">2</span>,
&#125;
<span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
    <span class="hljs-attr">value</span>:<span class="hljs-number">3</span>,
    <span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">false</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行效果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c9b4fcd330a44b9ae210998dd1ee80a~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
不可配置之不能修改配置：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
    <span class="hljs-attr">value</span>:<span class="hljs-number">3</span>,
    <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">false</span>,
&#125;)<span class="hljs-comment">//初始特性设置</span>
<span class="hljs-built_in">Object</span>.defineProperty(obj1, <span class="hljs-string">'z'</span>,&#123;
    <span class="hljs-attr">writable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">false</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;)<span class="hljs-comment">//想要修改配置</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：报错，原因，初始设置时，设置<code>configurable:false,</code><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7735c095a5dd443d9a14a2580f198df7~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>多属性：</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-built_in">Object</span>.defineProperties(obj1,&#123;
    <span class="hljs-attr">z</span>: &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-number">3</span>,
        <span class="hljs-attr">writable</span>:<span class="hljs-literal">false</span>,
        <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
    &#125;,
    <span class="hljs-attr">t</span> : &#123;
        <span class="hljs-attr">value</span>: <span class="hljs-number">4</span>,
        <span class="hljs-attr">writable</span>: <span class="hljs-literal">true</span>,
        <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
        <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
    &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>查看属性的特性：Object.getOwnPropertyDescriptor(对象, 属性名)</strong><br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4106661978dc4db7bbc80acbe1791eaf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>set与get</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//某班级男生10人，女生8人，算班费</span>
<span class="hljs-keyword">var</span> classFare = &#123;<span class="hljs-attr">boy</span>:<span class="hljs-number">10</span>, <span class="hljs-attr">girl</span>:<span class="hljs-number">8</span>, <span class="hljs-attr">allmoney</span>:<span class="hljs-number">0</span>&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(classFare, <span class="hljs-string">'onemoney'</span>,&#123;
    <span class="hljs-attr">set</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">money</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.allmoney = (<span class="hljs-built_in">this</span>.boy + <span class="hljs-built_in">this</span>.girl )* money ;
    &#125;,
    <span class="hljs-attr">get</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'总共：'</span>+<span class="hljs-built_in">this</span>.allmoney;
    &#125;,
    <span class="hljs-comment">// writable:true,//Cannot both specify accessors and a value or writable attribute</span>
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果：<br>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a7edd22a9c54792807e245f7f7a1094~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"><br>
<strong>注意：不能在set和get中使用本属性，会造成死循环</strong></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">//某班级男生10人，女生8人，算班费</span>
<span class="hljs-keyword">var</span> classFare = &#123;<span class="hljs-attr">boy</span>:<span class="hljs-number">10</span>, <span class="hljs-attr">girl</span>:<span class="hljs-number">8</span>, <span class="hljs-attr">allmoney</span>:<span class="hljs-number">0</span>&#125;;
<span class="hljs-built_in">Object</span>.defineProperty(classFare, <span class="hljs-string">'onemoney'</span>,&#123;
    <span class="hljs-attr">set</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params">money</span>)</span>&#123;
        <span class="hljs-built_in">this</span>.onemoney = <span class="hljs-number">100</span>;<span class="hljs-comment">//这一句相当于set，就会一直在这两行中绕圈子循环</span>
        <span class="hljs-built_in">this</span>.allmoney = (<span class="hljs-built_in">this</span>.boy + <span class="hljs-built_in">this</span>.girl )* money ;
    &#125;,
    <span class="hljs-attr">get</span>:<span class="hljs-function"><span class="hljs-keyword">function</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> <span class="hljs-string">'总共：'</span>+<span class="hljs-built_in">this</span>.allmoney;
    &#125;,
    <span class="hljs-comment">// writable:true,//Cannot both specify accessors and a value or writable attribute</span>
    <span class="hljs-attr">enumerable</span>:<span class="hljs-literal">true</span>,
    <span class="hljs-attr">configurable</span>:<span class="hljs-literal">true</span>,
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            