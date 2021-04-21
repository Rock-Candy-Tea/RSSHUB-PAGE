
---
title: 'Styled Components和Tailwind配置以及使用方法'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5338184924142976ca2d05c4a838c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Wed, 21 Apr 2021 01:58:23 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5338184924142976ca2d05c4a838c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h2 data-id="heading-0">Part1 Styled Components</h2>
<h3 data-id="heading-1">1 介绍</h3>
<p>Styled Components 是一个常用的 CSS in JS 类库。和所有同类型的类库一样，通过 js 解决了原生 css 所不具备的能力，比如变量、循环、函数等。诸如 sass&less 等预处理可以解决部分 css 的局限性，但还是要学习新的语法，而且需要对其编译，其复杂的 webpack 配置也总是让开发者抵触，而 Styled Components 很好的解决了这些问题。</p>
<h3 data-id="heading-2">2 安装和使用</h3>
<p>安装方法</p>
<pre><code class="copyable">yarn add styled-components
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用方法</p>
<pre><code class="copyable">import styled from 'Styled Components';
const Wrapper = styled.section`
  margin: 0 auto;
  width: 300px;
  text-align: center;
`;
const Button = styled.button`
  width: 100px;
  color: white;
  background: skyblue;
`;
render(
  <Wrapper>
    <Button>Hello World</Button>
  </Wrapper>
);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>上述的代码片段展示了 React 项目中使用 Styled Components，定义了 Wrapper 和 Button 两个组件，包含了 html 结构和对应的 css 样式，从而将样式和组件之间的 class 映射关系移除。<br>
具体使用细节：<a href="https://segmentfault.com/a/1190000017155008" target="_blank" rel="nofollow noopener noreferrer">segmentfault.com/a/119000001…</a></p>
<h3 data-id="heading-3">3 提示插件</h3>
<p>安装 vscode-Styled Components 即可。</p>
<h2 data-id="heading-4">Part2  Tailwind</h2>
<h3 data-id="heading-5">1  Tailwind介绍</h3>
<p>先来看下官网的介绍：
Tailwind CSS 是一个高度可定制的基础层 CSS 框架，它为您提供了构建定制化设计所需的所有构建块，而无需重新覆盖任何内建于框架中的设计风格。<br>
它不同于Bootstrap等前端ui库，提供已经写好的组件。更像是之前的原子化css, 将css属性颗粒化，生成对应的功能class。相较原子css它还支持伪类、响应式，并且可高度自定义。</p>
<h3 data-id="heading-6">2  Tailwind的配置和使用</h3>
<p>配置方法<br>
第一步：首先生成tailwind.config.js文件</p>
<pre><code class="copyable">npx tailwindcss init
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第二步：在tailwind.config.js配置联盟项目的基础样式（会默认覆盖tailwind的prefight）</p>
<pre><code class="copyable">module.exports = &#123;
  important: true,
  corePlugins: &#123;
    preflight: false, // 禁用tailwind的预设样式
  &#125;,
  variants: &#123;
    extend: &#123;
      backgroundColor: ['checked'],
      borderColor: ['checked'],
    &#125;,
  &#125;,
  theme: &#123;
    extend: &#123;
      // 设置font-size，第二个数据是行高，用法：text-size12,text-base
      fontSize: &#123;
        base: '12px',
        12: '12px',
        14: '14px',
        16: '16px',
        18: '18px',
        20: '20px',
        24: '24px',
      &#125;,
      // 设置font-family，用法 font-normal
      fontFamily: &#123;
        normal: ['Proxima Nova', 'PingFangSC', 'sans-serif'],
        semibold: ['Proxima Nova Semibold', 'PingFangSC', 'sans-serif'],
        bold: ['Proxima Nova Bold', 'PingFangSC', 'sans-serif'],
      &#125;,
      // 设置line-height，用法：leading-18
      lineHeight: &#123;
        base: '21px',
        18: '18px',
        21: '21px',
        24: '24px',
        27: '27px',
        30: '30px',
      &#125;,
      // 设置font-weight，用法：font-bold
      fontWeight: &#123;
        regular: '400',
        semibold: '600',
        bold: '700',
      &#125;,
      // 设置颜色，用法：font-gray-20 / bg-brand / border-gray-border
      colors: &#123;
        transparent: 'transparent',
        current: 'currentColor',
        black: '#000',
        white: '#fff', // 灰度/白色
        red: '#ff6453',
        // 这三个一般用于文字颜色
        grey: &#123;
          default: '#242f57',
          10: '#191d32', // 灰度/一级文字
          20: '#474c66', // 灰度/二级文字、次级文字按钮
          30: '#777d99', // 灰度/三级文字、icon
          40: '#b8bbcc',
          50: '#d9dbe5',
          60: '#eaecf6',
          70: '#f6f6fb',
          80: '#fafafd',
          300: '#b8bbcc',
          500: '#eaecf6',
          700: '#fafafd',
        &#125;,
        // 品牌色
        brand: &#123;
          default: '#0080ff',
          10: '#369afe',
          20: '#67b3fe',
          30: '#3088e0',
          40: '#a0d0ff',
          50: '#e6f3ff',
          60: '#f4faff',
          A100: '#369afe',
        &#125;,
      &#125;,
      // 用于设置边距，用法：px-2 / my-3
      spacing: &#123;
        default: '1px',
        1: '1px',
        2: '2px',
        3: '3px',
        4: '4px',
        6: '6px',
        8: '8px',
        12: '12px',
        14: '14px',
        16: '16px',
        18: '18px',
        20: '20px',
        24: '24px',
        28: '28px',
        32: '32px',
        36: '36px',
        40: '40px',
        48: '48px',
        64: '64px',
        72: '72px',
        74: '74px',
        auto: 'auto',
      &#125;,
      // borderRadius，用法：rounded, rounded-md
      borderRadius: &#123;&#125;,
      // borderWidth,用法：
      borderWidth: &#123;
        default: '1px',
      &#125;,
      screens: &#123;
        default: '1280px',
      &#125;,
    &#125;,
  &#125;,
