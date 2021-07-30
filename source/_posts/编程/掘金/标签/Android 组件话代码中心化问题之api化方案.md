
---
title: 'Android 组件话代码中心化问题之.api化方案'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e948abf45f4ad19996103e74629048~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Thu, 29 Jul 2021 22:29:51 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e948abf45f4ad19996103e74629048~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>@charset "UTF-8";.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#2b2b2b;font-family:-apple-system,system-ui,BlinkMacSystemFont,Helvetica Neue,PingFang SC,Hiragino Sans GB,Microsoft YaHei,Arial,sans-serif;background-image:linear-gradient(90deg,rgba(159,219,252,.15) 3%,transparent 0),linear-gradient(1turn,rgba(159,219,252,.15) 3%,transparent 0);background-size:20px 20px;background-position:50%&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;padding:30px 0;margin-top:35px;margin-bottom:10px;color:#4dd0e1&#125;.markdown-body h1&#123;font-size:30px;text-align:center;position:relative;width:max-content;margin:0 auto&#125;.markdown-body h1:before&#123;position:absolute;content:"";z-index:-1;top:-20px;height:100%;width:100px;left:0;right:0;margin:0 auto;background:url(data:image/png;base64,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) no-repeat 50%;background-size:64px 64px;opacity:.84&#125;.markdown-body h1:after&#123;position:absolute;content:"";width:150%;left:-25%;height:50%;bottom:12px;border-radius:50%;background:linear-gradient(transparent 80%,rgba(77,208,225,.8));background-size:400% 200%;opacity:.6;animation:h1Animate 6s linear infinite&#125;@keyframes h1Animate&#123;0%&#123;background-position:100% 100%&#125;50%&#123;background-position:100% 50%&#125;to&#123;background-position:100% 100%&#125;&#125;.markdown-body h2&#123;display:block;border-bottom:4px solid #4dd0e1;position:relative;font-size:24px;padding:12px 32px;margin:30px 0&#125;.markdown-body h2:before&#123;width:24px;height:24px;left:0;top:0;margin:auto;background-size:24px 24px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAADGklEQVRYR81X32vTYBQ999s6mFjQgQ+DrbHiVFZYU4cDcQ/6pGhTFVYFEXGi82H+Bz448UnEF1Fx9ccEEcXpZE3d5tP2ooKiTacTHaLNpigMHDgnU9tcSbrWrkwWR0sbyEOSe885ObnfvV8IRT6oyPwoLQHBx+OVM5WJvSyEVAhnBOjt7yU/+/rr6r6l8TMO+F/EN0JQhICqQpD/xaRpcpAc9tS+M+9lBCia/oqBamK+zeDuQogQZaKJk3wcQjxSva7tGQGB2Ke1zIk3DNyMyNL+QpCnMQOaPsDAVuGAp9cjvbYc8Ec/bCYSg0zoiHilk1tHxqsqEsYlML4kjIpT/eurJxRNPweQU5VdrWaOEo1fgKAVbBgXIz73kF3R/ph+ghgdzMYWM29eAWlBJqgZaFlFYtC6nhWpaDqnSGlIlV1WjJ3DloDNgyNLncudqgX//Ucg3LxuStHGuhi8pqKCW3rqV342rwFjRznKm+/LNaN2yC237ThgF2wxcfMLeP6+ncrKzoPoKTGeLQbYbg4TNoC5iZPJY5HGVRdSNZAWYBclD3FzBQzrR8hACAKdzBzKA/4/IYioDQaOskBbpEG6PO8qKKSAEi3CnEb0Pw4oMf0OmKbTDWqh3Lw6EIiNBZi5lxh3wz4puBD5ovqAMvxhHSdFKxE1CQe3m/07TeTX4lcJdAhE+1Sv65Z5P/ByvIGTRowIZ9igbtXnmrOsbTvgj+kHBNMuBu9OdVw8EeU4nC1A0cYmAHZOTRrLhra4Z8ywnSN6vZHAFTA2WnnMfQB3qz73ddsOZM8CACFDIPSgQXqebXEgqgeZcAeEe6pXasm1f8ew3igMtAHWac0Uc/jYdyAaP0xEBwFsmgUPqbJ0NE2UKj4EGcahiOzuyhagaHpnmtgcVgTcCMuua7YdyAHbA3ArQNscVFbb4635aD6fnYaTvxxi9UNP7ddMXaRWVBdAcaLk6bDXPZCNZ9uBXEsDUX1T2Cc9yjig6Z0EHg3LK8/aqf6MwJKchkXfks1+0+JtSq3qLPa23BRR1B+T/6nkfMaW1r9hPt/MLtYfTLEpP+T9FNoAAAAASUVORK5CYII=)&#125;.markdown-body h2:after,.markdown-body h2:before&#123;content:"";display:block;position:absolute;bottom:0&#125;.markdown-body h2:after&#123;right:0;width:400px;height:10px;border-top-right-radius:24px;background:linear-gradient(90deg,#fff,#4dd0e1);max-width:50vw&#125;.markdown-body h3&#123;margin:30px 0;font-size:18px;position:relative;padding:4px 32px;width:max-content&#125;.markdown-body h3:before&#123;border-bottom:2px solid #4dd0e1;width:100%;content:"";display:block;height:28px;position:absolute;left:0;top:0;bottom:-2px;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);background-repeat:no-repeat;animation:h3AnimationBefore 2s infinite alternate&#125;@keyframes h3AnimationBefore&#123;0%&#123;width:28px&#125;25%&#123;width:100%&#125;50%&#123;width:100%&#125;to&#123;width:100%&#125;&#125;.markdown-body h3:after&#123;content:"";display:block;width:28px;height:28px;position:absolute;border:2px solid #4dd0e1;border-radius:50%;right:-15px;top:0;bottom:0;margin:auto;background-size:28px 28px;background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABRklEQVRYR2NkGGDAOMD2M4w6YDQERkNg+ITAppcfY/8zMv3wF+NdTUrZQpUQ2PT6cz8Dw/8CkMWMDIwNvqK8jcQ6gmIHNN19EaXPx1XPyMCghrCUKcpPlGc5MY6gyAE+Fx52MjL8j3cU5a1UYWXtZGBkEAVb+p8hxU+Mby5NHQCxnKEMaskzJ37uFmUetkmMjAzrfUX4woixHBJlZAA0y2EmPPYU4enLkhGeQIqRJDsAh+UgO7duNpD3IcVykkOA2paT5ABaWE60A2hlOdEO8D3/4CMDIyMfWvySFefoaYSoROh74eFXBgYGLiTNVLGc+BC48PAnAwMDG9QBVLOcaAd8P5ox+x/jf5AjGLgYfnwnKqv9/8/PwPO/kFF/MSj0cAKiouD/0bgYoixFU8RovWgJIX1EOYCQIZTIjzpgNARGQ2DAQwAAvHBaIdB7zxsAAAAASUVORK5CYII=);animation:h3AnimationAfter 2s infinite alternate&#125;@keyframes h3AnimationAfter&#123;0%&#123;transform:rotate(0)&#125;10%&#123;transform:rotate(0)&#125;50%&#123;transform:rotate(-1turn)&#125;to&#123;transform:rotate(-1turn)&#125;&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin:22px 0;letter-spacing:2px;font-size:14px;word-spacing:2px&#125;.markdown-body img&#123;max-width:80%;border-radius:6px;display:block;margin:20px auto!important;object-fit:contain;box-shadow:0 0 16px hsla(0,0%,43.1%,.45)&#125;.markdown-body figcaption&#123;display:block;font-size:13px;color:#2b2b2b&#125;.markdown-body figcaption:before&#123;content:"";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAGFBMVEVHcExAuPtAuPpAuPtAuPpAuPtAvPxAuPokzOX5AAAAB3RSTlMAkDLqNegkoiUM7wAAAGBJREFUKM9jYBhcgMkBTUDVBE1BeDGqEtXychNUBeXlKEqACsrLQxB8lnCQQClCiWt5OYoSiAIkJVAF5eVBqAqAShTAAs7l5ShKWMwRAmAlSArASpAVgJUkCqIAscESHwCVVjMBK9JnbQAAAABJRU5ErkJggg==);display:inline-block;width:18px;height:18px;background-size:18px;background-repeat:no-repeat;background-position:50%;margin-right:5px;margin-bottom:-5px&#125;.markdown-body hr&#123;border:none;border-top:1px solid #4dd0e1;margin-top:32px;margin-bottom:32px&#125;.markdown-body del&#123;color:#4dd0e1&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:rgba(77,208,225,.08);color:#26c6da;padding:.195em .4em&#125;.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace;overflow:auto;position:relative;line-height:1.75;box-shadow:0 0 8px hsla(0,0%,43.1%,.45);border-radius:4px;margin:16px&#125;.markdown-body pre:before&#123;content:"";display:block;height:30px;width:100%;margin-bottom:-7px;background:url(data:image/png;base64,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) 10px 10px no-repeat;background-size:40px&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;color:#4dd0e1;border-bottom:1px solid #4dd0e1;font-weight:400;text-decoration:none;margin:0 4px&#125;.markdown-body a:active,.markdown-body a:hover&#123;background-color:rgba(77,208,225,.1)&#125;.markdown-body strong&#123;color:#26c6da&#125;.markdown-body strong:before&#123;content:"「"&#125;.markdown-body strong:after&#123;content:"」"&#125;.markdown-body em&#123;font-style:normal;color:#4dd0e1;font-weight:700&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:rgba(77,208,225,.05)&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;margin:2em 0;padding:24px 32px;border-left:4px solid #26c6da;background:rgba(77,208,225,.15);position:relative&#125;.markdown-body blockquote:before&#123;content:"❝";top:8px;left:8px;color:#4dd0e1;font-size:30px;line-height:1;font-weight:700;position:absolute;opacity:.7&#125;.markdown-body blockquote:after&#123;content:"❞";font-size:30px;position:absolute;right:8px;bottom:0;color:#4dd0e1;opacity:.7&#125;.markdown-body blockquote p&#123;color:#595959;line-height:2&#125;.markdown-body ol,.markdown-body ul&#123;color:#595959;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h3 data-id="heading-0">一、代码中心化问题</h3>
<blockquote>
<p>将一个大型的项目拆分成多个Module或者新开的组件化项目,想要的预期是这些module之间是平级的关系．这样一来就可以使得业务相对集中，每个人都可以专注在一件事上。同时，代码的耦合度也会随之降低，达到高度解耦状态，因为同级的module不存在依赖关系，在编译上就是隔离的，这会让组件间的依赖非常清楚，同时也具有更高的重用性，<strong>组件强调复用，模块强调职责划分。</strong> 他们没有非常严格的划分。</p>
</blockquote>
<blockquote>
<p>达到可复用要求的模块，那么这个模块就是组件。每个组件的可替代性、热插拔、独立编译都将可行，</p>
</blockquote>
<h4 data-id="heading-1">1.1 代码中心化在Android组件化中的问题体现</h4>
<p>貌似Android的组件化是非常简单且可行的，AS提供的module创建方式加gradle.properies 自定义属性可读，或者ext全局可配置的project属性亦或kotlin dsl 中kotlin的语法糖都为我们提供了application和library的切换。</p>
<p>然后将代码放在不同的仓库位置最好是单独git 仓库级别的管理隔离，就能达到我们想要解决的一系列问题。</p>
<p>然而事情并不是想象的那么简单...</p>
<p>一些列的问题接踵而至，于我而言影响最深的就是应用设计时使用映射型数据库，导致集成模式和组件模式中复用出现问题；最终使用注解配合Java特性生成代码，虽然不完美但是依然解决了此问题。正当我为了胜利欢呼的时刻，一片<a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F6Q818XA5FaHd7jJMFBG60w" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/6Q818XA5FaHd7jJMFBG60w" ref="nofollow noopener noreferrer">《微信Android模块化架构重构实践》</a>文章进入我的眼帘。</p>
<p>随即闪现出了一个重要且紧急的问题，<strong>代码中心化的问题</strong></p>
<p>这个问题是怎么出现的呢？在微信Android模块化架构重构实践中是这样描述的</p>
<p>"""</p>
<p>然而随着代码继续膨胀，一些问题开始突显出来。首先出问题的是基础工程libnetscene和libplugin。基础工程一直处于不断膨胀的状态，同时主工程也在不断变大。<strong>同时基础工程存在中心化问题</strong>，许多业务Storage类被附着在一个核心类上面，久而久之这个类已经没法看了。此外当初为了平滑切换到gradle避免结构变化太大以及太多module，我们将所有工程都对接到一个module上。缺少了编译上的隔离，模块间的代码边界出现一些劣化。虽然紧接着开发了工具来限制模块间的错误依赖，但这段时间里的影响已经产生。在上面各种问题之下，许多模块已经称不上“独立”了。所以当我们重新审视代码架构时，以前良好模块化的架构设计已经逐渐变了样。</p>
<p>"""</p>
<p>再看他们分析问题的原因：</p>
<p>"""</p>
<p>翻开基础工程的代码，我们看到除了符合设计初衷的存储、网络等支持组件外，还有相当多的业务相关代码。这些代码是膨胀的来源。但代码怎么来的，非要放这？一切不合理皆有背后的逻辑。在之前的架构中，我们大量适用Event事件总线作为模块间通信的方式，也基本是唯一的方式。使用Event作为通信的媒介，自然要有定义它的地方，好让模块之间都能知道Event结构是怎样的。这时候基础工程好像就成了存放Event的唯一选择——Event定义被放在基础工程中；接着，遇到某个模块A想使用模块B的数据结构类，怎么办？把类下沉到基础工程；遇到模块A想用模块B的某个接口返回个数据，Event好像不太适合？那就把代码下沉到基础工程吧……</p>
<p>就这样越来越多的代码很“自然的”被下沉到基础工程中。</p>
<p>我们再看看主工程，它膨胀的原因不一样。分析一下基本能确定的是，首先作为主干业务一直还有需求在开发，膨胀在所难免，缺少适当的内部重构但暂时不是问题的核心。另一部分原因，则是因为模块的生命周期设计好像已经不满足使用需要。之前的模块生命周期是从“Account初始化”到“Account已注销”，所以可以看出在这时机之外肯定还有逻辑。放在以前这不是个大问题，刚启动还不等“Account初始化”就要执行的逻辑哪有那么多。而现在不一样，再简单的逻辑堆积起来也会变复杂。此时，在模块生命周期外的逻辑基本上只能放主工程。</p>
<p>此外的问题，模块边界破坏、基础工程中心化，都是代码持续劣化的帮凶...</p>
<p>"""</p>
<p>看完之后就陷入了沉思，这个问题不就是我们面临的问题吗？不仅是在组件化中，在很多形成依赖关系的场景中都有此类问题。</p>
<p>具体是怎么体现的呢，我们来看一组图：</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/99e948abf45f4ad19996103e74629048~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<h5 data-id="heading-2">1.1.1 图1</h5>
<blockquote>
<p>解决方式为分享组件依赖user组件，能解决问题，假设，有一个组件A，需要引用分享组件，就必须依赖分享组件和user组件，这就一举打破了组件编译隔离的远景，组件化将失去香味儿。</p>
</blockquote>
<h5 data-id="heading-3">1.1.2 图2</h5>
<blockquote>
<p>将user组件中的公共数据部分下沉到base组件，分享组件依赖base组件即可实现数据提供，然而当非常多的组件需要互相提供数据时，将出现中心化问题，只需要分享组件的B组件不得不依赖base组件，引入其他数据。也就造成了代码中心化下沉失去组件化的意义。</p>
</blockquote>
<blockquote>
</blockquote>
<h3 data-id="heading-4">二、 怎么解决代码中心化问题</h3>
<p>微信面对这个痛心疾首的问题时发出了“君有疾在腠理，不治将恐深” 的感慨，但也出具了非常厉害的操作-.api 化</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/09064d1185a5483bbea87f3fde728efa~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>这个操作非常高级，做法非常腾讯，但是此文档中只提到了精髓，没有具体的操作步骤，对我们来讲依然存在挑战，</p>
<h4 data-id="heading-5">2.1 什么是代码中心化问题的.api方案</h4>
<p>先看一下具体的操作过程是什么样的，</p>
<p>上图3中，我们使用某种技术将user组件中需要共享数据的部分抽象成接口，利用AS对文件类型的配置将（kotlin）后拽修改为.api ，然后再创建一个同包名的module-api 组件用来让其他组件依赖，</p>
<p>分享组件和其他组件以及自身组件在module模式下均依赖该组件，这样就能完美的将需要共享的数据单独出去使用了，</p>
<h5 data-id="heading-6">2.1.1 SPI 方式实现</h5>
<p>这个有点类似SPI(Service Provider Interface)机制，具体可参考：<a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F46b42f7f593c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/46b42f7f593c" ref="nofollow noopener noreferrer">www.jianshu.com/p/46b42f7f5…</a>
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/295220e953bd4771bb259b157cd88dda~tplv-k3u1fbpfcp-zoom-1.image" alt loading="lazy" referrerpolicy="no-referrer"></p>
<p>（来源上面的文档）</p>
<p>大概就是说我们可以将要共享的数据先抽象到接口中形成标准服务接口，然后在具体的实现中，然后在对应某块中实现该接口，当服务提供者提供了接口的一种具体实现后，在jar包的META-INF/services目录下创建一个以“接口全限定名”为命名的文件，内容为实现类的全限定名；</p>
<p>然后利用 ServiceLoader 来加载配置文件中指定的实现，此时我们在不同组件之间通过ServiceLoader加载需要的文件了</p>
<h5 data-id="heading-7">2.1.2 利用ARouter</h5>
<p>利用ARouter 在组件间传递数据的方式+ gralde 自动生成module-api 组件，形成中心化问题的.api 化</p>
<p>假设我们满足上述的所有关系，并且构建正确，那我们怎么处理组件间的通信，</p>
<p>Arouter 阿里通信路由</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-meta">@Route(path = <span class="hljs-meta-string">"/test/activity"</span>)</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">YourActivity</span> <span class="hljs-title">extend</span> <span class="hljs-title">Activity</span> </span>&#123;

