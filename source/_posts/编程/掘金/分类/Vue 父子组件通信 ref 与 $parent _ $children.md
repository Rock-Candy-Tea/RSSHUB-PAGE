
---
title: 'Vue 父子组件通信 ref 与 $parent _ $children'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9e9846fc9a4599b66c00107f7bebc6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 11 May 2021 18:50:51 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9e9846fc9a4599b66c00107f7bebc6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:37.5px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:120px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:30px 0 15px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body li::marker&#123;color:#a862ea&#125;.markdown-body li,.markdown-body p&#123;opacity:.9;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;padding-bottom:2px;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:2px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;box-shadow:0 0 20px 0 #e7daff;transition:transform .2s ease 0s;background-color:#f8f5ff&#125;.markdown-body img:hover&#123;opacity:1;transform:translateY(-2px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:15px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:4px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:22.5px;color:#383838;border-radius:3px;scroll-behavior:smooth&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse;border:1px solid #e7daff&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:1em .5em&#125;.markdown-body tr&#123;background-color:#fcfcfc&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><h1 data-id="heading-0">ref 与 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">parent / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">/</span></span></span></span></span>children通信</h1>
<blockquote>
父组件通过ref向子组件传参并调用子组件方法
</blockquote>
<p>在父组件代码中，通过在子组件上标签上设置属性ref，可在this.$ref中获取到子组件对象，以此调用子组件内的变量和方法，触发子组件的变化</p>
<pre><code class="hljs language-js copyable" lang="js"><!-- 父组件 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"family"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"father_methods"</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">div</span>></span>父组件的本地参数:&#123;&#123;father_string&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">button</span> @<span class="hljs-attr">click</span>=<span class="hljs-string">"change_son"</span>></span>ref获取子组件实例并触发其函数<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-comment"><!-- 子组件 --></span>
        <span class="hljs-tag"><<span class="hljs-name">Son</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"child1"</span>></span><span class="hljs-tag"></<span class="hljs-name">Son</span>></span>
        <span class="hljs-comment"><!-- 子组件 --></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> Son <span class="hljs-keyword">from</span> <span class="hljs-string">"./Son"</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"HelloWorld"</span>,

    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">father_string</span>: <span class="hljs-string">"father_string"</span>,
        &#125;;
    &#125;,
    <span class="hljs-attr">components</span>: &#123;
        Son,
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        father_methods (str) &#123;
            <span class="hljs-built_in">this</span>.father_string = str
        &#125;,
        change_son () &#123;
            <span class="hljs-built_in">this</span>.$refs.child1.son_methods(<span class="hljs-string">'changed_from_father'</span>)
        &#125;
    &#125;,
    mounted () &#123;
        <span class="hljs-built_in">console</span>.log();
    &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><!-- 子组件 -->
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>子组件的本地参数&#123;&#123;son_string&#125;&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">template</span>></span></span>

<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Son"</span>,
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">son_string</span>: <span class="hljs-string">"son_string"</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">/* 这个方法到时候供父组件调用 */</span>
        son_methods (str) &#123;
            <span class="hljs-built_in">this</span>.son_string = str
        &#125;
    &#125;
&#125;;
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
</script>


