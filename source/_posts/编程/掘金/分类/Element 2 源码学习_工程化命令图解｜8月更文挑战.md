
---
title: 'Element 2 源码学习_工程化命令图解｜8月更文挑战'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5bb1ddd3454a9b9829a58c32e4f358~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Sat, 31 Jul 2021 22:41:33 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5bb1ddd3454a9b9829a58c32e4f358~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:14px;overflow-x:hidden;color:#353535&#125;.markdown-body h1&#123;padding-bottom:4px;font-size:30px&#125;.markdown-body h1,.markdown-body h2&#123;margin-top:36px;margin-bottom:10px;line-height:1.5;color:#005bb7&#125;.markdown-body h2&#123;position:relative;padding-left:16px;padding-right:10px;padding-bottom:10px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h2:before&#123;content:"「";position:absolute;top:-6px;left:-10px&#125;.markdown-body h2:after&#123;content:"」";position:absolute;top:6px;right:auto&#125;.markdown-body h3&#123;position:relative;padding-bottom:0;margin-top:30px;margin-bottom:10px;font-size:20px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h3:before&#123;content:"»";padding-right:6px;color:#2196f3&#125;.markdown-body h4&#123;margin-top:24px;font-size:16px&#125;.markdown-body h4,.markdown-body h5&#123;padding-bottom:0;margin-bottom:10px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body h5&#123;margin-top:18px;font-size:14px&#125;.markdown-body h6&#123;padding-bottom:0;margin-top:12px;margin-bottom:10px;font-size:12px;line-height:1.5;color:#005bb7;padding-left:6px&#125;.markdown-body p&#123;line-height:inherit;margin-top:16px;margin-bottom:16px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;position:relative;width:98%;height:1px;margin-top:32px;margin-bottom:32px;background-image:linear-gradient(90deg,#007fff,rgba(255,0,0,.3),hsla(0,0%,100%,.1),rgba(255,0,0,.3),#007fff);border-width:0;overflow:visible&#125;.markdown-body hr:after&#123;content:"";position:absolute;margin:auto;left:0;right:0;bottom:0;top:0;display:inline-block;width:60px;height:20px;background:#fff;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAgCAYAAABgrToAAAADoklEQVRYR82XTYgcRRTHf2933Q1RjAa9eFO8JHoJ8RQVBQ2iBwXBET0YEUTXNVmNQtTpmeqaWV0XNRq/o4KoECSCEPSg4CF+BYUkIIiCoCJCPIhC/Ihh2Z0nVV27VnZnenumW9i6ddV7//frV69fVQurfMgq56NawFTPAU6QyomqXrw6wIZeyhCPebA5buNR+akKyGoAjd6BshthnYdSjqNcRVuOlIUsD2j0SuA94IwuMHdh5ZUykOUBXfSGbmKI54EtAeYIHSZoy5dl4JxvNYBOKdW1KE8BQ8AkVk6WhasWsAiN0TX9gveXQaPP+Aytpc4u+bMI06JNohsYYYYOR2lJWtS3OKDRfcAtQfgDoI6Vo4UCGb0OmAEuDvZvYmVbEd/igC3dzDz7gQu8sPA9kJDK27mBmjqBeLjTg90PDFOjWawFFQd06kZHEfaj3LAIpTRpSXsZ5E06zEYP9sDimnAApYaV2SLZG/wjMeqAkijwW4xQJ5Gf/ZzRC8OW3hiBTGGlURRswW55Bh/Ssxljrwew8l1PQaM14GngvGDzBUKdDsMeTtgU5o8B92PFlUf3YXUrHa7Fys6lBqcCGnX15YQ2A18FyPd7Crd1A3M8C1wdbH4DD3hWeP6IEXbQkG97ajR1HPFnuPP5jFFq1OWX7hl8WM9l1AO648uNfwLk7tytMeogty+xeQ4rO3r6bdcx1nuwOGsHmaXGtPzae4uzGnLH1kQkvpdZGrHjssBZJrL+pqS05KWc8tgITAPXRzYvYOXe/C2OV43eDcRBDtIhoS2f9wzc0Cv8Wls+zoFzUC5zF0U241h5uZtPfptp6OUM8wbK+cH5GEpCS17P3fJei0Z3+npTxryJ8CPzbKMtn/ZyWbkPGl0PuFPkmkjkcb4h4R2ZLwRq1H0ALmvjkf2HwK1Y+T1PY2XABe/sHJ6MxN5lnoSpnC/UGbsTaI5phK2R7x6s3Ffk5YoDOrWm3onwJHBmEP86bPmBrsGaenNoIdnxCH+gPEhLXi0Cl1VBvyPVLSh7gEuC62yAfOIUqabWEaaiucMIk6RyqJ+Q/QM69V26jjW86Gvov/EaoyT8zRCn+Xq7PVrbx0nuYUaO9wM3WAbjCE1NEUw09Um4UV+2OKfYfu5/S19gsAzGKqm6LE5FrShbdS0ku465DjDwKA/oQht19ejqbaEVuRbiLhuHByYLjtUAZpDutzP7cYdHsPJXWbjyNVgFwQoa1WXwf4Jd9YD/Ap80+yE7+u9aAAAAAElFTkSuQmCC);background-repeat:no-repeat;background-size:auto 100%;background-position-x:center&#125;.markdown-body code&#123;padding:.065em .4em;font-size:.87em;color:#c2185b;word-break:break-word;overflow-x:auto;background-color:#fff4f4;border-radius:2px&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;display:block;padding:16px 12px;margin:0;font-size:12px;color:#333;word-break:normal;overflow-x:auto;background:#f8f8f8&#125;.markdown-body pre>code::-webkit-scrollbar&#123;width:4px;height:4px&#125;.markdown-body pre>code::-webkit-scrollbar-track&#123;background-color:#bedcff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#2196f3;border-radius:10px&#125;.markdown-body a&#123;position:relative;text-decoration:none;color:#3da8f5;border-bottom:1px solid #bedcff&#125;.markdown-body a:hover&#123;color:#007fff;border-bottom-color:#007fff&#125;.markdown-body a:active&#123;color:#007fff&#125;.markdown-body a:after&#123;position:absolute;content:"";top:100%;left:0;width:100%;opacity:0;border-bottom:1px solid #bedcff;transition:top .3s,opacity .3s;transform:translateZ(0)&#125;.markdown-body a:hover:after&#123;top:0;opacity:1;border-bottom-color:#007fff&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #c3e0fd;border-spacing:0;border-collapse:collapse&#125;.markdown-body table thead&#123;color:#000;text-align:left;font-size:14px;background:#f6f6f6&#125;.markdown-body table tr:nth-child(2n)&#123;background-color:#f7fbff&#125;.markdown-body table tr:hover&#123;background-color:#e0edf7&#125;.markdown-body table td,.markdown-body table th&#123;padding:12px 8px;line-height:24px;border:1px solid #c3e0fd&#125;.markdown-body table th&#123;color:#005bb7;background-color:#dff0ff&#125;.markdown-body table td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#8c8c8c;border-left:4px solid #2196f3;background-color:#f0fdff;padding:1px 20px;margin:22px 0&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body b,.markdown-body blockquote>b,.markdown-body blockquote>strong,.markdown-body strong&#123;color:#2196f3&#125;.markdown-body em,.markdown-body i&#123;color:#4fc3f7&#125;.markdown-body del&#123;color:#ccc&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:4px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body details>summary&#123;outline:none;color:#005bb7;font-size:20px;font-weight:bolder;border-bottom:1px solid #bedcff;cursor:pointer&#125;.markdown-body details>p&#123;padding:10px 20px;margin:10px 0 0;color:#666;background-color:#f0fdff;border:2px dashed #2196f3&#125;.markdown-body h1::selection,.markdown-body h2::selection,.markdown-body h3::selection,.markdown-body h4::selection,.markdown-body h5::selection,.markdown-body h6::selection&#123;color:#005bb7;background-color:rgba(160,200,255,.15)&#125;.markdown-body p::selection&#123;color:#c80000&#125;.markdown-body a::selection,.markdown-body b::selection,.markdown-body del::selection,.markdown-body em::selection,.markdown-body i::selection,.markdown-body strong::selection&#123;background-color:transparent&#125;.markdown-body code::selection&#123;background-color:#ffeaeb&#125;.markdown-body pre>code::selection&#123;background-color:rgba(160,200,255,.25)&#125;.markdown-body ol ::selection,.markdown-body ul ::selection&#123;background-color:rgba(160,200,255,.15)&#125;.markdown-body .contains-task-list&#123;padding-left:14px;list-style:none&#125;.markdown-body .contains-task-list input[type=checkbox]&#123;position:relative&#125;.markdown-body .contains-task-list input[type=checkbox]:before&#123;content:"";position:absolute;top:0;left:0;right:0;bottom:0;width:inherit;height:inherit;background:#f0f8ff;border:1px solid #add6ff;border-radius:2px;box-sizing:border-box;z-index:1&#125;.markdown-body .contains-task-list input[type=checkbox]:checked:after&#123;content:"✓";position:absolute;top:-12px;left:0;right:0;bottom:0;width:0;height:0;color:#f55;font-size:20px;font-weight:700;z-index:2&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">0x00 前言</h1>
<p>在工程化系列文章中介绍了项目构建、代码开发、分支管理、自动化测试、持续集成、项目部署、性能等内容。涉及到繁多的命令、工作流程、依赖文件。下面将通过图解的方式更加直观的说明其工作流，耐心读完，相信会对您有所帮助。</p>
<p>本文涉及知识点均为工程化系列文章内容，请优先阅读该系列文章👇。</p>
<p><a href="https://juejin.cn/column/6975866472513929247" target="_blank" title="https://juejin.cn/column/6975866472513929247">专栏：Element 2 源码学习--项目工程化剖析</a></p>
<h1 data-id="heading-1">0x01 文件构建</h1>
<h2 data-id="heading-2">npm run i18n</h2>
<p>执行 <code>node build/bin/i18n.js</code>，基于 <code>examples/i18n/page.json</code> 各页面及国际化配置、 <code>examples/pages/template</code> 目录下的所有模版文件，在目录<code>examples/pages/&#123;lang&#125;</code>下生成 <code>zh-CN</code>、<code>en-US</code>、<code>es</code>、<code>fr-FR</code> 等四种语言的网站.vue文件。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0f5bb1ddd3454a9b9829a58c32e4f358~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-3">npm run build:file</h2>
<p>执行命令后，并行执行多个任务生成文件</p>
<p>执行 <code>node build/bin/iconInit.js</code> ，使用 <code>postcss</code> 解析 <code>packages/theme-chalk/src/icon.scss</code>，提取所有 <code>icon</code> 名字生成 <code>examples/icon.json</code> 图标集合文件。 <code>icon.json</code> 在官网入口文件<code>examples\entry.js</code> 中导入，挂载到 <code>Vue.prototype</code>。 用于<code>Icon图标</code>文档页生成所有的图标集合 。</p>
<p>执行 <code>node build/bin/build-entry.js</code>，基于组件清单文件<code>components.json</code>结合字符串模版库<code>json-templater/string</code>自动生成 <code>src/index.js</code> 组件库入口文件。</p>
<p>执行 <code>node build/bin/i18n.js</code> 生成官网的多语言网站文件,详见命令  <code>npm run i18n</code> 介绍。</p>
<p>执行 <code>node build/bin/version.js</code> 获取<code>package.json</code>中 <code>version</code>版本号， 生成 <code>examples/version.json</code>项目版本列表信息，用于网站版头部导航版本切换。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2e6e923a8cf04e2f8620a433b670602c~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-4">npm run build:theme</h2>
<p>用于项目的主题和样式生成。</p>
<h3 data-id="heading-5">1️⃣ 生成入口文件</h3>
<p><code>node build/bin/gen-cssfile</code> 找到 <code>components.json</code>， 获取组件列表，找到<code>packages/theme-chalk/src</code>目录下对应的各组件的 <code>component-name.scss</code> 文件，以<code>@import "./component-name.scss"</code>的形式，写入<code>packages/theme-chalk/index.scss</code>文件-样式总入口文件。若是组件对应的样式不存在，会自动创建遗漏的样式文件。</p>
<h3 data-id="heading-6">2️⃣ 构建主题</h3>
<p><code>gulp build --gulpfile packages/theme-chalk/gulpfile.js</code> 会执行 <code>gulpfile.js</code> 定义两个任务(task):</p>
<ul>
<li>将<code>packages/theme-chalk/src</code>目录下的 scss 文件转换成 css 文件，经过浏览器兼容、压缩处理，输出至<code>packages/theme-chalk/src/lib</code>目录下;</li>
<li>将<code>packages/theme-chalk/src/fonts</code>目录下的字体图标文件压缩处理，输出至 <code>packages/theme-chalk/src/lib/fonts</code> 目录下。</li>
</ul>
<h3 data-id="heading-7">3️⃣ 拷贝至lib/theme-chalk下</h3>
<p>通过<code>cp-cli</code>，将<code>packages/theme-chalk/src/lib</code>目录下文件拷贝至<code>lib/theme-chalk</code>目录下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aea93defb9214cc8ab39365357569e77~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-8">npm run build:utils</h2>
<p>把 <code>src</code> 目录下除了 <code>src/index.js </code>文件外的其他文件通过 <code>babel</code> 转译后，输出至 <code>lib</code> 文件夹下。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/946a24996bfa4429814393631ffec6c0~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-9">npm run build:umd</h2>
<p>执行 <code>node build/bin/build-locale.js</code> ,遍历 <code>src/locale/lang</code> 目录下所有JS文件，通过 <code>babel</code> 转译成 <code>umd</code> 格式，输出至 <code>lib/umd/locale</code> 目录下。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2449e93c607c4ade8169aa26a7613b9b~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-10">0x02 开发调试模式</h1>
<h2 data-id="heading-11">npm run dev</h2>
<p>首先，执行命令<code>npm run bootstrap</code> 安装项目依赖， 初始化开发环境。<br>
其次，执行命令<code>npm run build:file</code> 构建网站相关文件，详见上文命令介绍。<br>
最后，运行<code>webpack-dev-server</code> 提供一个本地服务(serve) ，编译运行项目网站(打包规则配置 <code>build/webpack.demo.js</code>, 模式是<code>development</code>，入口文件是<code>examples/entry.js</code>);同时执行 <code>node build/bin/template.js</code> 文件启动<code>chokidar</code>监听 <code>examples/pages/template</code> 目录下模板文件，若内容发生变化，执行命令 <code>npm run i18n</code> 重新生成网站文件。</p>
<p><code>webpack-dev-server</code> 具有 <code>live reloading</code> 功能,网站文件变更会重新编译加载。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/36d4daea6355436aafbf5781e374b38d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-12">npm run dev:play</h2>
<p>首先，执行命令<code>npm run build:file</code> 构建网站相关文件，详见上文命令介绍。<br>
其次，运行<code>webpack-dev-server</code> 提供一个本地服务(serve) ，编译运行项目网站(打包规则配置 <code>build/webpack.demo.js</code>)。</p>
<p>命令中设置环境变量 <code>NODE_ENV=development PLAY_ENV=true</code>,打包入口文件为<code> examples/play.js</code>, 该文件引用 <code> examples/play/index.vue</code>, 用于组件库功能展示。</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e2b0a7ac895040118e7c5a4f25c35a9e~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-13">npm run dev:extension</h2>
<p>chorme 插件项目开发调试 ,首先 <code>rimraf examples/extension/dist</code> 清除项目上次打包构建内容，然后使用 <code>webpack</code> 打包构建项目，配置文件<code>build/webpack.extension.js</code>, 入口文件为<code>examples/extension/src/background.js</code>和<code>examples/extension/src/entry.js</code>。使用 <code>watch</code> 模式,若开发中文件发生变化，则重新打包.</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/891751a16bd241fb8041c03beafd8fac~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-14">0x03 项目构建</h1>
<h2 data-id="heading-15">npm run deploy:extension</h2>
<p>与命令<code>npm run dev:extension</code>相似，使用同一打包配置文件，相同的入口文件。不同之处基于 <code>production</code> 模式对应规则进行打包,没有使用 <code>watch</code> 模式。</p>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/0b2c189210af40d7a21485ce345776ee~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-16">npm run deploy:build</h2>
<p>首先，执行命令<code>npm run build:file</code> 构建网站相关文件，详见上文命令介绍。<br>
其次，执行<code>webpack --config build/webpack.demo.js</code> 基于 production 模式，打包生成内容输出至examples/element-ui/目录下。
最后将项目域名<code>element.eleme.io</code>写入<code> examples/element-ui/CNAME</code> 文件中 。</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ed698989f828457eab000cb36a227200~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-17">npm run dist</h2>
<ul>
<li>执行命令<code>npm run clean</code>,清除打包/测试生成的目录及文件;</li>
<li>执行命令<code>npm run build:file</code>,详见上文;</li>
<li>执行命令<code>npm run lint</code>,详见上文;</li>
<li>执行打包<code>webpack --config build/webpack.conf.js</code>,入口文件 <code>src/index.js</code> 以 <code>umd</code> 格式输出到 <code>lib/index.js</code>;</li>
<li>执行打包<code>webpack --config build/webpack.common.js</code>,入口文件 <code>src/index.js</code> 以<code>commonjs2</code>格式输出到 <code>lib/element-ui.common.js</code>;</li>
<li>执行打包<code>webpack --config build/webpack.component.js</code>,入口文件 <code>components.json</code>,将<code>packages</code>目录下的组件，以<code>commonjs2</code>格式分别输出到<code>lib</code>目录,用于按需引入;</li>
<li>执行命令<code>npm run build:utils</code> ,详见上文;</li>
<li>执行命令<code>npm run build:umd</code> ,详见上文;</li>
<li>执行命令<code>npm run build:theme</code>,详见上文。</li>
</ul>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/c566919392d249c8962e6b50d17e4610~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-18">npm run pub</h2>
<ul>
<li>执行命令npm run bootstrap,安装依赖环境;</li>
<li>运行shell脚本sh build/git-release.sh ，检查代码 dev 分支是否存在冲突(No conflicts);</li>
<li>运行shell脚本sh build/release.sh,合并dev分支到master分支、更新版本号、发布主题、push代码到远程仓库、发布组件库至NPM;</li>
<li>执行文件node build/bin/gen-indices.js,提供 algoliasearch 搜索功能，需要把 examples/docs 目录下 .md 文件内容格式化后上传 algolia。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/ad36334759274774a818281195ca2dc2~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-19">0x04 关注专栏</h1>
<p>此文章已收录到专栏中 👇，可以直接关注。</p></div>  
</div>
            