...

&#125;

跳转：

ARouter.getInstance().build(<span class="hljs-string">"/test/activity"</span>).withLong(<span class="hljs-string">"key1"</span>, <span class="hljs-number">666L</span>).navigation()
<span class="copy-code-btn">复制代码</span></code></pre>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-comment">// 声明接口,其他组件通过接口来调用服务</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">HelloService</span> <span class="hljs-title">extends</span> <span class="hljs-title">IProvider</span> </span>&#123;

String sayHello(String name);

&#125;

<span class="hljs-comment">// 实现接口</span>

<span class="hljs-meta">@Route(path = <span class="hljs-meta-string">"/yourservicegroupname/hello"</span>, name = <span class="hljs-meta-string">"测试服务"</span>)</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">HelloServiceImpl</span> <span class="hljs-title">implements</span> <span class="hljs-title">HelloService</span> </span>&#123;

<span class="hljs-meta">@Override</span>

<span class="hljs-keyword">public</span> String sayHello(String name) &#123;

<span class="hljs-keyword">return</span> <span class="hljs-string">"hello, "</span> + name;

&#125;

<span class="hljs-meta">@Override</span>

<span class="hljs-keyword">public</span> void <span class="hljs-keyword">init</span>(Context context) &#123;

&#125;

&#125;

