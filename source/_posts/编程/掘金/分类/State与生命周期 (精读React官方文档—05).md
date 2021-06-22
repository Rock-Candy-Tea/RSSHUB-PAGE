
---
title: 'State与生命周期 (精读React官方文档—05)'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3701'
author: 掘金
comments: false
date: Sat, 19 Jun 2021 17:29:44 GMT
thumbnail: 'https://picsum.photos/400/300?random=3701'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p>这是我参与更文挑战的第18天，活动详情查看：<a href="https://juejin.cn/post/6967194882926444557" target="_blank">更文挑战</a></p>
<h2 data-id="heading-0">state是私有的。</h2>
<blockquote>
<p>官方描述：State 与 props 类似，但是 state 是私有的，并且完全受控于当前组件。</p>
</blockquote>
<p><strong>解读</strong></p>
<ul>
<li>官方对state的介绍很重要，我们必须要知道state是私有的，并且完全受控于当前组件。</li>
</ul>
<h2 data-id="heading-1">将函数组件转换为类组件</h2>
<ol>
<li>创建一个同名的类，并且继承与React.Component.</li>
<li>添加一个空的render()方法.</li>
<li>将函数体(return(...))移动到render方法中.</li>
<li>在render方法中使用this.props代替props.</li>
<li>删除剩余的空函数声明.</li>
</ol>
<h3 data-id="heading-2">函数组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">Clock</span>(<span class="hljs-params">props</span>) </span>&#123;
    <span class="hljs-keyword">return</span> (
        <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
            <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>It is &#123;props.date.toLocaleTimeString()&#125;.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
        <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">类组件</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>It is &#123;this.props.date.toLocaleTimeString()&#125;.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        );
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>每次更新的时候render函数都会被调用。</li>
</ul>
<h2 data-id="heading-4">向类组件中添加局部state</h2>
<ol>
<li>将render方法中的this.props.data转换为this.state.date.</li>
<li>给类添加一个构造函数，并为this.state赋值.</li>
<li>移出类元素中的date属性.</li>
</ol>
<h2 data-id="heading-5">将声明周期方法添加到类组件中</h2>
<ul>
<li>componentDidMount():组件挂载后开始运行，此处适合开启定时器。</li>
<li>componentWillUnMount():组件将要卸载的时候运行，此处适合清除定时器。</li>
<li>上面的这种方法叫做声明周期方法。</li>
</ul>
<h3 data-id="heading-6">使用类组件实现计时功能</h3>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Clock</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
        <span class="hljs-built_in">super</span>(props);
        <span class="hljs-built_in">this</span>.state = &#123;<span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()&#125;
    &#125;

    <span class="hljs-function"><span class="hljs-title">tick</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.setState(&#123;
            <span class="hljs-attr">date</span>: <span class="hljs-keyword">new</span> <span class="hljs-built_in">Date</span>()
        &#125;)
    &#125;

    <span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">this</span>.timerID = <span class="hljs-built_in">setInterval</span>(<span class="hljs-function">() =></span> &#123;
            <span class="hljs-built_in">this</span>.tick();
        &#125;, <span class="hljs-number">1000</span>);
    &#125;
    <span class="hljs-function"><span class="hljs-title">componentWillUnmount</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-built_in">clearInterval</span>(<span class="hljs-built_in">this</span>.timerID)
    &#125;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Hello, world!<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>It is &#123;this.state.date.toLocaleTimeString()&#125;.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
        );
    &#125;
&#125;

ReactDOM.render(
    <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Clock</span> /></span></span>,
    <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'root'</span>)
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">计时器的执行顺序</h3>
<ol>
<li>当Clock组件传递给ReactDOM.reder后，React会首先调用Clock组件的构造函数，然后初始化state.</li>
<li>React调用组件的render方法，然后更新DOM进行渲染。</li>
<li>当Clock的输出被插入到DOM中后，开始调用componentDidMount这个生命周期函数，这个生命周期函数中，React向浏览器设置一个定时器，每隔1秒，调用组件的tick方法。</li>
<li>浏览器每调用一次tick方法，tick方法都会通过setState更新一次状态，只要状态发生了改变，React就会重新调用组件的render方法，然后进行重新渲染，然后更新DOM。</li>
<li>一旦Clock组件从DOM中删除，React就会调用生命周期函数componentWillUnmount，然后清除定时器。</li>
</ol>
<h2 data-id="heading-8">正确使用state</h2>
<ol>
<li>不要直接修改state,而是需要通过setState.</li>
</ol>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-built_in">this</span>.state.comment = <span class="hljs-string">'Hello'</span>;  <span class="hljs-comment">//不行</span>
<span class="hljs-built_in">this</span>.setState(&#123;<span class="hljs-attr">comment</span>: <span class="hljs-string">'Hello'</span>&#125;);  <span class="hljs-comment">//可以</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>state的更新可能是异步的.</li>
</ol>
<ul>
<li>下面的代码可能无法更新state</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Wrong</span>
<span class="hljs-built_in">this</span>.setState(&#123;
  <span class="hljs-attr">counter</span>: <span class="hljs-built_in">this</span>.state.counter + <span class="hljs-built_in">this</span>.props.increment,
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>解决上面的问题，可以让state接收一个函数，这也是setState更新状态的第二种方式。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// Correct</span>
<span class="hljs-built_in">this</span>.setState(<span class="hljs-function">(<span class="hljs-params">state, props</span>) =></span> (&#123;
  <span class="hljs-attr">counter</span>: state.counter + props.increment
&#125;));
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="3">
<li>state的更新会被合并。</li>
</ol>
<blockquote>
<p>看下面的例子你就明白了。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">posts</span>: [],
      <span class="hljs-attr">comments</span>: []
    &#125;;
  &#125;
<span class="hljs-function"><span class="hljs-title">componentDidMount</span>(<span class="hljs-params"></span>)</span> &#123;
    fetchPosts().then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">posts</span>: response.posts
      &#125;);
    &#125;);

    fetchComments().then(<span class="hljs-function"><span class="hljs-params">response</span> =></span> &#123;
      <span class="hljs-built_in">this</span>.setState(&#123;
        <span class="hljs-attr">comments</span>: response.comments
      &#125;);
    &#125;);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>官方解释：this.setState(&#123;comments&#125;) 完整保留了 this.state.posts， 但是完全替换了 this.state.comments。</p>
</blockquote>
<p>这里官方的解释非常完善了。</p>
<h2 data-id="heading-9">数据是向下流动的</h2>
<blockquote>
<p>官方描述：组件可以选择把它的 state 作为 props 向下传递到它的子组件中。FormattedDate 组件会在其 props 中接收参数 date，但是组件本身无法知道它是来自于 Clock 的 state，或是 Clock 的 props，还是手动输入的。</p>
</blockquote>
<pre><code class="hljs language-js copyable" lang="js"><FormattedDate date=&#123;<span class="hljs-built_in">this</span>.state.date&#125; />
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">FormattedDate</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h2</span>></span>It is &#123;props.date.toLocaleTimeString()&#125;.<span class="hljs-tag"></<span class="hljs-name">h2</span>></span></span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><strong>解读</strong></p>
<ul>
<li>这种数据流就是单向数据流，因为state产生的数据只能影响其子组件，</li>
</ul>
<blockquote>
<p>欢迎大家关注我的专栏，每日用碎片化的时间学习提高自己，加油！</p>
</blockquote></div>  
</div>
            