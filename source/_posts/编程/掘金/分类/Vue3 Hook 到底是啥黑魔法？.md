
---
title: 'Vue3 Hook 到底是啥黑魔法？'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=8838'
author: 掘金
comments: false
date: Wed, 28 Jul 2021 21:21:25 GMT
thumbnail: 'https://picsum.photos/400/300?random=8838'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>早就听说，<code>React</code>社区，已经全面拥抱<code>Hook</code>。<code>Vue3</code>的发布也支持了自定义<code>Hook</code>，作为只会<code>Vue</code>的前端小码农自然要去看看<code>Vue3 Hook</code>到底是啥黑魔法？</p>
<p>个人博客网站欢迎交流：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fblog.xkongkeji.com" target="_blank" rel="nofollow noopener noreferrer" title="https://blog.xkongkeji.com" ref="nofollow noopener noreferrer">萤火之森：https://blog.xkongkeji.com</a></p>
<h3 data-id="heading-0">从不了解React Hook的角度来看一下啥是Hook？</h3>
<ul>
<li>Vue 官方给出的自定义 <code>Hook</code> 的例子是这样的：</li>
</ul>
<pre><code class="copyable">import &#123; ref, onMounted, onUnmounted &#125; from "vue";

export function useMousePosition() &#123;
  const x = ref(0);
  const y = ref(0);

  function update(e) &#123;
    x.value = e.pageX;
    y.value = e.pageY;
  &#125;

  onMounted(() => &#123;
    window.addEventListener("mousemove", update);
  &#125;);

  onUnmounted(() => &#123;
    window.removeEventListener("mousemove", update);
  &#125;);

  return &#123; x, y &#125;;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>组件中使用：</p>
<pre><code class="copyable">import &#123; useMousePosition &#125; from "./mouse";

export default &#123;
  setup() &#123;
    const &#123; x, y &#125; = useMousePosition();
    return &#123; x, y &#125;;
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>相信写<code>vue2</code>的小伙伴应该都有被<code>Mixin</code>支配过，特别是拿到应该不熟悉的项目的时候，简直是噩梦，各种<code>Mixin</code>，各种变量，方法，完全看不出从哪来的。</p>
<p>从代码中使用中可以清晰的找到鼠标位置<code>X</code>,<code>Y</code>来自于<code>useMousePosition</code>函数，<code>useMousePosition</code>就是一个函数，使用了<code>composition-api</code>定义了响应式数据<code>X</code>，<code>Y</code>然后导出，个人感觉是将<code>mixin</code>拆分了，将导入的操作交给了开发者，以前是vue直接帮我们把数据合并在了一起，反而导致了数据无从溯源的问题。</p>
<h4 data-id="heading-1">个人理解，欢迎纠正</h4>
<ul>
<li><code>hook</code>可以当作以前<code>mixin</code>的来用</li>
<li><code>hook</code>是一个函数，<code>mixin</code>是一个对象</li>
<li><code>hook</code>就是拆分版的<code>mixin</code>，将导入操作交给开发者，<code>mixin</code>是根据对应的<code>options Api</code>直接merge到组件了</li>
<li><code>hook</code>可以借用<code>composition-api</code>完全使用<code>vue</code>的能力，简而言之就是你在<code>setup</code>函数用能用的<code>hook</code>都能用.</li>
</ul>
<h3 data-id="heading-2">参考</h3>
<p>1、[精读《Vue3.0 Function API》] <a href="https://juejin.cn/post/6844903877574295560" target="_blank" title="https://juejin.cn/post/6844903877574295560">juejin.cn/post/684490…</a></p>
<p>2、[Vue3 究竟好在哪里？（和 React Hook 的详细对比）])]<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsegmentfault.com%2Fa%2F1190000022616689" target="_blank" rel="nofollow noopener noreferrer" title="https://segmentfault.com/a/1190000022616689" ref="nofollow noopener noreferrer">segmentfault.com/a/119000002…</a></p></div>  
</div>
            