<span class="hljs-comment">//测试</span>

<span class="hljs-keyword">public</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">Test</span> </span>&#123;

<span class="hljs-meta">@Autowired</span>

HelloService helloService;

<span class="hljs-meta">@Autowired(name = <span class="hljs-meta-string">"/yourservicegroupname/hello"</span>)</span>

HelloService helloService2;

HelloService helloService3;

HelloService helloService4;

<span class="hljs-keyword">public</span> Test() &#123;

ARouter.getInstance().inject(<span class="hljs-keyword">this</span>);

&#125;

<span class="hljs-keyword">public</span> void testService() &#123;

<span class="hljs-comment">// 1. (推荐)使用依赖注入的方式发现服务,通过注解标注字段,即可使用，无需主动获取</span>

<span class="hljs-comment">// Autowired注解中标注name之后，将会使用byName的方式注入对应的字段，不设置name属性，会默认使用byType的方式发现服务(当同一接口有多个实现的时候，必须使用byName的方式发现服务)</span>

helloService.sayHello(<span class="hljs-string">"Vergil"</span>);

helloService2.sayHello(<span class="hljs-string">"Vergil"</span>);

<span class="hljs-comment">// 2. 使用依赖查找的方式发现服务，主动去发现服务并使用，下面两种方式分别是byName和byType</span>

