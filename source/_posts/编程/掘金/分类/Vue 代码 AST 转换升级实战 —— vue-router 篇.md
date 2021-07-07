
---
title: 'Vue 代码 AST 转换升级实战 —— vue-router 篇'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=5376'
author: 掘金
comments: false
date: Wed, 07 Jul 2021 01:28:10 GMT
thumbnail: 'https://picsum.photos/400/300?random=5376'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">前言</h2>
<p>最近我们发布了<a href="https://juejin.cn/post/6977259197566517284" target="_blank" title="https://juejin.cn/post/6977259197566517284">《阿里妈妈又做了新工具，帮你把 Vue2 代码改成 Vue3 的》</a>这个 Vue2 升级工具，下面跟大家分享下我们如何利用<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a>对 VueRouter 进行代码升级的。</p>
<h2 data-id="heading-1">Vue Router是什么</h2>
<p>贴一个官方介绍：
Vue Router 是 <a href="https://link.juejin.cn/?target=http%3A%2F%2Fcn.vuejs.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="http://cn.vuejs.org/" ref="nofollow noopener noreferrer"><strong>Vue.js</strong></a> 官方的路由管理器。它和 Vue.js 的核心深度集成，让构建单页面应用变得易如反掌</p>
<p>作为 Vue 开发的标配之一 ，Vue Router 跟随 Vue3 同步升级，API 定义与使用上有了一些<a href="https://link.juejin.cn/?target=https%3A%2F%2Fnext.router.vuejs.org%2Fzh%2Fguide%2Fmigration%2Findex.html" target="_blank" rel="nofollow noopener noreferrer" title="https://next.router.vuejs.org/zh/guide/migration/index.html" ref="nofollow noopener noreferrer">破坏性的变化</a>。为了实现一键 Vue2 升级 Vue3，我们把 Vue Router 的转换规则进行了拆解与研究，下面举几个使用 GoGoCode 的转换场景跟大家分享下：</p>
<h2 data-id="heading-2">利用 GoGoCode 升级 Vue Router</h2>
<p><strong>GoGoCode的使用可以</strong><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh%2Fdocs%2Fspecification%2Fgetting-started" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh/docs/specification/getting-started" ref="nofollow noopener noreferrer"><strong>参考这里</strong></a></p>
<h3 data-id="heading-3">1. new Router 变成 createRouter</h3>
<h4 data-id="heading-4">1.1 API的变化</h4>
<p>Vue Router 不再是一个类，而是一组函数。现在你不用再写 new Router()，而是要调用
<code>createRouter:</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// 以前是</span>
<span class="hljs-comment">// import Router from 'vue-router'</span>
<span class="hljs-keyword">import</span> &#123; createRouter &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>

