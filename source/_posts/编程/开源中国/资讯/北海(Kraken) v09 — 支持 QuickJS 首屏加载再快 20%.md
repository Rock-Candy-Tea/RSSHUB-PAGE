
---
title: '北海(Kraken) v0.9 — 支持 QuickJS 首屏加载再快 20%'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://oscimg.oschina.net/oscnet/up-f1c32804da7bbbc367c1d1b4a758f0b6778.gif'
author: 开源中国
comments: false
date: Thu, 04 Nov 2021 08:52:00 GMT
thumbnail: 'https://oscimg.oschina.net/oscnet/up-f1c32804da7bbbc367c1d1b4a758f0b6778.gif'
---

<div>   
<div class="content">
                                                                                            <p>渲染引擎北海 (Kraken) 发布 v0.9 版本，首屏性能又有新的突破。</p> 
<p>继 v0.8 升级到 Flutter 2.0 + Null Safety 之后，在这个版本我们重点对首屏的加载性能、布局的正确性和性能以及前端社区生态做了重点优化，详细的更新日志可见 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fkraken%2FCHANGELOG.md" target="_blank">CHANGELOG</a>。</p> 
<p>接下来我会重点介绍在 v0.9 加入的几大新特性。</p> 
<h2>支持 QuickJS 作为 JavaScript Engine</h2> 
<p>QuickJS 是一个轻量级的 JavaScript 引擎，与 JavaScriptCore 相比它具有以下几个优点：</p> 
<ul> 
 <li>轻量，它的实现仅仅由几个 C 文件，没有外部依赖，一个 x86 下的简单的 “hello world” 程序只要约 180 KiB。</li> 
 <li>具有极低启动时间的快速解释器，配合将 JS 源码预编译为 bytecode 格式，忽略解析耗时后对应用启动性能有很大提升。</li> 
 <li>几乎完整的 ECMA 标准支持，最新版本原生支持 ES2020，不再需要 babel 编译为 ES5，不仅 JSBundle 体积可以下降，也能提升执行的性能。</li> 
 <li>更好的多平台支持，即使完整编译也不需要耗费太多工夫。</li> 
</ul> 
<p>Kraken v0.9 将原先的 Bridge 层的 JavaScript Engine 默认实现迁移为 QuickJS，配合 bytecode 预编译可以将应用启动性能得到提升。而且这些改动对前端开发者是完全无感的。</p> 
<p>我们也对 Kraken 新版本和上一个版本进行了 Benchmark 性能测试：</p> 
<blockquote> 
 <p>测试设备： MI 6 (Android arm64) 测试页面：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkraken.oss-cn-hangzhou.aliyuncs.com%2Fdata%2Fcvd3r6f068.js" target="_blank">https://kraken.oss-cn-hangzhou.aliyuncs.com/data/cvd3r6f068.js</a> 测试方法：使用 0.8.4（JavaScriptCore） 和 0.9.0-rc（QuickJS） 版本各冷启动一次页面，对比加载耗时。 详细日志：</p> 
 <ul> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fpull%2F446%2Fchecks%3Fcheck_run_id%3D3926123626" target="_blank">0.9.0-rc</a></li> 
  <li><a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fruns%2F3893542997%3Fcheck_suite_focus%3Dtrue" target="_blank">0.8.4</a></li> 
 </ul> 
</blockquote> 
<p>分析日志中与 JavaScript 相关的关键性能指标：</p> 
<ol> 
 <li>js_context_init_cost：JS Engine 初始化耗时</li> 
 <li>polyfill_init_cost：Kraken JS polyfill 初始化耗时</li> 
 <li>js_bundle_eval_cost：JS Bundle 执行耗时</li> 
 <li>js_parse_time_cost：JS Bundle 解析耗时</li> 
</ol> 
<table> 
 <thead> 
  <tr> 
   <th>Version</th> 
   <th>js_context_init_cost</th> 
   <th>polyfill_init_cost</th> 
   <th>js_bundle_eval_cost</th> 
   <th>js_parse_time_cost</th> 
   <th> </th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>0.8.4</td> 
   <td>17.30ms</td> 
   <td>20.39ms</td> 
   <td>229.53ms</td> 
   <td>31.25ms</td> 
   <td> </td> 
  </tr> 
  <tr> 
   <td>0.9.0-rc</td> 
   <td>0.55ms</td> 
   <td>2.06ms</td> 
   <td>122.61ms</td> 
   <td>122.91ms</td> 
   <td> </td> 
  </tr> 
 </tbody> 
</table> 
<p>QuickJS 支持 bytecode 加载，故 <code>js_parse_time_cost</code> 在使用 bytecode 格式的时候可几乎忽略不计。</p> 
<p>得到有关 JS 的总加载耗时：</p> 
<ul> 
 <li>JavaScriptCore: 17.3 + 20.39 + 229.53 + 31.25 = 298.47ms</li> 
 <li>QuickJS: 0.55 + 2.06 + 122.61 = 125ms</li> 