helloService3 = ARouter.getInstance().navigation(HelloService.<span class="hljs-keyword">class</span>);

helloService4 = (HelloService) ARouter.getInstance().build(<span class="hljs-string">"/yourservicegroupname/hello"</span>).navigation();

helloService3.sayHello(<span class="hljs-string">"Vergil"</span>);

helloService4.sayHello(<span class="hljs-string">"Vergil"</span>);

&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>假如user组件的用户信息需要给支付组件使用，那我们怎么处理？</p>
<p>ARouter 可以通过上面的IProvider 注入服务的方式通信,或者使用EventBus这种方式</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">*<span class="hljs-keyword">data</span> <span class="hljs-class"><span class="hljs-keyword">class</span>* <span class="hljs-title">UserInfo</span></span>(*<span class="hljs-keyword">val</span>* uid: <span class="hljs-built_in">Int</span>, *<span class="hljs-keyword">val</span>* name: String)

*<span class="hljs-comment">/***

*** ***<span class="hljs-doctag">@author</span>*** *kpa*

*** ***<span class="hljs-doctag">@date</span>*** *2021/7/21 2:15 下午*

*** ***<span class="hljs-doctag">@email</span>*** *billkp<span class="hljs-doctag">@yeah</span>.net*

*** ***<span class="hljs-doctag">@description</span>*** *用户登录、获取信息等*

***/</span>*

