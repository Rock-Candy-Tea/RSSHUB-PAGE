
---
title: 'Next.js 12.0.4 发布，React 应用后端渲染框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=1124'
author: 开源中国
comments: false
date: Wed, 17 Nov 2021 07:12:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=1124'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#000000">Next.js 是一个用于在服务端渲染 React 应用程序的简单框架。目前，Next.js 发布了 12.0.4 版本，更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>核心变化</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>更新中间件 eval 检查：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30883" target="_blank">#30883</a></li> 
 <li>优化 SSR 中间件运行时大小：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30906" target="_blank">#30906</a></li> 
 <li>改进 SSR 中间件中的错误处理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31057" target="_blank">#31057</a></li> 
 <li>确保最小模式下的解码错误响应为 400 而不是 500：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31037" target="_blank">#31037</a></li> 
 <li>更新 ServerlessPlugin 以使用 chunkGraph：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31058" target="_blank">#31058</a></li> 
 <li>修复启用 concurrentFeatures 时的自定义 404 页面问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31059" target="_blank">#31059</a></li> 
 <li>将 React alpha 和实验依赖项升级到最新版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31039" target="_blank">#31039</a></li> 
 <li>将禁用的 SWC 消息更改为<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31091" target="_blank">Log.info：#31091</a></li> 
 <li>将渲染道具支持添加到<span> </span><code><Main></code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30156" target="_blank">#30156</a></li> 
 <li>将文档页面的 .web 扩展名更改为路径的一部分：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31116" target="_blank">#31116</a></li> 
 <li>为 Web 运行时构建启用代码拆分：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31090" target="_blank">#31090</a></li> 
 <li>宣布页面更改时，将 document.title 优先于 h1：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31147" target="_blank">#31147</a></li> 
 <li>添加 webpack5 命名空间以修复类型错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31140" target="_blank">#31140</a></li> 
 <li>当图像有未使用的<code>sizes</code><span> </span>要素时添加警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31064" target="_blank">#31064</a></li> 
 <li>添加实验性的 next-swc jest 变换：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30993" target="_blank">#30993</a></li> 
 <li>修复：支持 --cache-strategy ESLint 参数（修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fissues%2F29926" target="_blank">#29926</a>）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F29928" target="_blank">#29928</a></li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fissues%2F31060" target="_blank">#31060</a>：NullReferenceException：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31061" target="_blank">#31061</a></li> 
 <li>为 resolve-url-loader 使用 loader-utils 2 ，以修复 sass 中的<code>./data:</code><span> </span>url：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31134" target="_blank">#31134</a></li> 
 <li>更新<span> </span><span style="color:#24292f">isolatedModules</span><span> </span>和 esModuleInterop 的原因消息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31150" target="_blank">#31150</a></li> 
 <li>为 30091 添加输入/输出测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31166" target="_blank">#31166</a></li> 
 <li>修复<code>useId</code><span> </span>在<span> </span><span style="color:#24292f">hydration<span> </span></span>不匹配的问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31102" target="_blank">#31102</a></li> 
 <li>启用 concurrentFeatures 时不再隐藏正文：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31187" target="_blank">#31187</a></li> 
 <li>修复中间件 i18n 重写：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31174" target="_blank">#31174</a></li> 
 <li>新的 SWC：添加<span> </span><code>displayNameAndId</code><span> </span>到<span> </span><code>styled-components</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31189" target="_blank">＃31189</a></li> 
 <li>使用 require.resolve 检测“框架”包（修复 pnpm）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F21048" target="_blank">#21048</a></li> 
 <li>添加所有使用 webpack5 类型的情况：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31206" target="_blank">#31206</a></li> 
 <li><span style="color:#2e3033">为禁用 SWC 转换的样式组件添加测试</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31214" target="_blank">#31214</a></li> 
 <li>添加初始的独立构建处理：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31003" target="_blank">#31003</a></li> 
 <li>修复（中间件）：公开<span> </span><code>CryptoKey</code><span> </span>和<span> </span><code>globalThis.CryptoKey</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31193" target="_blank">#31193</a></li> 
 <li>在生产中禁用样式组件 displayName：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31216" target="_blank">#31216</a></li> 
 <li>修复（31013）：将基本路径添加到预请求网址：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31101" target="_blank">#31101</a></li> 
 <li>在中间件 vm 上下文中共享集合：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31043" target="_blank">#31043</a></li> 
 <li>支持 assetPrefix 特定协议：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31213" target="_blank">#31213</a></li> 
 <li>升级 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31034" target="_blank">#31034</a></li> 
 <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31233" target="_blank">#31233</a></li> 
 <li>仅为中间件模块运行中间件解析器处理程序：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31219" target="_blank">#31219</a></li> 
 <li>更新 swc 压缩器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31242" target="_blank">#31242</a></li> 
 <li>修复 web 运行时覆盖的 process.env：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31261" target="_blank">#31261</a></li> 
 <li>修复：替换了无用的<span> </span><span style="color:#24292f">let</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31239" target="_blank">#31239</a></li> 
 <li>实验性 next/jest 配置助手：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31246" target="_blank">#31246</a></li> 
 <li>当 nonce 属性存在时，正确评估节点的相等性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F27573" target="_blank">#27573</a></li> 
 <li>bugfix/i18n 不支持路径名中的第二个语言环境：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31229" target="_blank">#31229</a></li> 
 <li>修复<span> </span><code>next build</code><span> </span>日志中的错字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31295" target="_blank">#31295</a></li> 
 <li>确保发布 next/jest：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31296" target="_blank">#31296</a></li> 
 <li>为<span> </span><code>jsc.paths</code><span> </span>更新 swc ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31290" target="_blank">#31290</a></li> 
 <li>next/jest：确保 typeof 窗口在 jsdom 环境中不被转换：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31304" target="_blank">#31304</a></li> 
 <li>保存首选项的输出：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31305" target="_blank">#31305</a></li> 
 <li>升级 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31313" target="_blank">#31313</a></li> 
 <li>使用 i18n 确保在 minimumMode 中正确标准化 asPath：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31281" target="_blank">#</a><span> </span>31281</li> 
 <li>自动使用不同的端口为非显式端口启动开发服务器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30736" target="_blank">#30736</a></li> 
 <li>在完整的 shell 上为 renderToReadableStream 解析流管道：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31186" target="_blank">#31186</a></li> 
 <li>修复（中间件）：获取资源可能是 URL 实例（或任何可字符串化的值）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31260" target="_blank">#31260</a></li> 
 <li>确保用 swc 正确替换<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31274" target="_blank">NODE_ENV</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31274" target="_blank">#31274</a></li> 
 <li>在 tsconfig/jsconfig 中添加对 jsxImportSource 的支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31358" target="_blank">#</a><span> </span>31358</li> 
 <li>修复（30724）：链接中间件时清除“x-middleware-next”标头：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30866" target="_blank">#30866</a></li> 
 <li>添加 eslint 规则以防止在 _middleware 之外导入 next/server：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30973" target="_blank">#30973</a></li> 
 <li>如果主机相同，则不要代理中间件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31180" target="_blank">#31180</a></li> 
 <li>通过 tsconfig/jsconfig 添加对遗留装饰器的支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31376" target="_blank">#31376</a></li> 
 <li>更新 swc 并修复<span> </span><code>styled-jsx</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31407" target="_blank">#31407</a></li> 
 <li>显示<code>(middleware only)</code>中间件何时添加到编译器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31409" target="_blank">#31409</a></li> 
 <li>添加 minify debug env var 以调查 minifier 错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31417" target="_blank">#31417</a></li> 
 <li>将文件名添加到关于匿名函数默认导出的 babel 警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31322" target="_blank">#31322</a></li> 
 <li>为 SSR 流重构服务器/渲染器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31231" target="_blank">#31231</a></li> 
 <li>从 craCompat 中删除 moment locale<span> </span><span style="color:#2e3033">replace</span>，因为它是 Next.js 12 中的默认值：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31431" target="_blank">#31431</a></li> 
 <li><span style="color:#2e3033">修复了当 path 为空字符串时， basePath 替换服务器端和 normalizeLocalePath() 的问题</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30978" target="_blank">#30978</a></li> 
 <li>发生致命错误时关闭流：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31164" target="_blank">#31164</a></li> 
 <li>中间件：添加请求引用支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31343" target="_blank">#31343</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>文档更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>扩展<span> </span><code>next/script</code><span> </span>文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31063" target="_blank">#31063</a></li> 
 <li>修复错别字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31161" target="_blank">#31161</a></li> 
 <li>在域路由中包含 www 子域示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30487" target="_blank">#30487</a></li> 
 <li>修复 URL 导入文档中的标题级别。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31163" target="_blank">#31163</a></li> 
 <li>更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31173" target="_blank">upgrade.md：#31173</a></li> 
 <li>文档：修复 css-in-js 页面中的错字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31244" target="_blank">#31244</a></li> 
 <li>测试文档：添加链接以跳转到部分：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31311" target="_blank">#31311</a></li> 
 <li>开发脚本（package.json）的变化：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31245" target="_blank">#31245</a></li> 
 <li>Markdown 文件上的错字修复：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31380" target="_blank">#31380</a></li> 
 <li>更新<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31394" target="_blank">data-fetching.md：#31394</a></li> 
 <li>更新<span> </span><span style="color:#24292f">image-optimization.md:</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31401" target="_blank">#31401</a></li> 
 <li>修复 API 路由文档的函数语法：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31414" target="_blank">#31414</a></li> 
 <li>文档：next-iron-session 重命名为 Iron-session：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31292" target="_blank">#31292</a></li> 
 <li>用逗号进行阐明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31224" target="_blank">#31224</a></li> 
 <li>文档（身份验证）：修复<span> </span><span style="color:#24292f">iron-session</span><span> </span>的示例 url + API：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31413" target="_blank">#31413</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>示例更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>使用超级令牌优化包大小示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31040" target="_blank">#</a><span> </span>31040</li> 
 <li>更新 remark 和 remark-html 依赖：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31051" target="_blank">#31051</a></li> 
 <li>文档/示例/带有 Iron 会话更新：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30956" target="_blank">#30956</a></li> 
 <li>修复 Auth0 示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31284" target="_blank">#31284</a></li> 
 <li>使用超级令牌更新示例以添加使用苹果登录：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31200" target="_blank">#31200</a></li> 
 <li>Auth0 示例：<code>getSession</code>应使用<code>req</code>和调用<code>res</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31330" target="_blank">#31330</a></li> 
 <li>示例：使用谷歌分析修复自述文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31384" target="_blank">#31384</a></li> 
 <li>添加剧作家示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F29426" target="_blank">#29426</a></li> 
 <li>使用 styled-jsx 5 修复故事书 styled-jsx 示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31357" target="_blank">#31357</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>其他更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进 Windows 对基准测试的支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31032" target="_blank">#31032</a></li> 
 <li>为 Suspense 和流媒体添加集成测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31197" target="_blank">#31197</a></li> 
 <li>将<span> </span><span style="color:#24292f">cancel-workflow-action</span><span> </span>升到 0.9.1：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31210" target="_blank">#31210</a></li> 
 <li>测试：跳过片状动态导入测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31221" target="_blank">#31221</a></li> 
 <li>添加<span> </span><code>concurrentFeatures</code><span> </span>启用API 路由的集成测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31227" target="_blank">#31227</a></li> 
 <li>使用 swc 的故障排除部分更新贡献文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31265" target="_blank">#31265</a></li> 
 <li>修复 CI 中的 test-pnp 停顿：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31282" target="_blank">#31282</a></li> 
 <li>修复故障排除中的 failed-loading-swc 链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31314" target="_blank">#31314</a></li> 
 <li>当 kodiak 合并时保持共同作者：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31316" target="_blank">#31316</a></li> 
 <li>错误修复/第二个语言环境中的路径名删除 console.log：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31289" target="_blank">#31289</a></li> 
 <li>用 Rust 重写 send-trace-to-jaeger：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31392" target="_blank">#31392</a></li> 
 <li>确保启用 Git feature.manyFiles：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31408" target="_blank">#31408</a></li> 
 <li>删除 .only 并确保 jest lint 规则适用于所有测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31456" target="_blank">#31456</a></li> 
 <li>确保为隔离测试复制 swc dep：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31462" target="_blank">#31462</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Freleases" target="_blank">https://github.com/vercel/next.js/releases</a></p> 
<p> </p>
                                        </div>
                                      
</div>
            