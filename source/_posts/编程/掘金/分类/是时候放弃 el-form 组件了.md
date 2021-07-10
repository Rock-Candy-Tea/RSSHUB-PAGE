
---
title: '是时候放弃 el-form 组件了'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/016236a56cdd4561b8dddceadc610e12~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Fri, 09 Jul 2021 23:31:46 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/016236a56cdd4561b8dddceadc610e12~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>相信很多正在用 element-ui 组件的同学，都会用到过 el-form 表单组件，这个组件帮助我们完成了表单验证和表单提交功能，但是在用的时候，会发现一些不方便的地方，比如说验证规则无法复用。</p>
<blockquote>
<h3 data-id="heading-0">关于无法复用</h3>
<p>比如说我的表单需要一个手机号格式验证规则，如果我在一个页面里面使用了，我就在这个页面里面复制一遍这个规则，这个还好，但是如果我在项目中的另外一个页面中，还要用到这个规则，还要复制一遍，这就让人有些不开心了。</p>
</blockquote>
<p>还有就是设定规则比较复杂，我们要使用一个规则的时候，需要在 <code>el-form</code> 组件上设置 <code>rules</code>, <code>model</code> 以及 <code>ref</code> 等属性，还要在 <code>el-form-item</code> 上设置 <code>prop</code> ，而且这里面有些是重复定义的变量，完全有优化的空间。而且内置的验证规则太少。</p>
<h1 data-id="heading-1">新的选择</h1>
<p>最近一段时间，在 Google 上找到了这么一款表单验证组件，初步试用，发现很强大，很方便，我们都知道，表单验证功能表单以及表单域的关联比较紧密，需要考虑数据的双向互通，以及错误数据的展示，要在已有的 element-ui 项目中，接入一个其他的项目来做，是很困难的，但是这款产品没有这个问题，因为 VueFormulate 是支持插件扩展的，首先它内置了一些比较漂亮的表单域，直接放在项目中也是没问题的，另外它还可以扩展使用其他的表单域，比如说 element-ui 中的文本输入框，数字输入框，级联选择器等等。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/016236a56cdd4561b8dddceadc610e12~tplv-k3u1fbpfcp-watermark.image" alt="2021-07-04 20-52-54 的屏幕截图.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>更多内容，可以查看 VueFormulate 的 <a href="https://link.juejin.cn/?target=https%3A%2F%2Ftu6ge.github.io%2Fvueformulate.com%2Fzh%2F" target="_blank" rel="nofollow noopener noreferrer" title="https://tu6ge.github.io/vueformulate.com/zh/" ref="nofollow noopener noreferrer">中文文档</a> ，最近这段时间刚刚翻译的。</p>
<h2 data-id="heading-2">融合 element-ui 和 VueFormulate</h2>
<p>因为我们的项目就是用的 element-ui 开发的，为了保持风格统一，还要用到 VueFormulate 就需要这样的一个插件，所以我就开源了这样一个插件 formulat-el-ui，为了减少大家的使用困难，这个插件是遵循语义化版本2.0 规范的。项目 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftu6ge%2Fformulate-el-ui" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tu6ge/formulate-el-ui" ref="nofollow noopener noreferrer">github 地址</a> ,如果无法访问，可以查看 <a href="https://link.juejin.cn/?target=https%3A%2F%2Fgitee.com%2Ftu6ge%2Fformulate_el_ui" target="_blank" rel="nofollow noopener noreferrer" title="https://gitee.com/tu6ge/formulate_el_ui" ref="nofollow noopener noreferrer">gitee</a></p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/da27e41f8033470da55fc4413e604d69~tplv-k3u1fbpfcp-watermark.image" alt="logo.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>请相信我，它一定会提高你的表单开发效率的。</p></div>  
</div>
            