*<span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">IAccountService</span>* : <span class="hljs-type">*IProvider* &#123;</span></span>

*<span class="hljs-comment">//获取账号信息 提供信息*</span>

*<span class="hljs-function"><span class="hljs-keyword">fun</span>* <span class="hljs-title">getUserEntity</span><span class="hljs-params">()</span></span>: UserInfo?

&#125;

<span class="hljs-comment">//注入服务</span>

<span class="hljs-meta">@Route(path = <span class="hljs-meta-string">"/user/user-service"</span>)</span>

*<span class="hljs-class"><span class="hljs-keyword">class</span>* <span class="hljs-title">UserServiceImpl</span> : <span class="hljs-type">IAccountService &#123;</span></span>

<span class="hljs-comment">//...</span>

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>在支付组件中</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin">IAccountService accountService = ARouter.getInstance().navigation(IAccountService.<span class="hljs-keyword">class</span>);

UserInfo bean = accountService. getUserEntity();
<span class="copy-code-btn">复制代码</span></code></pre>
<p>问题就暴露在了我们眼前，支付组件中的IAccountService 和UserInfo 从哪里来？</p>
<p>这也就是module-api 需要解决的问题，在原理方面：</p>
<ol>
<li>将需要共享的数据和初始化数据的类文件设计为.api文件</li>
</ol>
<p>打开AS-> Prefernces -> File Types 找到kotlin （Java）选中 在File name patterns 里面添加"<em>.api"（注意这个后缀随意开心的话都可以设置成</em>.kpa）</p>
<p>举例：</p>
<p>UserInfo.api</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-keyword">data</span> <span class="hljs-class"><span class="hljs-keyword">class</span> <span class="hljs-title">UserInfo</span></span>(<span class="hljs-keyword">val</span> userName: String, <span class="hljs-keyword">val</span> uid: <span class="hljs-built_in">Int</span>)
<span class="copy-code-btn">复制代码</span></code></pre>
<p>UserService.api</p>
<pre><code class="hljs language-kotlin copyable" lang="kotlin"><span class="hljs-class"><span class="hljs-keyword">interface</span> <span class="hljs-title">UserService</span> </span>&#123;