&#125;;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>第三步：在config.js中引入tailwind.config.js</p>
<pre><code class="copyable">const &#123;theme,important,corePlugins&#125; = require('../tailwind.config');
const getBaseConfig = moduleName => &#123;
  return &#123;
    source: &#123;
      ...
      designSystem: theme //添加配置
    &#125;,
    tools:&#123;
    tailwind: &#123;
        important,        //其他配置类似
         corePlugins,
        purge: &#123;          //treeshake掉不需要的tailwindcss
          enabled: isProd,   
          content: ['./src/**/*'], //对应每个模块下的src文件夹
          //layers: ['utilities'], 
        &#125;,
      &#125;,
      styledComponents: &#123;
        pure: true,
        displayName: true,
        ssr: false,
        transplitTemplateLiterals: true,
      &#125;,
      ...
    &#125;
 &#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-7">使用方法</h3>
<p>在需要使用tailwind的文件下导入tailwind.css即可，它主要有3个模块<br>
• base:css reset，重置默认属性<br>
• components：一些组件样式<br>
• utilities：工具类，也就是最常用的样式封装<br>
方法一：</p>
<pre><code class="copyable">//Example.jsx:
import React from 'react';
import 'tailwindcss/tailwind.css'; // 全部导入
<span class="copy-code-btn">复制代码</span></code></pre>
<p>方法二：</p>
<pre><code class="copyable">import React from 'react';
import 'tailwindcss/base.css'; // 导入base部分
import 'tailwindcss/components.css'; // 导入components部分
import 'tailwindcss/utilities.css'; // 导入utilities部分
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在接下来就可以直接使用tailwind的css类了，类名虽多，但是比较有规律<br>
具体使用方法：</p>
<ol>
<li>颜色   类名= 使用目标+颜色+权重</li>
</ol>
<p>一般都把颜色作为背景色、文字颜色或者边框颜色。举个🌰，颜色green：<br>
文字颜色： text-green<br>
背景颜色： bg-green<br>
边框颜色1： border-green      //default，不需要数字描述<br>
边框颜色2： border-green-700  //数字表示颜色的深浅，越大颜色越深</p>
<ol start="2">
<li>文本    "text-"</li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d6a5338184924142976ca2d05c4a838c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
文本颜色、文本装饰、大小写转换和溢出样式 见：<a href="https://docs.tailwindchina.com/docs/text-color" target="_blank" rel="nofollow noopener noreferrer">docs.tailwindchina.com/docs/text-c…</a></p>
<ol start="3">
<li>字体  "font-"</li>
</ol>
<p>字体类型  "font-"+&#123;type&#125;
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/92e32999380040378b3b3f2c9fbd7871~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>字体粗细 <code>"font-"+&#123;weight&#125;</code>
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99cdff285e2849b2b487c719dea735c0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="4">
<li>行高 <code>"leading-"+&#123;size&#125;</code></li>
</ol>
<p><img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/73638b20cc514a4f8c7e95513c2e9aac~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
5. 背景 <code> "bg-"</code></p>
<pre><code class="copyable"><div class="bg-purple-600 bg-opacity-100"></div>
<div class="bg-purple-600 bg-opacity-75"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>背景颜色、背景图片位置等见： <a href="https://docs.tailwindchina.com/docs/background-image" target="_blank" rel="nofollow noopener noreferrer">docs.tailwindchina.com/docs/backgr…</a><br>
6. 边框  <code>"rounded-"或"border-"</code><br>
"rounded-"设置边框的圆角样式，"border-"设置边框颜色、粗细、边框类型等</p>
<pre><code class="copyable"><div class="rounded-full py-3 px-6">Pill Shape</div> //rounded-full=border-raduis:9999px
<div class="rounded-full h-24 w-24 flex items-center justify-center...">Circle</div>
<div class="border-4 border-light-blue-500 border-opacity-100"></div>
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="7">
<li>边距  "p-"  "m-"</li>
</ol>
<p>内边距padding：  使用<code>p&#123;t|r|b|l|x|y&#125;-&#123;size&#125;</code>功能类控制元素一侧的内边距。size是tailwind.config.js中配置的spacing对象的键。<br>
<img alt="image.png" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f966bc2298fe4e788a3ab9edc96f9350~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
外边距margin：  使用 <code>m&#123;t|r|b|l|x|y&#125;-&#123;size&#125;</code>,用法同padding</p>
<ol start="8">
<li>布局</li>
</ol>
<p>8.1 display：元素显示类型<br>
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2c2b280b1c4843788aa6c94aaa33582f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer">
其他样式：<a href="https://docs.tailwindchina.com/docs/display" target="_blank" rel="nofollow noopener noreferrer">docs.tailwindchina.com/docs/displa…</a></p>
<p>8.2 Flex  <code>"flex-"</code>
<img alt="image.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3b981198e7fa44b2a57ed0f4ae48c10e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<pre><code class="copyable"><div class="flex">
  <div class="flex-1">1</div>
  <div class="flex-1">2</div>
  <div class="flex-1 hidden">3</div>
