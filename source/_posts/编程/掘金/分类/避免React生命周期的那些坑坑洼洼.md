
---
title: '避免React生命周期的那些坑坑洼洼'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/787d5de1ea88429e8dd4714b57f6d32e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 24 Mar 2021 17:02:25 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/787d5de1ea88429e8dd4714b57f6d32e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>“如何避免坑？”换种思维思考也就是“为什么会有坑？”在代码编写中，遇到的坑往往会有两种：</p>
<ul>
<li>在不恰当的时机调用了不合适的代码</li>
<li>在需要调用的时候，没有调用</li>
</ul>
<p>-- 来自：伯约文章</p>
<p>要避免生命周期的坑，就需要先了解React有那些生命周期？在React的不同版本生命周期的钩子函数也大同小异。React的生命周期分为三个挂载、更新、销毁阶段，不同的阶段触发不用的钩子函数。接下来我们就一一来看看。</p>
<h3 data-id="heading-0">React 15生命周期</h3>
<p>生命周期测试<a href="https://codesandbox.io/s/react-15-life-test-vj675?file=/src/index.js" target="_blank" rel="nofollow noopener noreferrer">例子</a>，测试版本React 15.7.0</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/787d5de1ea88429e8dd4714b57f6d32e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">组件的初始化渲染（挂载）</h4>
<p><img alt="2.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f99e6b8a70042578288f5aab6870353~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">constructor</h5>
<p>constructor是类的构造函数，在组件初始化的时候只会执行一次，用于初始化state和绑定函数。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"进入constructor"</span>);
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">text</span>: <span class="hljs-string">"这个子组件文本"</span> &#125;;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是随着类属性的流行，我在很多的代码中看到不在写constructor，而是改用类属性。移除constructor的原因无非就是：</p>
<ul>
<li>让代码变得更加简洁</li>
<li>constructor并不是React生命周期的一部分</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifeCycelContainer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">"组件文本"</span>,
    <span class="hljs-attr">hideChild</span>: <span class="hljs-literal">false</span>
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fatherContainer"</span>></span>
        &#123;this.state.text&#125;
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-3">componentWillMount</h5>
<p>该方法也是也是在挂载的时候调用一次，并且方法在render方法之前调用。该方法在React后期的版本就已经标记废弃。原因是在React异步机制下，该生命周期钩子可能会被多次调用。最直观的一个例子，在该方法中写了异步请求，那有可能会被多次触发。</p>
<h5 data-id="heading-4">render</h5>
<p>render方法并不会去真正的操作DOM，它的作用是把需要的东西返回回来。真正渲染的工作，是挂载阶段的ReactDOM.render方法去操作。</p>
<h5 data-id="heading-5">componentDidMount</h5>
<p>componentDidMount方法执行，意味着初始化挂载的操作基本完成。它主要用于组件加载完成时做某些操作，比如发起网络请求、绑定事件或者你已经可以对DOM进行操作了，该函数是接着 render 之后调用的。但 componentDidMount 一定是在真实 DOM 绘制完成之后调用吗？在浏览器端，我们可以这么认为。</p>
<p>但在其他场景下，尤其是 React Native 场景下，componentDidMount 并不意味着真实的界面已绘制完毕。由于机器的性能所限，视图可能还在绘制中。</p>
<h4 data-id="heading-6">组件更新阶段</h4>
<p><img alt="1.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/842a863bfefa49988168ace375a04f92~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-7">componentWillReceiveProps</h5>
<p>该方法在后续的版本已经标记弃用，被getDerivedStateFromProps方法替代。在早起的版本这个方法还是有用的，有用的原因是在很多人其实并没有很明白这个方法到底由什么触发：</p>
<ol>
<li>当父组件修改传递给子组件的属性时，这个修改会带动子组件的对于属性的修改，触发componentWillReceiveProps生命周期。</li>
<li>当父组件触发了个子组件无关的属性也会触发子组件的componentWillReceiveProps，这说明componentWillReceiveProps方法的触发不一定都是由于父组件传递给子组件的属性改变而引入的。</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/72fc82f85b804076b72bf44dbec8a742~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-8">shouldComponentUpdate</h5>
<p>在更新的过程中，会触发render方法来生成新的虚拟DOM，进行diff找出需要修改的DOM。这个过程是很耗费时间的。在实际操作中，我们会无意触发render方法，为了避免不必要的render调用带来的性能消耗，所以React让我们可以在shouldComponent方法决定是否要执行余下的声明周期，默认它是返回true。我们也可以手动设置false，不进行余下的生命周期。</p>
<h5 data-id="heading-9">componentWillUpdate</h5>
<p>在render函数之前执行，运行做一些不涉及真实DOM的操作。后续版本已经被废弃。</p>
<h5 data-id="heading-10">render</h5>
<p>和挂载阶段一致</p>
<h5 data-id="heading-11">componentDidUpdate</h5>
<p>在render函数之后执行，DOM已经更新完成。这个生命周期也经常被用来处理 DOM 操作。此外，我们也常常将 componentDidUpdate 的执行作为子组件更新完毕的标志通知到父组件。</p>
<h4 data-id="heading-12">组件销毁</h4>
<p><img alt="3.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/14f52c23189745faa3fe99f4c2a8d84d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-13">componentWillUnmount</h5>
<p>组件卸载之前触发的生命周期，该函数主要用于执行清理工作。一个比较常见的 Bug 就是忘记在 componentWillUnmount 中取消定时器，导致定时操作依然在组件销毁后不停地执行。所以一定要在该阶段解除事件绑定，取消定时器。在平时写代码的时候如果不解除事件绑定和定时器可能会带来意向不想的问题。</p>
<p>componentWillUnmount会在两种情况下触发</p>
<ul>
<li>组件在父组件中被移除（销毁）</li>
<li>组件设置了KEY属性，父组件在re-render的时候发现key和上一次不一致了就会被移除</li>
</ul>
<h3 data-id="heading-14">React 16生命周期</h3>
<p>对于React16x版本的生命周期可以分为两个版本16.3和>=16.4。有一位大神弄了一个在线查看React生命周期的网页，有兴致的同学可看看，<a href="https://projects.wojtekmaj.pl/react-lifecycle-methods-diagram/" target="_blank" rel="nofollow noopener noreferrer">地址</a>。</p>
<p>生命周期测试<a href="https://juejin.cn/post/undefined">例子</a>，测试版本React 16.3.0</p>
<h4 data-id="heading-15">组件的初始化渲染（挂载）</h4>
<p><img alt="2 (1).png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4f82b237cc0149c78b699bab0fac085d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-16">消失的 componentWillMount，新增的 getDerivedStateFromProps</h5>
<blockquote>
<p>注意这个的getDerivedSatateFromProps不是componentWillMount的替代品 。getRerivedSatateFromProps设计的初衷是为了替代componentWillReceiveProps。但是说用来替代componentWillReceiveProps也不是完全正确。具体的原因我会在后续说明。</p>
</blockquote>
<ul>
<li>getDerivedStateFromProps是一个静态方法，不依赖实例存储，所以在getDerivedStateFromProps方法内是访问不到this的。</li>
</ul>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromProps</span>(<span class="hljs-params">props, state</span>)</span> &#123;
    <span class="hljs-built_in">this</span>.xxx <span class="hljs-comment">//  this -> null</span>
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ul>
<li>getDerivedStateFromProps接受两个参数，第一个参数是接受来自父组件的props，第二参数是当前组件自生的state。</li>
<li>getDerivedStateFromProps需要一个对象格式的返回值，如果你没有返回值，React会发出警告。</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e9bd44422a01434792c86ef68fd562d7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>getReriverSatateFromProps的返回值之所以不可或缺，是因为React需要使用这个返回值来更新组件的state。因此当你确实不存在“使用 props 派生state”这个需求的时候，最好是直接省略掉这个生命周期方法的编写，否则一定记得给它 return 一个 null。</li>
</ul>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/038166024a104317897d6c6e51532bad~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>注意getDerivedStateFromProps对state的更新动作不是覆盖式，是针对性的更新。</li>
</ul>
<h5 data-id="heading-17">其他的生命周期</h5>
<p>16版本和15版本在挂载阶段的其他生命周期如出一辙的，这里就不过多的阐述了。</p>
<h4 data-id="heading-18">组件更新阶段</h4>
<p><img alt="1 (1).png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f07005370b284ee39c861a9144948380~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-19">getRerivedStateFromProps</h5>
<blockquote>
<p>React16.3和>=React16.4版本差异在哪？</p>
</blockquote>
<p>React16.3和>=React16.4版本生命周期在加载和卸载都是一样的，差异就在更新阶段。在React16.4中，任何因素触发的组件的更新（包括this.setState和forceUpdate触发的更新流程）都会触发getRerivedStateFromProps，在React.16.3只有在父组件更新是会触发getRerivedStateFromProps。</p>
<p>这里请记住，在不同版本getRerivedStateFromProps方法的触发源点可能不同。</p>
<blockquote>
<p>为什么要用getRerivedStateFromProps代替componentWillReceivedProps?</p>
</blockquote>
<p>其实getRerivedStateProps并不能完全替代componentWillReceivedProps，而是保证了这个方法的单一性，相对来说是在做一个合理的减法。getRerivedSatetFromProps方法是一个静态方法，是拿不到组件实例的this，这就导致你无法咋在这个方法内做this.fetch、不合理的this.setState，这类副作用的操作。</p>
<p>因此，getDerivedStateFromProps 生命周期替代 componentWillReceiveProps 的背后，是 React 16 在强制推行『只用 getDerivedStateFromProps 来完成 props 到 state 的映射』这一最佳实践。意在确保生命周期函数的行为更加可控可预测，从根源上帮开发者避免不合理的编程方式，避免生命周期的滥用；</p>
<h5 data-id="heading-20">getSnapshotBeforeUpdate</h5>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 组件更新时调用</span>
  <span class="hljs-function"><span class="hljs-title">getSnapshotBeforeUpdate</span>(<span class="hljs-params">prevProps, prevState</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"getSnapshotBeforeUpdate方法执行"</span>);
    <span class="hljs-keyword">return</span> <span class="hljs-string">"haha"</span>;
  &#125;
  <span class="hljs-comment">// 组件更新后调用</span>
  <span class="hljs-function"><span class="hljs-title">componentDidUpdate</span>(<span class="hljs-params">prevProps, prevState, valueFromSnapshot</span>)</span> &#123;
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"componentDidUpdate方法执行"</span>);
    <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"从 getSnapshotBeforeUpdate 获取到的值是"</span>, valueFromSnapshot);
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/30a9abdcd50648239d3319b4ac976eff~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>getSnapshotBeforeUpdate是render方法之后，DOM更新之前执行。</li>
<li>getSnapshotBeforeUpdate的返回值会作为componentDidUpdate的第三个参数。</li>
<li>getSnapshotBeforeUpdate可以获取到跟新之前的DOM和更新之后的state、pprops。</li>
</ul>
<h4 data-id="heading-21">组件销毁</h4>
<p>16版本销毁阶段和15无差异。如果有不了解，请回看15版本声明周期的销毁阶段。</p>
<h3 data-id="heading-22">React15 和 React16的本质差别</h3>
<p>在16版本开始React引入了Fiber架构。Fiber是React 16 对React核心算法的一次重写。Fiber的核心就是原本的同步渲染变成了异步渲染。</p>
<h4 data-id="heading-23">Fiber的初衷</h4>
<p>Fiber的初衷就是解决React 15版本中JS无控制的长期占用主线程导致白屏、卡顿等情况。JavaScript在浏览器的主线程上运行，恰好与样式计算、布局以及许多情况下的绘制一起运行。如果JavaScript运行时间过长，就会阻塞这些其他工作，也可能导致掉帧。</p>
<h4 data-id="heading-24">Fiber核心目标</h4>
<ul>
<li>把可中断的工作拆分成小任务</li>
<li>对正在做的工作调整优先次序、重做、复用上次</li>
<li>在父子任务之间从容切换（yield back and forth），以支持React执行过程中的布局刷新</li>
<li>支持render()返回多个元素</li>
<li>更好地支持error boundary</li>
</ul>
<h4 data-id="heading-25">没有Fiber架构</h4>
<p>在React16之前，每当组件更新时，都会生成一个新的虚拟DOM。然后和上一次的虚拟DOM进行diff，找出差异实现更新。这个过程是一个递归的过程。只要没有到最后一步，就会一直递归，最可怕的是，这是一个串行的过程，可想而知这有多么恐怖。</p>
<p>同步渲染的递归调用栈是非常深的，只有底层调用返回了，这个渲染过程才会逐层返回。但是同步的过程中，会导致主线程不能做其他事情，直到递归完成，还有就是如果这个递归渲染的时间过程，会造成页面的卡顿或者卡死。</p>
<h4 data-id="heading-26">有Fiber架构</h4>
<p>在React16之后，引入了Fiber架构，Fiber将一个大的更新任务拆分成很多小的任务，每一个小的任务完成字后，渲染线程会把主线程交还回去，看看有没有优先级更高的工作需要处理，从而避免卡顿的情况。在整个过程中，线程不在是一去不回头的状态了，而是可以被打断的，这就是所谓的"异步渲染"。</p>
<h3 data-id="heading-27">换一个角度来看生命周期工作流</h3>
<p>在上面说到React16之后的一个重大变革就是引入了Fiber架构，整个架构吧同步渲染变成了异步渲染，在异步渲染的过程中，这个异步是可以被"打断"的，但是注意"打断"是有原则的。</p>
<h4 data-id="heading-28">什么时候可以被打断？</h4>
<p><img alt class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7e83ee97c492402cac601e13ec6e4806~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
如图，在React16中，生命周期被划分成两个阶段，render和commit。commit又可以细分为pre-commmit和commit。</p>
<ul>
<li>render阶段：纯净没有副作用，可以暂停、重启、终止。</li>
<li>pre-commit阶段：可以读取DOM.</li>
<li>commit阶段：可以使用DOM，运行副作用，安排更新。</li>
</ul>
<p>在render阶段是可以被打断的，而commit阶段是不可以被打断的，同步执行。</p>
<blockquote>
<p>Why? render阶段可以被打断，commit阶段就不行了</p>
</blockquote>
<p>因为render阶段的操作对用户是不可见的，无论怎么操作对用户来说都是零感知，但是commit阶段涉及到真实DOM的渲染，如果在用户眼皮下胡乱的更改视图，哪也太胆大包天了。</p>
<h3 data-id="heading-29">为什么要变更生命周期？</h3>
<p>我们在回过头在想想为什么在React要"废旧立新"。在React16废弃了:</p>
<ul>
<li>componentWillMount</li>
<li>componentWillUpdate</li>
<li>componentReceiveProps</li>
</ul>
<p>这三个生命周期，这三个生命周期的共性就是出于render阶段，都可能被重复执行。重复执行的过程可能有很多风险：</p>
<ul>
<li>componentWillxxx方法的异步请求可能被触发多次</li>
<li>componentWillxxx方法里面滥用setState导致重复渲染出现死循环。</li>
</ul>
<p>所以，React16改造生命周期的主要动机就是配合Fiber架构带来的异步渲染。在改造的过程中，针对生命周期中长期被滥用的部分推行了具有强制性的最佳实践。</p>
<h3 data-id="heading-30">生命周期的那些坑坑洼洼</h3>
<p>上面介绍了在不同版本的生命周期，那在生命周期中有那些坑了。开篇提到，出现坑就是在：</p>
<ul>
<li>在不恰当的时机调用了不合适的代码</li>
<li>在需要调用的时候，没有调用</li>
</ul>
<p>那避免这些坑就是</p>
<ul>
<li>不在恰当的时机调用不合适的代码</li>
<li>在需要调用的时候，去正确调用。</li>
</ul>
<h4 data-id="heading-31">函数组件的无效触发</h4>
<p>函数组件是一种无状态的组件，无生命周期，它在任何情况下都会被触发。看个[例子]</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">import</span> React <span class="hljs-keyword">from</span> <span class="hljs-string">"react"</span>;
<span class="hljs-keyword">import</span> ReactDom <span class="hljs-keyword">from</span> <span class="hljs-string">"react-dom"</span>;

