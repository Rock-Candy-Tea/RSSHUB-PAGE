
---
title: 'React--15_生命周期新版本'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1e45de837e54c8f94cb4191822f7e28~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 23 Aug 2021 06:41:58 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1e45de837e54c8f94cb4191822f7e28~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第22天，活动详情查看:<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>首先我们来看一张图，这是新版本的生命周期图</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1e45de837e54c8f94cb4191822f7e28~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-0">查看React的版本</h2>
<p>我这个可以看到是17，现在好像已经到18了。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/57b8325d797744bbacb4493243219d8c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们还是用上篇文章的计数器来作为例子</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Count</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"count-constructor"</span>)
        <span class="hljs-built_in">super</span>(props)
        <span class="hljs-comment">// 初始化状态</span>
        <span class="hljs-built_in">this</span>.state = &#123;
            <span class="hljs-attr">count</span>: <span class="hljs-number">0</span>
        &#125;
    &#125;
    <span class="hljs-comment">// 将要挂载</span>
    <span class="hljs-function"><span class="hljs-title">componentWillMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentWillMount"</span>)
    &#125;
    <span class="hljs-comment">//挂载完毕</span>
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentDidMount"</span>)
    &#125;
    <span class="hljs-comment">// +1 按钮回调 </span>
    add = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-comment">//获取原状态</span>
        <span class="hljs-keyword">const</span> &#123; count &#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-comment">// 更新状态</span>
        <span class="hljs-built_in">this</span>.setState(&#123; <span class="hljs-attr">count</span>: count + <span class="hljs-number">1</span> &#125;)
    &#125;
    <span class="hljs-comment">// 卸载组件的回调</span>
    death = <span class="hljs-function">() =></span> &#123;
        ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
    &#125;
    <span class="hljs-comment">// 组件将要卸载调用</span>
    <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentWillUnmount"</span>)
    &#125;
    <span class="hljs-comment">// 控制组件更新的“阀门”</span>
    <span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"shouldComponentUpdate"</span>)
        <span class="hljs-keyword">return</span> <span class="hljs-literal">true</span>
    &#125;
    <span class="hljs-comment">// 组件将要更新的钩子</span>
    <span class="hljs-function"><span class="hljs-title">componentWillUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentWillUpdate"</span>)
    &#125;
    <span class="hljs-comment">// 组件更新完毕的钩子</span>
    <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentDidUpdate"</span>)
    &#125;
    force = <span class="hljs-function">() =></span> &#123;
        <span class="hljs-built_in">this</span>.forceUpdate()
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"count-render"</span>)
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>当前求和为&#123;this.state.count&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.add&#125;</span>></span>点我+1<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.death&#125;</span>></span>销毁<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.force&#125;</span>></span>强制更新<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">旧版本生命周期</h2>
<p>我们再看一下旧版本的生命周期图</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/eb16b1d6aafe4578b2012846e60c22d2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">三个钩子改了名字</h2>
<p>旧版本中我们也见过这些钩子函数。那么新版本究竟差在哪里？虽然，没有影响页面</p>
<p>的渲染，但可以看到控制台中已经给出了警告。</p>
<p>警告的意思componentWillMount已经改名为UNSAFE_componentWillMount</p>
<p>componentWillUpdate已经改名为 UNSAFE_componentWillUpdate</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29218b62ec36407a8bf1c0231ec01670~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>忘了一个componentWillRecieveProps钩子,这个钩子是接收到props时才会触发的，所以我们再写一个子组件。并在 <code><Count/></code> 中引用 <code><B/></code> 组件</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">B</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">componentWillReceiveProps</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentWillReceiveProps"</span>)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>我是B组件,接收到的是&#123;this.props.carName&#125;<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Count</span> <span class="hljs-attr">carName</span>=<span class="hljs-string">"BM"</span>/></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到同样是有警告的（记住componentWillRecieveProps在接收到第二次props时才会打印，也就是更新时才会执行）</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4d8788f0d50445aba0c21851d8ea5960~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>怎么记忆哪个钩子改名了呢？除了componentWillUnmount的其他 名字中带Will 的钩子。都需要加UNSAFE_</p>
<h2 data-id="heading-3">新增两个钩子</h2>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9dd05cdd4f674a52b4fefeb7238f9e3a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我们从挂载时开始对比：</p>
<ol>
<li>新的和旧的刚开始都走了构造器constructor</li>
<li>新的没有 componentWillMount，在这个位置出现了个getDerivedStateFromProps</li>
<li>新旧接下来都是render</li>
<li>新的多了一个React更新DOM和ref，其实旧版本也更新了，只是没画出来。这部分是我们没有办法插手的。</li>
<li>接下来执行的都是componentDidMount</li>
</ol>
<p>卸载时：</p>
<ol>
<li>旧的挂载和更新最终都会到componentWillUnmount。其实新的也是，只是单列出来了。</li>
</ol>
<p>更新时：</p>
<ol>
<li>
<p>commentWillReceiveProps不见了 换成了getDerivedStateFromProps。getDerivedStateFromProps横跨了挂载和更新。</p>
</li>
<li>
<p>新旧 都会经过“阀门” shouldComponentUpdate</p>
</li>
<li>
<p>旧版本的render和componentDidUpdate之间是没有其他钩子的。而新版新增了getSnapshotBeforeUpdate</p>
</li>
</ol>
<h2 data-id="heading-4">最后</h2>
<p>新版和旧版本相比 废弃了三个钩子，新增了两个钩子。这两个钩子的用法我们下一篇文章再去了解。</p></div>  
</div>
            