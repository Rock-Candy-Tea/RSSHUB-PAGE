
---
title: 'element-ui 自定义主题配置'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25645036b12f49a0bb06690754667b8c~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 03 May 2021 02:44:05 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25645036b12f49a0bb06690754667b8c~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>根据官方文档，按需引入配合<code>babel-plugin-component</code>使用，然后将.babelrc修改为：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-string">"presets"</span>: [[<span class="hljs-string">"es2015"</span>, &#123; <span class="hljs-string">"modules"</span>: <span class="hljs-literal">false</span> &#125;]],
  <span class="hljs-string">"plugins"</span>: [
    [
      <span class="hljs-string">"component"</span>,
      &#123;
        <span class="hljs-string">"libraryName"</span>: <span class="hljs-string">"element-ui"</span>,
        <span class="hljs-string">"styleLibraryName"</span>: <span class="hljs-string">"theme-chalk"</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>我们还可以自定义的去覆盖element-ui的scss样式变量，来修改主题颜色。创建element-variables.scss</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">/* 改变主题色变量 */</span>
<span class="hljs-variable">$--color-primary</span>: <span class="hljs-number">#912</span>;
<span class="hljs-comment">/* 改变 icon 字体路径变量，必需 */</span>
<span class="hljs-variable">$--font-path</span>: <span class="hljs-string">'~element-ui/lib/theme-chalk/fonts'</span>;

<span class="hljs-keyword">@import</span> <span class="hljs-string">"~element-ui/packages/theme-chalk/src/index"</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>然后在main.js文件中导入element-variables.scss:</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>
<span class="hljs-keyword">import</span> <span class="hljs-string">'@/assets/style/element-variables.scss'</span>

Vue.component(Button.name, Button)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>但是现在有一个问题是，通过这种方式修改主题打包出来的css非常大。但是如果注释掉该语句样式又不会起作用，这是非常让人懊恼的。</p>
<p>通过下图，我们可以知道其实<code>babel-plugin-component</code>是生效了的。但是<code>app.[hash].css</code>的体积十分巨大，里面包含了element-ui的所有样式，甚至和<code>chunk-vendors.[hash].css</code>中的样式有重复的部分。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/25645036b12f49a0bb06690754667b8c~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-05-03_17-53-16.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>追其原因还是因为在<code>babel-plugin-component</code>中默认使用的是<code>lib</code>文件夹进行打包，但是在lib文件夹中样式文件是css文件，使我们没办法通过仅仅只是修改scss样式变量的覆盖方式来做到动态的去更改主题色。这就是为什么如果我们注释了<code>@import "~element-ui/packages/theme-chalk/src/index";</code>语句，自定义主题就不生效了的原因，我们前面重新定义的样式变量其实为了覆盖<code>index.scss</code>文件中的变量，再通过重新生成新的样式去覆盖原有的样式文件来做到自定义主题的效果。</p>
<p>但是我们可以通过修改<code>babel-plugin-component</code>配置+全局导入样式变量的方式来实现真正的样式的按需加载。</p>
<p>修改.babelrc文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">presets</span>: [
    <span class="hljs-string">'@vue/cli-plugin-babel/preset'</span>
  ],
  <span class="hljs-attr">plugins</span>: [
    [
      <span class="hljs-string">'component'</span>,
      &#123;
        <span class="hljs-string">'libraryName'</span>: <span class="hljs-string">'element-ui'</span>,
        <span class="hljs-comment">// 默认情况下，libDir的默认是lib文件夹</span>
        <span class="hljs-string">'libDir'</span>: <span class="hljs-string">'packages'</span>,
        <span class="hljs-comment">// scss文件是放在packages/theme-chalk/src下的</span>
        <span class="hljs-string">'styleLibraryName'</span>: <span class="hljs-string">'theme-chalk/src'</span>,
        <span class="hljs-string">'ext'</span>: <span class="hljs-string">'.scss'</span>
      &#125;
    ]
  ]
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这时候，就可以实现按需引入的是scss了，然后我们在配置全局scss变量。
修改element-variables.scss文件，只保留变量：</p>
<pre><code class="hljs language-scss copyable" lang="scss"><span class="hljs-comment">/* 改变主题色变量 */</span>
<span class="hljs-variable">$--color-primary</span>: <span class="hljs-number">#912</span>;
<span class="hljs-comment">/* 改变 icon 字体路径变量，必需 */</span>
<span class="hljs-comment">// $--font-path: '~element-ui/lib/theme-chalk/fonts';</span>

<span class="hljs-comment">// @import "~element-ui/packages/theme-chalk/src/index";</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>配置vue.config.js文件：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript">&#123;
  <span class="hljs-attr">css</span>: &#123;
    <span class="hljs-attr">loaderOptions</span>: &#123;
      <span class="hljs-attr">scss</span>: &#123;
        <span class="hljs-attr">prependData</span>: [
          <span class="hljs-string">'@import "src/assets/style/element-variables.scss";'</span>,
          <span class="hljs-comment">// 非必须</span>
          <span class="hljs-comment">// 这里引入element-ui本身的变量，是因为其他样式文件可能会用到它本身的变量</span>
          <span class="hljs-comment">// 但是在自定义变量文件中又没有做覆盖定义</span>
          <span class="hljs-string">'@import "~element-ui/packages/theme-chalk/src/common/var.scss";'</span>
        ].join(<span class="hljs-string">''</span>)
      &#125;
    &#125;
  &#125;
&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在main.js中可以不需要像开始那样引入自定义主题样式了：</p>
<pre><code class="hljs language-javascript copyable" lang="javascript"><span class="hljs-keyword">import</span> &#123; Button &#125; <span class="hljs-keyword">from</span> <span class="hljs-string">'element-ui'</span>
<span class="hljs-comment">// import '@/assets/style/element-variables.scss'</span>

Vue.component(Button.name, Button)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>打包效果：</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f3b5c2e0281a47fb8dfbf6077cb2d37b~tplv-k3u1fbpfcp-watermark.image" alt="Snipaste_2021-05-03_18-14-04.png" loading="lazy" referrerpolicy="no-referrer"></p></div>  
</div>
            