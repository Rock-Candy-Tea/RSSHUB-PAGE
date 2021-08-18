
---
title: 'React--10_ 组件的三大核心属性3_refs与事件处理'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8f050353a1b47fca7490eabc0894e99~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Tue, 17 Aug 2021 17:04:50 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8f050353a1b47fca7490eabc0894e99~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与8月更文挑战的第18天，活动详情查看:<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></p>
<h1 data-id="heading-0">1. 字符串形式的ref</h1>
<p>首先这种形式是不推荐使用的。</p>
<p>过时 API：String 类型的 Refs：</p>
<p>如果你之前使用过 React，你可能了解过之前的 API 中的 string 类型的 ref 属性，例如 <code>"textInput"</code>。你可以通过 <code>this.refs.textInput</code> 来访问 DOM 节点。我们不建议使用它，因为 string 类型的 refs 存在一些效率上的问题。它已过时并可能会在未来的版本被移除（16.8版本还没有移除）。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a8f050353a1b47fca7490eabc0894e99~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-1">点击按钮获取输入框数据</h2>
<p>按照我们原生的写法，怎么在函数中获得输入框中的内容呢？首先给输入框一个id，然后通过getElementById 获得输入框中的值。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    showData = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">let</span> value = <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'input1'</span>).value
        <span class="hljs-built_in">console</span>.log(value)
    &#125;   
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span>  <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"点击按钮提示数据"</span>/></span><span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>点击提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"失去焦点提示数据"</span> /></span><span class="hljs-symbol">&nbsp;</span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是在React中去使用原生不是很好。因此ref就出现了。给input标签中添加ref属性（就类似于id）</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/11c21ab38f064881b2f5f348ba6db4ba~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>此时输出的this是类的实例 。 我们发现了refs中有 input1，是键值对类型。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cd0930a0efa40099c996f6b43539fbb~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>打印、获取输入框的内容</p>
<pre><code class="hljs language-js copyable" lang="js">    showData = <span class="hljs-function">()=></span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.refs.input1.value)
       <span class="hljs-keyword">const</span> &#123;input1&#125; = <span class="hljs-built_in">this</span>.refs
    &#125;   
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-2">失去焦点提示数据</h2>
<pre><code class="hljs language-js copyable" lang="js"><input type=<span class="hljs-string">"text"</span>  ref=<span class="hljs-string">"input2"</span> 
onBlur=&#123;<span class="hljs-built_in">this</span>.showData2&#125;  placeholder=<span class="hljs-string">"失去焦点提示数据"</span> />&nbsp;
  showData2 =<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> &#123;input2&#125; = <span class="hljs-built_in">this</span>.refs
        alert(input2.value)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a7341994378d46c2947e5cb27c43c597~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">总结</h2>
