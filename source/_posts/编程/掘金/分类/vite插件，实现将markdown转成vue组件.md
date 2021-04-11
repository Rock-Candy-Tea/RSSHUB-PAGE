
---
title: 'vite插件，实现将markdown转成vue组件'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=882'
author: 掘金
comments: false
date: Wed, 07 Apr 2021 04:24:11 GMT
thumbnail: 'https://picsum.photos/400/300?random=882'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<p>本文目标是实现vite插件，面向vue做的代码实现，所以代码全是以vue的api形式展示，不过不管什么框架实现思路基本一致。</p>
</blockquote>
<h2 data-id="heading-0">前言</h2>
<p>我们在开发库或者文档系统的时候，希望能够直接将编写的markdown作为组件的内容，目前多数博客提供的解决方案要干两个事</p>
<ol>
<li>利用markdown的解析库将md解析成html内容</li>
<li>在业务中编写一个组件将前一步解析出的html文本作为v-html属性的值</li>
</ol>
<p>那么问题来了，这个承载markdown的组件作用仅仅是提供了插入html文本的容器，而你需要在业务里编写，即便提出到组件库，也需要进行导入和使用，可以说是事倍功半。</p>
<p>所以我们希望能够将编写的md文件直接导入成可使用的组件，比如：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><template>
  <span class="xml"><span class="hljs-tag"><<span class="hljs-name">Start</span> /></span></span>
</template>
<span class="xml"><span class="hljs-tag"><<span class="hljs-name">script</span>></span><span class="javascript">
<span class="hljs-keyword">import</span> &#123; defineComponent &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue'</span>;
<span class="hljs-keyword">import</span> Start <span class="hljs-keyword">from</span> <span class="hljs-string">'docs/start.md'</span>;
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> defineComponent(&#123;  
    <span class="hljs-attr">name</span>: <span class="hljs-string">'App'</span>, 
    <span class="hljs-attr">components</span>: &#123; Start &#125;,
&#125;)
</span><span class="hljs-tag"></<span class="hljs-name">script</span>></span></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>也就是插件需要把前面所提到的两件事都干完，输出一个vue组件。</p>
<h2 data-id="heading-1">实现</h2>
<h3 data-id="heading-2">理清需求</h3>
<p>遇到markdown文件，将内容解析成html，利用vue渲染函数的api编写代码，将html内容插入，最终输出整个代码</p>
<h3 data-id="heading-3">解析markdown文件</h3>
<p>我们采用marked库对markdown文件做解析，所以先安装</p>
<pre><code class="copyable">yarn add marked
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-4">vite插件</h3>
<p>vite插件的使用和基本api可以直接看<a href="https://cn.vitejs.dev/" target="_blank" rel="nofollow noopener noreferrer">中文文档</a>，这里不做赘述，直接看实现。</p>
<p>拦截markdown文件我们利用的是<code>transform</code>，意思是转换，功能类似webpack的loader，基本结构代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// /plugins/vite-plugin-md2vue.js</span>

<span class="hljs-keyword">const</span> marked = <span class="hljs-built_in">require</span>(<span class="hljs-string">'marked'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'vitePluginMd2Vue'</span>,
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">src, id</span>)</span> &#123;
      <span class="hljs-comment">/**
      * id是导入的文件路径
      * src是导入的文件内容
      */</span>
      <span class="hljs-keyword">if</span> (id.endsWith(<span class="hljs-string">".md"</span>)) &#123; <span class="hljs-comment">// 判断结尾字符串判断是否为markdown文件</span>
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">code</span>: <span class="hljs-string">``</span>, <span class="hljs-comment">// code是转换后最终输出的代码</span>
          <span class="hljs-attr">map</span>: <span class="hljs-literal">null</span> <span class="hljs-comment">// 是否提供source map，这里可以不用考虑</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>code中我们需要编写组件代码，但是这里不能使用sfc也就是单文件组件的形式去写，因为vite中会专门拦截<code>.vue</code>结尾的文件去做解析，如果我们直接导出sfc形式的代码，就没有走vite中的解析流程导致报错，所以我们直接编写渲染函数，代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123;h, defineComponent&#125; <span class="hljs-keyword">from</span> <span class="hljs-string">"vue"</span>;
<span class="hljs-keyword">const</span> _sfc_md = defineComponent(&#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">"Markdown"</span>,
&#125;);

<span class="hljs-keyword">const</span> _sfc_render =<span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> h(<span class="hljs-string">"div"</span>, &#123;
      <span class="hljs-comment">// 这里赋值解析好的markdown内容，marked是上一段代码中导入的解析库</span>
      <span class="hljs-comment">// src也是上一段代码中md文件的导入内容，我们直接解析后转成字符串</span>
      <span class="hljs-attr">innerHTML</span>: $&#123;<span class="hljs-built_in">JSON</span>.stringify(marked(src))&#125;, 
    &#125;)
&#125;;

_sfc_md.render = _sfc_render
<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> _sfc_md
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终合成代码如下：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// /plugins/vite-plugin-md2vue.js</span>

<span class="hljs-keyword">const</span> marked = <span class="hljs-built_in">require</span>(<span class="hljs-string">'marked'</span>)

<span class="hljs-keyword">export</span> <span class="hljs-keyword">default</span> <span class="hljs-function"><span class="hljs-keyword">function</span> (<span class="hljs-params">options</span>) </span>&#123;
  <span class="hljs-keyword">return</span> &#123;
    <span class="hljs-attr">name</span>: <span class="hljs-string">'vitePluginMd2Vue'</span>,
    <span class="hljs-function"><span class="hljs-title">transform</span>(<span class="hljs-params">src, id</span>)</span> &#123;
      <span class="hljs-keyword">if</span> (id.endsWith(<span class="hljs-string">".md"</span>)) &#123;
        <span class="hljs-keyword">return</span> &#123;
          <span class="hljs-attr">code</span>: <span class="hljs-string">`import &#123;h, defineComponent&#125; from "vue";
                const _sfc_md = defineComponent(&#123;
                    name: "Markdown",
                &#125;);

                const _sfc_render =() => &#123;
                    return h("div", &#123;
                      innerHTML: <span class="hljs-subst">$&#123;<span class="hljs-built_in">JSON</span>.stringify(marked(src))&#125;</span>, 
                    &#125;)
                &#125;;

                _sfc_md.render = _sfc_render
                export default _sfc_md`</span>,
          <span class="hljs-attr">map</span>: <span class="hljs-literal">null</span>
        &#125;
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-5">使用插件</h3>
<p>在<code>vite.config.js</code>使用插件，代码如下：</p>
<pre><code class="copyable">import &#123; defineConfig &#125; from "vite";
import vue from "@vitejs/plugin-vue";
import vitePluginMd2Vue from "./plugins/vite-plugin-md2vue";

// https://vitejs.dev/config/
export default defineConfig(&#123;
  plugins: [vue(), vitePluginMd2Vue()],
  ...
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>最终实现的代码在<a href="https://github.com/WangXueZhi/vite-plugin-md2vue" target="_blank" rel="nofollow noopener noreferrer">vite-plugin-md2vue</a></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            