
---
title: 'Next.js 12.0.2 已发布，服务端渲染 React 应用'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=9056'
author: 开源中国
comments: false
date: Tue, 02 Nov 2021 07:02:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=9056'
---

<div>   
<div class="content">
                                                                                            <p style="color:#000000; margin-left:0; margin-right:0; text-align:start"><span style="color:#333333">Next.js 是一个用于在服务端渲染 React 应用程序的简单框架。目前，</span><span style="color:#000000">Next.js 发布了<span> </span></span>12.0.2<span style="color:#000000"> 版本，更新内容如下：</span></p> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">核心改动</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>在未设置 compilerOptions 时正确更新 tsconfig：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30355" target="_blank">#30355</a></li> 
 <li>更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30404" target="_blank">#30404</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30426" target="_blank">#30426</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30509" target="_blank">#3050​​9</a><span> </span>/<span> </span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30685" target="_blank">#30685</a></li> 
 <li>修复无效包的外部回退：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30427" target="_blank">#30427</a></li> 
 <li>删除 console.log：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30447" target="_blank">#30447</a></li> 
 <li>放宽<span> </span><code>next/image</code><span> </span>父元素的警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30453" target="_blank">#30453</a></li> 
 <li>确保 externals 是一个数组：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30466" target="_blank">#30466</a></li> 
 <li><span style="color:#2e3033">修复 native-url 包含非 es5 的用法：<span> </span></span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30474" target="_blank">#30474</a></li> 
 <li>修复占位符后面带数字的问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30493" target="_blank">#30493</a></li> 
 <li>从 dep 复制必要的 RSC 文件：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30505" target="_blank">#3050​​5</a></li> 
 <li>共享跟踪和外部的解析逻辑：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30499" target="_blank">#30499</a></li> 
 <li>更新 swc 以修复 minifier 问题：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30540" target="_blank">#30540</a></li> 
 <li>从目标中排除 musl：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30548" target="_blank">#30548</a></li> 
 <li>恢复“更新 swc 以修复缩小器问题”：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30551" target="_blank">#30551</a></li> 
 <li>修复错误弹出窗口中的文件路径溢出：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F27575" target="_blank">#27575</a></li> 
 <li>在<span> </span><span style="color:#24292f">FEATURE_USAGE</span><span> </span>后端添加<span style="color:#2e3033">更新 featureName 的警告：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30283" target="_blank">#30283</a></li> 
 <li><span style="color:#2e3033">更新 publish-native 以避免错误阻塞：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30565" target="_blank">#30565</a></li> 
 <li>简化并发功能相关配置，修复测试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30546" target="_blank">#30546</a></li> 
 <li>正确拆分 Set-Cookie 标头：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30560" target="_blank">#30560</a></li> 
 <li>放宽<span> </span><code>next/image</code><span> </span>加载器的宽度警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30562" target="_blank">#30562</a></li> 
 <li>修复<span> </span><span style="color:#2e3033">publish-native 包含非包的问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30589" target="_blank">#30589</a></li> 
 <li>修复冗余<span> </span><span style="color:#24292f">styled-jsx 全局问题。</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30584" target="_blank">#30584</a></li> 
 <li>为流添加缓冲直到 shell 完成：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30585" target="_blank">#30585</a></li> 
 <li><span style="color:#24292f">检查 18 个 react 标签，以及更多测试：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30575" target="_blank">#30575</a></li> 
 <li>更新到最新版本的<span> </span><span style="color:#24292f">shell-quote：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30621" target="_blank">#30621</a></li> 
 <li>进一步放松对<span> </span><code>next/image</code><span> </span>加载器宽度的警告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30624" target="_blank">#30624</a></li> 
 <li><span style="color:#24292f">Chore/rust 工作流：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30577" target="_blank">#30577</a></li> 
 <li>更新 webpack：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30634" target="_blank">#30634</a></li> 
 <li>更新输出跟踪，每个输出跟踪有单独的目标：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30637" target="_blank">#30637</a></li> 
 <li><span style="color:#24292f">恢复增量配置以修复丢失的类型</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30644" target="_blank">#30644</a></li> 
 <li><span style="color:#2e3033">修复检查编译的步骤：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30645" target="_blank">#30645</a></li> 
 <li><span style="color:#24292f">修复中间件 SSR 加载器缺少的 dev 选项</span>：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30639" target="_blank">#30639</a></li> 
 <li><span style="color:#2e3033">修正了 .ts 文件中 TypeScript 泛型和<span> </span></span>angle bracket<span> </span><span style="color:#2e3033">类型断言的<span> </span><code>Expected jsx identifier</code><span> </span>错误：</span><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30619" target="_blank">#30619</a></li> 
 <li>添加 auto-commonjs 并更新 swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30661" target="_blank">#30661</a>、</li> 
 <li>为并发模式提供默认回退  _document 和  _app：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30642" target="_blank">#30642</a></li> 
 <li>删除 isCommonJS 检查，因为它已移至 next-swc：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30677" target="_blank">#30677</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start">文档改动</h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>删除重复的单词：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30442" target="_blank">#30442</a></li> 
 <li>修复（文档）：修复测试文档中损坏的链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30448" target="_blank">#30448</a></li> 
 <li>SWC 更新失败时，错误链接会指向讨论组：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30469" target="_blank">#30469</a></li> 
 <li>文档：更新中间件 API 参考：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30485" target="_blank">#30485</a></li> 
 <li>更新标题文档中的示例：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30502" target="_blank">#3050​​2</a></li> 
 <li>文档跨平台 VS Code 调试：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30052" target="_blank">#30052</a></li> 
 <li>在 swc 错误文档中添加关于 no-optional 的注释：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30566" target="_blank">#30566</a></li> 
 <li>从已弃用的目标配置消息中，修复指向文档的链接：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30607" target="_blank">#30607</a></li> 
 <li>正确的 Next.js 11 升级说明：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30665" target="_blank">#30665</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>示例更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>跨示例将 next-transpile-modules 更新为 9.0.0：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30418" target="_blank">#30418</a></li> 