<span class="copy-code-btn">复制代码</span></code></pre>
<p>简单实例效果如下</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4c9e9846fc9a4599b66c00107f7bebc6~tplv-k3u1fbpfcp-watermark.image" alt="1-1.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>点击父组件的button，触发change_son，触发子组件的方法son_methods并且传递传递参数给子组件，如图子组件的参数改变</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9a23d0928e764e26824ca686a93f685c~tplv-k3u1fbpfcp-watermark.image" alt="1-2.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>Vue2中，在父组件中通过this.<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>c</mi><mi>h</mi><mi>i</mi><mi>l</mi><mi>d</mi><mi>r</mi><mi>e</mi><mi>n</mi><mtext>和</mtext><mi>t</mi><mi>h</mi><mi>i</mi><mi>s</mi><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">children和this.</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.69444em;vertical-align:0em;"></span><span class="mord mathnormal">c</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal" style="margin-right:0.01968em;">l</span><span class="mord mathnormal">d</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord cjk_fallback">和</span><span class="mord mathnormal">t</span><span class="mord mathnormal">h</span><span class="mord mathnormal">i</span><span class="mord mathnormal">s</span><span class="mord">.</span></span></span></span></span>ref调用的效果没有太大差别</p>
<p>值得注意的是Vue3移除了this中的$children属性</p>
</blockquote>
<p>我们来看看子组件中调用<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mtext>的效果，在子组件</mtext><mi>m</mi><mi>o</mi><mi>u</mi><mi>n</mi><mi>t</mi><mi>e</mi><mi>d</mi><mtext>周期中查看</mtext></mrow><annotation encoding="application/x-tex">parent的效果，在子组件mounted周期中查看</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord cjk_fallback">的</span><span class="mord cjk_fallback">效</span><span class="mord cjk_fallback">果</span><span class="mord cjk_fallback">，</span><span class="mord cjk_fallback">在</span><span class="mord cjk_fallback">子</span><span class="mord cjk_fallback">组</span><span class="mord cjk_fallback">件</span><span class="mord mathnormal">m</span><span class="mord mathnormal">o</span><span class="mord mathnormal">u</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord mathnormal">e</span><span class="mord mathnormal">d</span><span class="mord cjk_fallback">周</span><span class="mord cjk_fallback">期</span><span class="mord cjk_fallback">中</span><span class="mord cjk_fallback">查</span><span class="mord cjk_fallback">看</span></span></span></span></span>parent</p>
<pre><code class="hljs language-js copyable" lang="js"><script>
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Son"</span>,
    data () &#123;
        <span class="hljs-keyword">return</span> &#123;
            <span class="hljs-attr">son_string</span>: <span class="hljs-string">"son_string"</span>
        &#125;
    &#125;,
    <span class="hljs-attr">methods</span>: &#123;
        <span class="hljs-comment">/* 这个方法到时候供父组件调用 */</span>
        son_methods (str) &#123;
            <span class="hljs-built_in">this</span>.son_string = str
        &#125;
    &#125;,
    mounted () &#123;
        <span class="hljs-built_in">this</span>.$parent
    &#125;
&#125;;
</script>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>后台打印我们可以看到对象里存放着父组件的变量和参数</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5c1e5650b77f4a7a991f4e6859895dcd~tplv-k3u1fbpfcp-watermark.image" alt="1-3.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们直接在子组件mounted生命中期中调用父组件的方法并且传递参数</p>
<pre><code class="hljs language-js copyable" lang="js"> mounted () &#123;
        <span class="hljs-built_in">this</span>.$parent.father_methods(<span class="hljs-string">'changed_by_son'</span>)
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9788d1b0693a4c4caf0a3c3fe4b7f08f~tplv-k3u1fbpfcp-watermark.image" alt="1-4.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>图中左侧，父组件的参数确实被子组件修改了</p>
<h1 data-id="heading-1">总结</h1>
<p>通过ref 与 <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>p</mi><mi>a</mi><mi>r</mi><mi>e</mi><mi>n</mi><mi>t</mi><mi mathvariant="normal">/</mi></mrow><annotation encoding="application/x-tex">parent / </annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal">p</span><span class="mord mathnormal">a</span><span class="mord mathnormal" style="margin-right:0.02778em;">r</span><span class="mord mathnormal">e</span><span class="mord mathnormal">n</span><span class="mord mathnormal">t</span><span class="mord">/</span></span></span></span></span>children 可以简单快捷的拿到父子组件实例并访问，调用其方法和参数，根据实际情况，配合其他通信方法可优雅高效，愉快地开发~</p></div>  
</div>
            