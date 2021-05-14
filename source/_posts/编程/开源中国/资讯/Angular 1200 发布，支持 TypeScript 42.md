
---
title: 'Angular 12.0.0 发布，支持 TypeScript 4.2'
categories: 
 - 编程
 - 开源中国
 - 资讯
headimg: 'https://picsum.photos/400/300?random=7185'
author: 开源中国
comments: false
date: Fri, 14 May 2021 07:15:00 GMT
thumbnail: 'https://picsum.photos/400/300?random=7185'
---

<div>   
<div class="content">
                                                                    
                                                        <p>Angular 12.0.0 正式发布，该版本更新内容如下：</p> 
<h3><strong>性能改进</strong></h3> 
<ul> 
 <li><strong>common:</strong> 删除 DomAdapter 中未使用的方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41102" target="_blank">#41102</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F3c66b100dd6f05f53740f596c5eadb999c27c9c4" target="_blank">3c66b10</a>)</li> 
 <li><strong>compiler:</strong> 减少生成的安全访问和无效合并的代码量 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41563" target="_blank">#41563</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F9a3b82f19d26819c95c340d702c1c32787f2931e" target="_blank">9a3b82f</a>)</li> 
 <li><strong>compiler-cli:</strong> 允许在存在重定向的源文件的情况下进行增量编译 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41448" target="_blank">#41448</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fffea31f433c1f71b78a2245d52d2969503db1784" target="_blank">ffea31f</a>)</li> 
 <li><strong>compiler-cli:</strong> 缓存 absoluteFromSourceFile 的结果 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41475" target="_blank">#41475</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Ffab1a6468e53ab6c59e2c3aebb3ed1ecd1a6e5e8" target="_blank">fab1a64</a>)</li> 
 <li><strong>core:</strong> 监听器指令的小改进 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41807" target="_blank">#41807</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F9346d61d92c722175ca7673efe475e838546fef7" target="_blank">9346d61</a>)</li> 
 <li><strong>core:</strong> 避免将 LView 存储在 ngContext 中 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41358" target="_blank">#41358</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F990067a0c6df8e97c5bbffec00a76f13c4d4c903" target="_blank">990067a</a>)</li> 
 <li><strong>core:</strong> 优化 getDirectives (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41525" target="_blank">#41525</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Ff7e391a912153d1ce43f9d0cf06d23121d1d49cd" target="_blank">f7e391a</a>)</li> 
</ul> 
<h3><strong>重大变化</strong></h3> 
<ul> 
 <li>最小化的 UMD 捆绑包不再包含在分发的 NPM 包中；</li> 
 <li>animations: 当 root 视图被移除时，DOM 元素现在被正确移除。如果你使用 SSR 并使用应用程序的 HTML 进行渲染，你将需要确保在销毁应用程序之前将 HTML 保存到一个变量中。测试也有可能意外地依赖旧的行为，即试图找到一个在以前的测试中没有被删除的元素。如果这种情况下，失败的测试应该被更新，以确保他们有适当的设置代码来初始化他们所依赖的元素。</li> 
 <li>common: <code>PlatformLocation</code> 类的方法，即 <code>onPopState</code> 和 <code>onHashChange</code>，被用于返回 <code>void</code>。这些方法可以返回调用以删除事件处理程序的函数；</li> 
 <li>common: The methods of the <code>HttpParams</code> class now accept <code>string | number | boolean</code>instead of <code>string</code> for the value of a parameter.If you extended this class in your application,you'll have to update the signatures of your methods to reflect these changes.</li> 
 <li>common: <code>HttpParams</code> 类的方法现在接受字符串、数字、布尔值，而不是字符串作为参数的值。如果你在你的应用程序中扩展了这个类。你将不得不更新你的方法的签名以反映这些变化。</li> 
 <li>Compiler-cli: 链接库不再生成传统的 i18n 消息 ID。任何为这些消息提供翻译的下游应用程序，将需要使用 <code>localize-migrate</code> 命令行工具迁移他们的消息 ID。</li> 
 <li>core: Angular 不再维护对 node v10 的支持；</li> 
 <li>core: 以前 ng.getDirectives 函数在给定的 DOM 节点没有与之相关的 Angular 上下文的情况下会出现错误。这种行为与其他在 ng 名称空间下的其他调试工具不一致，后者处理这种情况时不会引发异常。现在为这样的 DOM 节点调用 ng.getDirectives 函数会导致从该函数返回一个空数组；</li> 
 <li>core：切换 <code>emitDistinctChangesOnlyDefaultValue</code> 的默认值，这改变了默认行为，可能会导致一些依赖不正确行为的应用程序失败。</li> 
