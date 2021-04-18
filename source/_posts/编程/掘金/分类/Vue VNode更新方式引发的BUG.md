
---
title: 'Vue VNode更新方式引发的BUG'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08531aaf2bd46b8ae7fbbf5029bdb3a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sun, 18 Apr 2021 00:57:22 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08531aaf2bd46b8ae7fbbf5029bdb3a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>近几日在调试一些“祖传代码”，遇到了vue更新使用VNode方式时带来的一些问题，于是乎费劲“九牛二虎”之力，终于找到了问题的根源，以后在此类代码设计中也算是增加了点经验，避免再次踩坑。项目中所使用的Vue版本：</p>
<p><strong>Vue.js v2.6.12</strong></p>
<h2 data-id="heading-0">问题背景</h2>
<p>由于原本的业务代码经过不断“迭代”已经比较复杂，相关操作逻辑散落在“代码海洋”的各处，这里简单描述一下问题的场景。</p>
<p><strong>组件在一个区域内可以自由拖动位置，有以下两种方法可以改变组件的位置</strong></p>
<ul>
<li>鼠标移动组件</li>
<li>通过快捷方式将组件快速移动到特定位置</li>
</ul>
<p>使用简单的示意图</p>
<p><img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b08531aaf2bd46b8ae7fbbf5029bdb3a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>红色区块可以通过鼠标进行移动，也可以通过右边两个按钮可以分布直接定位到左上角、右上角。业务场景经过简化后，其实是比较简单和清晰的，但是真实情况中，由于各个业务逻辑耦合，导致各个代码功能耦合，还是比较难以直接定位问题关键原因的。</p>
<h2 data-id="heading-1">问题现象</h2>
<p>通过鼠标移动红色区块后，再次通过右边两个快捷按钮进行定位，无法定位到左上角或者右上角，只能实现靠左以及靠右定位的效果。有兴趣的可以自己操作以下尝试一番，<a href="https://github.com/flyingbirdhub/vnode" target="_blank" rel="nofollow noopener noreferrer">代码链接</a></p>
<h2 data-id="heading-2">问题原因</h2>
<h3 data-id="heading-3">首先可以确认的是点击右边按钮之后，vuex中的属性值被改变成了期望值</h3>
<p>这点可以借助与vue的调试工具来证明</p>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f667b6cf02d14e3b9836aa789e3d2293~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>这时我们可以再看一下代码中样式渲染逻辑</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"container"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"root"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">ref</span>=<span class="hljs-string">"el"</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"block"</span> <span class="hljs-attr">:style</span>=<span class="hljs-string">"style"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是说，<strong>在vuex的style属性值更新后，Vue并没有能正确渲染组件el的样式</strong>，那究竟是什么原因造成这一结果呢？？？</p>
<h3 data-id="heading-4">Vue响应式原理</h3>
<p>经过一番定位后，基本上可以确认是Vue在重新渲染组件样式时出了问题，组件的样式并没有按照我们的设定值进行渲染，因为<strong>渲染出来的组件样式，与我们设置的style值并不一致</strong>, 此时通过chrome调试功能查看组件的样式，可以看到组件的样式为：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">div</span> <span class="hljs-attr">data-v-160ac6a1</span>=<span class="hljs-string">""</span> <span class="hljs-attr">class</span>=<span class="hljs-string">"block"</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"inset: 38px auto auto 0px;"</span>></span><span class="hljs-tag"></<span class="hljs-name">div</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件的top值被渲染成了38px，并不是我们所期望的0。</p>
<p>此时我们不得不深入Vue的响应式中进行查看，正如大家所知道的那样，组件的渲染其实是一个大的Watcher，在相应状态改变后，会调用这个Watcher对页面进行渲染，给各个组件设置正确的状态。</p>
<p>而在组件的渲染中，Vue为了减少渲染的工作量，尽量避免渲染不需要改变的节点，使用了VNode的概念，每个VNode与真实渲染的DOM一一对应，<strong>在渲染真实的DOM之前，会对更新前后的VNode状态进行比较，如果更改前后的VNode状态是一样的，Vue就会跳过这个VNode对应DOM的更新</strong>。</p>
<h3 data-id="heading-5">VNode更新</h3>
<p>于是，我们就是查看Vue更新Style的函数，由于代码较多，这里省略一些分支判断逻辑和注释，关注代码主干逻辑。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-function"><span class="hljs-keyword">function</span> <span class="hljs-title">updateStyle</span> (<span class="hljs-params">oldVnode, vnode</span>) </span>&#123;
  <span class="hljs-keyword">var</span> data = vnode.data;
  <span class="hljs-keyword">var</span> oldData = oldVnode.data;
  <span class="hljs-keyword">var</span> cur, name;
  <span class="hljs-keyword">var</span> el = vnode.elm;
  <span class="hljs-keyword">var</span> oldStaticStyle = oldData.staticStyle;
  <span class="hljs-keyword">var</span> oldStyleBinding = oldData.normalizedStyle || oldData.style || &#123;&#125;;
  <span class="hljs-comment">// ...</span>
  <span class="hljs-keyword">var</span> oldStyle = oldStaticStyle || oldStyleBinding;
  <span class="hljs-keyword">var</span> newStyle = getStyle(vnode, <span class="hljs-literal">true</span>)；
  <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> oldStyle) &#123;
    <span class="hljs-keyword">if</span> (isUndef(newStyle[name])) &#123;
      setProp(el, name, <span class="hljs-string">''</span>);
    &#125;
  &#125;
  <span class="hljs-keyword">for</span> (name <span class="hljs-keyword">in</span> newStyle) &#123;
    cur = newStyle[name];
    <span class="hljs-keyword">if</span> (cur !== oldStyle[name]) &#123;
      setProp(el, name, cur == <span class="hljs-literal">null</span> ? <span class="hljs-string">''</span> : cur);
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在setProp之前，会对更新前后的VNode上的style值进行比较，如果更新前后VNode的值相同就会跳过这个属性的更新。</p>
<p>通过chrome调试控制台查看newStyle和oldStyle值：</p>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/033552c64e134b0d9d23bebd5a2f35e7~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>基本上可以看出来问题所在了，<strong>VNode中的top值仍然是0，并不是当前DOM真实的top值</strong></p>
<h3 data-id="heading-6">问题根因</h3>
<p>为什么VNode中的值和DOM中的真实值不一致呢，<strong>这时应该就要考虑出了通过Vue响应式原理更新DOM属性值，是不是还有其他地方通过其他方式更新了DOM属性值？</strong></p>
<p>很明显，在组件拖动过程中，我们<strong>通过直接改变DOM的值改变了DOM的属性状态，但是并没有改变vuex中style的值</strong>，造成了VNode的状态和DOM中状态不一致的结果。</p>
<h2 data-id="heading-7">解决方法</h2>
<p><strong>在移动过程中通过改变vuex中style属性值来改变组件的样式，而不是通过直接改变DOM样式。</strong></p>
<p>思考：收敛更改状态的入口，可以在日常业务的代码海洋中减少此类问题的出现频率。</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            