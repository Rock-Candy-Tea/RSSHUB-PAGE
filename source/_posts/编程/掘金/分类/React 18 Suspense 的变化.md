
---
title: 'React 18 Suspense 的变化'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=4683'
author: 掘金
comments: false
date: Thu, 19 Aug 2021 02:29:50 GMT
thumbnail: 'https://picsum.photos/400/300?random=4683'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文源于翻译 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F7" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/7" ref="nofollow noopener noreferrer">Behavioral changes to Suspense in React 18</a></p>
</blockquote>
<h2 data-id="heading-0">概述</h2>
<p>在 React 16.x 版本中，我们基本支持了 Suspense 功能。但是，那时并没有完美支持 Suspense，在我们的示例中有一些东西并未展示出来，比如延迟变化（解析数据完成之后进行状态转换）、占位符节流（限制嵌套和连续的占位符来减少 UI 抖动）和 SuspenseList（调整列表或栅格组件，如按顺序流式处理）等。为了方便做区分，我们把 React 16 和 17 版本中的 Suspense 称为 Legacy Suspense。</p>
<p>我们全套的 Suspense 功能依赖于 Concurrent React，这些功能将会在 React 18 版本里面支持。这意味着 Suspense 在 React 18 中的工作方式与以前的版本会略有不同。从技术上来说，这是一个突破性的变化，但与自动批处理更新一样，预计会对现有代码的影响相对较小，并且不会对应用程序的迁移造成较大的负担。</p>
<p>本文主要讨论 Suspense 的行为差异 —— 影响用户组件代码兼容性的部分。</p>
<h2 data-id="heading-1">术语说明</h2>
<p><strong>这个功能本身仍然被称为 "Suspense"</strong></p>
<p>Legacy Suspense 和 Concurrent Suspense 之间的区别只在迁移的背景下才重要。因为我们希望大多数人在升级时不会遇到任何重大障碍，所以在迁移场景之外，我们不会提到这些术语。</p>
<h2 data-id="heading-2">悬停组件的兄弟组件会被中断</h2>
<h3 data-id="heading-3">简单解释</h3>
<p>Legacy Suspense 和 Concurrent Suspense 两者的基本的用户体验是一致的。在下面的代码示例中，组件 <code>ComponentThatSuspends</code> 在请求处理数据过程中，React 会在它的位置上展示 <code>Loading</code> 组件：</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><Suspense fallback=&#123;<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Loading</span> /></span></span>&#125;>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ComponentThatSuspends</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Sibling</span> /></span></span>
</Suspense>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>两者的不同点主要体现在悬停组件 (suspended component) 对其同级组件渲染带来的影响：</p>
<ul>
<li>Legacy Suspense 中，同级兄弟组件会立即从 DOM 上卸载（mounted），相关的 effects 和生命周期会被触发，最后会隐藏这个组件。具体可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fkeen-banach-nzut8%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/keen-banach-nzut8?file=/src/App.js" ref="nofollow noopener noreferrer">代码示例</a>。</li>
<li>Concurrent Suspense 中，同级兄弟组件并不会从 DOM 上卸载，相关的 effects 和生命周期会在 <code>ComponentThatSuspends</code> 处理完成时触发。具体可以查看<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcodesandbox.io%2Fs%2Fromantic-architecture-ht3qi%3Ffile%3D%2Fsrc%2FApp.js" target="_blank" rel="nofollow noopener noreferrer" title="https://codesandbox.io/s/romantic-architecture-ht3qi?file=/src/App.js" ref="nofollow noopener noreferrer">代码示例</a>。</li>
</ul>
<h3 data-id="heading-4">详细解释</h3>
<p>在以往的 React 版本里，已经形成这样一个固有印象，当一个组件开始渲染那么就一定会完成渲染。例如，在类组件的渲染过程中，<code>render</code> 方法和组件的 <code>componentDidMount/Update</code> 生命周期是 1:1 对应的。虽然大多数开发人员并没有真正思考过这个过程，也没有下意识的使用它，但是有可能无意中依赖它而没有意识到。</p>
<p>不难发现，这点对于一些功能是特别重要的，Suspense 的作用就是延迟子组件的渲染，直到组件树依赖的数据解析完成再进行渲染。如果某个组件还没有准备好提交 (commit) 操作，我们该如何处理它的兄弟节点，其中一些可能已经开始渲染了？(例如，如果列表中的第三个组件处于悬停中，而前两个组件的 <code>render</code> 方法将被调用。）</p>
<p>当我们第一次引入 Legacy Suspense 时，我们发现了一种保持 1:1 render-commit 对应关系的巧妙方法：我们将跳过悬停的组件，继续渲染兄弟组件，并尽可能多地更新到 DOM。这意味着 DOM 会出现不一致的状态，但我们可以避免这种情况，因为无论如何，我们将用一个 fallback UI 来替换它。在允许浏览器绘制之前，我们将显示 fallback UI，并使用<code>display:hidden</code> 隐藏 Suspense 边界内的所有内容。</p>
<p>使用这个小技巧，兄弟节点的渲染行为不受影响，但从用户的角度来看，他们看不到任何不一致：他们只看到一个占位符。</p>
<p>Legacy Suspense 的实现方式虽然听起来有点奇怪，但它却是一个很好的折衷方案，以向后兼容的方式引入了 Suspense 的基本功能。</p>
<p>在 Concurrent Suspense 中，我们所做的是中断兄弟组件并阻止他们提交到 DOM 树。直到相关数据被处理之后，才会将 Suspense 边界内的内容进行提交，这里面包括被悬停的组件和它的兄弟节点。然后将批量处理成一个一致的状态提交到的整个树。无论是从实现的复杂性方面，还是以此为基础支持的功能，这都比较适合我们的渲染模型。从开发人员的角度来看，这可以说是一种更可预测的行为，因为副作用不应该渲染在页面上（这已经被阻止了）。</p>
<p>因此，需要让我们的代码能够支持这种中断。这与使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Freactwg%2Freact-18%2Fdiscussions%2F41" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/reactwg/react-18/discussions/41" ref="nofollow noopener noreferrer">startTransition</a> 有着同样的要求。通常，这些实现中都涉及将副作用 (effect) 和突变 (mutation) 从渲染阶段移动到提交阶段。可以使用 Strict Mode 在开发过程中尽早发现这些类型的 bug。</p>
<h2 data-id="heading-5">Suspense 边界之外的 ref</h2>
<p>另一个差异实际上也是 render-commit 问题引起的：父级 ref 传入的时间。</p>
<pre><code class="hljs language-JavaScript copyable" lang="JavaScript"><span class="hljs-keyword">const</span> refPassedFromParent = useRef(<span class="hljs-literal">null</span>)
<Suspense fallback=&#123;<span class="xml"><span class="hljs-tag"><<span class="hljs-name">Loading</span> /></span></span>&#125;>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">ComponentThatSuspends</span> /></span></span>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">button</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">&#123;refPassedFromParent&#125;</span> &#123;<span class="hljs-attr">...buttonProps</span>&#125; /></span></span>
</Suspense>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在 Legacy Suspense 中，在渲染之初 <code>refPassedFromParent.current</code> 立即指向 DOM 节点，此时 <code>ComponentThatSuspends</code> 还未处理完成。</p>
<p>在 Concurrent Suspense 中，在 <code>ComponentThatSuspends</code> 完成处理、Suspense 边界解除锁定之前 <code>refPassedFromParent.current</code> 一直为 null。</p>
<p>也就是说，在父级代码中访问此类 ref 都需要关注当前 ref 是否已经指向相应的节点。</p>
<p>我们认为这导致行为出现差异的可能性很低，事实上，新的行为与 React 的其它的渲染模型更加一致。但值得注意的是，它可能会影响现有代码。</p>
<hr>
<p>微信关注公众号 <strong>ikoofe</strong>， 「<a href="https://link.juejin.cn/?target=https%3A%2F%2Fp3-juejin.byteimg.com%2Ftos-cn-i-k3u1fbpfcp%2Ff37bc98a8bae45269ca7982cbb0d344a~tplv-k3u1fbpfcp-zoom-1.image" target="_blank" rel="nofollow noopener noreferrer" title="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f37bc98a8bae45269ca7982cbb0d344a~tplv-k3u1fbpfcp-zoom-1.image" ref="nofollow noopener noreferrer">KooFE前端团队</a>」不定期发布前端技术文章。</p></div>  
</div>
            