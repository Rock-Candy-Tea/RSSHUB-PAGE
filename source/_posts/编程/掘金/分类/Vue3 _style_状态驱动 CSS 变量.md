
---
title: 'Vue3 _style_状态驱动 CSS 变量'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=2005'
author: 掘金
comments: false
date: Thu, 15 Jul 2021 22:34:57 GMT
thumbnail: 'https://picsum.photos/400/300?random=2005'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>用法就是在style中使用关键方法 <code>v-bind()</code>，vue回去实例里找到对象变量并加入style变量中。</p>
<blockquote>
<p>在前面版本中可能是 <code><style vars="&#123; color &#125;"></code> 这样。</p>
</blockquote>
<p>新版是如下：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><script>
export default &#123;
  data() &#123;
    return &#123;
      color: red
    &#125;;
  &#125;
&#125;;
</script>

<style>
.box &#123;
  background: v-bind("color");
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-0">这东西用途在哪里？</h2>
<ul>
<li>其一，做动态主题肯定是可行这块没有太多值得说的。</li>
<li>其二，我想说的是它可以减少<code><template></code>\ <code><script></code>中的计算属性使其各执其职</li>
</ul>
<h2 data-id="heading-1">在vue2中里可能会有如下操作</h2>
<h3 data-id="heading-2">案例一</h3>
<p>使用 <code>:style</code> 动态改变其样式。</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about" :style="&#123; width: size + 'px', height: size + 'px' &#125;">
    <span>This is an about page</span>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      size: 100
    &#125;;
  &#125;,
  mounted() &#123;
    setInterval(() => &#123;
      this.size = Math.floor(Math.random() * 500) + 100;
    &#125;, 1 * 1000);
  &#125;
&#125;;
</script>

<style>
.about &#123;
  width: 100px;
  height: 100px;
  background: red;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-3">案例二</h3>
<p>使用 <code>compute</code> 计算属性触发其样式</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about" :style="aboutStyle">
    <span>This is an about page</span>
  </div>
</template>

<script>
export default &#123;
  data() &#123;
    return &#123;
      size: 100
    &#125;;
  &#125;,
  computed: &#123;
    aboutStyle() &#123;
      return &#123;
        width: this.size + "px",
        height: this.size + "px"
      &#125;;
    &#125;
  &#125;,
  mounted() &#123;
    setInterval(() => &#123;
      this.size = Math.floor(Math.random() * 500) + 100;
    &#125;, 1 * 1000);
  &#125;
&#125;;
</script>

<style>
.about &#123;
  width: 100px;
  height: 100px;
  background: red;
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-4">但这一切在Vue3你可以~</h2>
<ul>
<li>你可以不用写两份默认值</li>
<li><code><template></code>\ <code><script></code>中减少不必要的样式状态</li>
</ul>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="about">
    <span>This is an about page</span>
  </div>
</template>

<script>
export default &#123;
  inject: ["theme"],
  data() &#123;
    return &#123;
      size: 100
    &#125;;
  &#125;,
  mounted() &#123;
    setInterval(() => &#123;
      this.size = Math.floor(Math.random() * 500) + 100;
    &#125;, 1 * 1000);
  &#125;
&#125;;
</script>

<style scoped>
.about &#123;
  width: v-bind(size + "px");
  height: v-bind(size + "px");
  background: v-bind("theme.color");
&#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">语法上值得的注意</h2>
<p>可以使用如下几种方式😊:</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="text">hello</div>
</template>

<script>
  export default &#123;
    data() &#123;
      return &#123;
        color: "red",
        font: &#123;
          size: "2em",
        &#125;,
        view: &#123;
          size: 100
        &#125;
      &#125;
    &#125;,
    compute: &#123;
        width() &#123;
            return this.view.size;
        &#125;
    &#125;
  &#125;
</script>

<style>
  .text &#123;
    color: v-bind(color);
    font-size: v-bind('font.size');
    width: v-bind(width + "px");
    height: v-bind(`$&#123;view.size&#125;px`);
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>绝不可以☹️:</p>
<pre><code class="hljs language-vue copyable" lang="vue"><style>
  .text &#123;
    height: v-bind("view.size" + "px");
  &#125;
</style>
<span class="copy-code-btn">复制代码</span></code></pre></div>  
</div>
            