
---
title: '用了很多动效，介绍 4个很 Nice 的 Vue 路由过渡动效！'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/571794bb5ab84db5ac7c805c5a086454~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Thu, 15 Apr 2021 16:21:43 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/571794bb5ab84db5ac7c805c5a086454~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;color:#595959;font-size:15px;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(60,10,30,.04) 3%,transparent 0),linear-gradient(1turn,rgba(60,10,30,.04) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body p&#123;color:#595959;font-size:15px;line-height:2;font-weight:400&#125;.markdown-body p+p&#123;margin-top:16px&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin:0;color:#135ce0&#125;.markdown-body h1&#123;position:relative;text-align:center;font-size:22px;margin:50px 0&#125;.markdown-body h1:before&#123;position:absolute;content:"";top:-10px;left:50%;width:32px;height:32px;transform:translateX(-50%);background-size:100% 100%;opacity:.36;background-repeat:no-repeat;background:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAABfVBMVEX///8Ad/8AgP8AgP8AgP8Aff8AgP8Af/8AgP8AVf8Af/8Af/8AgP8AgP8Af/8Afv8AAP8Afv8Afv8Aef8AgP8AdP8Afv8AgP8AgP8Acf8Ae/8AgP8Af/8AgP8Af/8Af/8AfP8Afv8AgP8Af/8Af/8Afv8Afv8AgP8Afv8AgP8Af/8Af/8AgP8AgP8Afv8AgP8Af/8AgP8AgP8AgP8Ae/8Afv8Af/8AgP8Af/8AgP8Af/8Af/8Aff8Af/8Abf8AgP8Af/8AgP8Af/8Af/8Afv8AgP8AgP8Afv8Afv8AgP8Af/8Aff8AgP8Afv8AgP8Aff8AgP8AfP8AgP8Ae/8AgP8Af/8AgP8AgP8AgP8Afv8AgP8AgP8AgP8Afv8AgP8AgP8AgP8AgP8AgP8Af/8AgP8Af/8Af/8Aev8Af/8AgP8Aff8Afv8AgP8AgP8AgP8Af/8AgP8Af/8Af/8AgP8Afv8AgP8AgP8AgP8AgP8Af/8AeP8Af/8Af/8Af//////rzEHnAAAAfXRSTlMAD7CCAivatxIDx5EMrP19AXdLEwgLR+6iCR/M0yLRzyFF7JupSXn8cw6v60Q0QeqzKtgeG237HMne850/6Qeq7QaZ+WdydHtj+OM3qENCMRYl1B3K2U7wnlWE/mhlirjkODa9FN/BF7/iNV/2kASNZpX1Wlf03C4stRGxgUPclqoAAAABYktHRACIBR1IAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4gEaBzgZ4yeM3AAAAT9JREFUOMvNUldbwkAQvCAqsSBoABE7asSOBRUVVBQNNuy9996789+9cMFAMHnVebmdm+/bmdtbQv4dOFOW2UjPzgFyLfo6nweKfIMOBYWwFtmMPGz2Yj2pJI0JDq3udJW6VVbmKa9I192VQFV1ktXUAl5NB0cd4KpnORqsEO2ZIRpF9gJfE9Dckqq0KuZt7UAH5+8EPF3spjsRpCeQNO/tA/qDwIDA+OCQbBoKA8NOdjMySgcZGVM6jwcgRuUiSs0nlPFNSrEpJfU0jTLD6llqbvKxei7OzvkFNQohi0vAsj81+MoqsCaoPOQFgus/1LyxichW+hS2JWCHZ7VlF9jb187pIAYcHiViHAMnp5mTjJ8B5xeEXF4B1ze/fTh/C0h398DDI9HB07O8ci+vRBdvdGnfP4gBuM8vw7X/G3wDmFhFZEdxzjMAAAAldEVYdGRhdGU6Y3JlYXRlADIwMTgtMDEtMjZUMDc6NTY6MjUrMDE6MDA67pVWAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDE4LTAxLTI2VDA3OjU2OjI1KzAxOjAwS7Mt6gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAWdEVYdFRpdGxlAGp1ZWppbl9sb2dvIGNvcHlxapmKAAAAV3pUWHRSYXcgcHJvZmlsZSB0eXBlIGlwdGMAAHic4/IMCHFWKCjKT8vMSeVSAAMjCy5jCxMjE0uTFAMTIESANMNkAyOzVCDL2NTIxMzEHMQHy4BIoEouAOoXEXTyQjWVAAAAAElFTkSuQmCC)&#125;.markdown-body h2&#123;position:relative;font-size:20px;border-left:4px solid;padding:0 0 0 10px;margin:30px 0&#125;.markdown-body h3&#123;font-size:16px&#125;.markdown-body ul&#123;list-style:disc outside;margin-left:2em;margin-top:1em&#125;.markdown-body li&#123;line-height:2;color:#595959&#125;.markdown-body img.loaded&#123;margin:0 auto;display:block&#125;.markdown-body blockquote&#123;background:#fff9f9;margin:2em 0;padding:2px 20px;border-left:4px solid #b2aec5&#125;.markdown-body blockquote p&#123;color:#666;line-height:2&#125;.markdown-body a&#123;color:#036aca;border-bottom:1px solid rgba(3,106,202,.8);font-weight:400;text-decoration:none&#125;.markdown-body em strong,.markdown-body strong&#123;color:#036aca&#125;.markdown-body hr&#123;border-top:1px solid #135ce0&#125;.markdown-body pre&#123;overflow:auto&#125;.markdown-body code,.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body table&#123;border-collapse:collapse;margin:1rem 0;overflow-x:auto&#125;.markdown-body table td,.markdown-body table th&#123;border:1px solid #dfe2e5;padding:.6em 1em&#125;.markdown-body table tr&#123;border-top:1px solid #dfe2e5&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f6f8fa&#125;</style><blockquote>
<p>作者：Ahmad shaded
译者：前端小智
来源：sitepoint</p>
</blockquote>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote>
<p>Vue Router 过渡是向Vue应用程序添加个性的一种快速简便的方法。 它让我们可以在应用程序的不同页面之间添加平滑的动画/过渡效果。</p>
<p>如果使用得当，它可以让我们的应用程序更加现代和专业，从而增强用户体验。</p>
<p>在今天的文章中，我们介绍使用Vue Router过渡的基础知识，然后再介绍一些基本示例，希望能给大家一些启发和灵感。</p>
<p>下面我们要创建的四个过渡页面。</p>
<p><img alt="111.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/571794bb5ab84db5ac7c805c5a086454~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-0">将 Vue 路由过渡添加到项目中</h3>
<p>通常，Vue路由器设置如下所示</p>
<pre><code class="copyable">// default template
<template>
  <router-view />
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在旧版本的<strong>Vue Router</strong>中，我们可以简单地用<code><transition></code>组件包装<code><router-view></code>。</p>
<p>然而，在Vue Router的新版本中，我们必须使用<code>v-slot</code>来解构我们的 <code>props</code> ，并将它们传递到我们的内部插槽。这个<code>slow</code>包含一个被<code>transition</code>包围的动态组件。</p>
<pre><code class="copyable"><router-view v-slot="&#123; Component &#125;">
  <transition>
    <component :is="Component" />
  </transition>