<span class="hljs-function"><span class="hljs-keyword">fun</span> <span class="hljs-title">getUserInfo</span><span class="hljs-params">()</span></span>: UserInfo

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<ol start="2">
<li>生成包含共享的数据和初始化数据的类文件的module-api 组件</li>
</ol>
<p>这步操作有以下实现方式，</p>
<ul>
<li>自己手动创建一个module-api 组件 显然这是不可取但是可行的</li>
<li>使用脚本语言shell 、python 等扫描指定路径生成对应module-api</li>
<li>利用Android 编译环境及语言groovy，编写gradle脚本，优势在于不用考虑何时编译，不打破编译环境，书写也简单</li>
</ul>
<h3 data-id="heading-8">三、module-api 脚本</h3>
<p>找到这些问题出现的原理及怎么去实现之后，从github上找到了优秀的人提供的脚本，完全符合我们的使用预期</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">*<span class="hljs-keyword">def</span>* includeWithApi(String moduleName) &#123;

*<span class="hljs-keyword">def</span>* packageName = <span class="hljs-string">"com/realu/dating"</span>

*<span class="hljs-comment">//先正常加载这个模块*</span>

**include(moduleName)

*<span class="hljs-comment">//找到这个模块的路径*</span>

**String originDir = project(moduleName).projectDir