<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">TestComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"我重新渲染了"</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>函数组件：1<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifeCycle</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">"这个子组件文本"</span>,
      <span class="hljs-attr">message</span>: <span class="hljs-string">"这个是子组件消息"</span>
    &#125;;
  &#125;
  changeText = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">"修改后的子组件文本"</span>
    &#125;);
  &#125;;
  changeMessage = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">"修改后的子组件消息"</span>
    &#125;);
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"container"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeText&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"changeText"</span>></span>
          修改子组件文本内容
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeMessage&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"changeText"</span>></span>
          修改子组件消息
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.text&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"textContent"</span>></span>
          <span class="hljs-tag"><<span class="hljs-name">TestComponent</span> /></span>
        <span class="hljs-tag"></<span class="hljs-name">p</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

<span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifeCycelContainer</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  state = &#123;
    <span class="hljs-attr">text</span>: <span class="hljs-string">"父组件文本"</span>,
    <span class="hljs-attr">message</span>: <span class="hljs-string">"父组件消息"</span>
  &#125;;
  changeText = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">text</span>: <span class="hljs-string">"修改后的父组件文本"</span>
    &#125;);
  &#125;;
  changeMessage = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-built_in">this</span>.setState(&#123;
      <span class="hljs-attr">message</span>: <span class="hljs-string">"修改后的父组件消息"</span>
    &#125;);
  &#125;;
  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">return</span> (
      <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"fatherContainer"</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeText&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"changeText"</span>></span>
          修改父组件文本
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">onClick</span>=<span class="hljs-string">&#123;this.changeText&#125;</span> <span class="hljs-attr">className</span>=<span class="hljs-string">"changeText"</span>></span>
          修改父组件消息
        <span class="hljs-tag"></<span class="hljs-name">button</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.text&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.state.message&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">LifeCycle</span> /></span>
      <span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>
    );
  &#125;