</router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-1">每个 Route 都有不同的过渡</h3>
<p>默认情况下，用<code><transition></code>包装<code><component></code>将在我们使用的每条路由上添加相同的过渡。</p>
<p>有两种不同的方法可以为每个路由定制转场。</p>
<h4 data-id="heading-2">将过 transition 移到各个组件部分</h4>
<p>首先，我们可以将<code><transition></code>移到每个单独的组件中，而不是用<code><transition></code>组件来包装我们的动态组件。 如下：</p>
<pre><code class="copyable">// app.vue
<template>
  <transition>
    <div class="wrapper">
      <!-- -->
    </div>
  </transition>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>对于我们想要每个路由都有一个过渡效果，通过这种方式，我们可以通过过渡的名称来定制每个路由。</p>
<h4 data-id="heading-3">使用 v-bind 的动态过渡</h4>
<p>另一种方法是将过渡的名称绑定到一个变量。然后，我们可以根据监听路由动态地改变这个变量。</p>
<pre><code class="copyable"><transition :name="transitionName">
  <component :is="Component" />
</transition>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">watch: &#123;
  '$route' (to, from) &#123;
    const toDepth = to.path.split('/').length
    const fromDepth = from.path.split('/').length
    this.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>现在，我们了解了Vue Router Transition 的基础知识，下面我们来看一些 Nice 的示例。</p>