*<span class="hljs-comment">//这个是新的路径*</span>

**String targetDir = <span class="hljs-string">"$&#123;originDir&#125;-api"</span>

*<span class="hljs-comment">//原模块的名字*</span>

**String originName = project(moduleName).name

*<span class="hljs-comment">//新模块的名字*</span>

*<span class="hljs-keyword">def</span>* sdkName = <span class="hljs-string">"$&#123;originName&#125;-api"</span>

*<span class="hljs-comment">//这个是公共模块的位置，我预先放了一个 新建的api.gradle 文件进去*</span>

**String apiGradle = project(<span class="hljs-string">":apilibrary"</span>).projectDir

*<span class="hljs-comment">// 每次编译删除之前的文件*</span>

**deleteDir(targetDir)

*<span class="hljs-comment">//复制.api文件到新的路径*</span>

**copy() &#123;

from originDir

into targetDir

exclude <span class="hljs-string">'**/build/'</span>

exclude <span class="hljs-string">'**/res/'</span>

include <span class="hljs-string">'**/*.api'</span>

&#125;

*<span class="hljs-comment">//直接复制公共模块的AndroidManifest文件到新的路径，作为该模块的文件*</span>

**copy() &#123;

from <span class="hljs-string">"$&#123;apiGradle&#125;/src/main/AndroidManifest.xml"</span>

into <span class="hljs-string">"$&#123;targetDir&#125;/src/main/"</span>

&#125;

*<span class="hljs-comment">//复制 gradle文件到新的路径，作为该模块的gradle*</span>

**copy() &#123;

from <span class="hljs-string">"$&#123;apiGradle&#125;/api.gradle"</span>

into <span class="hljs-string">"$&#123;targetDir&#125;/"</span>

&#125;

*<span class="hljs-comment">//删除空文件夹*</span>

**deleteEmptyDir(*<span class="hljs-keyword">new</span>* File(targetDir))

*<span class="hljs-comment">//todo 替换成自己的包名*</span>

*<span class="hljs-comment">//为AndroidManifest新建路径，路径就是在原来的包下面新建一个api包，作为AndroidManifest里面的包名*</span>

**String packagePath = <span class="hljs-string">"$&#123;targetDir&#125;/src/main/java/"</span> + packageName + <span class="hljs-string">"$&#123;originName&#125;/api"</span>

*<span class="hljs-comment">//todo 替换成自己的包名，这里是apilibrary模块拷贝的AndroidManifest，替换里面的包名*</span>

*<span class="hljs-comment">//修改AndroidManifest文件包路径*</span>

**fileReader(<span class="hljs-string">"$&#123;targetDir&#125;/src/main/AndroidManifest.xml"</span>, <span class="hljs-string">"commonlibrary"</span>, <span class="hljs-string">"$&#123;originName&#125;.api"</span>)

*<span class="hljs-keyword">new</span>* File(packagePath).mkdirs()

*<span class="hljs-comment">//重命名一下gradle*</span>

*<span class="hljs-keyword">def</span>* build = *<span class="hljs-keyword">new</span>* File(targetDir + <span class="hljs-string">"/api.gradle"</span>)

*<span class="hljs-keyword">if</span>* (build.exists()) &#123;

build.renameTo(*<span class="hljs-keyword">new</span>* File(targetDir + <span class="hljs-string">"/build.gradle"</span>))

&#125;

*<span class="hljs-comment">// 重命名.api文件，生成正常的.java文件*</span>

**renameApiFiles(targetDir, <span class="hljs-string">'.api'</span>, <span class="hljs-string">'.java'</span>)

*<span class="hljs-comment">//正常加载新的模块*</span>

**include <span class="hljs-string">":$sdkName"</span>

&#125;

*<span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span>* deleteEmptyDir(File dir) &#123;

