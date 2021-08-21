
---
title: '原子化 JSS 方案 broken-css'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d521e91b1f4a56a1e4d1f14ba3b374~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 20 Aug 2021 04:11:07 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d521e91b1f4a56a1e4d1f14ba3b374~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">技术背景</h1>
<p>对于现代 UI 框架来说，选择使用 JSS 逐渐让人可以接受，而不再被视为“大逆不道”之举。 然而， JSS 作为管理样式的前沿解决方案，有些 JSS 方案可以说被称为前沿的前沿。如：</p>
<ul>
<li>linaria</li>
</ul>
<p>一个零运行时开源的 JSS 方案，在编译期将你的 JSS 抽离解压出来，不用维持一个运行时来解析 JSS 并使得浏览器可以并行的下载 CSS 和 JSS ，具有更高的性能和体积优势。</p>
<ul>
<li>stylex</li>
</ul>
<p>Facebook 内部闭源的原子化的 JSS 方案，其最大的特点是在编译期将 JSS 编译为原子 CSS 解压出来，达到最大程度的复用</p>
<pre><code class="copyable">const styles = stylex.create(&#123;
  blue: &#123;color: 'blue'&#125;,
  red: &#123;color: 'red'&#125;
&#125;);
function MyComponent(props) &#123;
  return (
    <span className=&#123;styles('blue', 'red')&#125;>
      I'm blue
    </span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被编译为</p>
<pre><code class="copyable">.c0 &#123; color: blue&#125;
.c1 &#123; color: red&#125;


const styles = stylex.create(&#123;
  blue: &#123;color: 'blue'&#125;,
  red: &#123;color: 'red'&#125;
&#125;);
function MyComponent(props) &#123;
  return (
    <span className=&#123;"c0 c1"&#125;>
      I'm blue
    </span>
  )
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>受到 linarira 和 stylex 的启发，broken-css 同样是一个零运行时原子化的 JSS 方案，不同点在于 broken-css 选择的 API 的形式，并非 react-native-like ，而是使用了模板字符串函数，这使得 broken-css 可以很容易的支持动画和伪类相关的 CSS 规则，并且使用起来也非常符合传统的使用方式。</p>
<h1 data-id="heading-1">介绍</h1>
<h2 data-id="heading-2">使用</h2>
<p>首先你需要安装以下两个库：</p>
<ul>
<li>yarn add @broken-css/core</li>
<li>yarn add -D @broken-css/webpack-loader</li>
</ul>
<h3 data-id="heading-3">@broken-css/core</h3>
<p>@broken-css/core 做的事情很简单，只是给 @broken-css/webpack-loader 一个信号，告诉这里需要编译，实际上我们可以看下 @broken-css/core 的源码，你会发现其非常的简洁</p>
<pre><code class="copyable">export const css = (_literal: TemplateStringsArray, ..._DOES_NOT_SUPPORT_EXPRESSIONS: never[]): string => &#123;
  throw new SyntaxError('Do not call css() on runtime!')
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>因为 css ... `` 表达式，在编译后会被替换成一段字符串，所以在运行期间，这个函数其实不会被真正执行到，所以并不会抛出这个错误。</p>
<h3 data-id="heading-4">@broken-css/webpack-loader</h3>
<p>@broken-css/webpack-loader 完成核心步骤，即将代码 JSS 替换成原子化的 CSS 类名 ，并将编译后的原子化 CSS 导入到相应的 JS 文件中，使得 webpack 接管导入 CSS 的流程，以便使用相关 loader 和 plugin 。</p>
<h3 data-id="heading-5">例子</h3>
<p>假如我们有两个组件 Foo 和 Bar</p>
<pre><code class="copyable">// Foo.tsx
import &#123; css &#125; from "@broken-css/core";
import React, &#123; FC &#125; from "react";

const Foo: FC = () => &#123;
  return (
    <div className=&#123;css`
      color: red;
      font-size: 24px;
      border: 1px solid black;
      @keyframes shake &#123;
        10%, 90% &#123;
          transform: translate3d(-1px, 0, 0);
        &#125;

        20%, 80% &#123;
          transform: translate3d(2px, 0, 0);
        &#125;

        30%, 50%, 70% &#123;
          transform: translate3d(-4px, 0, 0);
        &#125;

        40%, 60% &#123;
          transform: translate3d(4px, 0, 0);
        &#125;
      &#125;
      &:hover &#123;
        animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
        transform: translate3d(0, 0, 0);
        backface-visibility: hidden;
        perspective: 1000px;
      &#125;
      &::after &#123;
        content: ' after';
        color: brown;
      &#125;
    `&#125;>foo</div>
  );
&#125;

export default Foo;

// Bar.tsx

import &#123; css &#125; from "@broken-css/core";
import React, &#123; FC &#125; from "react";

const Bar: FC = () => &#123;
  return (
    <div className=&#123;css`
      color: red;
      font-size: 24px;
      border: 1px black solid;
    `&#125;>bar</div>
  );
&#125;

export default Bar;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在编译后会变成</p>
<pre><code class="copyable">// Foo.tsx
import &#123; css &#125; from "@broken-css/core";
import React, &#123; FC &#125; from "react";

const Foo: FC = () => &#123;
  return <div className=&#123;"_0e91 _b38a _43fe _b04b _4b6c"&#125;>foo</div>;
&#125;;

export default Foo;
;require("../node_modules/.cache/broken-css-webpack-loader/broken.css");

// Bar.tsx

import &#123; css &#125; from "@broken-css/core";
import React, &#123; FC &#125; from "react";

const Bar: FC = () => &#123;
  return <div className=&#123;"_43fe _b04b _f617"&#125;>bar</div>;
&#125;;

export default Bar;
;require("../node_modules/.cache/broken-css-webpack-loader/broken.css");


/** broken.css **/
@keyframes shake &#123;
    10%, 90% &#123;
        transform: translate3d(-1px, 0, 0);
    &#125;
    20%, 80% &#123;
        transform: translate3d(2px, 0, 0);
    &#125;
    30%, 50%, 70% &#123;
        transform: translate3d(-4px, 0, 0);
    &#125;
    40%, 60% &#123;
        transform: translate3d(4px, 0, 0);
    &#125;
&#125;

._0e91:hover &#123;
    animation: shake 0.82s cubic-bezier(.36,.07,.19,.97) both;
    transform: translate3d(0, 0, 0);
    backface-visibility: hidden;
    perspective: 1000px;
&#125;

._b38a::after &#123;
    content: ' after';
    color: brown;
&#125;

._43fe &#123;color: red;&#125;

._b04b &#123;font-size: 24px;&#125;

._4b6c &#123;border: 1px solid black;&#125;

._f617 &#123;border: 1px black solid;&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">原子化</h2>
<p>如例子所演示的那样，broken-css 会根据样式的内容计算出一个哈希值来表示这个样式规则，同时这个哈希值会被当做类名替换到相应的 JS 文件中，因为哈希是根据其内容计算的，来自两个文件相同的样式计算出的哈希值是一样的，因此在后续的去重步骤中可以将其筛选掉，从而达到复用的目的。 这里需要多说一点的是，对于样式 border: 1px solid black; 和 border: 1px black solid; 来说， broken-css 并不会视为是同一种样式，尽管他们的效果是一样的。如果要做到这种程度的复用，需要考虑太多的边界情况，我希望有一种简单通用的方法来解决这个问题，还在研究中。</p>
<h2 data-id="heading-7">体积优势</h2>
<p>在使用 broken-css 后，你的 CSS 体积在刚开始不会明显的减少，但随着项目的发展，越来越多的样式存在重复，使得复用的可能性大大增多，体积就会降下来，如果把体积的变化汇成一条线的话，传统的 CSS 体积增长是一条直线，而 broken-css 则是一条曲线。 <img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5d521e91b1f4a56a1e4d1f14ba3b374~tplv-k3u1fbpfcp-watermark.image" alt loading="lazy" referrerpolicy="no-referrer"> 配图源于<a href="https://link.juejin.cn/?target=https%3A%2F%2Fsebastienlorber.com%2Fatomic-css-in-js" target="_blank" rel="nofollow noopener noreferrer" title="https://sebastienlorber.com/atomic-css-in-js" ref="nofollow noopener noreferrer">《Atomic CSS-in-JS》</a></p>
<h2 data-id="heading-8">伪类支持</h2>
<p>broken-css 支持伪类选择器，对于形如 &::after &#123; ... &#125; 的规则，broken-css 会根据整体样式规则计算出哈希值，然后将 & 替换成对应的哈希值。</p>
<pre><code class="copyable">// a.js
const cls1 = css`
        color: red;
`

// b.js

const cls2 = css`
        &:hover &#123;
                color: red;
                font-size: 24px;
        &#125;
`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会编译为</p>
<pre><code class="copyable">// a.js
const cls1 = 'c1'
/*
    color: red;
*/

// b.js
const cls2 = 'c2 c3'
/*
    &:hover &#123;
            color: red;
            font-size: 24px;
    &#125;
*/


.c1, .c2:hover &#123; color: red; &#125;
.c3:hover &#123; font-size: 24px; &#125;  
<span class="copy-code-btn">复制代码</span></code></pre>
<p>从而达到更细粒度的复用，~~但是对于现有的版本来说，只会编译成 ，已经实现，~~有一些情况会导致样式冲突，已经切换为老的实现</p>
<h2 data-id="heading-9">@规则支持</h2>
<p>@ 规则的支持是自然而然的，因此你可以自由的使用动画和媒体查询等规则，broken-css 不会对他们做任何处理，只是简单的解压到最终的 CSS 文件中。 这里我纠结的一点在于要不要在 @keyframes 命名的隔离，但是在后续的思考中发现这并不是简单的事情，例如命名 scope 的范围，是隔离在每一次 css ... `` 调用期间，这样的话怎么做复用？全局范围的话，意味着需要维持一张状态表，并且分析全局的 CSS 代码将相应的命名替换掉，同样的很复杂。</p>
<h2 data-id="heading-10">CSS 变量</h2>
<p>broken-css 将 CSS 变量视作一个普通的样式声明，并没有任何特殊的处理，同样的会根据其内容计算出一个哈希值，并分配一个唯一的类名</p>
<pre><code class="copyable">const cls1 = css`
        --main-color: red;
        backgroud-color: var(--main-color);
`

const cls2 = css`
        backgroud-color: var(--main-color);
`
<span class="copy-code-btn">复制代码</span></code></pre>
<p>会被编译为</p>
<pre><code class="copyable">const cls1 = 'c1 c2'
const cls2 = 'c2'


.c1 &#123; --main-color: red; &#125;
.c2 &#123; backgroud-color: var(--main-color); &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">问题</h1>
<h2 data-id="heading-12">智能语法提示</h2>
<p>我不太熟悉其他的 IDE ，如果你使用 VSCode ，这个问题可以很完美的解决， broken-css 的 API 形式兼容了 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Djpoissonnier.vscode-styled-components" target="_blank" rel="nofollow noopener noreferrer" title="https://marketplace.visualstudio.com/items?itemName=jpoissonnier.vscode-styled-components" ref="nofollow noopener noreferrer">vscode-styled-components</a> 扩展。</p>
<h2 data-id="heading-13">stylelint</h2>
<p>broken-css 在编译期间会 JSS 抽离解压出来，在转换成原子化的 CSS 后，会将后续的行为委托给 webpack ，因此你可以自由的选择是否使用 stylelint-webpack-plugin ，并且 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fmarketplace.visualstudio.com%2Fitems%3FitemName%3Djpoissonnier.vscode-styled-components" target="_blank" rel="nofollow noopener noreferrer" title="https://marketplace.visualstudio.com/items?itemName=jpoissonnier.vscode-styled-components" ref="nofollow noopener noreferrer">vscode-styled-components</a> 支持书写期间的 lint 检查。</p>
<p>我所在的字节电商广告前端团队，现有大量HC。实习，初级和资深前端都可。可以加微信私聊（yunfeihe），或者简历直发 <a href="https://link.juejin.cn/?target=mailto%3Awujiantao%40bytedance.com" target="_blank" title="mailto:wujiantao@bytedance.com" ref="nofollow noopener noreferrer">wujiantao@bytedance.com</a> ，邮件标题请注明【简历】。</p>
<p>作者：<strong>何云飞</strong></p></div>  
</div>
            