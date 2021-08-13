
---
title: '这7个 Vue 模式，可能你经常用！但现在看对你很有帮助！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=7594'
author: 掘金
comments: false
date: Thu, 12 Aug 2021 16:11:56 GMT
thumbnail: 'https://picsum.photos/400/300?random=7594'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>说实话，阅读文档并不是我们大多数人喜欢的事情，但是当使用像Vue这样不断发展的现代前端框架时，每一个新版本都会有所变化，我们很有可爱已经错过了一些后来推出的新且好用的功能。</p>
<p>今天，刷碗智带大家来看看那些有趣但不那么流行的功能。记住，所有这些都是官方<a href="https://link.juejin.cn/?target=https%3A%2F%2Fvuejs.org%2Fv2%2Fguide%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://vuejs.org/v2/guide/" ref="nofollow noopener noreferrer">Vue文档的一部分</a>。</p>
<h3 data-id="heading-0">1. 处理加载状态</h3>
<p>在大型项目中，我们可能需要将组件分成小块，只有在需要时才从服务器上加载。为了更容易做到这一点，Vue允许我们将组件定义为一个工厂函数，异步地解析组件定义。Vue只会在组件需要渲染的时候触发工厂函数，并把结果缓存起来以备后面的重新渲染。2.3版的新内容是，异步组件工厂还可以返回以下格式的对象。</p>
<pre><code class="copyable">const AsyncComponent = () => (&#123;
  // 需要加载的组件 (应该是一个 `Promise` 对象)
  component: import('./MyComponent.vue'),
  // 异步组件加载时使用的组件
  loading: LoadingComponent,
  // 加载失败时使用的组件
  error: ErrorComponent,
  // 展示加载时组件的延时时间。默认值是 200 (毫秒)
  delay: 200,
  // 如果提供了超时时间且组件加载也超时了，
  // 则使用加载失败时使用的组件。默认值是：`Infinity`
  timeout: 3000
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用这种方法，我们有额外的选项，包括加载和错误状态、组件获取的延迟和超时。</p>
<h3 data-id="heading-1">2.通过 <code>v-once</code> 创建低开销的静态组件</h3>
<p>渲染普通的 HTML 元素在 Vue 中是非常快速的，但有的时候你可能有一个组件，这个组件包含了大量静态内容。在这种情况下，我们可以在根元素上添加 <code>v-once</code> attribute 以确保这些内容只计算一次然后缓存起来，就像这样：</p>
<pre><code class="copyable">Vue.component('terms-of-service', &#123;
  template: `
    <div v-once>
      <h1>Terms of Service</h1>
      ... a lot of static content ...
    </div>
  `
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<blockquote>
<p>更多详细内容看官网：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fcn.vuejs.org%2Fv2%2Fguide%2Fcomponents-edge-cases.html" target="_blank" rel="nofollow noopener noreferrer" title="https://cn.vuejs.org/v2/guide/components-edge-cases.html" ref="nofollow noopener noreferrer">cn.vuejs.org/v2/guide/co…</a></p>
</blockquote>
<h3 data-id="heading-2">3.递归组件</h3>
<p>组件是可以在它们自己的模板中调用自身的。不过它们只能通过 <code>name</code> 选项来做这件事：</p>
<pre><code class="copyable">name: 'unique-name-of-my-component'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>当你使用 <code>Vue.component</code> 全局注册一个组件时，这个全局的 ID 会自动设置为该组件的 name 选项。</p>
<pre><code class="copyable">Vue.component('unique-name-of-my-component', &#123;
  // ...
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>稍有不慎，递归组件就可能导致无限循环：</p>
<pre><code class="copyable">name: 'stack-overflow',
template: '<div><stack-overflow></stack-overflow></div>'
<span class="copy-code-btn">复制代码</span></code></pre>
<p>类似上述的组件将会导致<code>“max stack size exceeded”</code>错误，所以请确保递归调用是条件性的 (例如使用一个最终会得到 <code>false</code> 的 <code>v-if</code>)。</p>
<h3 data-id="heading-3">4.内联模板</h3>
<p>当 <code>inline-template</code> 这个特殊的 <code>attribute</code> 出现在一个子组件上时，这个组件将会使用其里面的内容作为模板，而不是将其作为被分发的内容。这使得模板的撰写工作更加灵活。</p>
<pre><code class="copyable"><my-component inline-template>
  <div>
    <p>These are compiled as the component's own template.</p>
    <p>Not parent's transclusion content.</p>
  </div>
</my-component>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>内联模板需要定义在 Vue 所属的 DOM 元素内。</p>
<blockquote>
<p>不过，<code>inline-template</code> 会让模板的作用域变得更加难以理解。所以作为最佳实践，请在组件内优先选择 <code>template</code> 选项或 .vue 文件里的一个 <code><template></code> 元素来定义模板。</p>
</blockquote>
<h3 data-id="heading-4">5. 动态指令参数</h3>
<p>指令的参数可以是动态的。例如，在 <code>v-mydirective:[argument]="value"</code> 中，<code>argument </code>参数可以根据组件实例数据进行更新！这使得自定义指令可以在应用中被灵活使用。</p>
<p>例如你想要创建一个自定义指令，用来通过固定布局将元素固定在页面上。我们可以像这样创建一个通过指令值来更新竖直位置像素值的自定义指令：</p>
<pre><code class="copyable"><div id="dynamicexample">
  <h3>Scroll down inside this section ↓</h3>
  <p v-pin:[direction]="200">I am pinned onto the page at 200px to the left.</p>
</div>
Vue.directive('pin', &#123;
  bind: function (el, binding, vnode) &#123;
    el.style.position = 'fixed'
    var s = (binding.arg == 'left' ? 'left' : 'top')
    el.style[s] = binding.value + 'px'
  &#125;
&#125;)

new Vue(&#123;
  el: '#dynamicexample',
  data: function () &#123;
    return &#123;
      direction: 'left'
    &#125;
  &#125;
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">6.事件 & 按键修饰符</h3>
<p>对于 <code>.passive</code>、<code>.capture</code> 和 <code>.once</code> 这些事件修饰符，Vue 提供了相应的前缀可以用于 on：</p>

























<table><thead><tr><th>修饰符</th><th>前缀</th></tr></thead><tbody><tr><td>.passive</td><td>&</td></tr><tr><td>.capture</td><td>!</td></tr><tr><td>.once</td><td>~</td></tr><tr><td>.capture.once 或.once.capture</td><td>~!</td></tr></tbody></table>
<p>例如：</p>
<pre><code class="copyable">on: &#123;
  '!click': this.doThisInCapturingMode,
  '~keyup': this.doThisOnce,
  '~!mouseover': this.doThisOnceInCapturingMode
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于所有其它的修饰符，私有前缀都不是必须的，因为你可以在事件处理函数中使用事件方法：</p>





























<table><thead><tr><th>修饰符</th><th>处理函数中的等价操作</th></tr></thead><tbody><tr><td><code>.stop</code></td><td><code>event.stopPropagation()</code></td></tr><tr><td><code>.prevent</code></td><td><code>event.preventDefault()</code></td></tr><tr><td><code>.self</code></td><td><code>if (event.target !== event.currentTarget) return</code></td></tr><tr><td>按键：<code>.enter</code>, <code>.13</code></td><td><code>if (event.keyCode !== 13) return</code> (对于别的按键修饰符来说，可将 <code>13</code> 改为另一个按键码)</td></tr><tr><td>修饰键：<code>.ctrl</code>, <code>.alt</code>, <code>.shift</code>, <code>.meta</code></td><td><code>if (!event.ctrlKey) return</code> (将 <code>ctrlKey</code> 分别修改为 <code>altKey</code>、<code>shiftKey</code> 或者 <code>metaKey</code>)</td></tr></tbody></table>
<h3 data-id="heading-6">7.依赖注入</h3>
<p>在Vue中，有几种方法可以让两个组件进行通信，所有这些方法都有优点和缺点。<code>2.2</code>版本中引入的一种新方法是使用 <code>Provide/Inject</code> 的依赖注入。</p>
<p>这对选项一起使用，允许一个祖先组件作为其所有后代的依赖注入器，无论组件层次有多深，只要它们在同一个父链上。如果你熟悉React，这与React的上下文功能非常相似。</p>
<pre><code class="copyable">// parent component providing 'foo'
var Provider = &#123;
  provide: &#123;
    foo: 'bar'
  &#125;,
  // ...
&#125;

// child component injecting 'foo'
var Child = &#123;
  inject: ['foo'],
  created () &#123;
    console.log(this.foo) // => "bar"
  &#125;
  // ...
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>今天就到这了，就这？</p>
<p>~完，我是刷碗智，疫情只能在家 LoL 了。</p>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.fundebug.com%2F%3Futm_source%3Dxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://www.fundebug.com/?utm_source=xiaozhi" ref="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<h2 data-id="heading-7">交流</h2>
<p>文章每周持续更新，可以微信搜索「 大迁世界 」第一时间阅读和催更（比博客早一到两篇哟），本文 GitHub <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fqq449245884%2Fxiaozhi" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/qq449245884/xiaozhi" ref="nofollow noopener noreferrer">github.com/qq449245884…</a>  已经收录，整理了很多我的文档，欢迎Star和完善，大家面试可以参照考点复习，另外关注公众号，后台回复<strong>福利</strong>，即可看到福利，你懂的。</p></div>  
</div>
            