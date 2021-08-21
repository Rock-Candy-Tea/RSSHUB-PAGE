
---
title: '5 分钟搞懂面试官必问 React 题（五）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6518e71d4a4fe48337a2f27eb7b55f~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 22:21:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6518e71d4a4fe48337a2f27eb7b55f~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><p><strong>这是我参与8月更文挑战的第21天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" title="https://juejin.cn/post/6987962113788493831" target="_blank">8月更文挑战</a></strong></p>
<h2 data-id="heading-0">相关文章：</h2>
<ul>
<li><a href="https://juejin.cn/post/6997269945394397197" target="_blank" title="https://juejin.cn/post/6997269945394397197">5 分钟搞懂面试官必问 React 题（一）</a></li>
<li><a href="https://juejin.cn/post/6997609116159967269" target="_blank" title="https://juejin.cn/post/6997609116159967269">5 分钟搞懂面试官必问 React 题（二）</a></li>
<li><a href="https://juejin.cn/post/6997978475579572255" target="_blank" title="https://juejin.cn/post/6997978475579572255">5 分钟搞懂面试官必问 React 题（三）</a></li>
<li><a href="https://juejin.cn/post/6998442828300812319" target="_blank" title="https://juejin.cn/post/6998442828300812319">5 分钟搞懂面试官必问 React 题（四）</a></li>
<li><a href="https://juejin.cn/post/6998764243910656030#" target="_blank" title="#">5 分钟搞懂面试官必问 React 题（五）</a></li>
</ul>
<h1 data-id="heading-1">说说 React 性能优化的手段有哪些？</h1>
<h2 data-id="heading-2">一、是什么</h2>
<p><code>React</code>凭借<code>virtual DOM</code>和<code>diff</code>算法拥有高效的性能，但是某些情况下，性能明显可以进一步提高</p>
<p>在前面文章中，我们了解到类组件通过调用<code>setState</code>方法， 就会导致<code>render</code>，父组件一旦发生<code>render</code>渲染，子组件一定也会执行<code>render</code>渲染</p>
<p>当我们想要更新一个子组件的时候，如下图绿色部分：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8e6518e71d4a4fe48337a2f27eb7b55f~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>理想状态只调用该路径下的组件<code>render</code>：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29eb943c7e5a45b2995ab2808b1a1d0e~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>但是<code>react</code>的默认做法是调用所有组件的<code>render</code>，再对生成的虚拟<code>DOM</code>进行对比（黄色部分），如不变则不进行更新</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f2bbe75add80403582f233361616377b~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>从上图可见，黄色部分<code>diff</code>算法对比是明显的性能浪费的情况</p>
<h2 data-id="heading-3">二、如何做</h2>
<p>避免不必要的<code>render</code>，主要手段是通过<code>shouldComponentUpdate</code>、<code>PureComponent</code>、<code>React.memo</code>，这三种形式。</p>
<p>除此之外， 常见性能优化常见的手段有如下：</p>
<ul>
<li>避免使用内联函数</li>
<li>使用 React Fragments 避免额外标记</li>
<li>使用 Immutable</li>
<li>懒加载组件</li>
<li>事件绑定方式</li>
<li>服务端渲染</li>
</ul>
<h4 data-id="heading-4">避免使用内联函数</h4>
<p>如果我们使用内联函数，则每次调用<code>render</code>函数时都会创建一个新的函数实例，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InlineFunctionComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Welcome Guest<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;(e)</span> =></span> &#123; this.setState(&#123;inputValue: e.target.value&#125;) &#125;&#125; value="Click For Inline Function" />
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们应该在组件内部创建一个函数，并将事件绑定到该函数本身。这样每次调用 <code>render</code> 时就不会创建单独的函数实例，如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">InlineFunctionComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  
  setNewStateData = <span class="hljs-function">(<span class="hljs-params">event</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">inputValue</span>: e.target.value
    &#125;)
  &#125;
  
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Welcome Guest<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">input</span> <span class="hljs-attr">type</span>=<span class="hljs-string">"button"</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.setNewStateData&#125;</span> <span class="hljs-attr">value</span>=<span class="hljs-string">"Click For Inline Function"</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    )
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">使用 React Fragments 避免额外标记</h4>
<p>用户创建新组件时，每个组件应具有单个父标签。父级不能有两个标签，所以顶部要有一个公共标签，所以我们经常在组件顶部添加额外标签<code>div</code></p>
<p>这个额外标签除了充当父标签之外，并没有其他作用，这时候则可以使用<code>fragement</code></p>
<p>其不会向组件引入任何额外标记，但它可以作为父级标签的作用，如下所示：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">NestedRoutingComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><></span>
                <span class="hljs-tag"><<span class="hljs-name">h1</span>></span>This is the Header Component<span class="hljs-tag"></<span class="hljs-name">h1</span>></span>
                <span class="hljs-tag"><<span class="hljs-name">h2</span>></span>Welcome To Demo Page<span class="hljs-tag"></<span class="hljs-name">h2</span>></span>
            <span class="hljs-tag"></></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-6">事件绑定方式</h3>
<p>从性能方面考虑，在<code>render</code>方法中使用<code>bind</code>和<code>render</code>方法中使用箭头函数这两种形式在每次组件<code>render</code>的时候都会生成新的方法实例，性能欠缺</p>
<p>而<code>constructor</code>中<code>bind</code>事件与定义阶段使用箭头函数绑定这两种形式只会生成一个方法实例，性能方面会有所改善</p>
<h3 data-id="heading-7">使用 Immutable</h3>
<p>使用 <code>Immutable</code>可以给 <code>React</code> 应用带来性能的优化，主要体现在减少渲染的次数</p>
<p>在做<code>react</code>性能优化的时候，为了避免重复渲染，我们会在<code>shouldComponentUpdate()</code>中做对比，当返回<code>true</code>执行<code>render</code>方法</p>
<p><code>Immutable</code>通过<code>is</code>方法则可以完成对比，而无需像一样通过深度比较的方式比较</p>
<h3 data-id="heading-8">懒加载组件</h3>
<p>从工程方面考虑，<code>webpack</code>存在代码拆分能力，可以为应用创建多个包，并在运行时动态加载，减少初始包的大小</p>
<p>而在<code>react</code>中使用到了<code>Suspense</code>和 <code>lazy</code>组件实现代码拆分功能，基本使用如下：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> johanComponent = React.lazy(<span class="hljs-function">() =></span> <span class="hljs-keyword">import</span>(<span class="hljs-comment">/* webpackChunkName: "johanComponent" */</span> <span class="hljs-string">'./myAwesome.component'</span>));
 
<span class="hljs-keyword">export</span> <span class="hljs-keyword">const</span> johanAsyncComponent = <span class="hljs-function"><span class="hljs-params">props</span> =></span> (
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">React.Suspense</span> <span class="hljs-attr">fallback</span>=<span class="hljs-string">&#123;</span><<span class="hljs-attr">Spinner</span> /></span>&#125;>
    <span class="hljs-tag"><<span class="hljs-name">johanComponent</span> &#123;<span class="hljs-attr">...props</span>&#125; /></span>
  <span class="hljs-tag"></<span class="hljs-name">React.Suspense</span>></span></span>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">服务端渲染</h3>
<p>采用服务端渲染端方式，可以使用户更快的看到渲染完成的页面</p>
<p>服务端渲染，需要起一个<code>node</code>服务，可以使用<code>express</code>、<code>koa</code>等，调用<code>react</code>的<code>renderToString</code>方法，将根组件渲染成字符串，再输出到响应中</p>
<p>例如：</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> &#123; renderToString &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom/server"</span>;
<span class="hljs-keyword">import</span> MyPage <span class="hljs-keyword">from</span> <span class="hljs-string">"./MyPage"</span>;
app.get(<span class="hljs-string">"/"</span>, <span class="hljs-function">(<span class="hljs-params">req, res</span>) =></span> &#123;
  res.write(<span class="hljs-string">"<!DOCTYPE html><html><head><title>My Page</title></head><body>"</span>);
  res.write(<span class="hljs-string">"<div id='content'>"</span>);  
  res.write(renderToString(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyPage</span>/></span></span>));
  res.write(<span class="hljs-string">"</div></body></html>"</span>);
  res.end();
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>客户端使用render方法来生成HTML</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> ReactDOM <span class="hljs-keyword">from</span> <span class="hljs-string">'react-dom'</span>;
<span class="hljs-keyword">import</span> MyPage <span class="hljs-keyword">from</span> <span class="hljs-string">"./MyPage"</span>;
ReactDOM.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">MyPage</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">'app'</span>));
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-10">其他</h3>
<p>除此之外，还存在的优化手段有组件拆分、合理使用<code>hooks</code>等性能优化手段...</p>
<h2 data-id="heading-11">三、总结</h2>
<p>通过上面初步学习，我们了解到<code>react</code>常见的性能优化可以分成三个层面：</p>
<ul>
<li>代码层面</li>
<li>工程层面</li>
<li>框架机制层面</li>
</ul>
<p>通过这三个层面的优化结合，能够使基于<code>react</code>项目的性能更上一层楼</p>
<h2 data-id="heading-12">参考文章</h2>
<ul>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fvue3js.cn%2Finterview%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vue3js.cn/interview/" ref="nofollow noopener noreferrer">web前端面试 - 面试官系列</a></li>
</ul></div>  
</div>
            