</ul> 
<p><strong>真机录屏验证</strong></p> 
<p>以上属于代码级别的 Benchmark 数据，实际用户体感效果如何呢，我们在真机上进行了录屏测试：</p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-f1c32804da7bbbc367c1d1b4a758f0b6778.gif" referrerpolicy="no-referrer"></p> 
<p>指标定义：</p> 
<ul> 
 <li>白屏阶段：从用户点击 App 启动到页面首帧出现的时间</li> 
 <li>渲染阶段：从页面首帧出现到目标页所有内容(含图片)渲染稳定完成的时间</li> 
</ul> 
<p>通过逐帧分析，多组取平均值得到以下数据：</p> 
<blockquote> 
 <p>受限于视频播放器进度条的精度，测试数据精度为 0.05s。</p> 
</blockquote> 
<table> 
 <thead> 
  <tr> 
   <th>测试分组</th> 
   <th>白屏阶段 (均值)</th> 
   <th>渲染阶段 (均值)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>0.8.4</td> 
   <td>0.95s</td> 
   <td>0.80s</td> 
  </tr> 
  <tr> 
   <td>0.9.0-rc</td> 
   <td>0.95s</td> 
   <td>0.60s</td> 
  </tr> 
  <tr> 
   <td>0.9.0-rc + bytecode</td> 
   <td>0.76s</td> 
   <td>0.66s</td> 
  </tr> 
 </tbody> 
</table> 
<p>可得结论，在上述条件下，Kraken v0.9 + bytecode 模式相比 v0.8 版本在首屏性能上可再提升 18.86%。值得注意的是，真机测试使用的是一台 Android 中端设备，JS Engine 解析耗时的影响在低端设备上影响更大，故有理由相信 QuickJS 带来的优化在低端设备上可以获得更多的收益，具体数据我们也将进一步测试更新。</p> 
<h2>支持 HTML 文件的解析和渲染</h2> 
<p>对浏览器来说，SSR 直出渲染的性能要比异步 JS 渲染的 CSR 要好上不少，对于 Kraken 也是如此。这次我们给 Kraken 带来了 HTML 文件解析渲染的支持，直接解析 HTML 并渲染视图，无需等待 JS 的初始化与执行。</p> 
<p>使用上与 JSBundle 并无任何不同，只需要将 HTML 文件的 URL 传入 bundleURL 即可：</p> 
<pre><code class="language-dart">void main() &#123;
  runApp(Kraken(
    bundleURL: 'https://domain.com/url/to/html',
  ));
&#125;
</code></pre> 
<p>Kraken 会根据 HTTP <code>Content-Type</code> 协商使用 HTML 解析或者是 JavaScript 引擎启动。</p> 
<p>性能测试：</p> 
<blockquote> 
 <p>测试设备： MI 11 Lite (Android arm64) 测试页面：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fkraken.oss-cn-hangzhou.aliyuncs.com%2Fdata%2F" target="_blank">https://kraken.oss-cn-hangzhou.aliyuncs.com/data/</a>....js 测试方法：使用 0.9.0-rc 分别用 JSBundle / Bytecode / HTML 格式各冷启动一次页面，对比加载耗时。</p> 
</blockquote> 
<table> 
 <thead> 
  <tr> 
   <th>测试分组</th> 
   <th>Total time cost (平均)</th> 
  </tr> 
 </thead> 
 <tbody> 
  <tr> 
   <td>JS Bundle</td> 
   <td>865ms</td> 
  </tr> 
  <tr> 
   <td>Bytecode</td> 
   <td>662ms</td> 
  </tr> 
  <tr> 
   <td>HTML</td> 
   <td>255ms</td> 
  </tr> 
 </tbody> 
</table> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-9edd80f368dce53d0532b5d609149d46315.gif" referrerpolicy="no-referrer"></p> 
<h2>支持 HTTP 协议的缓存特性</h2> 
<p>众所周知，编程的终极问题有两个，其一是给变量命名，另一个就是缓存的使用。</p> 
<p>在浏览器中默认支持 HTTP 缓存，包含强缓存、协商缓存，它是由多个 HTTP Headers 组合形成的一种描述缓存的规范。而在客户端生态或者 Flutter 的基础能力中，都是不包含 HTTP 缓存功能的。Kraken v0.9 开始默认支持了 HTTP 缓存功能，无论是 XHR/fetch 或者是通过 img 标签加载的图片，script 标签加载的 JS 文件等，只要是从 Kraken 内部发出的 HTTP(s) 请求，都能够享受到缓存带来的收益，目前支持的特性包括：</p> 
<ul> 
 <li>无需二次请求的强缓存 
  <ul> 
   <li>Expires</li> 
   <li>Cache-Control (max-age/no-store/no-cache)</li> 
  </ul> </li> 
 <li>需要二次请求的协商缓存 (根据 HTTP 状态码 304 协商) 
  <ul> 
   <li>Last-Modified / If-Modified-Since</li> 
   <li>Etag / If-None-Match</li> 
  </ul> </li> 
