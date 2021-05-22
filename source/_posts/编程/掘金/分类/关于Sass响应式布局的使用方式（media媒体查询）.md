
---
title: '关于Sass响应式布局的使用方式（media媒体查询）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797aec2057a41caa1bc177fcf8bbb1c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 22 May 2021 02:16:31 GMT
thumbnail: 'https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797aec2057a41caa1bc177fcf8bbb1c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">前言</h3>
<p>当我们在做PC端页面的时候，免不了与<strong>响应式</strong>布局打交道。这篇文章就是为了记录一下我在工作中遇到的问题：如何使用sass来做响应式布局。</p>
<h3 data-id="heading-1">业务场景</h3>
<p>假设此时有两个<code>div</code>，并排排列。在视窗宽度小于<code>1000px</code>的时候，变成竖直排列的状态。运行环境的话选择vue脚手架创建出来的项目。</p>
<p>然后创建vue文件。代码如下所示：</p>
<pre><code class="hljs language-vue copyable" lang="vue"><template>
  <div class="media_test">
    <div id="box1">
      <p>这是box1</p>
    </div>
    <div id="box2">
      <p>这是box2</p>
    </div>
  </div>
</template>

<script>
export default &#123;
  name: "Test"
&#125;
</script>

<style scoped lang="scss">
#box1 &#123;
  box-sizing: border-box;
  width: 50%;
  height: 300px;
  display: inline-block;
  background-color: coral;
  color: white;
  padding: 10px;
&#125;

#box2 &#123;
  box-sizing: border-box;
  width: 50%;
  height: 300px;
  display: inline-block;
  background-color: mediumpurple;
  color: white;
  padding: 10px;
&#125;
</style>

<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/8797aec2057a41caa1bc177fcf8bbb1c~tplv-k3u1fbpfcp-watermark.image" alt="媒体查询之前.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果我们想要在<code>1000px</code>以下的时候，让两个<code>div</code>上下叠在一起的话，用媒体查询我们需要这么写：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1000px</span>)&#123;
  <span class="hljs-selector-id">#box1</span> &#123;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">background-color</span>: coral;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
  <span class="hljs-selector-id">#box2</span> &#123;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">background-color</span>: mediumpurple;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
&#125;
<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">375px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">999px</span>)&#123;
  <span class="hljs-selector-id">#box1</span> &#123;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background-color</span>: coral;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  &#125;
  <span class="hljs-selector-id">#box2</span> &#123;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">background-color</span>: mediumpurple;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在<code>1000px</code>下的运行结果如图：</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a3dcf59a3ec2457d9842db1d1294a7a6~tplv-k3u1fbpfcp-watermark.image" alt="小于1000px.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-2">将公共代码抽取进@mixin中</h4>
<p>但是，很显然这么写的话过于繁琐。那我们可以将这些公共代码抽取出来作为<code>@mixin</code>函数，然后传入参数，再使用参数作为判断条件选择使用不同的css代码；</p>
<p>代码改造如下：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-keyword">@mixin</span> boxStyle ( <span class="hljs-variable">$screenWidth</span> )&#123;
  <span class="hljs-selector-id">#box1</span> &#123;
    <span class="hljs-keyword">@if</span> ( <span class="hljs-variable">$screenWidth</span> == <span class="hljs-number">1600</span>) &#123;
      <span class="hljs-attribute">display</span>: inline-block;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    &#125;<span class="hljs-keyword">@else</span> if( <span class="hljs-variable">$screenWidth</span> == <span class="hljs-number">1000</span> ) &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
      <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    &#125;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">background-color</span>: coral;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
  <span class="hljs-selector-id">#box2</span> &#123;
    <span class="hljs-keyword">@if</span> ( <span class="hljs-variable">$screenWidth</span> == <span class="hljs-number">1600</span>) &#123;
      <span class="hljs-attribute">display</span>: inline-block;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
      <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
    &#125;<span class="hljs-keyword">@else</span> if( <span class="hljs-variable">$screenWidth</span> == <span class="hljs-number">1000</span> ) &#123;
      <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
      <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
      <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
    &#125;
    <span class="hljs-attribute">box-sizing</span>: border-box;
    <span class="hljs-attribute">background-color</span>: mediumpurple;
    <span class="hljs-attribute">color</span>: white;
    <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
  &#125;
&#125;

<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1000px</span>)&#123;
  <span class="hljs-keyword">@include</span> boxStyle( <span class="hljs-number">1600</span> );
&#125;
<span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">375px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">999px</span>)&#123;
  <span class="hljs-keyword">@include</span> boxStyle( <span class="hljs-number">1000</span> );
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这个代码的话还可以再继续拆分，抽取公共代码，但是就太繁琐了，这里就没必要演示了。</p>
<p>接下来还有第二种方法：</p>
<h4 data-id="heading-3">sass中的@media嵌套</h4>
<p>在sass中，<code>@media</code>标签经过了处理，既可以像普通的<code>media</code>标签一样使用。还具有sass赋予的独特的能力——可以在css规则中嵌套。具体的使用方法可以参见官网： <a href="https://www.sass.hk/docs/" target="_blank" rel="nofollow noopener noreferrer">sass中的@media</a>。</p>
<p>还是上面的例子，我们可以这么写：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-selector-id">#box1</span> &#123;
  <span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1000px</span>)&#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
  &#125;
  <span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">375px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">999px</span>)&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  &#125;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">background-color</span>: coral;
  <span class="hljs-attribute">color</span>: white;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="hljs-selector-id">#box2</span> &#123;
  <span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">1000px</span>)&#123;
    <span class="hljs-attribute">display</span>: inline-block;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">50%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">300px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">16px</span>;
  &#125;
  <span class="hljs-keyword">@media</span> screen <span class="hljs-keyword">and</span> (<span class="hljs-attribute">min-width</span>: <span class="hljs-number">375px</span>) <span class="hljs-keyword">and</span> (<span class="hljs-attribute">max-width</span>: <span class="hljs-number">999px</span>)&#123;
    <span class="hljs-attribute">width</span>: <span class="hljs-number">100%</span>;
    <span class="hljs-attribute">height</span>: <span class="hljs-number">150px</span>;
    <span class="hljs-attribute">font-size</span>: <span class="hljs-number">14px</span>;
  &#125;
  <span class="hljs-attribute">box-sizing</span>: border-box;
  <span class="hljs-attribute">background-color</span>: mediumpurple;
  <span class="hljs-attribute">color</span>: white;
  <span class="hljs-attribute">padding</span>: <span class="hljs-number">10px</span>;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>运行结果的话和之前是一模一样的。</p>
<h3 data-id="heading-4">结语</h3>
<p>这两种方法都可以让我们最大程度的精简代码。但是具体孰优孰劣我暂时还没有定夺。如果你觉得哪种方式更好，或者有什么建议的话可以在评论区告诉我。最后，无论是sass，还是@media标签，还是响应式布局。都有太多需要学习的地方了。希望自己以后懂的东西越来越多吧</p></div>  
</div>
            