<span class="hljs-keyword">const</span> router = createRouter(&#123;
  <span class="hljs-comment">// ...</span>
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-5">1.2 使用 GoGoCode 转换</h4>
<p>处理上面API的变化，我们只需要利用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a> 的<code>replace</code>方法，两行代码搞定</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-comment">// import 方式转换</span>
ast.replace(<span class="hljs-string">`import $_$ from 'vue-router'`</span>, 
            <span class="hljs-string">`import * as VueRouter from 'vue-router'`</span>);

<span class="hljs-comment">// 创建Router实例方法转换</span>
ast.replace(<span class="hljs-string">`new Router($_$)`</span>, <span class="hljs-string">`VueRouter.createRouter($_$)`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我也来试试：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fplay.gogocode.io%2F%23code%2FN4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAEpLxoHEBmBSOxA5AG4xoC09lBTAOhAEBjJBADOJbnDRjiAXmIBtALoCBENAHcyFaQQAUwAcRPEpMgQF8AlAJAAaEJsIBrZOiwgaMCELhhRYjgCAENxGkIcfRowABs0AEkICPtiEKgwVKQof1Exa2IjCBMRcRIAEnk0jIA6AHMkBpF0Y2JSiWIxCgIhNCqY%2BKSImq6YHrRW1oI0ODHi8v1R8dti4hrpqFiQ3v0AAzA8QgqAfUq6BmY2TnNeXdT9w6JiACo02QA1dnIeWnpGVnYXF0VCYuxWJnWaE22zQew02m%2Ben05VO1juxF2nzQiKoNSE0xC0hxBhR5TR4LWdTQGlC0n0FKsdkckFgcAAMmE6p44ABPKAyfFgHIOEAACxCYgACtM4P4qFhguxHCI8CFpgB5eCshUEdiWIA" target="_blank" rel="nofollow noopener noreferrer" title="https://play.gogocode.io/#code/N4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAEpLxoHEBmBSOxA5AG4xoC09lBTAOhAEBjJBADOJbnDRjiAXmIBtALoCBENAHcyFaQQAUwAcRPEpMgQF8AlAJAAaEJsIBrZOiwgaMCELhhRYjgCAENxGkIcfRowABs0AEkICPtiEKgwVKQof1Exa2IjCBMRcRIAEnk0jIA6AHMkBpF0Y2JSiWIxCgIhNCqY+KSImq6YHrRW1oI0ODHi8v1R8dti4hrpqFiQ3v0AAzA8QgqAfUq6BmY2TnNeXdT9w6JiACo02QA1dnIeWnpGVnYXF0VCYuxWJnWaE22zQew02m+en05VO1juxF2nzQiKoNSE0xC0hxBhR5TR4LWdTQGlC0n0FKsdkckFgcAAMmE6p44ABPKAyfFgHIOEAACxCYgACtM4P4qFhguxHCI8CFpgB5eCshUEdiWIA" ref="nofollow noopener noreferrer">地址</a></p>
<h3 data-id="heading-6">2. 新的 history 配置取代 mode</h3>
<h4 data-id="heading-7">2.1 API 的变化</h4>
<p><code>mode: 'history'</code> 配置已经被一个更灵活的 <code>history</code> 配置所取代。根据你使用的模式，你必须用适当的函数替换它：</p>
<ul>
<li><code>"history": createWebHistory()</code></li>
<li><code>"hash": createWebHashHistory()</code></li>
<li><code>"abstract": createMemoryHistory()</code></li>
</ul>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
<span class="hljs-comment">// 还有 createWebHashHistory 和 createMemoryHistory</span>

createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(),
  <span class="hljs-attr">routes</span>: [],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-8">2.2 使用 GoGoCode 转换</h4>
<p>VueRouter 中的 <code>mode</code> 配置，可以通过 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a> 的<code>replace</code>方法，替换成<code>history</code>配置，如果没有<code>mode</code>配置，则使用默认配置：<code>history:createWebHashHistory</code></p>
<pre><code class="hljs language-javascript copyable" lang="javascript">
<span class="hljs-keyword">if</span> (ast.has(<span class="hljs-string">`&#123;mode:$_$&#125;`</span>)) &#123;
  <span class="hljs-comment">// router定义中存在 mode 属性，replace替换</span>
ast.replace(<span class="hljs-string">`mode:'history'`</span>, 
              <span class="hljs-string">`history: VueRouter.createWebHistory()`</span>);
ast.replace(<span class="hljs-string">`mode:'hash'`</span>, 
              <span class="hljs-string">`history: VueRouter.createWebHashHistory()`</span>);
ast.replace(<span class="hljs-string">`mode:'abstract'`</span>, 
              <span class="hljs-string">`history: VueRouter.createMemoryHistory()`</span>);
&#125; <span class="hljs-keyword">else</span> &#123;
  <span class="hljs-comment">// router定义中不存在 mode 属性，默认采用 createWebHashHistory</span>
ast.replace(<span class="hljs-string">`&#123;routes:$_$,$$$&#125;`</span>, 
              <span class="hljs-string">`&#123;history: VueRouter.createWebHashHistory(),routes:$_$,$$$&#125;`</span>);
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我也来试试：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fplay.gogocode.io%2F%23code%2FN4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAFTECGAzsQGoxoBKS8aBxAZgUjsQOQA3BgFpurAnwA6EaQGMkEKiTFw0NALzEA2gF1p0gPQHA4gqA%2B6OIQ0AdzoNm4gBQBKYoCfdQPN%2BgG3jARsaAEI1tMLKoEAHSyBGgUqvbBztL0geJhEVGJscDSxFnEKmoANJnZOKhomPwAFmBKhACefAUQAL5O0iB5IFaEANbI6FggHDAQsnBgCsRwBBSKHIQ4DhxgADZoAJIQs3mUUGBbSFCjClQuGRBZ8ookACTEmhQ7IQDmSM-y6IUXSsRULASyaLdOMs1hskCEfjA-mgPkcSNQSJorg4IVCWmdiGAOMQHPCQuVqA4AAbAYroTBXAD6V0ahKcJ0KRhyQTYgCztQCScoBaOUAGtqACnViKSAYA9HUA5Ab6OC4iJQJYUf5EgWYPiVaoEOqEraFbKarWEpVwWplBIxNjJSKqADqaAARgAJKp6lXOWkAbjFErQUplaDlJQV%2BKo5T4auIGq1oZ1dv1ASNoXCprQFpt1HKtuVNUdThdMnFShCkulssJ8r4FEtSimI0D6vRobDusjhuZMZSqgAsmhiiqU-a005ndJGsQ0EsqADTllGbkCOyOYBYOV5-JKxBFgBh-wAbeYAS6MA44mACldiLHUgnrUmu7VXTm856icBclRyVS8ldHzSqzWa8S6yqDXZGyaD1aj-6J4Ok4eQ3neVwPk%2BfZNIUERwJCZy4o8aCWFMqhxOi-atO0kCwHAAAy0yPP0cA1FAajhGABxtCAfoAApwaMbBYJMDDtPIeAUBEADy8B4SxBAMI0QA" target="_blank" rel="nofollow noopener noreferrer" title="https://play.gogocode.io/#code/N4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAFTECGAzsQGoxoBKS8aBxAZgUjsQOQA3BgFpurAnwA6EaQGMkEKiTFw0NALzEA2gF1p0gPQHA4gqA+6OIQ0AdzoNm4gBQBKYoCfdQPN+gG3jARsaAEI1tMLKoEAHSyBGgUqvbBztL0geJhEVGJscDSxFnEKmoANJnZOKhomPwAFmBKhACefAUQAL5O0iB5IFaEANbI6FggHDAQsnBgCsRwBBSKHIQ4DhxgADZoAJIQs3mUUGBbSFCjClQuGRBZ8ookACTEmhQ7IQDmSM-y6IUXSsRULASyaLdOMs1hskCEfjA-mgPkcSNQSJorg4IVCWmdiGAOMQHPCQuVqA4AAbAYroTBXAD6V0ahKcJ0KRhyQTYgCztQCScoBaOUAGtqACnViKSAYA9HUA5Ab6OC4iJQJYUf5EgWYPiVaoEOqEraFbKarWEpVwWplBIxNjJSKqADqaAARgAJKp6lXOWkAbjFErQUplaDlJQV+Ko5T4auIGq1oZ1dv1ASNoXCprQFpt1HKtuVNUdThdMnFShCkulssJ8r4FEtSimI0D6vRobDusjhuZMZSqgAsmhiiqU-a005ndJGsQ0EsqADTllGbkCOyOYBYOV5-JKxBFgBh-wAbeYAS6MA44mACldiLHUgnrUmu7VXTm856icBclRyVS8ldHzSqzWa8S6yqDXZGyaD1aj-6J4Ok4eQ3neVwPk+fZNIUERwJCZy4o8aCWFMqhxOi-atO0kCwHAAAy0yPP0cA1FAajhGABxtCAfoAApwaMbBYJMDDtPIeAUBEADy8B4SxBAMI0QA" ref="nofollow noopener noreferrer">地址</a></p>
<h3 data-id="heading-9">3. 移动了 base 配置</h3>
<h4 data-id="heading-10">3.1 API的变化</h4>
<p><code>base​</code>配置被作为 <code>createWebHistory</code> (其他 history 也一样)的第一个参数传递：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; createRouter, createWebHistory &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'vue-router'</span>
createRouter(&#123;
  <span class="hljs-attr">history</span>: createWebHistory(<span class="hljs-string">'/base-directory/'</span>),
  <span class="hljs-attr">routes</span>: [],
&#125;)
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-11">3.2 使用 GoGoCode 转换</h4>
<p>通过<a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh%2Fdocs%2Fspecification%2Fselector" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh/docs/specification/selector" ref="nofollow noopener noreferrer">GoGoCode通配符号</a>： <code>$_$</code>和<code>$$$</code>,将<code>base</code>及其它代码进行乾坤大挪移，可以瞬间完成代码片段转移。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">  ast.replace(<span class="hljs-string">`&#123;$$$,history: VueRouter.createWebHistory(), base: $_$&#125;`</span>,
    <span class="hljs-string">`&#123;$$$,history: VueRouter.createWebHistory($_$)&#125;`</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我也来试试：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fplay.gogocode.io%2F%23code%2FN4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAFTECGAzsQGoxoBKS8aBxAZgUjsQOQA3BgFpurAnwA6EaQGMkEKiTFw0NALzEA2gF1p0gPQHA4gqA%2B6OIQ0AdzoNm4gBQBKYoCfdQPN%2BgG3jARsaAEI1tMLKoEAHSyBGgUqvbBztL0geJhEVGJscDSxFnEKmoANJnZABZgSoQAnpgBMWzJkaoA6mgARgASpXAVzgUQ2cTN1GhVfAbcSHBSEAC%2BTtIgeSBWhADWyOhYIBwwELJwYArEcAQUihyEOA4cYAA2aACSEGd5lFBgz0hQewpULhm9xPJFCQACTETQUV4hADmSBh8nQhUBSmIVBYBFkaDBnBu90eSBCqJg6LQiO%2BJGoJE0wIchOJs3%2BFJCESg1woGIcAANgMCeXkSmUCJVqkFauF6mgmm0Ol0nM8BlQhsRgQB9YFTDk9PpcnnAvnSwVVBI1UJi1KS9oC8oOFXApzq%2BmFCJwIm9RlQtCWY6qOIyaZzBaQWBwAAyJyhGzg5SganCYE%2B8xARWoAAUnXs2FgjgwFvI8BQIgB5eBBzMEBhTIA" target="_blank" rel="nofollow noopener noreferrer" title="https://play.gogocode.io/#code/N4IglgdgDgrgLgYQPYBMCmIBc4C2UkBOcABAFTECGAzsQGoxoBKS8aBxAZgUjsQOQA3BgFpurAnwA6EaQGMkEKiTFw0NALzEA2gF1p0gPQHA4gqA+6OIQ0AdzoNm4gBQBKYoCfdQPN+gG3jARsaAEI1tMLKoEAHSyBGgUqvbBztL0geJhEVGJscDSxFnEKmoANJnZABZgSoQAnpgBMWzJkaoA6mgARgASpXAVzgUQ2cTN1GhVfAbcSHBSEAC+TtIgeSBWhADWyOhYIBwwELJwYArEcAQUihyEOA4cYAA2aACSEGd5lFBgz0hQewpULhm9xPJFCQACTETQUV4hADmSBh8nQhUBSmIVBYBFkaDBnBu90eSBCqJg6LQiO+JGoJE0wIchOJs3+FJCESg1woGIcAANgMCeXkSmUCJVqkFauF6mgmm0Ol0nM8BlQhsRgQB9YFTDk9PpcnnAvnSwVVBI1UJi1KS9oC8oOFXApzq+mFCJwIm9RlQtCWY6qOIyaZzBaQWBwAAyJyhGzg5SganCYE+8xARWoAAUnXs2FgjgwFvI8BQIgB5eBBzMEBhTIA" ref="nofollow noopener noreferrer">地址</a></p>
<h3 data-id="heading-12">4. <router-view>、<keep-alive> 和 <transition></h3>
<h4 data-id="heading-13">4.1 API 的变化</h4>
<p>transition 和 keep-alive 现在必须通过 v-slot API 在 RouterView <strong>内部</strong>使用：</p>
<pre><code class="hljs language-html copyable" lang="html"><span class="hljs-tag"><<span class="hljs-name">router-view</span> <span class="hljs-attr">v-slot</span>=<span class="hljs-string">"&#123; Component &#125;"</span>></span>
  <span class="hljs-tag"><<span class="hljs-name">transition</span>></span>
    <span class="hljs-tag"><<span class="hljs-name">keep-alive</span>></span>
      <span class="hljs-tag"><<span class="hljs-name">component</span> <span class="hljs-attr">:is</span>=<span class="hljs-string">"Component"</span> /></span>
    <span class="hljs-tag"></<span class="hljs-name">keep-alive</span>></span>
  <span class="hljs-tag"></<span class="hljs-name">transition</span>></span>
<span class="hljs-tag"></<span class="hljs-name">router-view</span>></span>
<span class="copy-code-btn">复制代码</span></code></pre>
<h4 data-id="heading-14">4.2 使用 GoGoCode 转换</h4>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a>同样能处理html代码，我们将router-view节点转移到transition外层，同时保持原来的属性及内部元素结构不变，使用<code>replace</code> 可瞬间完成。</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">ast.replace(<span class="hljs-string">`<transition $$$1><router-view $$$2>$$$3</router-view></transition>`</span>,
<span class="hljs-string">`<router-view v-slot="&#123; Component &#125;" $$$2>
<transition $$$1>
<component :is="Component" >$$$3</component>
</transition>
</router-view>`</span>);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我也来试试：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fplay.gogocode.io%2F%23code%2FN4IglgdgDgrgLgYQPYBMCmIBcIA8c0C2UANgIb4B8AOhHgE6kQDOYcYSEABBKQWgLxUQAM1LohnAqgFCk8ALSQh1LpzVqcdOfjryAbmDQB3TgGMyTJoJAHjynAHot8NLttGVjuA2at2ETwd8IjJKEAAaECMkOgBrZHQsERgIUzYOTm9GJmEYggAKYTBiNABJCFzwzlIoMCqkKHTmAEpOYBo1Uw4mOE4AEk5%2BatqAOgBzJAmu8VUu5l6mOTpTNEHOIpLy3JHFmGW0DrNu3tIetb783f3w4E4oUjomNAB5Rv8mTDbOMggxmFIxmhPgByPQwNDAzgAX2hzUODgcgD8jQAMSsESOQ0IAs7UAknKHU5wEZFCAofLAvCEdGULwU0JoCjAuGqEZ0NDolb5AAG9GyfgyfX5AEYKJptK59IYTPy%2BgAmChSgDMjmcOnFxmFQR8LCaFA54RoXOVYvcnD08iYxCQcGst2QRA4aAgvShEilspoVDg3N8TX6gpUHo9OC6dogDt6mDAViEtqg9sdEjl-MVDmDsdDjv9no1PO1NCVorcEp1jMOLLgey4%2BPGDtcGPyJYgzogEXA0HgABlGGMkgALOAEYgtnunAAKZbYriw3nBkVTDxe8FgcCndHBUKAA" target="_blank" rel="nofollow noopener noreferrer" title="https://play.gogocode.io/#code/N4IglgdgDgrgLgYQPYBMCmIBcIA8c0C2UANgIb4B8AOhHgE6kQDOYcYSEABBKQWgLxUQAM1LohnAqgFCk8ALSQh1LpzVqcdOfjryAbmDQB3TgGMyTJoJAHjynAHot8NLttGVjuA2at2ETwd8IjJKEAAaECMkOgBrZHQsERgIUzYOTm9GJmEYggAKYTBiNABJCFzwzlIoMCqkKHTmAEpOYBo1Uw4mOE4AEk5+atqAOgBzJAmu8VUu5l6mOTpTNEHOIpLy3JHFmGW0DrNu3tIetb783f3w4E4oUjomNAB5Rv8mTDbOMggxmFIxmhPgByPQwNDAzgAX2hzUODgcgD8jQAMSsESOQ0IAs7UAknKHU5wEZFCAofLAvCEdGULwU0JoCjAuGqEZ0NDolb5AAG9GyfgyfX5AEYKJptK59IYTPy+gAmChSgDMjmcOnFxmFQR8LCaFA54RoXOVYvcnD08iYxCQcGst2QRA4aAgvShEilspoVDg3N8TX6gpUHo9OC6dogDt6mDAViEtqg9sdEjl-MVDmDsdDjv9no1PO1NCVorcEp1jMOLLgey4+PGDtcGPyJYgzogEXA0HgABlGGMkgALOAEYgtnunAAKZbYriw3nBkVTDxe8FgcCndHBUKAA" ref="nofollow noopener noreferrer">地址</a></p>
<h2 data-id="heading-15">最后</h2>
<p>这里只是列举了四个比较典型的VueRouter使用场景上的变化，包含了js和html代码转换。其他转换规则可以看下我们的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fthx%2Fgogocode%2Ftree%2Fmain%2Fpackages%2Fgogocode-plugin-vue" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/thx/gogocode/tree/main/packages/gogocode-plugin-vue" ref="nofollow noopener noreferrer">GitHub</a>。这些转换规则都是使用了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a> 之后极大地简化了操作AST对象成本，基本上一个<code>replace</code>方法就能搞定，遇到代码转换需求非常推荐大家使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a>！
​</p>
<p>如果在使用 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgogocode.io%2Fzh" target="_blank" rel="nofollow noopener noreferrer" title="https://gogocode.io/zh" ref="nofollow noopener noreferrer">GoGoCode</a> 过程中遇到问题可以联系我们：
github: <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Fthx%2Fgogocode%2Fissues" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/thx/gogocode/issues" ref="nofollow noopener noreferrer">github.com/thx/gogocod…</a>
钉钉群：34266233</p>
<p>感谢您的阅读，祝您有美好的一天！</p></div>  
</div>
            