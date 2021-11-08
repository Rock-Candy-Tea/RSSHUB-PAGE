
---
title: 'Next.js 12.0.3 已发布，服务端渲染 React 应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=2184'
author: 开源中国
comments: false
date: Mon, 08 Nov 2021 07:32:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=2184'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start">Next.js 是一个用于在服务端渲染 React 应用程序的简单框架。目前，Next.js 发布了 12.0.2 版本，更新内容如下：</p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>核心变化</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>改进了在边缘运行时导入本机 Node API 的错误消息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30696" target="_blank">#30696</a></li> 
 <li>失败后继续尝试加载二进制文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30755" target="_blank">#30755</a></li> 
 <li>修复标题 ["Content-Disposition"] 中的无效字符：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30287" target="_blank">#30287</a></li> 
 <li>放宽对<span> </span><code>images.path</code><span> </span>next.config.js 的限制：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30741" target="_blank">#30741</a></li> 
 <li><span style="color:#2e3033">禁止在SSG +预览模式下存储页面道具缓存</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30757" target="_blank">#30757</a></li> 
 <li>优化 Google 提供的其他字体：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30554" target="_blank">#30554</a></li> 
 <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30790" target="_blank">#30790</a></li> 
 <li>添加再生器路径：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30786" target="_blank">#30786</a></li> 
 <li>更新 loader-utils：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30743" target="_blank">#30743</a></li> 
 <li>重新启用缩小中间件块：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30823" target="_blank">#30823</a></li> 
 <li>不要求源文件在开发模式下可写：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30758" target="_blank">#30758</a></li> 
 <li>修复不正确的<code>_document.js</code>错误<code>disableStaticImages: true</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30768" target="_blank">#30768</a></li> 
 <li>改进导入不受支持的本机模块的错误消息：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30829" target="_blank">#30829</a></li> 
 <li>更新 mini-css-plugin 并删除<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30617" target="_blank">ExperimentalUseImportModule</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30617" target="_blank">#30617</a></li> 
 <li>确保在跟踪中不会忽略开发反应包：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30849" target="_blank">#30849</a></li> 
 <li>修复未正确跟踪客户端组件导入的问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30853" target="_blank">#30853</a></li> 
 <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30859" target="_blank">#30859</a></li> 
 <li>在全局之前修复丢失的组合器：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30771" target="_blank">#30771</a></li> 
 <li>添加 Next.js 版本以进行跟踪：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30881" target="_blank">#30881</a></li> 
 <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30890" target="_blank">#30890</a></li> 
 <li>边缘函数：暴露<code>globalThis</code>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30877" target="_blank">#30877</a></li> 
 <li>移动浏览器列表加载 webpack-config.ts：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30889" target="_blank">#30889</a></li> 
 <li>将 linux-x64-musl 添加到 napi 数组：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30909" target="_blank">#30909</a></li> 
 <li>重新启用 linux-musl-x64 构建目标：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30910" target="_blank">#</a><span> </span>30910</li> 
 <li>修复 musll 错字：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30912" target="_blank">#30912</a></li> 
 <li>添加对构建活动指示器位置的配置支持：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30109" target="_blank">#30109</a></li> 
 <li>更新以使用 repo 特定的 napi 而不是<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30914" target="_blank">npx</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30914" target="_blank">#30914</a></li> 
 <li>修复<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fissues%2F30604" target="_blank">#30604</a><span> </span>- 无法读取 null 的属性（读取“tagName”）：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30919" target="_blank">#30919</a></li> 
 <li>更新以使用项目目录进行文件跟踪基础：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30857" target="_blank">#30857</a></li> 
 <li>修复不应动态化的样式：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30928" target="_blank">#30928</a></li> 
 <li><code>assetPrefix</code>初始化 HMR 连接时的帐户：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30632" target="_blank">#30632</a></li> 
 <li>升级 webpack 源：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30944" target="_blank">#30944</a></li> 
 <li><code>next-swc</code>: 添加<code>.bundle()</code>:<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30935" target="_blank">#30935</a></li> 
 <li>修复预设名称以提高性能：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30954" target="_blank">#30954</a></li> 
 <li>为中间件 SSR 加载程序使用绝对文档和应用程序路径：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30963" target="_blank">#30963</a></li> 
 <li>修复跟踪版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30982" target="_blank">#30982</a></li> 
 <li>node_modules 跟踪传递的更新解析：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30985" target="_blank">#30985</a></li> 
 <li>修复 server-web 构建的代码拆分和构建目标：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30972" target="_blank">#30972</a></li> 
 <li>将 Buffer 直接传递给 Rust：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30975" target="_blank">#30975</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>文档更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加有关 HMR WebSocket 的注释，以升级指南：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30704" target="_blank">#30704</a></li> 
 <li>向 URL 导入文档添加安全说明。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30708" target="_blank">#30708</a></li> 
 <li>为文档添加默认语言环境前缀的解决方法。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30673" target="_blank">#30673</a></li> 
 <li>修复拼写错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30737" target="_blank">#30737</a></li> 
 <li>文档：更新 react 18 配置：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30726" target="_blank">#30726</a></li> 
 <li>建议对 Docker 入口点使用 next CLI 而不是 yarn：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F29024" target="_blank">#29024</a></li> 
 <li>添加关于重写查询更新的注释：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30747" target="_blank">#30747</a></li> 
 <li>更新response-helpers.md：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30816" target="_blank">＃30816</a></li> 
 <li>添加关于带有 express 的 HMR WebSocket 升级的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30905" target="_blank">注释</a>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30905" target="_blank">#30905</a></li> 
 <li>添加结束标签：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30983" target="_blank">#30983</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>示例更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复指向 Elasticsearch 产品页面的链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30752" target="_blank">#30752</a></li> 
 <li>更新 with-supertokens 示例的依赖项：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30162" target="_blank">#30162</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>其他更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>修复更多缺失的 doc only 检查：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30748" target="_blank">#30748</a></li> 
 <li>删除<span> </span><code>id: binary-cache</code><span> </span>的<span> </span><code>binary-cache</code><span> </span>检车：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30658" target="_blank">#30658</a></li> 
 <li>将 Node.js 17 添加到 CI：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30760" target="_blank">#30760</a></li> 
 <li>将节点通知程序版本升级到 8.0.1：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30777" target="_blank">#30777</a></li> 
 <li>添加 postinstall 脚本以安装本机软件包：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30850" target="_blank">#30850</a></li> 
 <li>确保 install-native 使用正确的 tmpdir ：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30855" target="_blank">#30855</a></li> 
 <li>更新 lock time 和消息。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30902" target="_blank">#30902</a></li> 
 <li>在 CI 中跳过 next-swc canary postinstall：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30916" target="_blank">#30916</a></li> 
 <li>更新代码所有者以更具体：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30908" target="_blank">#30908</a></li> 
 <li>将 lock time 从 90 减少到45。：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30922" target="_blank">#30922</a></li> 
 <li>继续使用 checkout 而不是缓存来构建 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30923" target="_blank">#30923</a></li> 
 <li>修复 flakey 预加载测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30969" target="_blank">#30969</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30790" target="_blank">https://github.com/vercel/next.js/pull/30790</a></p>
                                        </div>
                                      
</div>
            