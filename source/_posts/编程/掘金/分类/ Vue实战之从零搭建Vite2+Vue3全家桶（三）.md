
---
title: '# Vue实战之从零搭建Vite2+Vue3全家桶（三）'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://picsum.photos/400/300?random=3899'
author: 掘金
comments: false
date: Tue, 27 Jul 2021 23:52:03 GMT
thumbnail: 'https://picsum.photos/400/300?random=3899'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">前言</h1>
<p>闲暇时间写写文章，能写多少写多少，主要是用来总结完善一下自己的技术栈，查漏补缺。 上一篇完善了http请求工具的使用，本篇主要介绍icon图标管理插件的使用。</p>
<h1 data-id="heading-1">上一篇传送门</h1>
<p><a href="https://juejin.cn/post/6989881321317204004" target="_blank" title="https://juejin.cn/post/6989881321317204004">Vue实战之从零搭建Vite2+Vue3全家桶（二）</a></p>
<h1 data-id="heading-2">icon图标管理</h1>
<p>这里采用\textrm\color&#123;red&#125;&#123; vite-plugin-svg-icons&#125; vite-plugin-svg-icons插件来对svg图标进行管理</p>
<h2 data-id="heading-3">vite-plugin-svg-icons特征</h2>
<ul>
<li>预加载，在项目运行时就生成所有图标，只需要操作一次dom</li>
<li>高性能 内置缓存,仅当文件被修改时才会重新生成</li>
</ul>
<h2 data-id="heading-4">安装vite-plugin-svg-icons</h2>
<pre><code class="copyable">  # 安装要求
  # node version: >=12.0.0
  # vite version: >=2.0.0

  npm i vite-plugin-svg-icons -d
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-5">修改vite.config.js</h2>
<pre><code class="copyable">import viteSvgIcons from 'vite-plugin-svg-icons'
plugins: [
  vue(),
  viteSvgIcons(&#123;
    // 配置路劲在你的src里的svg存放文件
    iconDirs: [path.resolve(process.cwd(), 'src/icons')],
    symbolId: 'icon-[name]'
  &#125;)
]
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-6">封装SvgIcon组件</h2>
<h3 data-id="heading-7">创建svgIcon公共组件</h3>
<p>src/components目录下新建SvgIcon目录,SvgIcon目录下新建index.vue</p>
<pre><code class="copyable">  <template>
    <svg aria-hidden="true" class="svg-icon">
      <use :xlink:href="symbolId" :fill="color" />
    </svg>
  </template>

  <script>
  import &#123; defineComponent, computed &#125; from 'vue'

  export default defineComponent(&#123;
    name: 'SvgIcon',
    props: &#123;
      prefix: &#123;
        type: String,
        default: 'icon'
      &#125;,
      name: &#123;
        type: String,
        required: true
      &#125;,
      color: &#123;
        type: String,
        default: 'white'
      &#125;
    &#125;,
    setup(props) &#123;
      const symbolId = computed(() => `#$&#123;props.prefix&#125;-$&#123;props.name&#125;`)
      return &#123; symbolId &#125;
    &#125;
  &#125;)
  </script>
  <style scoped>
  .svg-icon &#123;
    width: 1em;
    height: 1em;
    fill: currentColor;
    vertical-align: middle;
  &#125;
  </style>

复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-8">icons目录结构</h3>
<pre><code class="copyable"># src/icons

- password.svg
- username.svg
- ...
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-9">修改main.js</h2>
<pre><code class="copyable"> import 'virtual:svg-icons-register' 
 import SvgIcon from '@/components/SvgIcon/index.vue' 

 const app = createApp(App)
 app.component('svg-icon', SvgIcon)

复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h2 data-id="heading-10">vue组件中使用svgIcon</h2>
<pre><code class="copyable"><template>
...
 <svg-icon name="password"  />
...
</template>
复制代码
<span class="copy-code-btn">复制代码</span></code></pre>
<h1 data-id="heading-11">往期传送门</h1>
<p><a href="https://juejin.cn/post/6989881321317204004" target="_blank" title="https://juejin.cn/post/6989881321317204004">Vue实战之从零搭建Vite2+Vue3全家桶（二）</a></p>
<p><a href="https://juejin.cn/post/6989880565973385247" target="_blank" title="https://juejin.cn/post/6989880565973385247">Vue实战之从零搭建Vite2+Vue3全家桶（一）</a></p>
<p><a href="https://juejin.cn/post/6984708706231386119" title="https://juejin.cn/post/6984708706231386119" target="_blank">基于Vue的架构设计</a></p></div>  
</div>
            