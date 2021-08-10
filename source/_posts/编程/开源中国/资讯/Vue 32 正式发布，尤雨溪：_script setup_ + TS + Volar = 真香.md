
---
title: 'Vue 3.2 正式发布，尤雨溪：_script setup_ + TS + Volar = 真香'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://static.oschina.net/uploads/space/2021/0810/171312_nphG_2720166.png'
author: 开源中国
comments: false
date: Tue, 10 Aug 2021 09:41:00 GMT
thumbnail: 'https://static.oschina.net/uploads/space/2021/0810/171312_nphG_2720166.png'
---

<div>   
<div class="content">
                                                                                            <p>今日凌晨，尤雨溪<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-3.2.html" target="_blank">宣布</a> Vue 3.2 正式发布（代号"Quintessential Quintuplets"），此版本增加了许多重要的新特性和性能改进，且不包含破坏性变更。</p> 
<p><img src="https://static.oschina.net/uploads/space/2021/0810/171312_nphG_2720166.png" referrerpolicy="no-referrer"></p> 
<h2>单文件组件 (SFC) 的新特性</h2> 
<p>单文件组件（SFC，又称作<code>.vue</code> 文件）的两项实验特性已毕业，现已提供稳定版本：</p> 
<ul> 
 <li> <p><code><script setup></code>属于编译时 (compile-time) 语法糖，可显著提升在 SFC 中使用 Composition API 时的开发效率</p> </li> 
 <li> <p><code><style> v-bind</code> 用于在 SFC <code><style></code> 标签中启用组件状态驱动的动态 CSS 值</p> </li> 
</ul> 
<p>使用示例</p> 
<pre><code class="language-javascript"><script setup>
import &#123; ref &#125; from 'vue'

const color = ref('red')
</script>

<template>
  <button @click="color = color === 'red' ? 'green' : 'red'">
    Color is: &#123;&#123; color &#125;&#125;
  </button>
</template>

<style scoped>
button &#123;
  color: v-bind(color);
&#125;
</style></code></pre> 
<p>在线体验：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fsfc.vuejs.org%2F%23eyJBcHAudnVlIjoiPHNjcmlwdCBzZXR1cD5cbmltcG9ydCB7IHJlZiB9IGZyb20gJ3Z1ZSdcblxuY29uc3QgY29sb3IgPSByZWYoJ3JlZCcpXG48L3NjcmlwdD5cblxuPHRlbXBsYXRlPlxuICA8YnV0dG9uIEBjbGljaz1cImNvbG9yID0gY29sb3IgPT09ICdyZWQnID8gJ2dyZWVuJyA6ICdyZWQnXCI%2BXG4gICAgQ29sb3IgaXM6IHt7IGNvbG9yIH19XG4gIDwvYnV0dG9uPlxuPC90ZW1wbGF0ZT5cblxuPHN0eWxlIHNjb3BlZD5cbmJ1dHRvbiB7XG4gIGNvbG9yOiB2LWJpbmQoY29sb3IpO1xufVxuPC9zdHlsZT4ifQ%3D%3D" target="_blank">SFC Playground</a>。相关文档：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fapi%2Fsfc-script-setup.html" target="_blank"><span style="color:null"><code><span style="background-color:null"><script setup></span></code></span></a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fapi%2Fsfc-style.html%23state-driven-dynamic-css" target="_blank"><span style="color:null"><code><span style="background-color:null"><style> v-bind</span></code></span></a></li> 
</ul> 
<p>对于<code><script setup></code>特性，尤雨溪<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fweibo.com%2F1761511274%2FKsLQMi36O%3Ffrom%3Dpage_1005051761511274_profile%26wvr%3D6%26mod%3Dweibotime%26type%3Dcomment" target="_blank">表示</a>，“<script setup> + TS + Volar = 真香”。</p> 
<p><img height="623" src="https://static.oschina.net/uploads/space/2021/0810/172423_MKWQ_2720166.png" width="727" referrerpolicy="no-referrer"></p> 
<h2>Web 组件</h2> 
<p>Vue 3.2 引入了新的<code>defineCustomElement</code>方法，支持使用 Vue 组件 API 轻松创建原生<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FWeb_Components%2FUsing_custom_elements" target="_blank">自定义元素</a>：</p> 
<pre><code class="language-javascript">import &#123; defineCustomElement &#125; from 'vue'

const MyVueElement = defineCustomElement(&#123;
  // normal Vue component options here
&#125;)

// Register the custom element.
// After registration, all `<my-vue-element>` tags
// on the page will be upgraded.
customElements.define('my-vue-element', MyVueElement)</code></pre> 
<h2>性能改进</h2> 
<p>Vue 3.2 针对响应式系统进行了重要的性能优化：</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fpull%2F3995" target="_blank">更高效的 ref 实现（读取速度提升约 260%，写入速度提升约 50%）</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fpull%2F4017" target="_blank">依赖跟踪速度提升约 40%</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fpull%2F4001" target="_blank">内存使用量减少约 17%</a></li> 
</ul> 
<p>以及优化模板编译器的性能：</p> 
<ul> 
 <li> <p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fpull%2F3334" target="_blank">创建 VNode 的速度提升约 200%</a></p> </li> 
 <li> <p>更激进的 constant hoisting [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2Fb7ea7c148552874e8bce399eec9fbe565efa2f4d" target="_blank">1</a>] [<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Fcommit%2F02339b67d8c6fab6ee701a7c4f2773139ed007f5" target="_blank">2</a>]</p> </li> 
</ul> 
<p>最后，新增的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fv3.vuejs.org%2Fapi%2Fdirectives.html%23v-memo" target="_blank"><code>v-memo</code>指令</a>提供了针对部分模板树进行 memoize 的能力，并显著提升了性能。</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-0fe10f6e09325c90410e0d838fc244b468d.png" referrerpolicy="no-referrer"></p> 
<h2>服务器端渲染</h2> 
<p>Vue 3.2 的<code>@vue/server-renderer</code>包现已提供 ES module build，并与 Node.js 的内置模块解耦。因此，开发者可在非 Node.js runtime 中（例如 CloudFlare Workers 和 Service Workers）绑定和使用<code>@vue/server-renderer</code>。</p> 
<p>此版本还改进了流式渲染 API，为 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FStreams_API" target="_blank">Web Streams API</a> 的渲染提供了新方法。详情查看<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvue-next%2Ftree%2Fmaster%2Fpackages%2Fserver-renderer%23streaming-api" target="_blank"><code>@vue/server-renderer</code></a>文档。</p> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fblog.vuejs.org%2Fposts%2Fvue-3.2.html" target="_blank">更多内容查看发布公告</a>。</p>
                                        </div>
                                      
</div>
            