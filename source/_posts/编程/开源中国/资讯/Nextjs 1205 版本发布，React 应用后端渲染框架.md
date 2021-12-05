
---
title: 'Next.js 12.0.5 版本发布，React 应用后端渲染框架'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9659'
author: 开源中国
comments: false
date: Sun, 05 Dec 2021 08:00:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9659'
---

<div>   
<div class="content">
                                                                    
                                                        <div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0">
  Next.js v12.0.5 发布了！Next.js 是一个用于在服务端渲染 React 应用程序的简单框架，此升级完全向后兼容，建议所有版本低于 12.0.5 的用户使用，此补丁到 Next.js 11 的后向移植版本为 11.1.3。此版本带来以下变化：
 </div> 
</div> 
<div style="margin-left:0; margin-right:0; text-align:start"> 
 <div style="margin-left:0; margin-right:0"> 
  <h2 style="margin-left:0px; margin-right:0px">核心变化</h2> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>添加 swc 转换以移除<code>console.*</code>呼叫：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31449" target="_blank">#31449</a></li> 
   <li>支持 ESLint v8：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F29865" target="_blank">#29865</a></li> 
   <li>修复：允许<code>next lint</code>不通过<code>eslint-config-next</code>安装：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F29823" target="_blank">#29823</a></li> 
   <li>删除 TextEncoder 和 TextDecoder 包装器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31490" target="_blank">#31490</a></li> 
   <li>简化输出消息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31454" target="_blank">#31454</a></li> 
   <li>更新 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31455" target="_blank">#31455</a></li> 
   <li>NextResponse: 添加<span> </span><code>.json</code><span> </span>静态方法：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31483" target="_blank">#31483</a></li> 
   <li>在流中使用  _error 进行开发：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31466" target="_blank">#31466</a></li> 
   <li>重构中间件 SSR 加载器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31508" target="_blank">#31508</a></li> 
   <li>为<span> </span><code>Google-PageRenderer</code><span> </span>机器人添加检测：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31521" target="_blank">#31521</a></li> 
   <li>开发覆盖的点击打开错误状态<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fissues%2F14461" target="_blank">#14461</a><span> </span>:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F21819" target="_blank">#21819</a></li> 
   <li>确保只呈现一种文档类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31534" target="_blank">#31534</a></li> 
   <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31540" target="_blank">#31540</a></li> 
   <li>添加<span> </span><code>/wasm</code><span> </span>构建：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31470" target="_blank">#31470</a></li> 
   <li>遥测：跟踪 'optimizeFonts' 的使用：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31522" target="_blank">#31522</a></li> 
   <li>使缺失 的<code>Document</code><span> </span>组件成为错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31505" target="_blank">#31505</a></li> 
   <li>调整 AVIF 大小，使其小于 WebP 大小：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31494" target="_blank">#31494</a></li> 
   <li>修复开发中路由更改的未处理拒绝：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31554" target="_blank">#31554</a></li> 
   <li>重新添加本机包文件夹并确保下载 wasm 工件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31561" target="_blank">#31561</a></li> 
   <li>修复中间件的 HMR<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fissues%2F30791" target="_blank">#30791</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31548" target="_blank">#31548</a></li> 
   <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31553" target="_blank">小幅</a>简化<code>renderToWebStream</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31553" target="_blank">#31553</a></li> 
   <li>在准备好 HMR ping 之前修复访问路由器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31588" target="_blank">#31588</a></li> 
   <li>实现 next-page-disallow-re-export-all-exports 的 SWC 端口：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31582" target="_blank">#31582</a></li> 
   <li>[ESLint] 防止<code>no-html-link-for-pages</code>对静态文件发出警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31495" target="_blank">#31495</a></li> 
   <li>将根 div 移动到应用程序包装器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31596" target="_blank">#31596</a></li> 
   <li>添加 geo lat 和 long 类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31624" target="_blank">#31624</a></li> 
   <li>修复非并发函数_document：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31628" target="_blank">#31628</a></li> 
   <li>删除关于不推荐使用的字符串子项的过时评论<code>next/link</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30606" target="_blank">#30606</a></li> 
   <li>修复（中间件）：考虑本地主机的变化：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31603" target="_blank">#31603</a></li> 
   <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31639" target="_blank">#31639</a></li> 
   <li>将 next-swc Rust 代码提取到自己的包中：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31635" target="_blank">#31635</a></li> 
   <li>在路由器初始化之前修复开发路由器的使用：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31632" target="_blank">#31632</a></li> 
   <li>避免改变 response.cookie 选项：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31679" target="_blank">#31679</a></li> 
   <li>为 RSC 中使用的请求添加 cookie 和标头：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31623" target="_blank">#31623</a></li> 
   <li>删除 trace_target env var 以支持 .next/trace：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31697" target="_blank">#31697</a></li> 
   <li>发生水化错误时添加错误链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31519" target="_blank">#31519</a></li> 
   <li>修复初始编译时间错误测量：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31733" target="_blank">#31733</a></li> 
   <li>延迟初始化 getStaticPathsWorker：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31760" target="_blank">#31760</a></li> 
   <li>删除 noop 导入：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31722" target="_blank">#31722</a></li> 
   <li>更新 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31759" target="_blank">#31759</a></li> 
   <li>修复 wasm 加载：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31772" target="_blank">#31772</a></li> 
   <li>删除一些观察者黑客并更新版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31768" target="_blank">#31768</a></li> 
   <li>改进和重构某些类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31704" target="_blank">#31704</a></li> 
   <li>当没有加载器跟随 next-swc-loader 时，在 swc 中读取文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31682" target="_blank">#31682</a></li> 
   <li>延迟加载 postcss：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31762" target="_blank">#31762</a></li> 
   <li>更新 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31798" target="_blank">#31798</a></li> 
   <li>确保保留中间件顺序：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31801" target="_blank">#31801</a></li> 
   <li>重构沙箱模块缓存：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31822" target="_blank">#31822</a></li> 
   <li>修复水化中间件效果：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31800" target="_blank">#31800</a></li> 
   <li>修复：支持 no-page-custom-font 中 _document 中的函数组件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31560" target="_blank">#31560</a></li> 
   <li>添加对移除 React 属性的支持。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31606" target="_blank">#31606</a></li> 
   <li>在导出的类型定义中包含子模块：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F28316" target="_blank">#28316</a></li> 
   <li>将 require.resolve 移入模块范围：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31799" target="_blank">#31799</a></li> 
   <li>修复放大器验证器消息格式：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31018" target="_blank">#31018</a></li> 
   <li>修复边缘 SSR 中的自动导出条件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31845" target="_blank">#31845</a></li> 
   <li>错误修复：输入 href 时未定义 href 值：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31813" target="_blank">#31813</a></li> 
   <li>如果找到本地，则不加载外部绑定：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31853" target="_blank">#31853</a></li> 
   <li>修复：rsc 标头：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31854" target="_blank">#31854</a></li> 
   <li>向 Next Server 添加端口和主机名选项：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31858" target="_blank">#31858</a></li> 
   <li>修复：无法分配给只读属性 'children'：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31784" target="_blank">#31784</a></li> 
   <li>如果有自定义加载器，则修复禁用内置 CSS 支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31078" target="_blank">#31078</a></li> 
   <li>在插件索引中包含 no-document-import-in-page 规则：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31890" target="_blank">#31890</a></li> 
   <li>napi-rs 不支持的平台/架构帐户：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31938" target="_blank">#31938</a></li> 
   <li>在 prod 中删除 prop 可写检查：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31929" target="_blank">#31929</a></li> 
   <li>启用 concurrentFeatures 时启用默认功能文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31954" target="_blank">#31954</a></li> 
   <li>停止使用环境变量<code>pages/_document</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31946" target="_blank">#31946</a></li> 
   <li>使用 react 18 beta 修复图像相关链接道具警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31895" target="_blank">#31895</a></li> 
   <li>转换为正则表达式时的转义字符串：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31791" target="_blank">#31791</a></li> 
   <li>为 NextMiddleware 添加 TS 类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30578" target="_blank">#30578</a></li> 
   <li>修复（类型）：为 NextRequest 添加缺少的 ua 类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31901" target="_blank">#31901</a></li> 
   <li>确保外部模块没有捆绑到 RSC 的客户端中：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31968" target="_blank">#31968</a></li> 
   <li>解析航班请求的流数据：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32010" target="_blank">#32010</a></li> 
   <li>允许预发布 React 18 作为对等：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31991" target="_blank">#31991</a></li> 
   <li>fix(Link): 不要忽略 onMouseEnter 属性与绝对 href:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32012" target="_blank">#32012</a></li> 
   <li>添加experimental.swcFileReading 标志以禁用swc 中的文件读取：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31995" target="_blank">#31995</a></li> 
   <li>使用 skipLibCheck 修复中间件类型：false：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32025" target="_blank">#32025</a></li> 
   <li>包含导出错误页面以便于调试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32013" target="_blank">#32013</a></li> 
   <li>避免将 webpack 配置保留太久：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32053" target="_blank">#32053</a></li> 
   <li>跳过图像未呈现到 dom 的警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32049" target="_blank">#32049</a></li> 
   <li>改进导出的根定义：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32077" target="_blank">#32077</a></li> 
   <li>使用 Polyfill fetch 修复正在运行的服务器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31935" target="_blank">#31935</a></li> 
   <li>确保无效的 URL 正确响应 400：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32092" target="_blank">#32092</a></li> 
   <li>删除<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32098" target="_blank">future.strictPostcssConfiguration</a>配置：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32098" target="_blank">#32098</a></li> 
   <li>恢复“使用 Polyfill fetch 修复正在运行的服务器（<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31935" target="_blank">#31935</a>）”：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32100" target="_blank">#32100</a></li> 
  </ul> 
  <h3 style="margin-left:.6em; margin-right:0"><strong>文档更改</strong></h3> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>更新<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31476" target="_blank">react-18.md：#31476</a></li> 
   <li>为 Rust 编译器（SWC）添加文档。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31467" target="_blank">#31467</a></li> 
   <li>脚本示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31181" target="_blank">#31181</a></li> 
   <li>修复 API 路由响应的类型声明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31486" target="_blank">#31486</a></li> 
   <li>更新环境<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31525" target="_blank">变量.md</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31525" target="_blank">#31525</a></li> 
   <li>向自定义页面扩展添加中间件示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31545" target="_blank">#31545</a></li> 
   <li>添加了使用 MDX 设置 Next.js 的指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30869" target="_blank">#30869</a></li> 
   <li>修复 MDX 指南中的错字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31709" target="_blank">#31709</a></li> 
   <li>添加了关于 env vars 的注释：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31237" target="_blank">#31237</a></li> 
   <li>docs(next-config): 延长相线参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31711" target="_blank">#31711</a></li> 
   <li>[文档][修复]<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31820" target="_blank">断开的</a>API 链接参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31820" target="_blank">#31820</a></li> 
   <li>文档（路由器）：为 url 参数添加类型：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31737" target="_blank">#31737</a></li> 
   <li>SWC：向 next-dynamic 添加错误检查和测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31683" target="_blank">#31683</a></li> 
   <li>文档（React 18）：添加缺少的<code>Suspense</code>导入：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31897" target="_blank">#31897</a></li> 
   <li>文档（React 18）：删除不必要的<code>React</code>导入：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31900" target="_blank">#31900</a></li> 
   <li>改进：中间件设置 Cookie API 参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31707" target="_blank">#31707</a></li> 
   <li>更新<code>next export</code>文档。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31465" target="_blank">#31465</a></li> 
   <li>更新 Jest 示例和文档：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31633" target="_blank">#31633</a></li> 
   <li>向文档添加<code>sharp</code>有关默认 Linux 设置中内存使用情况的注释：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31919" target="_blank">#31919</a></li> 
   <li>文档（测试）：删除重复链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32071" target="_blank">#32071</a></li> 
  </ul> 
  <h3 style="margin-left:.6em; margin-right:0"><strong>示例更改</strong></h3> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>用 public 替换旧的静态路径 | 错别字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31573" target="_blank">#31573</a></li> 
   <li>更新 cms-cosmic 示例的 README：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31701" target="_blank">#31701</a></li> 
   <li>cms-cosmic 示例中的“imgix.cosmicjs.com”图像域：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31703" target="_blank">#31703</a></li> 
   <li>修复 pwa 演示：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31734" target="_blank">#31734</a></li> 
   <li>文档（示例）：向 with-iron-session 添加安全标志说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31896" target="_blank">#31896</a></li> 
   <li>[WIP] 添加跟踪到<span> </span><code>with-sentry</code><span> </span>示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30401" target="_blank">#30401</a></li> 
   <li>通过删除不推荐使用的函数来修复 with-mongo 示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30675" target="_blank">#30675</a></li> 
   <li>alert.js 中的语法错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32062" target="_blank">#32062</a></li> 
  </ul> 
  <h3 style="margin-left:.6em; margin-right:0"><strong>其他更改</strong></h3> 
  <ul style="margin-left:0; margin-right:0"> 
   <li>恢复“为 Rust 编译器（SWC）添加文档。”：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31484" target="_blank">#31484</a></li> 
   <li>确保在发布之前编写了 wasm package.json：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31568" target="_blank">#31568</a></li> 
   <li>更新 labeler.json</li> 
   <li>更新 labeler.json</li> 
   <li>更新发送到 jaeger 的 URL 输出：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31563" target="_blank">#31563</a></li> 
   <li>修复有关测试的文档中的错字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31653" target="_blank">#31653</a></li> 
   <li>为用 Rust 编写的 Next.js 编译器添加文档（利用 SWC）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31485" target="_blank">#31485</a></li> 
   <li>修复更漂亮的<span> </span><span style="color:#24292f">linting</span></li> 
   <li>修复发布部分的标签</li> 
   <li>修复 musl 构建</li> 
   <li>为 swc_bundler 启用 require：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31663" target="_blank">#31663</a></li> 
   <li>添加测试用例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31691" target="_blank">#31691</a></li> 
   <li>更新swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31816" target="_blank">#31816</a></li> 
   <li>文档（中间件）：文件扩展名一致性：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31879" target="_blank">#31879</a></li> 
   <li>删除<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31898" target="_blank">无用的</a>测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31898" target="_blank">#31898</a></li> 
   <li>删除不必要的工作流程步骤：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31943" target="_blank">#31943</a></li> 
   <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31963" target="_blank">#31963</a></li> 
   <li>文档（NextRequest）：req.cookie => req.cookies：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F31975" target="_blank">#31975</a></li> 
   <li>将 next-swc 添加到贴标机</li> 
   <li>将 Rich、Maedah 和 Ismael 添加到文档标签</li> 
   <li>更新标签生成配置中的 Maedahs 名称：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32005" target="_blank">#32005</a></li> 
   <li>修复为本地隔离测试复制 swc 二进制文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32026" target="_blank">#32026</a></li> 
   <li>CI 的锁定节点版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32057" target="_blank">#32057</a></li> 
   <li>使 CI 构建缓存键更具体：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32059" target="_blank">#32059</a></li> 
   <li>从 Next.js 存储库脚本中删除“yarn jest”：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32042" target="_blank">#32042</a></li> 
   <li>修复 testall npm 脚本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F32081" target="_blank">#32081</a></li> 
  </ul> 
  <p style="margin-left:0; margin-right:0">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Freleases%2Ftag%2Fv12.0.5" target="_blank">https://github.com/vercel/next.js/releases/tag/v12.0.5</a></p> 
 </div> 
</div>
                                        </div>
                                      
</div>
            