</div>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>其他对齐方式：<a href="https://docs.tailwindchina.com/docs/justify-items" target="_blank" rel="nofollow noopener noreferrer">docs.tailwindchina.com/docs/justif…</a></p>
<p><code>box-sizing ：</code>控制浏览器如何计算元素的总大小的功能类。
<img alt="image.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/acb9523ab5964f11ac460d739e5fa2b2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ol start="9">
<li>伪类 <code>&#123; hover: | focus: | checked: |active: | visited: |disabled: &#125; + 功能类</code></li>
</ol>
<p>并不是所有功能类都可以放在伪类的后面，只有tailwind文档规定的才可使用，如果需要在tailwind的配置文件中配置variants选项。</p>
<pre><code class="copyable">//hover active
<button class="bg-red-500 hover:bg-red-700 active:bg-purple-500 ">
  Hover me
</button>
//disabled
<button class="disabled:opacity-50">
  Submit
</button>
//checked
<input type="checkbox" class="appearance-none checked:bg-blue-600">
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="10">
<li>其他</li>
</ol>
<p>tailwind2.0有暗黑模式和浅色模式的转换方法，另外taliwind.config.js的配置可丰富tailwindcss的使用功能。</p>
<h3 data-id="heading-8">3 提示插件</h3>
<p>安装 <code>Tailwind CSS IntelliSense</code> 插件后，智能代码提示，就不用担心自己记不住tailwind的属性类了。</p>
<h2 data-id="heading-9">Tailwind 和Styled components的结合</h2>
<p>考虑到tailwindcss不可能囊括我们项目开发中所有的样式代码。</p>
<ol>
<li>比如一些魔法数值（例如元素宽固定260，等等）。</li>
<li>或者我们使用类第三方ui库，需要更改其样式。</li>
</ol>
<p>这些用tailwindcss去设置就不那么方便了，这个时候我们就需要借助styled-component来进行样式编写来。</p>
<pre><code class="copyable">import 'tailwindcss/tailwind.css'；
import styled from 'styled-components';

const Wrapper = styled.div.attrs<&#123;active: boolean&#125;>(&#123;
  className: 'bg-chartbox-dark',
&#125;)`
  height: 100vh;
  box-sizing: border-box;
  overflow: hidden;
`;
<span class="copy-code-btn">复制代码</span></code></pre></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            