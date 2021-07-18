
---
title: 'Electron+Vue3 MAC 版日历开发记录(31)——Icons Font 制作'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e0be631a6434a2fba58e5c48b3cd772~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Sun, 18 Jul 2021 00:04:29 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e0be631a6434a2fba58e5c48b3cd772~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>在之前，我们的 <code>设置</code> 按钮因为 FullCalendar 没有提供对应的图标，所以独立于 FullCalendar 在 Main 界面添加，但这导致页面的不统一和协调。</p>
<p>今天就想着如何自己手动创建一个只带图标 icons 的字体 CSS，把需要的 icons 打包进去。</p>
<h2 data-id="heading-0">参考模仿</h2>
<p>先看看我们引用的 FullCalendar 提供的 <code>font-face</code>：</p>
<pre><code class="copyable">// icons.css

@font-face &#123;
  font-family: 'fcicons';
  src: url("data:application/x-font-ttf;charset=utf-8;base64,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") format('truetype');
  font-weight: normal;
  font-style: normal;
&#125;

.fc-icon &#123;
  /* added for fc */
  display: inline-block;
  width: 1em;
  height: 1em;
  text-align: center;
  user-select: none;

  /* use !important to prevent issues with browser extensions that change fonts */
  font-family: 'fcicons' !important;
  speak: none;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;

  /* Better Font Rendering =========== */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
&#125;

.fc-icon-chevron-left:before &#123;
  content: "\e900";
&#125;
.fc-icon-chevron-right:before &#123;
  content: "\e901";
&#125;
.fc-icon-chevrons-left:before &#123;
  content: "\e902";
&#125;
.fc-icon-chevrons-right:before &#123;
  content: "\e903";
&#125;
.fc-icon-minus-square:before &#123;
  content: "\e904";
&#125;
.fc-icon-plus-square:before &#123;
  content: "\e905";
&#125;
.fc-icon-x:before &#123;
  content: "\e906";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里我们看到两个关注点：</p>
<ol>
<li>字体可以导出成 base64；所以如何将我们的图标转成 base64 需要看看；</li>
<li>每个图标都需要增加一个 <code>before</code> 伪类，具体看看还是有规律的，所以我们自己生成的尽可能和他们保持一致，前缀：<code>.fc-icon-</code>。</li>
</ol>
<h2 data-id="heading-1">制作 Font</h2>
<p>搜索一圈网站，大部分人推荐使用 icomoon <a href="https://link.juejin.cn/?target=https%3A%2F%2Ficomoon.io%2Fapp%2F%23%2Fselect" target="_blank" rel="nofollow noopener noreferrer" title="https://icomoon.io/app/#/select" ref="nofollow noopener noreferrer">icomoon.io/app/#/selec…</a></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/4e0be631a6434a2fba58e5c48b3cd772~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>官网提供了一些免费的和专题图标，但这不是我们需要的，这里，我先从 Naive UI 推荐的  xicons <a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.xicons.org%2F%23%2Fzh-CN" target="_blank" rel="nofollow noopener noreferrer" title="https://www.xicons.org/#/zh-CN" ref="nofollow noopener noreferrer">www.xicons.org/#/zh-CN</a> 里挑选出需要的 icons 的 SVG。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/428c48a001f449739aa768ca2334af93~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>再导入到 <a href="https://link.juejin.cn/?target=icomoon.io" target="_blank" title="icomoon.io" ref="nofollow noopener noreferrer">icomoon.io</a>。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/55821c668ec844f1ba5837bb7bf6ea63~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>然后，再为他们设定一些属性：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f93510927ad4a4bb0dd670fdba53263~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>下葬后的文件夹里，除了字体文件，还有一个 css 文件，内容和上面的 css 居然高度相似 (难道 FullCalendar 也是这个网站制作他们的 Font 的？)：</p>
<pre><code class="copyable">@font-face &#123;
  font-family: 'fcicons';
  src:
    url('fonts/fcicons.ttf?c33sp3') format('truetype'),
    url('fonts/fcicons.woff?c33sp3') format('woff'),
    url('fonts/fcicons.svg?c33sp3#fcicons') format('svg');
  font-weight: normal;
  font-style: normal;
  font-display: block;
&#125;

[class^="fc-icon-"], [class*=" fc-icon-"] &#123;
  /* use !important to prevent issues with browser extensions that change fonts */
  font-family: 'fcicons' !important;
  speak: never;
  font-style: normal;
  font-weight: normal;
  font-variant: normal;
  text-transform: none;
  line-height: 1;

  /* Better Font Rendering =========== */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
&#125;

.fc-icon-chevron-left:before &#123;
  content: "\e900";
&#125;
.fc-icon-chevron-right:before &#123;
  content: "\e901";
&#125;
.fc-icon-chevrons-left:before &#123;
  content: "\e902";
&#125;
.fc-icon-chevrons-right:before &#123;
  content: "\e903";
&#125;
.fc-icon-minus-square:before &#123;
  content: "\e904";
&#125;
.fc-icon-plus-square:before &#123;
  content: "\e905";
&#125;
.fc-icon-setting:before &#123;
  content: "\e907";
&#125;
.fc-icon-x:before &#123;
  content: "\e906";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>下面就是需要将字体文件转为 <code>base64</code> 格式的。</p>
<p>借助 <code>transfonter</code> 工具<a href="https://link.juejin.cn/?target=https%3A%2F%2Ftransfonter.org%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://transfonter.org/" ref="nofollow noopener noreferrer">transfonter.org/</a></p>
<blockquote>
<p>Modern and simple css @font-face generator</p>
</blockquote>
<pre><code class="copyable">@font-face &#123;
    font-family: 'fcicons';
    src: url('data:font/ttf;charset=utf-8;base64,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') format('truetype');
    font-weight: normal;
    font-style: normal;
    font-display: swap;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>所以，我们可以直接重写 css 了。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/03f7ba9ed1124f648cc9f1455126d1d6~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这样，我们就比 FullCalendar 多了一个<code>设置</code> 按钮：</p>
<pre><code class="copyable">::v-deep(.fc-icon-setting:before) &#123;
  content: "\e907";
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>好了，验证下，按钮图标的可用性，创建一个 Custorm Button：</p>
<pre><code class="copyable">  calendarOptions: &#123;
    plugins: [dayGridPlugin, interactionPlugin],
    customButtons: &#123;
      settingButton: &#123;
        icon: 'setting',
        click: this.settingClick,
      &#125; as CustomButtonInput,
    &#125; as unknown,
    headerToolbar: &#123;
      left: 'settingButton',
      center: 'title',
      right: 'prev,next',
    &#125;,
    
    ...
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看看效果：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/94e0cd04aa2e49feac774e9d8319e0d3~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">总结</h2>
<p>只要稍微调整下，以后可以根据需要，增加一些需要的图标，然后制作成 <code>base64</code> 格式，直接修改 <code>@font-face</code> 即可。</p>
<p>今天只是简单的介绍如何自制 Font 图标字体样式。之后可能可以做一些复杂的。</p></div>  
</div>
            