</ul> 
<h3 style="margin-left:.6em; margin-right:0; text-align:start"><strong>其他更改</strong></h3> 
<ul style="margin-left:0; margin-right:0"> 
 <li>添加<code>incremental</code>到 template/tsconfig.json ，避免在首次构建时发生更改：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30357" target="_blank">#30357</a></li> 
 <li>修复<span> </span><span style="color:#24292f">playwright</span><span> </span>轨迹名称：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30374" target="_blank">#30374</a></li> 
 <li>在错误消息中包含 stdio：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30358" target="_blank">#30358</a></li> 
 <li>在测试重试时禁用对 webpack 的轮询：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30372" target="_blank">#30372</a></li> 
 <li>更新测试跟踪，只在重试时运行：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30459" target="_blank">#30459</a></li> 
 <li>删除 PR 统计信息的额外配置：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30478" target="_blank">#30478</a></li> 
 <li>修复了<span> </span><span style="color:#24292f">contributing.md<span> </span></span>中的语法错误：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30542" target="_blank">#30542</a></li> 
 <li>二进制发布失败时，使用回退 SWC 版本：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30568" target="_blank">#30568</a></li> 
 <li>更新可选时，使用未过滤的 SWC 包：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30571" target="_blank">#30571</a></li> 
 <li>在测试工具中删除 node 10 的 Object.fromEntries polyfill：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30657" target="_blank">#30657</a></li> 
 <li>确保本机二进制文件可用于发布：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Fpull%2F30649" target="_blank">#30649</a></li> 
</ul> 
<p style="color:#000000; margin-left:0; margin-right:0; text-align:start">更新公告：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fvercel%2Fnext.js%2Freleases%2Ftag%2Fv12.0.2" target="_blank">https://github.com/vercel/next.js/releases/tag/v12.0.2</a></p>
                                        </div>
                                      
</div>
            