</ul> 
<p>本功能对于电商商品 Feeds 流等页面中包含大量图片的场景，带来的优化收益更明显，由于图片几乎全是强缓存类型的资源，在缓存命中的情况下无需再次请求网络，且缓存是落磁盘的固化式缓存，对于二次冷启应用也能享受到优化。</p> 
<h2>支持 Vue/React 官方工具链</h2> 
<p>前端开发者是 Kraken 面向的用户，在开源之后我们也持续收到了许多社区开发者的反馈。</p> 
<p>对于现代前端开发来说，框架是必不可少的，除了淘系广泛使用的 Rax，最近我们也对 Vue 和 React 的官方工具链、生态库进行了支持，现在使用 v0.9 开发 Vue/React App 会更加顺畅。</p> 
<p><img src="https://gw.alicdn.com/imgextra/i3/O1CN01edtT9l1Pq7g1nk5YI_!!6000000001891-2-tps-1920-1080.png" referrerpolicy="no-referrer"></p> 
<p>具体可参考官方示例工程：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fsamples" target="_blank">https://github.com/openkraken/samples</a></p> 
<h2>支持模块热更新 (Hot Module Replacement)</h2> 
<p>模块热更新是 Webpack 的常用功能，通过它可以在修改代码后直接替换、添加或者删除节点，而无需重新加载整个页面。<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fwebpack.js.org%2Fconcepts%2Fhot-module-replacement%2F" target="_blank">Webpack 官方说明文档</a></p> 
<p><img alt src="https://oscimg.oschina.net/oscnet/up-a7648cc11df1f53d330636f3ca7ce417aa5.gif" referrerpolicy="no-referrer"></p> 
<h2>支持 querySelector / querySelectorAll*</h2> 
<p>同时我们也对呼声比较大的 <code>querySelector/querySelectorAll</code> 做了支持，目前已支持的 CSS 选择器包括：</p> 
<ul> 
 <li>id ID 选择器</li> 
 <li>class 类名选择器</li> 
 <li>tag 标签选择器</li> 
 <li>attr 属性选择器，包含以下几种判断 
  <ul> 
   <li>=</li> 
   <li>^=</li> 
   <li>*=</li> 
   <li>$=</li> 
  </ul> </li> 
</ul> 
<blockquote> 
 <p>*：目前仅支持部分 CSS 选择器，详见上述说明。</p> 
</blockquote> 
<h2>关于北海 KRAKEN 更多的内容</h2> 
<h3>社区协作机制</h3> 
<p>我们期望通过一种良好的社区协作机制，来与社区的众多开发者一起共建 Kraken 底层能力及生态。</p> 
<p>Kraken 团队通过<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E5%258D%258F%25E4%25BD%259C%25E8%2580%2585" target="_blank">协作者</a>的方式来参与 Kraken 功能迭代以及 issue 讨论等工作。同时，通过由一部分协作者组成的<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2FGOVERNANCE.zh-CN.md%23%25E6%258A%2580%25E6%259C%25AF%25E5%25A7%2594%25E5%2591%2598%25E4%25BC%259A" target="_blank">技术委员会（TSC）</a>来确定技术方向、发布以及定制标准等工作。</p> 
<p>简单地说，只要向 Openkraken Group 提交一定质量和数量的代码即可成为协作者；对项目提交建设性的贡献后，TSC 成员有权提名协作者参与到 TSC 中。</p> 
<p>Kraken 团队期望通过一种友好、共同参与的协作机制，让社区的开发者能够更好地参与到对项目的演进中去，让每个人的声音都能被听到，共同促进 Kraken 以及 Web 标准 的发展。</p> 
<p>更详细的协作机制可以移步 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2FTSC%2Fblob%2Fmaster%2FGOVERNANCE.zh-CN.md" target="_blank">Github TSC</a>。</p> 
<h3>往期文章推荐</h3> 
<ul> 
 <li><a href="https://my.oschina.net/u/3161824/blog/5027369">基于 Flutter 的 Web 渲染引擎「北海」正式开源</a></li> 
 <li><a href="https://my.oschina.net/u/3161824/blog/5193553">Flutter 的 Web 渲染引擎「北海 Kraken」技术原理</a></li> 
</ul> 
<h3>联系我们</h3> 
<p>详细的 CHANGELOG 可以查阅 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken%2Fblob%2Fmain%2Fkraken%2FCHANGELOG.md" target="_blank">CHANGELOG</a>。 如若希望获取更多关于 Kraken 的信息，可以访问我们的 <a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fopenkraken%2Fkraken" target="_blank">Github</a>、<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fopenkraken.com" target="_blank">官方文档</a> 与 Kraken 项目组取得联系。</p>
                                        </div>
                                      
</div>
            