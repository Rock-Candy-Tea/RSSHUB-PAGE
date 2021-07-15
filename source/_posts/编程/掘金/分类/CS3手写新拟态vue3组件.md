
---
title: 'CS3手写新拟态vue3组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aee8ce49efd74e048171bf9e798ec68e~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 14 Jul 2021 00:57:29 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aee8ce49efd74e048171bf9e798ec68e~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">CS3手写新拟态vue3组件</h1>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aee8ce49efd74e048171bf9e798ec68e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-1">按钮的拟态组件效果</h4>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <button>
    <slot></slot>
  </button>
</template>

<script lang="ts">
import &#123; defineComponent &#125; from "vue";

export default defineComponent(&#123;
  setup() &#123;
    //不能为空
  &#125;,
&#125;);
</script>


<style scoped>
button &#123;
  border: none;
  padding: 20px 40px;
  cursor: pointer;
  font-weight: 500;
  letter-spacing: 2px;
  color: #5a84a2;
  font-size: 18px;
  border-radius: 60px;
  background-color: #ecf0f3;
  box-shadow: -2px -2px 8px rgba(255, 255, 255, 1),
    -2px -2px 12px rgba(255, 255, 255, 0.5),
    inset 2px 2px 4px rgba(255, 255, 255, 0.1), 2px 2px 8px rgba(0, 0, 0, 0.15);
&#125;

button:hover &#123;
  box-shadow: inset -2px -2px 8px rgba(255, 255, 255, 1),
    inset -2px -2px 12px rgba(255, 255, 255, 0.5),
    inset 2px 2px 4px rgba(255, 255, 255, 0.1),
    inset 2px 2px 8px rgba(0, 0, 0, 0.15);
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-2">下拉框拟态组件</h4>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="dropdown">
    <button class="dropbtn">
      <slot name="title"></slot>
    </button>
    <div class="dropdown-content">
      <slot name="item"></slot>
    </div>
  </div>
</template>
<script lang="ts">
import &#123; defineComponent &#125; from "vue";

export default defineComponent(&#123;
  setup() &#123;
    // 不能为空
  &#125;,
&#125;);
</script>

  <style scoped>
.dropbtn &#123;
  box-shadow: -5px -5px 12px rgba(255, 255, 255, 1),
    -5px -5px 16px rgba(255, 255, 255, 0.5),
    inset 5px 5px 8px rgba(255, 255, 255, 0.1), 5px 5px 12px rgba(0, 0, 0, 0.15);
  background: #ecf0f3;
  color: #5a84a2;
  border-radius: 10px;
  padding: 20px 30px;
  font-size: 16px;
  border: none;
  cursor: pointer;
&#125;

.dropdown &#123;
  position: relative;
  display: inline-block;
&#125;

.dropdown-content &#123;
  display: none;
  position: absolute;
  border-radius: 10px;
  cursor: pointer;
  color: #5a84a2;
  min-width: 130px;
  box-shadow: -5px -5px 12px rgba(255, 255, 255, 1),
    -5px -5px 16px rgba(255, 255, 255, 0.5),
    inset 5px 5px 8px rgba(255, 255, 255, 0.1), 5px 5px 12px rgba(0, 0, 0, 0.15);
&#125;

.dropdown-content div &#123;
  border-radius: 10px;
  color: #5a84a2;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
&#125;

.dropdown-content div:hover &#123;
  box-shadow: inset -5px -5px 12px rgba(255, 255, 255, 1),
    inset -5px -5px 16px rgba(255, 255, 255, 0.5),
    inset 5px 5px 8px rgba(255, 255, 255, 0.1),
    inset 5px 5px 12px rgba(0, 0, 0, 0.15);
&#125;

.dropdown:hover .dropdown-content &#123;
  display: block;
&#125;

.dropdown:hover .dropbtn &#123;
  box-shadow: inset -5px -5px 12px rgba(255, 255, 255, 1),
    inset -5px -5px 16px rgba(255, 255, 255, 0.5),
    inset 5px 5px 8px rgba(255, 255, 255, 0.1),
    inset 5px 5px 12px rgba(0, 0, 0, 0.15);
&#125;
</style>
  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在父组件中可以这样引用</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-comment"><!-- 按钮组件 --></span>
<span class="hljs-tag"><<span class="hljs-name">Neu_button</span>></span> 按钮 <span class="hljs-tag"></<span class="hljs-name">Neu_button</span>></span>
<span class="hljs-comment"><!-- 下拉框组件 --></span>
    <span class="hljs-tag"><<span class="hljs-name">Neu_dropdown</span> <span class="hljs-attr">style</span>=<span class="hljs-string">"padding-left:50px"</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:title</span>></span> 下拉框 <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">template</span> <span class="hljs-attr">v-slot:item</span>></span>
        <span class="hljs-comment"><!-- 需要加样式 --></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>111<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>111<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>222<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>111<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
        <span class="hljs-tag"><<span class="hljs-name">div</span>></span>111<span class="hljs-tag"></<span class="hljs-name">div</span>></span>
      <span class="hljs-tag"></<span class="hljs-name">template</span>></span>
    <span class="hljs-tag"></<span class="hljs-name">Neu_dropdown</span>></span>

<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-3">拟态头像框</h4>
<pre><code class="hljs language-vue copyable" lang="vue"><div class="inner-shadow-ring item"> </div>
    <div class="inner-shadow-ring-2 item"> </div>

<style>
.item &#123;
  position: relative;
  width: 200px;
  height: 200px;
  margin-left: 80px;
  margin-top: 80px;
  background: #ecf0f3;
&#125;
.inner-shadow-ring &#123;
  border-radius: 100%;
  box-shadow: 9px 9px 15px #d1d9e6, -9px -9px 15px #fff;
&#125;

.inner-shadow-ring:before &#123;
  content: "";
  position: absolute;
  left: 10%;
  top: 10%;
  width: 80%;
  height: 80%;
  border-radius: 100%;
  background: #ecf0f3;
  background-image:url(../../public/head.jpg);
  background-position: 50% 50%;
  background-size:100% 100%;
  box-shadow: inset 9px 9px 15px #d1d9e6, inset -9px -9px 15px #fff;
&#125;
.inner-shadow-ring-2 &#123;
  border-radius: 100%;
  box-shadow: inset 9px 9px 15px #d1d9e6, inset -9px -9px 15px #fff;
&#125;

.inner-shadow-ring-2:before &#123;
  content: "";
  position: absolute;
  left: 10%;
  top: 10%;
  width: 80%;
  height: 80%;
  border-radius: 100%;
  background: #ecf0f3;
  background-image:url(../../public/head.jpg);
  background-position: 50% 50%;
  background-size:100% 100%;
  box-shadow: 9px 9px 15px #d1d9e6, -9px -9px 15px rgb(247, 247, 247);
  /* box-shadow: inset 3px 3px 15px #d1d9e6, inset -3px -3px 15px #fff; */
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            