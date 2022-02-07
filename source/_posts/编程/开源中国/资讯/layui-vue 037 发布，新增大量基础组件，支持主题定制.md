
---
title: 'layui-vue 0.3.7 发布，新增大量基础组件，支持主题定制'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-5bcc0f750d390ee98239365f797763b1dfd.png'
author: 开源中国
comments: false
date: Mon, 07 Feb 2022 14:47:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-5bcc0f750d390ee98239365f797763b1dfd.png'
---

<div>   
<div class="content">
                                                                                            <p>更新内容：</p> 
<p><strong>0.3.7</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[新增] slider 滑块组件 setp 属性, 支持设置步长。</li> 
 <li>[新增] index.less 样式文件, 支持一定程度的主题定制。</li> 
 <li>[移除] `defineProps`,`defineEmits` 两个全局宏命令引入，消除控制台警告。</li> 
 <li>[修复] menu 组件 inverted 属性不兼容 string 类型。</li> 
 <li>[修复] menu 组件 level 属性不兼容 string 类型。</li> 
 <li>[升级] icons-vue 1.0.4 版本。</li> 
 <li>[升级] layer-vue 1.3.3 版本。</li> 
</ul> 
<p><strong>0.3.6</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[新增] result 结果组件, 提供 success error 通用状态页。</li> 
 <li>[新增] exception 异常组件, 提供 403, 404, 500 通用异常页。</li> 
 <li>[新增] menu 组件 level 属性, 控制菜单层级之间的背景色差异。</li> 
 <li>[新增] menu 组件 inverted 属性, 提供另一种树形菜单选中效果。</li> 
 <li>[新增] menu 组件 theme 属性, 可选值 light 和 dark。</li> 
 <li>[修复] table 组件 header 不随 body 滚动。</li> 
 <li>[升级] vue 3.2.29 版本。</li> 
</ul> 
<p><strong>0.3.5</strong></p> 
<ul style="margin-left:0; margin-right:0"> 
 <li>[新增] split-panel 分割面板, 高度灵活的布局组件。</li> 
 <li>[新增] layer 弹层 type 属性 drawer 可选值, 提供抽屉模式。</li> 
 <li>[修复] tab-item 组件 closable 属性警告, 兼容 string 类型。</li> 
 <li>[修复] dropdown 下拉菜单 content 显示位置问题。</li> 
 <li>[升级] icons-vue 1.0.3 版本。</li> 
 <li>[升级] layer-vue 1.3.1 版本。</li> 
</ul> 
<p>更新详情：</p> 
<p><strong>主题定制</strong></p> 
<p>新版本发布后，<span style="color:rgba(0, 0, 0, 0.85)">支持一定程度的主题定制，以满足业务和品牌上多样化的视觉需求，包括但不限于主色、圆角、边框和部分组件的视觉定制。以下是一些最常用的通用变量，所有样式变量可以在 这里 找到。</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#cc99cd"><span>@global-primary-color</span><span style="color:#cccccc">:</span> #009688<span style="color:#cccccc">;</span></span> // 主题色
<span style="color:#cc99cd"><span>@global-checked-color</span><span style="color:#cccccc">:</span> #5FB878<span style="color:#cccccc">;</span></span> // 选中色 
<span style="color:#cc99cd"><span>@global-border-radius</span><span style="color:#cccccc">:</span> 2px<span style="color:#cccccc">;</span></span> // 圆角度数</code></pre> 
<p><span style="color:rgba(0, 0, 0, 0.85)">除全局的主题配置外, 我们还对组件提供定制化的主题配置</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#cc99cd"><span>@button-primary-color</span><span style="color:#cccccc">:</span> #009688<span style="color:#cccccc">;</span></span> // 按钮主题色
<span style="color:#cc99cd"><span>@button-border-radius</span><span style="color:#cccccc">:</span> 2px<span style="color:#cccccc">;</span></span> // 按钮圆角度数
...</code></pre> 
<p><span style="color:rgba(0, 0, 0, 0.85)">如何定制 ，建立一个单独的 less 变量文件，引入这个文件覆盖 index.less 里的变量。</span></p> 
<pre style="margin-left:0; margin-right:0; text-align:left"><code><span style="color:#cc99cd"><span>@import</span> <span style="color:#7ec699">'@layui/layui-vue/lib/index.less'</span><span style="color:#cccccc">;</span></span> // 引入官方提供的 less 样式入口文件
<span style="color:#cc99cd"><span>@import</span> <span style="color:#7ec699">'your-theme-file.less'</span><span style="color:#cccccc">;</span></span> // 用于覆盖上面定义的变量</code>
</pre> 
<p><strong>异常组件</strong></p> 
<p>在实际开发场景中，开发者需要去定义常用错误页面，为避免大量重复的编码工作，我们为开发者预定义了一组通用的错误页面，使用 lay-exception 标签进行创建</p> 
<p><img height="2170" src="https://oscimg.oschina.net/oscnet/up-5bcc0f750d390ee98239365f797763b1dfd.png" width="1386" referrerpolicy="no-referrer"></p> 
<p><strong>结果组件</strong></p> 
<p>除异常页面外，我们还可以通过 result 组件，来构建 成功 与 失败 的反馈提醒</p> 
<p><img height="844" src="https://oscimg.oschina.net/oscnet/up-0450a8ccbce9f1dd08a7b702d2fb0982383.png" width="1523" referrerpolicy="no-referrer"></p> 
<p> </p> 
<p><strong>分割面板</strong></p> 
<p>更灵活的布局方案</p> 
<p><img height="638" src="https://oscimg.oschina.net/oscnet/up-cb4de581b0a914bd73cc5b21060fbba2452.png" width="1531" referrerpolicy="no-referrer"></p>
                                        </div>
                                      
</div>
            