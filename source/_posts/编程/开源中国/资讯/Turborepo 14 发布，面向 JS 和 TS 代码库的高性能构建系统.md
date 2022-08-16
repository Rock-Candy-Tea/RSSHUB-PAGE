
---
title: 'Turborepo 1.4 发布，面向 JS 和 TS 代码库的高性能构建系统'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-28316ae18d78feb8a0b7ed784bd2a998df0.png'
author: 开源中国
comments: false
date: Tue, 16 Aug 2022 07:21:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-28316ae18d78feb8a0b7ed784bd2a998df0.png'
---

<div>   
<div class="content">
                                                                                            <p>Turborepo 1.4 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fturborepo.org%2Fblog%2Fturbo-1-4-0" target="_blank">已发布</a>。</p> 
<blockquote> 
 <p>Turborepo 是一个适用于 JavaScript 和 TypeScript 代码库的高性能 monorepo 构建系统。</p> 
 <p><img alt src="https://oscimg.oschina.net/oscnet/up-28316ae18d78feb8a0b7ed784bd2a998df0.png" referrerpolicy="no-referrer"></p> 
 <p>所谓 monorepo，简单来说就是将所有项目代码放到一个 Git / Mercurial / Subversion 代码仓库中。当下许多大型前端项目和公司都采用了 monorepo 方案，比如 Google、Facebook，以及社区知名开源项目 Babel、Vue-next 都使用了 monorepo 方来管理他们的代码。</p> 
 <p><img src="https://static.oschina.net/uploads/space/2022/0815/165311_rpS9_2720166.png" referrerpolicy="no-referrer"></p> 
</blockquote> 
<p>Turborepo 1.4 主要变化</p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fturborepo.org%2Fblog%2Fturbo-1-4-0%23automatic-environment-variable-inclusion" target="_blank"><strong>自动引入环境变量：</strong></a>此功能可自动推导出流行框架的环境变量，因此开发者无需在<code>turbo.json</code>中自行声明</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fturborepo.org%2Fblog%2Fturbo-1-4-0%23eslint-config-turbo" target="_blank"><strong><code>eslint-config-turbo</code>：</strong></a>使用新的 ESLint 插件来增强反馈功能</li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fturborepo.org%2Fblog%2Fturbo-1-4-0%23new-framework-and-library-examples" target="_blank"><strong>增加新框架和库示例</strong>：</a>社区建议添加的新入门和示例</li> 
</ul> 
<p><strong>自动引入环境变量</strong></p> 
<p>为了帮助确保在跨环境场景中正确缓存，当计算 Astro、Create React App、Gatsby、Next.js、Nuxt、SvelteKit、Vite、Vue 等构建的应用的缓存密钥 (cache keys) 时，Turborepo 现在会自动推导和引入公开环境变量。</p> 
<pre><code>&#123;
  "pipeline": &#123;
    "build": &#123;
      "dependsOn": [
        "^build"
-       // Include build time public inlined environment variables that
-       // are different in development and production, so that
-       // Turborepo does not use the same cached build
-       // across environments
-       "$NEXT_PUBLIC_EXAMPLE_ENV_VAR"
      ]
    &#125;
  &#125;
&#125;</code></pre> 
<p><strong>新框架和库示例</strong></p> 
<ul> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-svelte" target="_blank">Svelte</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-docker" target="_blank">Docker</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-create-react-app" target="_blank">Create React App</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-react-native-web" target="_blank">React Native</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-prisma" target="_blank">Prisma</a></li> 
 <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples%2Fwith-tailwind" target="_blank">Tailwind</a></li> 
 <li>…<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fturborepo%2Ftree%2Fmain%2Fexamples" target="_blank">and more!</a></li> 
</ul> 
<p><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fturborepo.org%2Fblog%2Fturbo-1-4-0" target="_blank">详情查看发布公告</a>。</p> 
<p> </p>
                                        </div>
                                      
</div>
            