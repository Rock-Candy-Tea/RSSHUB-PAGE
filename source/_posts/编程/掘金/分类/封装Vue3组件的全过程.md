
---
title: '封装Vue3组件的全过程'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97615dd6a0d940059e7b132cb51f7e98~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 27 Aug 2021 01:30:37 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97615dd6a0d940059e7b132cb51f7e98~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body html cache"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>这是我参与8月更文挑战的第7天，活动详情查看：<a href="https://juejin.cn/post/6987962113788493831" target="_blank" title="https://juejin.cn/post/6987962113788493831">8月更文挑战</a></p>
<p>在前端开发中使用组件可以大幅度提升整个项目的开发效率，而且使项目更容易维护。
这里楼主以封装一个 Loader 组件为例，记录其封装过程。</p>
<h5 data-id="heading-0">需求分析</h5>
<p>1、全局 Loader 组件<br>
2、实现自定义显示文案及背景颜色（主要考虑到不需要背景的场景）<br>
3、实现 loading 动画</p>
<h5 data-id="heading-1">基础编码</h5>
<p>准备工作：新建 Loader.vue 文件</p>
<pre><code class="copyable">// Loader.vue
<template>
  <div class="loader" :style="&#123;background: background&#125;">
      <div>
        <div class="icon-loading"></div>
        <label class="text-loading">&#123;&#123; text &#125;&#125;</label>
      </div>
    </div>
</template>

<script lang="ts">
import &#123; defineComponent, onUnmounted &#125; from 'vue'
export default defineComponent(&#123;
  props: &#123;
    text: &#123;
      type: String,
      default: '加载中...'
    &#125;,
    background: &#123;
      type: String
    &#125;
  &#125;
&#125;)
</script>

<style>
  // todo
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>可以看出组件接收两个参数：<br>
（1）text: 提升文案。默认为“加载中...”<br>
（2）background：背景颜色。</p>
<p>下面继续完成样式部分</p>
<pre><code class="copyable"><style>
.loader&#123;
  width: 100%;
  height: 100%;
  position: fixed;
  top: 0;
  left: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgba(0,0,0,.2);
&#125;
.loader>div&#123;
  width: 130px;
  height: 130px;
  border-radius: 15px;
  background-color: rgba(0,0,0,.5);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
&#125;
.loader .text-loading&#123;
  color: #fff;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h5 data-id="heading-2">组件使用及效果</h5>
<p>template部分</p>
<pre><code class="copyable"><Loader v-if="!loading"></Loader>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>ts部分</p>
<pre><code class="copyable">import &#123; useStore &#125; from 'vuex'
import Loader from './components/Loader.vue'

setup () &#123;
    const store = useStore();
    const loading = computed(() => store.state.loading);
    return &#123;
      loading
    &#125;
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>基础效果：<br>
<img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/97615dd6a0d940059e7b132cb51f7e98~tplv-k3u1fbpfcp-watermark.image" alt="111.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><strong>继续添加 loading 动画</strong><br>
loading 动画实现的方式多种多样，可以用gif图片，可以用SVG，可以用字体。楼主这里就用CSS3实现一个简单的loading动画</p>
<pre><code class="copyable"><template>
  ...
  <div>
    <div class="icon-loading"></div>
    <label class="text-loading">&#123;&#123; text &#125;&#125;</label>
  </div>
</template>

<style>
.loader .icon-loading&#123;
  width: 30px;
  height: 30px;
  border-radius: 30px;
  margin-bottom: 12px;
  border: 6px solid #518cff;
  border-bottom-color: #f1f1f1;
  animation: loading .8s linear infinite;
&#125;
@keyframes loading &#123;
  to &#123;
    transform: rotate(0deg);
  &#125;
  from &#123;
    transform: rotate(-360deg);
  &#125;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终效果：
<img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/591a3abe2deb4860a1c0f628b3664754~tplv-k3u1fbpfcp-watermark.image" alt="222.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-3">优化组件</h5>
<p>此时已经完成了一个 Loader 组件的封装，我们可以进一步优化。Loader 是一个全局样式的组件，但是现在是被包裹在我们页面内容里面的。所以我们使用 vue3 的传送门技术来优化一下结构。</p>
<p>（1）使用 teleport 标签将组件包裹起来</p>
<pre><code class="copyable"><template>
  <teleport to="#back">
    ...
  </teleport>
</template>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>（2）组件挂载之前在 body 节点新增节点，并在组件卸载时移除节点</p>
<pre><code class="copyable">import &#123; onUnmounted &#125; from 'vue'

setup () &#123;
    const node = document.createElement('div');
    node.id = 'back';
    document.body.appendChild(node);
    onUnmounted(() => &#123;
      document.body.removeChild(node);
    &#125;)
  &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>完！</p></div>  
</div>
            