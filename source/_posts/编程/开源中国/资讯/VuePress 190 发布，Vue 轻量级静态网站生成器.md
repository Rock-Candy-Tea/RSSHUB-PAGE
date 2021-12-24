
---
title: 'VuePress 1.9.0 发布，Vue 轻量级静态网站生成器'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-c0a095636019ea357c633020985c063dad6.png'
author: 开源中国
comments: false
date: Fri, 24 Dec 2021 07:02:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-c0a095636019ea357c633020985c063dad6.png'
---

<div>   
<div class="content">
                                                                                            <p>VuePress 1.9.0 发布了，此版本<span style="color:#24292f"><strong>为配置文件引入了完整的 TypeScript 支持</strong>，还引入了<strong>拥有类型推断功能的官方插件</strong>，</span>完整更新内容如下：</p> 
<h2><strong>支持 </strong><code><strong>.vuepress/config.ts</strong></code></h2> 
<p>之前，VuePress 只支持这些类型的配置文件</p> 
<ul> 
 <li><code>.vuepress/config.js</code></li> 
 <li><code>.vuepress/config.yml</code></li> 
 <li><code>.vuepress/config.toml</code></li> 
</ul> 
<p>从现在开始，<code>.vuepress/config.ts</code> 获得官方支持。</p> 
<p><img alt height="221" src="https://oscimg.oschina.net/oscnet/up-c0a095636019ea357c633020985c063dad6.png" width="700" referrerpolicy="no-referrer"></p> 
<h2><code><strong>defineConfig</strong></code> 智能感知配置助手</h2> 
<p><span style="color:#2e3033">一个在 <code>vuepress/config</code> 中显示的辅助函数，它可以辅助类型提示符:</span></p> 
<pre><code class="language-javascript">import &#123; defineConfig &#125; from "vuepress/config";

export default defineConfig(&#123;
  title: "VuePress",
  description: "Vue-powered Static Site Generator"
  // ...
&#125;);</code></pre> 
<h2><code><strong>Theme</strong></code><span style="color:#2e3033"> 基于主题的类型推断</span></h2> 
<p><span style="color:#2e3033">默认情况下，defineConfig 助手利用默认主题配置的类型作为 <code>themeConfig</code>，也就是说，所有默认主题配置的类型提示现在都可用。</span></p> 
<pre><code class="language-javascript">import &#123; defineConfig &#125; from "vuepress/config";

export default defineConfig(&#123;
  themeConfig: &#123;
    repo: "vuejs/vuepress",
    editLinks: true,
    docsDir: "packages/docs/docs"
    // Type is `DefaultThemeConfig`
  &#125;
&#125;);</code></pre> 
<p><span style="color:#2e3033">如果你使用一个自定义主题，则可以使用 <code>defineConfig4CustomTheme</code> 助手来传递你的主题的泛型类型:</span></p> 
<pre><code class="language-javascript">import &#123; defineConfig4CustomTheme &#125; from "vuepress/config";

interface MyThemeConfig &#123;
  hello: string;
&#125;

export default defineConfig4CustomTheme<MyThemeConfig>(&#123;
  themeConfig: &#123;
    // Type is `MyThemeConfig`
    hello: "vuepress"
  &#125;
&#125;);</code></pre> 
<h2><code><strong>Official Plugins</strong></code> 官方插件类型推断</h2> 
<p>从 1.9 开始，用户<span style="color:#24292f">将可以享受官方插件的类型提示：</span></p> 
<p><img alt height="226" src="https://oscimg.oschina.net/oscnet/up-f50ea3b05f5944998e5b92d38458bf883a7.png" width="700" referrerpolicy="no-referrer"></p> 
<p><span style="color:#2e3033">元组样式（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuepress.vuejs.org%2Fplugin%2Fusing-a-plugin.html%23plugin-options" target="_blank"><strong>Tuple Style</strong></a><span style="color:#2e3033">）、对象样式（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuepress.vuejs.org%2Fplugin%2Fusing-a-plugin.html%23plugin-options" target="_blank"><strong>Object Style</strong></a><span style="color:#2e3033">）和插件简写（</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuepress.vuejs.org%2Fplugin%2Fusing-a-plugin.html%23plugin-shorthand" target="_blank"><strong>Plugin Shorthand</strong></a><strong> </strong><span style="color:#2e3033">）都支持类型推断。</span></p> 
<ul> 
 <li><strong>元组样式：</strong></li> 
</ul> 
<pre><code class="language-javascript">import &#123; defineConfig &#125; from "vuepress/config";

export default defineConfig(&#123;
  plugins: [
    [
      "@vuepress/pwa",
      &#123;
        serviceWorker: true
      &#125;
    ]
  ]
&#125;);</code></pre> 
<p><img alt height="234" src="https://oscimg.oschina.net/oscnet/up-2f26f5fff56d906deeaba05d2dd78c77b13.png" width="700" referrerpolicy="no-referrer"></p> 
<ul> 
 <li><strong>对象样式：</strong></li> 
</ul> 
<pre><code class="language-javascript">import &#123; defineConfig &#125; from "vuepress/config";

export default defineConfig(&#123;
  plugins: &#123;
    "@vuepress/pwa": &#123;
      serviceWorker: true
    &#125;
  &#125;
&#125;);</code></pre> 
<h2>ISO 语言代码</h2> 
<p>类型推断支持 <a href="https://www.oschina.net/action/GoToLink?url=http%3A%2F%2Fwww.lingoes.net%2Fen%2Ftranslator%2Flangcode.htm" target="_blank">ISO 语言代码</a></p> 
<p><img alt height="331" src="https://oscimg.oschina.net/oscnet/up-891d1142ab79428ea63f6233781cdc4597c.png" width="500" referrerpolicy="no-referrer"></p> 
<h2>上下文 API</h2> 
<p>VuePress 的配置也可以是一个函数，而它的第一个参数是当前的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fvuepress.vuejs.org%2Fplugin%2Fcontext-api.html%23context-api" target="_blank">应用上下文</a>：</p> 
<pre><code>import &#123; defineConfig &#125; from "vuepress/config";

export default defineConfig(ctx => (&#123;
  // do not execute babel compilation under development
  evergreen: ctx.isProd
&#125;));</code></pre> 
<p>以上为 Vuepress 1.9 的更新内容，更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvuejs%2Fvuepress%2Freleases%2Ftag%2Fv1.9.0" target="_blank">https://github.com/vuejs/vuepress/releases/tag/v1.9.0</a></p>
                                        </div>
                                      
</div>
            