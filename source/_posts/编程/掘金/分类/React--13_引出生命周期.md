
---
title: 'React--13_引出生命周期'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0554ad93bc95470e9f9a57e1ea6bdbc6~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 21 Aug 2021 02:30:14 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0554ad93bc95470e9f9a57e1ea6bdbc6~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第20天，活动详情查看:<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<p>例子：
点击按钮，文字从0变为1，再从1变为0</p>
<h2 data-id="heading-0">点击按钮，让组件消失</h2>
<ul>
<li>给按钮加点击事件</li>
<li>卸载组件  API：unmountComponentAtNode</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Life</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-comment">// 挂载：mount</span>
    <span class="hljs-comment">// 卸载：unmount</span>
    leave = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 卸载</span>
        ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
    &#125;  
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>React学不会怎么办？<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.leave&#125;</span>></span>不活了<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-1">改变文字的透明度</h2>
<ul>
<li>谁能驱动页面的更新？状态中的数据。所以在state中添加透明度的变量。</li>
<li>怎么让这个state中的opacity驱动页面透明度呢？给文字添加样式</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"> state = &#123;
        <span class="hljs-attr">opacity</span>:<span class="hljs-number">1</span>
    &#125;
    <span class="hljs-comment">// 挂载：mount</span>
    <span class="hljs-comment">// 卸载：unmount</span>
    leave = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 卸载</span>
        ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;opacity:this.state.opacity&#125;&#125;</span>></span>React学不会怎么办？<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.leave&#125;</span>></span>不活了<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">实现从完全可见到彻底消失，耗时2s</h2>
<ul>
<li>开启一个循环定时器，每次减少0.1。循环定时器每200ms减少0.1。</li>
</ul>
<p>我们将定时函数写到类中发现报错了，注意类中是不可以随便写代码的。类中可以写：构造器、自定义函数、赋值语句、static声明的赋值语句。<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0554ad93bc95470e9f9a57e1ea6bdbc6~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
所以定时方法不能写在这。我们能放在leave中吗？都已经卸载组件了，好像不太合适。那我们只能写到render方法中了。写在return底下合适吗？都已经return了，下面的代码不执行了，好像也不太合适。所以只能写在render方法中的 return 的顶部。</p>
<ul>
<li>在定时器中修改state状态值，当opacity<=0，再把opacity变为1</li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 获取原状态</span>
            <span class="hljs-keyword">let</span> &#123;opacity&#125; = <span class="hljs-built_in">this</span>.state
            <span class="hljs-comment">// -0.1</span>
            opacity -= <span class="hljs-number">0.1</span>
            <span class="hljs-comment">// 当小于等于0时，再把值变为 1。没有else条件省略 &#123;&#125;</span>
            <span class="hljs-keyword">if</span>(opacity <= <span class="hljs-number">0</span>) opacity = <span class="hljs-number">1</span>
            <span class="hljs-comment">//设置新的透明度</span>
            <span class="hljs-built_in">this</span>.setState(&#123;opacity&#125;)
        &#125;, <span class="hljs-number">200</span>);
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span> <span class="hljs-attr">style</span>=<span class="hljs-string">&#123;&#123;opacity:this.state.opacity&#125;&#125;</span>></span>React学不会怎么办？<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.leave&#125;</span>></span>不活了<span class="hljs-tag"></<span class="hljs-name">button</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-3">无限递归</h2>
<p>但是现在页面刷新的有些不太正常。引发了一个无限的递归。</p>
<p>原因：render中的定时器每200ms执行一次，每次都会更改状态state，state改变就会触发render对页面进行渲染。</p>
<p>我们在render中打印 一下 "render"。发现打印次数是指数型式的增长📈 。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/45b7439972b247d9b15546eb8b8c473f~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
所以定时器放在这里不太合适。</p>
<h2 data-id="heading-4">componentDidMount</h2>
<p>为什么componentDidMount就不用写成赋值语句加尖头函数的形式呢？
因为componentDidMount是跟render同一级别的，是React创建类的实例对象之后弄出来的。它的this指向是不会丢失的。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;

 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>componentDidMount在什么时候调用？在组件挂载页面之后调用</p>
<p>所以我们现在把定时器写到 componentDidMount 中。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"> <span class="hljs-comment">// 组件挂载页面之后调用</span>
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 获取原状态</span>
            <span class="hljs-keyword">let</span> &#123;opacity&#125; = <span class="hljs-built_in">this</span>.state
            <span class="hljs-comment">// -0.1</span>
            opacity -= <span class="hljs-number">0.1</span>
            <span class="hljs-comment">// 当小于等于0时，再把值变为 1</span>
            <span class="hljs-keyword">if</span>(opacity <= <span class="hljs-number">0</span>) opacity = <span class="hljs-number">1</span>
            <span class="hljs-comment">//设置新的透明度</span>
            <span class="hljs-built_in">this</span>.setState(&#123;opacity&#125;)
        &#125;, <span class="hljs-number">200</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，实现了我们想要的结果。但是点击按钮会发现如下的报错：大体意思是组件被卸载了，没法执行状态的更新。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ca6d422faefc47b9a026356d6d52d0e8~tplv-k3u1fbpfcp-watermark.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer">
原因：组件已经被卸载了，计时器还在跑。所以我们需要停掉计时器。</p>
<h2 data-id="heading-5">停止定时器</h2>
<p>那么什么时候清空定时器比较好？在点击按钮的时候。</p>
<p>使用clearInterval() 方法，需要定时器的id，才能清除定时器。</p>
<p>给setInterval 挂载到实例自身<code>this.timer = setInterval</code> 。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  leave = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 清除定时器</span>
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timer)
        <span class="hljs-comment">// 卸载</span>
        ReactDOM.unmountComponentAtNode(<span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
    &#125;
    <span class="hljs-comment">// 组件挂载页面之后调用</span>
    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-built_in">this</span>.timer = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-comment">// 获取原状态</span>
            <span class="hljs-keyword">let</span> &#123;opacity&#125; = <span class="hljs-built_in">this</span>.state
            <span class="hljs-comment">// -0.1</span>
            opacity -= <span class="hljs-number">0.1</span>
            <span class="hljs-comment">// 当小于等于0时，再把值变为 1</span>
            <span class="hljs-keyword">if</span>(opacity <= <span class="hljs-number">0</span>) opacity = <span class="hljs-number">1</span>
            <span class="hljs-comment">//设置新的透明度</span>
            <span class="hljs-built_in">this</span>.setState(&#123;opacity&#125;)
        &#125;, <span class="hljs-number">200</span>);
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">componentWillUnmount</h2>
<p>组件将要被卸载的时候调用。把定时器加到这也是可以的。</p>
<p>像 componentWillUnmount、componentDidMount这些
生命周期回调函数 === 生命周期钩子函数 ===生命周期函数 ===生命周期钩子</p></div>  
</div>
            