*<span class="hljs-keyword">if</span>* (dir.isDirectory()) &#123;

File[] fs = dir.listFiles()

*<span class="hljs-keyword">if</span>* (fs != *<span class="hljs-literal">null</span>* && fs.length > <span class="hljs-number">0</span>) &#123;

*<span class="hljs-keyword">for</span>* (*<span class="hljs-keyword">int</span>* i = <span class="hljs-number">0</span>; i < fs.length; i++) &#123;

File tmpFile = fs[i]

*<span class="hljs-keyword">if</span>* (tmpFile.isDirectory() &#123;

deleteEmptyDir(tmpFile)

&#125;

*<span class="hljs-keyword">if</span>* (tmpFile.isDirectory() && tmpFile.listFiles().length <= <span class="hljs-number">0</span>) &#123;

tmpFile.delete()

&#125;

&#125;

&#125;

*<span class="hljs-keyword">if</span>* (dir.isDirectory() && dir.listFiles().length == <span class="hljs-number">0</span>) &#123;

dir.delete()

&#125;

&#125;

&#125;

*<span class="hljs-keyword">private</span> <span class="hljs-keyword">void</span>* deleteDir(String targetDir) &#123;

*FileTree* targetFiles = fileTree(targetDir)

targetFiles.exclude <span class="hljs-string">"*.iml"</span>

targetFiles.each &#123; File file ->

file.delete()

&#125;

&#125;

*<span class="hljs-comment">/***

** rename api files(java, kotlin...)*

**/</span>*

*<span class="hljs-keyword">private</span> <span class="hljs-keyword">def</span>* renameApiFiles(root_dir, String suffix, String replace) &#123;

*FileTree* files = fileTree(root_dir).include(<span class="hljs-string">"**/*$suffix"</span>)

files.each &#123;

File file ->

file.renameTo(*<span class="hljs-keyword">new</span>* File(file.absolutePath.replace(suffix, replace)))

&#125;

&#125;

*<span class="hljs-comment">//替换AndroidManifest里面的字段*</span>

*<span class="hljs-keyword">def</span>* fileReader(path, name, sdkName) &#123;

*<span class="hljs-keyword">def</span>* readerString = <span class="hljs-string">""</span>

*<span class="hljs-keyword">def</span>* hasReplace = *<span class="hljs-literal">false</span>*

**file(path).withReader(<span class="hljs-string">'UTF-8'</span>) &#123; reader ->

reader.eachLine &#123;

*<span class="hljs-keyword">if</span>* (it.find(name)) &#123;

it = it.replace(name, sdkName)

hasReplace = *<span class="hljs-literal">true</span>*

**&#125;

readerString <<= it

readerString << <span class="hljs-string">'\n'</span>

&#125;

*<span class="hljs-keyword">if</span>* (hasReplace) &#123;

file(path).withWriter(<span class="hljs-string">'UTF-8'</span>) &#123;

within ->

within.append(readerString)

&#125;

&#125;

*<span class="hljs-keyword">return</span>* readerString

&#125;

&#125;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>使用：</p>
<pre><code class="hljs language-groovy copyable" lang="groovy">includeWithApi <span class="hljs-string">":user"</span>
<span class="copy-code-btn">复制代码</span></code></pre>
<p>参考文献：</p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fmp.weixin.qq.com%2Fs%2F6Q818XA5FaHd7jJMFBG60w" target="_blank" rel="nofollow noopener noreferrer" title="https://mp.weixin.qq.com/s/6Q818XA5FaHd7jJMFBG60w" ref="nofollow noopener noreferrer">《微信Android重构模块化架构重构实践》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fgithub.com%2Ftyhjh%2Fmodule_api" target="_blank" rel="nofollow noopener noreferrer" title="https://github.com/tyhjh/module_api" ref="nofollow noopener noreferrer">《gradle实现API方案》</a></p>
<p><a href="https://link.juejin.cn/?target=https%3A%2F%2Fwww.jianshu.com%2Fp%2F46b42f7f593c" target="_blank" rel="nofollow noopener noreferrer" title="https://www.jianshu.com/p/46b42f7f593c" ref="nofollow noopener noreferrer">《高级开发必须理解的Java中SPI机制》</a></p></div>  
</div>
            