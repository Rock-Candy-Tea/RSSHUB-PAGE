
---
title: '一点点开发中的JS小技巧'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6f3a63d65f44f969c617be0d6fa2599~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 09 Jun 2021 22:16:22 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6f3a63d65f44f969c617be0d6fa2599~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与更文挑战的第10天，活动详情查看： <a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">前言</h2>
<p>在实际工作中，经常会遇到一些特殊的场景，需要做一些处理。</p>
<p>这里收集了一些常用的处理方式，希望能够对大家有一些帮助。</p>
<h2 data-id="heading-1">一、字符串收尾去空格、填充</h2>
<h4 data-id="heading-2">1、去除空格</h4>
<p>首先去字符串收尾去空格，在搜索功能中使用较多。</p>
<p>需要对用户输入的内容做搜索，但是考虑到用户会输入多个不必要的空格，所以主动去除一下</p>
<p><strong>String.trim()</strong>  用于去除开头和结尾的空格</p>
<p><strong>String.trimStart()</strong> 去除头部空格</p>
<p><strong>String.trimEnd()</strong> 去除尾部空格</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> search =<span class="hljs-string">"  关键字   "</span>;

search.trim(); <span class="hljs-comment">// "关键字"</span>
search.trimStart(); <span class="hljs-comment">// "关键字   "</span>
search.trimEnd(); <span class="hljs-comment">// "   关键字"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">2、填充字符</h4>
<p>上面讲完了去除空格，那么自然还有填充的方法；</p>
<p>这个用法我常用于时间补齐， 如： 2021-6-9 -> 2021-06-09</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">let</span> str = <span class="hljs-string">'关键字'</span>;

str.padStart(<span class="hljs-number">5</span>, <span class="hljs-string">'1'</span>); <span class="hljs-comment">// '11关键字';</span>
str.padEnd(<span class="hljs-number">5</span>,<span class="hljs-string">'1'</span>); <span class="hljs-comment">// '关键字11'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>先说参数：
参数一：是填充到指定长度， 等于或大于该长度不填充，
参数二：是填充的字符串，未达到指定长度，则用指定的字符串填充。</p>
<p>另外需要补充一点,如果用于填充的字符串并非单一，那么会循环填充</p>
<blockquote>
<p>str.padStart(5, '很长的'); // '很长关键字'</p>
</blockquote>
<blockquote>
<p>str.padStart(9,'很长的'); // '很长的很长的关键字'</p>
</blockquote>
<h2 data-id="heading-4">二、类名操作</h2>
<p>类名操作，在原生开发中是经常用到的手段之一。</p>
<p>如果需要针对元素实现一些动画、显示操作，使用类名控制又比直接操作css性价比更高，也更好统一管理。</p>
<p><strong>Ele.classList.add()</strong>  添加类名</p>
<p><strong>Ele.classList.remove()</strong> 移除类名</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"name"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>

<span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
    <span class="hljs-keyword">let</span> oDiv = docuemnt.getElementsByClassName(<span class="hljs-string">'name'</span>)[<span class="hljs-number">0</span>];
    
    oDiv.classList.add(<span class="hljs-string">'first-name'</span>);   <span class="hljs-comment">// 添加类名</span>
    oDiv.classList.remove(<span class="hljs-string">'first-name'</span>); <span class="hljs-comment">// 移除类名</span>
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>除了上述两种以外，还有比较实用的两个方法。</p>
<blockquote>
<p>Ele.classList.contains();  // 检查是否包含指定类名，返回Boolean</p>
</blockquote>
<p>值得一提的是，还有个方法 <strong>Ele.classList.toggle();</strong>， 它接受两个参数， 第一个参数是类名， 第二个非必填参数是bool控制添加还是删除。</p>
<blockquote>
<p>Ele.classList.toggle('first-name' [, Boolean]);</p>
</blockquote>
<p>当我们执行上述命令的时候，如果元素内存在该类名，则删除，否则添加上去。</p>
<p>如果设置第二个参数为false， 则判断是否存在该类名，存在则删除。 不存在不操作。  设置为true则判断是否存在，不存在即添加上去。</p>
<h2 data-id="heading-5">三、兜底与可选链</h2>
<p>兜底： 即当预期的值不存在时、使用自己设置的一个默认值；</p>
<p>而ES6的发布，也为兜底带来的新的写法。</p>
<p>原写法与ES6现在的写法做个对比</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 原写法</span>
<span class="hljs-keyword">var</span> url = res && res.data && res.data.imgUrl || <span class="hljs-string">'https://www.baidu.com/'</span>

<span class="hljs-comment">// es6写法</span>
<span class="hljs-keyword">var</span> url = res?.data?.imgUrl || <span class="hljs-string">'https://www.baidu.com/'</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可选链 <strong>?.</strong> 的作用是，当不存在后面的属性时，返回undefined</p>
<p>例如   var res = &#123; name: '123'; &#125;</p>
<p>此时 res.data.imgUrl 是不存在的。</p>
<p>调用 res.data 返回undefined， 调用res.data.imgUrl 则会返回报错</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6f3a63d65f44f969c617be0d6fa2599~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时使用res.data?.imgUrl 则会继续返回undefined，而不会报错。</p>
<h2 data-id="heading-6">四、数组扁平化</h2>
<p>在常规的业务中一般很少用到， 但是在如果需要针对数组做处理的话，也是很好用的一个方法。</p>
<p>ES6则进一步降低这个过程的复杂度。</p>
<p>原写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">flatten</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">var</span> result = [],
        len = arr.length;
    
    <span class="hljs-keyword">for</span>(<span class="hljs-keyword">let</span> i = <span class="hljs-number">0</span>; i < len; i==)&#123;
        <span class="hljs-keyword">if</span>(<span class="hljs-built_in">Array</span>.isArray(arr[i])&#123;
            result.result.contact(flatten(arr[i])
        &#125; <span class="hljs-keyword">else</span> &#123;
            result.push(arr[i]);
        &#125;
    &#125;
    <span class="hljs-keyword">return</span> result;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ES6写法</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">faltten</span>(<span class="hljs-params">arr</span>)</span>&#123;
    <span class="hljs-keyword">while</span>(arr.some(<span class="hljs-function"><span class="hljs-params">item</span> =></span> <span class="hljs-built_in">Array</span>.isArray(item)&#123;
        arr = [].contact(...arr);
    &#125;
    <span class="hljs-keyword">return</span> arr;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-7">五、获取滚动距离</h2>
<p>这个功能本身没什么太大的难度，这里主要提下兼容性的写法。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">scrolloffset</span>(<span class="hljs-params"></span>)</span>&#123;
    <span class="hljs-keyword">if</span>(<span class="hljs-built_in">window</span>.pageXOffset)&#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">x</span>: <span class="hljs-built_in">window</span>.pageXOffset,
            <span class="hljs-attr">y</span>: <span class="hljs-built_in">window</span>.pageYOffset
        &#125;
    &#125; <span class="hljs-keyword">else</span> &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">x</span>: <span class="hljs-built_in">document</span>.body.scrollLeft + <span class="hljs-built_in">document</span>.documentElement.scrollLeft,
            <span class="hljs-attr">y</span>: <span class="hljs-built_in">document</span>.body.scrollTop + <span class="hljs-built_in">document</span>.documentElement.scrollTop
        &#125;
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-8">总结</h2>
<p>暂时先写这么多， 后面有好的技巧再写，嘻嘻嘻。</p>
<p>希望能帮助到大家。</p></div>  
</div>
            