</ul> 
<h3><strong>特性：</strong></h3> 
<ul> 
 <li>animations: 更新节点版本的支持范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41544" target="_blank">#41544</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F547363a851567f66e9aee6c80f9e98c739889969" target="_blank">547363a</a>)</li> 
 <li>animations: 通过 BrowserAnimationsModule.withConfig 添加对禁用动画的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F40731" target="_blank">#40731</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F29d8a0ab09a13600405343037079d151c3a04095" target="_blank">29d8a0a</a>)</li> 
 <li>bazel: 更新节点版本的支持范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41544" target="_blank">#41544</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fd583d926db537cc74f9235cad51189dbe83fbb44" target="_blank">d583d92</a>)</li> 
 <li>common: 更新节点版本的支持范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41544" target="_blank">#41544</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fe0250e567ae47ed7b77e9d88a3289727c056a6f1" target="_blank">e0250e5</a>)</li> 
 <li>common: 为 Location 服务添加 historyGo 方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F38890" target="_blank">#38890</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fe05a6f3bb3048e9a94a4b154526221dea290312d" target="_blank">e05a6f3</a>)</li> 
 <li>common: 在 HttpParams 上实现 appendAll() 方法 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F20930" target="_blank">#20930</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F575a2d1" target="_blank">575a2d1</a>)</li> 
 <li>compiler: 支持模板中的 nullish coalescing (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41437" target="_blank">#41437</a>)</li> 
 <li>compiler: 更新节点版本的支持范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41544" target="_blank">#41544</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F75cc8133ad8efd6453694f222e2cc6789c4de7b2" target="_blank">75cc813</a>)</li> 
 <li>compiler-cli: 将使用部分编译模式的功能标记为稳定 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41518" target="_blank">#41518</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F6ba67c6fff52d5da443f36fa1bfe1cc1f0919c51" target="_blank">6ba67c6</a>)</li> 
 <li>compiler-cli: 更新受支持的节点版本范围 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41544" target="_blank">#41544</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fb7bd23817ed81c7359c0559e825ca385975fcafd" target="_blank">b7bd238</a>)</li> 
 <li>compiler-cli: 支持转换组件样式资源 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41307" target="_blank">#41307</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F1de04b124e1e92ea21a070c9d928664f193d220c" target="_blank">1de04b1</a>)</li> 
 <li>compiler-cli: 支持生成特定的 Closure 的 PURE 注释 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41021" target="_blank">#41021</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Ffbc9df181ea50527cb755382b54b8b45d0f9ef39" target="_blank">fbc9df1</a>)</li> 
 <li>core: 引入 getDirectiveMetadata 全局调试实用程序 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41525" target="_blank">#41525</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Fa07f30370848ecd051649a4862de39cf5bc2b541" target="_blank">a07f303</a>)</li> 
 <li>core: 为 XhrFactory 导入添加迁移 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41313" target="_blank">#41313</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F95ff5ecb239d55a239113b0a2e1f7620f6e34676" target="_blank">95ff5ec</a>)</li> 
 <li>core: 放弃对 TypeScript 4.0 和 4.1 的支持 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41158" target="_blank">#41158</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2Ffa048948be75c30dafebda69efbeb81776460500" target="_blank">fa04894</a>)</li> 
 <li>core: 支持 TypeScript 4.2 (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fissues%2F41158" target="_blank">#41158</a>) (<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Fcommit%2F59ef40988e94f3173134368bc7d4e2726cdd8455" target="_blank">59ef409</a>)</li> 
</ul> 
<p>更多详情可查看：<a href="https://www.oschina.net/action/GoToLink?url=https%3A%2F%2Fgithub.com%2Fangular%2Fangular%2Freleases%2Ftag%2F12.0.0" target="_blank">https://github.com/angular/angular/releases/tag/12.0.0</a></p>
                                        </div>
                                      
</div>
            