<h3 data-id="heading-4">1 – Fade Vue Router Transitions</h3>
<p>添渐隐页面过渡可能是我们可以添加到Vue应用程序中最常用的动效之一。</p>
<p>我们可以通过更改元素的<code>opacity</code> 来实现此效果。</p>
<p>首先，我们创建一个带有<code>fade</code>名称的 Vue Router transition。 还要注意的另一件事是，我们将过渡模式设置为 <code>out-in</code>。</p>
<p>有三种不同的过渡模式:</p>
<ul>
<li>
<p><code>default</code> – 进入和离开过渡同时发生</p>
</li>
<li>
<p><code>in-out</code> – 新元素的过渡先进入。然后，当前元素过渡出去。</p>
</li>
<li>
<p><code>out-in</code> - 当前元素先过渡出去。然后，新元素过渡进来。</p>
</li>
</ul>
<p>为了让新元素平滑地淡入，我们需要在开始新的过渡之前删除当前元素。所以我们使用 <code>mode="out-in"</code>。</p>
<p><code><transition></code>为我们提供了几个CSS类，它们在动画周期中被动态添加/删除。</p>
<p>有6个不同的过渡类（3个用于进入，3个用于离开）。</p>
<ol>
<li>
<p><code>v-enter-from</code>：定义进入过渡的开始状态。在元素被插入之前生效，在元素被插入之后的下一帧移除。</p>
</li>
<li>
<p><code>v-leave-from</code>：定义离开过渡的开始状态。在离开过渡被触发时立刻生效，下一帧被移除。</p>
</li>
<li>
<p><code>v-enter-active</code>：定义进入过渡生效时的状态。在整个进入过渡的阶段中应用，在元素被插入之前生效，在过渡/动画完成之后移除。这个类可以被用来定义进入过渡的过程时间，延迟和曲线函数。</p>
</li>
<li>
<p><code>v-leave-active</code>：定义离开过渡生效时的状态。在整个离开过渡的阶段中应用，在离开过渡被触发时立刻生效，在过渡/动画完成之后移除。这个类可以被用来定义离开过渡的过程时间，延迟和曲线函数。</p>
</li>
<li>
<p><code>v-enter-to</code>：定义进入过渡的结束状态。在元素被插入之后下一帧生效 (与此同时 <code>v-enter-from</code> 被移除)，在过渡/动画完成之后移除。</p>
</li>
<li>
<p><code>v-leave-to</code>：离开过渡的结束状态。在离开过渡被触发之后下一帧生效 (与此同时 <code>v-leave-from</code> 被删除)，在过渡/动画完成之后移除。</p>
</li>
</ol>
<p>注意:当我们为过渡提供一个<code>name</code>属性时，这是默认名称。类的格式是<code>name-enter-from</code>、<code>name-enter-active</code>，等等。</p>
<p>我们希望进入和离开状态的<code>opacity</code> 为0。然后，当我们的过渡处生效状态时，对 <code>opacity</code> 进行动画的处理。</p>
<pre><code class="copyable">// fade styles!
.fade-enter-active,
.fade-leave-active &#123;
  transition: opacity 0.5s ease;
&#125;


.fade-enter-from,
.fade-leave-to &#123;
  opacity: 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后的效果 ：</p>
<p><img alt="222.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/404ff01a6d4e4def86f79cc45ad72349~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">2 – Slide Vue Router Transitions</h3>
<p>我们要构建的下一个过渡是幻灯片过渡。</p>
<p>模板如下所示。 由于我们希望进入和离开过渡同时发生，因此使用默认模式即可。</p>
<pre><code class="copyable">// slide transition
<router-view v-slot="&#123; Component &#125;">
  <transition name="slide">
    <component :is="Component" />
  </transition>