<p>refs 是实例上的属性。ref就像原生js的id，可以理解为打标签。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">'react'</span>;
<span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> PropTypes <span class="hljs-keyword">from</span> <span class="hljs-string">'prop-types'</span>;
<span class="hljs-keyword">import</span> <span class="hljs-string">'./index.css'</span>;
<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    showData = <span class="hljs-function">()=></span>&#123;
       <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.refs.input1.value)
    &#125;   
    showData2 =<span class="hljs-function">()=></span>&#123;
        <span class="hljs-keyword">const</span> &#123;input2&#125; = <span class="hljs-built_in">this</span>.refs
        alert(input2.value)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"input1"</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"点击按钮提示数据"</span>/></span><span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>点击提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>  <span class="hljs-attr">ref</span>=<span class="hljs-string">"input2"</span> <span class="hljs-attr">onBlur</span>=<span class="hljs-string">&#123;this.showData2&#125;</span>  <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"失去焦点提示数据"</span> /></span><span class="hljs-symbol">&nbsp;</span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Demo</span>/></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>))
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-4">2. 回调形似的ref</h1>
<p>ref 中写回调函数，传入的参数是什么呢？我们打印看一下。</p>
<pre><code class="hljs language-js copyable" lang="js">  <input ref=&#123;<span class="hljs-function">(<span class="hljs-params">a</span>)=></span>&#123;<span class="hljs-built_in">console</span>.log(a)&#125;&#125; type=<span class="hljs-string">"text"</span> placeholder=<span class="hljs-string">"点击按钮提示数据"</span>/>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看到打印出来的是ref所处节点</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4ea6d5f2d2e94ffca92a01ba7593addd~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer">
我们接下来把ref所处节点挂载到实例自身上，并取了个名字input1（剪头函数的 this 是其外部的 this，也就是render的实例，也就是 Demo实例）
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9853981c098f40b1b7f5c14a6f170d08~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>完整代码：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    showData = <span class="hljs-function">()=></span>&#123;
       <span class="hljs-keyword">const</span> &#123;input1&#125; = <span class="hljs-built_in">this</span>
       alert(input1.value)
    &#125;   
    showData2 =<span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>)
        <span class="hljs-keyword">const</span> &#123;input2&#125; = <span class="hljs-built_in">this</span>
        alert(input2.value)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(a)</span>=></span>&#123;this.input1 = a&#125;&#125; type="text" placeholder="点击按钮提示数据"/><span class="hljs-symbol">&nbsp;</span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>点击提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-symbol">&nbsp;</span>
                &#123;/* 剪头函数只有一个参数的时候可以简写 */&#125;
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span>  <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;c</span>=></span>this.input2=c&#125; onBlur=&#123;this.showData2&#125;  placeholder="失去焦点提示数据" /><span class="hljs-symbol">&nbsp;</span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">回调执行次数问题</h2>
<h3 data-id="heading-6">关于回调 refs 的说明</h3>
<p>如果 <code>ref</code> 回调函数是以<strong>内联函数</strong>的方式定义的，在<strong>更新过程中</strong>它会被执行两次，第一次传入参数 <code>null</code>，然后第二次会传入参数 DOM 元素。这是因为在每次渲染时会创建一个新的函数实例，所以 React 清空旧的 ref 并且设置新的。通过将 ref 的回调函数定义成 class 的绑定函数的方式可以避免上述问题，但是大多数情况下它是无关紧要的。</p>
<h3 data-id="heading-7">内联的写法</h3>
<p>首先什么是内联函数？如下ref中的函数就是内联函数。</p>
<pre><code class="hljs language-js copyable" lang="js">   <input ref=&#123;<span class="hljs-function">(<span class="hljs-params">currentNode</span>)=></span>&#123;<span class="hljs-built_in">this</span>.input1 = currentNode;<span class="hljs-built_in">console</span>.log(<span class="hljs-string">"currentNode"</span>,currentNode)&#125;&#125; type=<span class="hljs-string">"text"</span> placeholder=<span class="hljs-string">"点击按钮提示数据"</span>/>&nbsp;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>那么什么又算更新过程呢？</p>
<p>我点击按钮输出文本框的内容算吗？这只是交互，并不算是更新。</p>
<p>还记得我们前几篇文章用到的点击按钮切换天气的例子吗？我们在这里再次用到它。也就是用setState的使用。</p>
<pre><code class="hljs language-js copyable" lang="js">    state = &#123;
        <span class="hljs-attr">isHot</span>:<span class="hljs-literal">true</span>
    &#125;
    showInfo = <span class="hljs-function">()=></span>&#123;
      <span class="hljs-keyword">const</span> &#123;input1&#125; = <span class="hljs-built_in">this</span>
      alert(input1.value)
    &#125;
    changeWeather = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 获取原来状态</span>
        <span class="hljs-keyword">const</span> &#123;isHot&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">isHot</span>:!isHot&#125;)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123;isHot&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>今天天气很&#123;isHot?"炎热":"凉爽"&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(currentNode)</span>=></span>&#123;this.input1 = currentNode;console.log("currentNode",currentNode)&#125;&#125; type="text" placeholder="点击按钮提示数据"/><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showInfo&#125;</span>></span>点击提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeWeather&#125;</span>></span>点击改变天气<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>点击改变天气按钮 我们发现 打印了两次，并且第一次是null，第二次才是节点。（点击改变天气使页面进行了更新）
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9d0b09842f6a454aa292ae3a1d763b36~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>🤔</p>
<p>当更新页面时，render方法就会被调用一次。然后<code><input ref=&#123;(currentNode)=>&#123;this.input1 = currentNode;console.log("currentNode",currentNode)&#125;&#125; type="text" placeholder="点击按钮提示数据"/></code>代码就会执行，它又会发现ref，而且还是函数式的ref。这个函数又是一个新的函数了，之前的函数被执行完释放了。它并不确定之前的函数执行了什么，因此为了清空上一次调用的函数，传了null将第函数清空，第二次才把当前节点传进来。</p>
<p>怎么解决呢？🤔</p>
<h3 data-id="heading-8">class 的绑定函数的写法</h3>
<p>通过将 ref 的回调函数定义成 class 的绑定函数的方式可以避免上述问题，但是大多数情况下它是无关紧要的。    this.saveInput</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    state = &#123;
        <span class="hljs-attr">isHot</span>:<span class="hljs-literal">true</span>
    &#125;
    showInfo = <span class="hljs-function">()=></span>&#123;
      <span class="hljs-keyword">const</span> &#123;input1&#125; = <span class="hljs-built_in">this</span>
      alert(input1.value)
    &#125;
    changeWeather = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-comment">// 获取原来状态</span>
        <span class="hljs-keyword">const</span> &#123;isHot&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">isHot</span>:!isHot&#125;)
    &#125;
    saveInput = <span class="hljs-function">(<span class="hljs-params">c</span>)=></span>&#123;
        <span class="hljs-built_in">this</span>.input1 = c
        <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"c"</span>,c)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123;isHot&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>今天天气很&#123;isHot?"炎热":"凉爽"&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                &#123;/* <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;(currentNode)</span>=></span>&#123;this.input1 = currentNode;console.log("currentNode",currentNode)&#125;&#125; type="text" placeholder="点击按钮提示数据"/><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span> */&#125;
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.saveInput&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"点击按钮提示数据"</span>/></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span> 
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showInfo&#125;</span>></span>点击提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeWeather&#125;</span>></span>点击改变天气<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在怎么点击都不会频繁的调用 saveInput 了，因为 saveInput已经放在实例自身了。</p>
<p>当然直接写成内联的也问题不太。内联的写法是比较常见的。</p>
<h1 data-id="heading-9">3. CreateRef</h1>
<p>使用 createRef API</p>
<p>React.createRef调用后可以返回一个<strong>容器</strong>，该容器可以存储被ref标识的节点。但是只能存放一个</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Demo</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span></span>&#123;
    <span class="hljs-comment">// React.createRef调用后可以返回一个容器，该容器可以存储被ref标识的节点</span>
    myRef = React.createRef()
    state = &#123;
        <span class="hljs-attr">isHot</span>:<span class="hljs-literal">true</span>
    &#125;
    showData = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.myRef)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">const</span> &#123;isHot&#125; = <span class="hljs-built_in">this</span>.state
        <span class="hljs-keyword">return</span>(
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>今天天气很&#123;isHot?"炎热":"凉爽"&#125;<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;this.myRef&#125;</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"text"</span> <span class="hljs-attr">placeholder</span>=<span class="hljs-string">"点击按钮提示数据"</span>/></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span> 
                <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.showData&#125;</span>></span>点击按钮提示数据<span class="hljs-tag"></<span class="hljs-name">button</span>></span><span class="hljs-tag"><<span class="hljs-name">br</span>></span><span class="hljs-tag"></<span class="hljs-name">br</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打印 myRef</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aec9b35698934320a1ab2f656355eeb8~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>获得节点对应的值</p>
<pre><code class="hljs language-js copyable" lang="js">showData = <span class="hljs-function">()=></span>&#123;
        <span class="hljs-built_in">console</span>.log(<span class="hljs-built_in">this</span>.myRef.current.value)
    &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是这种容器，只能存一个。如果有多个节点，那只能声明多个myRef。</p></div>  
</div>
            