&#125;

ReactDom.render(<span class="xml"><span class="hljs-tag"><<span class="hljs-name">LifeCycelContainer</span> /></span></span>, <span class="hljs-built_in">document</span>.getElementById(<span class="hljs-string">"root"</span>));

<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/60f48c84c19547eaaf5113cb640b95ab~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>函数组件任何情况下都会重新渲染。它并没有生命周期，但官方提供了一种方式优化手段，那就是 React.memo。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> MyComponent = React.memo(<span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">MyComponent</span>(<span class="hljs-params">props</span>) </span>&#123;
  <span class="hljs-built_in">console</span>.log(<span class="hljs-string">"memo: 我重新渲染了"</span>);
  <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">div</span>></span>memo函数组件：2<span class="hljs-tag"></<span class="hljs-name">div</span>></span></span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/10b651c512bb487b907620412b6b22a5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>React.memo 并不是阻断渲染，而是跳过渲染组件的操作并直接复用最近一次渲染的结果，这与 shouldComponentUpdate 是完全不同的。</p>
<h4 data-id="heading-32">React.Component的无效触发</h4>
<p>定义shouldComponentUpdate函数来避免无效的触发</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-title">shouldComponentUpdate</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-comment">// xxxx</span>
    <span class="hljs-keyword">return</span> <span class="hljs-literal">false</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-33">React.PureComponent谨慎使用</h4>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">LifeComponent</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">PureComponent</span></span>&#123;
    <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span>&#123;
        <span class="hljs-keyword">return</span> (
            <span class="xml"><span class="hljs-tag"><<span class="hljs-name">p</span>></span>&#123;this.props.title&#125;<span class="hljs-tag"></<span class="hljs-name">p</span>></span></span>
        )
    &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>React.PureComponent 与 React.Component 几乎完全相同，但 React.PureComponent 通过prop和state的浅对比来实现 shouldComponentUpate()。</p>
<p>如果React组件的 render() 函数在给定相同的props和state下渲染为相同的结果，在某些场景下你可以使用 React.PureComponent 来提升性能。</p>
<p>React.PureComponent 的 shouldComponentUpdate() 只会对对象进行浅对比。如果对象包含复杂的数据结构，它可能会因深层的数据不一致而产生错误的否定判断(表现为对象深层的数据已改变视图却没有更新, 原文：false-negatives)。当你期望只拥有简单的props和state时，才去继承 PureComponent ，或者在你知道深层的数据结构已经发生改变时使用 forceUpate() 。或者，考虑使用 不可变对象 来促进嵌套数据的快速比较。</p>
<h4 data-id="heading-34">componentWillMount</h4>
<p>componentWillMount 在 React 中已被标记弃用，不推荐使用，主要原因是新的异步渲染架构会导致它被多次调用。所以网络请求及事件绑定代码应移至 componentDidMount 中。</p>
<p>componentWillMount在页面初始化render之前会执行一次或多次(async rendering)。</p>
<p>很多同学在此生命周期进行请求数据想加快首页的渲染速度，但是由于JavaScript中异步事件的性质，当您启动API调用时，浏览器会在此期间返回执行其他工作。当React渲染一个组件时，它不会等待componentWillMount它完成任何事情，React继续前进并继续render，没有办法“暂停”渲染以等待数据到达。componentDidMount操作更加合适做这些操作。</p>
<h4 data-id="heading-35">componentWillReceiveProps</h4>
<p>componentWillReceiveProps被标记弃用，新版使用 getDerivedStateFromProps 取代，一方面是性能问题，另一方面是从根本上实现代码的最优解，避免副作用。</p>
<h4 data-id="heading-36">componentWillUnmount</h4>
<p>记得在 componentWillUnmount 函数中去处理解除事件绑定，取消定时器等清理操作，以免引起不必要的bug。</p>
<h4 data-id="heading-37">添加边界处理</h4>
<p>默认情况下，若一个组件在渲染期间（render）发生错误，会导致整个组件树全部被卸载。错误边界：是一个组件，该组件会捕获到渲染期间（render）子组件发生的错误，并有能力阻止错误继续传播。</p>
<p>错误边界是一种 React 组件，这种组件可以捕获并打印发生在其子组件树任何位置的 JavaScript 错误，并且，它会渲染出备用 UI，而不是渲染那些崩溃了的子组件树。错误边界在渲染期间、生命周期方法和整个组件树的构造函数中捕获错误。</p>
<blockquote>
<p>注意，错误边界无法捕获以下场景中产生的错误：1、事件处理。2、异步代码（例如 setTimeout 或 requestAnimationFrame 回调函数）。3、服务端渲染。4、它自身抛出来的错误（并非它的子组件）。</p>
</blockquote>
<p>如果一个 class 组件中定义了 static getDerivedStateFromError() 或 componentDidCatch() 这两个生命周期方法中的任意一个（或两个）时，那么它就变成一个错误边界。当抛出错误后，请使用 static getDerivedStateFromError() 渲染备用 UI ，使用 componentDidCatch() 打印错误信息。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">ErrorBoundary</span> <span class="hljs-keyword">extends</span> <span class="hljs-title">React</span>.<span class="hljs-title">Component</span> </span>&#123;
  <span class="hljs-function"><span class="hljs-title">constructor</span>(<span class="hljs-params">props</span>)</span> &#123;
    <span class="hljs-built_in">super</span>(props);
    <span class="hljs-built_in">this</span>.state = &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">false</span> &#125;;
  &#125;

  <span class="hljs-keyword">static</span> <span class="hljs-function"><span class="hljs-title">getDerivedStateFromError</span>(<span class="hljs-params">error</span>)</span> &#123;
    <span class="hljs-comment">// 更新 state 使下一次渲染能够显示降级后的 UI</span>
    <span class="hljs-keyword">return</span> &#123; <span class="hljs-attr">hasError</span>: <span class="hljs-literal">true</span> &#125;;
  &#125;

  <span class="hljs-function"><span class="hljs-title">componentDidCatch</span>(<span class="hljs-params">error, errorInfo</span>)</span> &#123;
    <span class="hljs-comment">// 你同样可以将错误日志上报给服务器</span>
    logErrorToMyService(error, errorInfo);
  &#125;

  <span class="hljs-function"><span class="hljs-title">render</span>(<span class="hljs-params"></span>)</span> &#123;
    <span class="hljs-keyword">if</span> (<span class="hljs-built_in">this</span>.state.hasError) &#123;
      <span class="hljs-comment">// 你可以自定义降级后的 UI 并渲染</span>
      <span class="hljs-keyword">return</span> <span class="xml"><span class="hljs-tag"><<span class="hljs-name">h1</span>></span>Something went wrong.<span class="hljs-tag"></<span class="hljs-name">h1</span>></span></span>;
    &#125;

    <span class="hljs-keyword">return</span> <span class="hljs-built_in">this</span>.props.children; 
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><a href="https://zh-hans.reactjs.org/docs/error-boundaries.html" target="_blank" rel="nofollow noopener noreferrer">代码来源</a></p>
<p>错误边界的工作方式类似于 JavaScript 的 catch &#123;&#125;，不同的地方在于错误边界只针对 React 组件。只有 class 组件才可以成为错误边界组件。大多数情况下, 你只需要声明一次错误边界组件, 并在整个应用中使用它。</p>
<p>注意错误边界仅可以捕获其子组件的错误，它无法捕获其自身的错误。如果一个错误边界无法渲染错误信息，则错误会冒泡至最近的上层错误边界，这也类似于 JavaScript 中 catch &#123;&#125; 的工作机制。</p>
<p><a href="https://codepen.io/gaearon/pen/wqvxGa?editors=0010" target="_blank" rel="nofollow noopener noreferrer">边界处理的例子</a></p>
<h3 data-id="heading-38">总结</h3>
<p>在日常的开发中可能你会遇到这样那样的坑，这里可能只是一些。也可能有些同学说我用的是React hooks，更根本没有这些生命周期，其实不管有没有用其实大致类似，只是模式不一样了。希望对大家有用，也希望更多的同学说出你遇到的坑，大家一起学习！skr~~~~</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            