</router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>为了让例子更好看，我们给每个页面加上下面的样式：</p>
<pre><code class="copyable">// component wrapper
.wrapper &#123;
  width: 100%;
  min-height: 100vh;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最后，在过渡样式里为要滑动的组件设置相关的属性。如果需要不同的滑动方向，只需更改CSS属性（<code>top</code>, <code>bottom</code>, <code>left</code>, <code>right</code>）。</p>
<pre><code class="copyable">// slide styles!
.slide-enter-active,
.slide-leave-active &#123;
  transition: all 0.75s ease-out;
&#125;


.slide-enter-to &#123;
  position: absolute;
  right: 0;
&#125;


.slide-enter-from &#123;
  position: absolute;
  right: -100%;
&#125;


.slide-leave-to &#123;
  position: absolute;
  left: -100%;
&#125;


.slide-leave-from &#123;
  position: absolute;
  left: 0;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终的效果:</p>
<p><img alt="333.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6fdc9540de984de08c21469f9a81a609~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-6">3 – Scale Vue Router Transitions</h3>
<p>创建缩放过渡与我们的淡入过渡非常相似。 我们再次将模式设置为 <code>out-in</code>，以便我们可以确保动画的正确顺序。</p>
<pre><code class="copyable">// scale transition!

<router-view v-slot="&#123; Component &#125;">
  <transition name="scale" mode="out-in">
    <component :is="Component" />
  </transition>
</router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.scale-enter-active,
.scale-leave-active &#123;
  transition: all 0.5s ease;
&#125;


.scale-enter-from,
.scale-leave-to &#123;
  opacity: 0;
  transform: scale(0.9);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里给整个网页提供黑色的背景色会让过渡看上去更干净。</p>
<p><img alt="444.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c9ca418408244ad98700d9db96e04164~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">4 – Combining Vue Router Transitions</h3>
<p>创建过渡的方式有很多很多但是，我认为不要过度过的，刻意的去做过渡。 过渡动效应该是很小的，微妙的增强功能，而不是会让应用产生干扰因素。</p>
<p>我认为实现较好过渡是将一些更基础的过渡结合在一起。</p>
<p>例如，让我们将幻灯片放大和缩小合并为一个过渡。</p>
<pre><code class="copyable"><router-view v-slot="&#123; Component &#125;">
  <transition name="scale-slide">
    <component :is="Component" />
  </transition>
</router-view>
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="copyable">.scale-slide-enter-active,
.scale-slide-leave-active &#123;
  position: absolute;
  transition: all 0.85s ease;
&#125;


.scale-slide-enter-from &#123;
  left: -100%;
&#125;


.scale-slide-enter-to &#123;
  left: 0%;
&#125;


.scale-slide-leave-from &#123;
  transform: scale(1);
&#125;


.scale-slide-leave-to &#123;
  transform: scale(0.8);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p><img alt="555.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9088c698c14f453d9d9d7b6a577a70d5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>~完，我是刷碗智， 我要去刷碗了，我们下期见！</p>
<p><strong>代码部署后可能存在的BUG没法实时知道，事后为了解决这些BUG，花了大量的时间进行log 调试，这边顺便给大家推荐一个好用的BUG监控工具 <a href="https://www.fundebug.com/?utm_source=xiaozhi" target="_blank" rel="nofollow noopener noreferrer">Fundebug</a>。</strong></p>
<p>原文：<a href="https://learnue.co/2021/01/4-awesome-of-vue-router-transitions/" target="_blank" rel="nofollow noopener noreferrer">learnue.co/2021/01/4-a…</a></p>
<h2 data-id="heading-8">刷碗</h2>
<blockquote>
<p>有梦想，有干货，微信搜索 <strong>【大迁世界】</strong> 关注这个在凌晨还在刷碗的刷碗智。</p>
<p>本文 GitHub  <a href="https://github.com/qq449245884/xiaozhi" target="_blank" rel="nofollow noopener noreferrer">github.com/qq449245884…</a> 已收录，有一线大厂面试完整考点、资料以及我的系列文章。</p>
</blockquote></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            