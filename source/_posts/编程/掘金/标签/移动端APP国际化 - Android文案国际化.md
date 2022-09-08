
---
title: '移动端APP国际化 - Android文案国际化'
categories: 
 - 编程
 - 掘金
 - 标签
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13b67e18257a4d748ae5d5f08fb74399~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
author: 掘金
comments: false
date: Sun, 04 Sep 2022 09:02:21 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13b67e18257a4d748ae5d5f08fb74399~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?'
---

<div>   
<div class="markdown-body cache"><style>.markdown-body&#123;color:#383838;font-size:15px;line-height:30px;letter-spacing:2px;word-break:break-word;font-family:-apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Oxygen,Ubuntu,Cantarell,Open Sans,Helvetica Neue,sans-serif;scroll-behavior:smooth;background-image:linear-gradient(0deg,transparent 24%,rgba(201,195,195,.329) 25%,hsla(0,8%,80.4%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent),linear-gradient(90deg,transparent 24%,rgba(204,196,196,.226) 25%,hsla(0,4%,66.1%,.05) 26%,transparent 27%,transparent 74%,hsla(0,5.2%,81%,.185) 75%,rgba(180,176,176,.05) 76%,transparent 77%,transparent);background-color:#fff;background-size:50px 50px;padding-bottom:60px&#125;.markdown-body ::selection&#123;color:#fff;background-color:#a862ea&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;margin:24px 0 12px;color:#a862ea&#125;.markdown-body h1&#123;line-height:2;font-size:1.4em&#125;.markdown-body h1~p:first-of-type:first-letter&#123;color:#a862ea;float:left;font-size:2em;margin-right:.4em;font-weight:bolder&#125;.markdown-body h2&#123;font-size:1.2em&#125;.markdown-body h3&#123;font-size:1.1em&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:2em&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;padding-left:.2em&#125;.markdown-body ol li::marker,.markdown-body ul li::marker&#123;color:#a862ea&#125;.markdown-body ol li.task-list-item,.markdown-body ul li.task-list-item&#123;list-style:none&#125;.markdown-body ol li.task-list-item ol,.markdown-body ol li.task-list-item ul,.markdown-body ul li.task-list-item ol,.markdown-body ul li.task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:10px&#125;.markdown-body a,.markdown-body code,.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6,.markdown-body li,.markdown-body p&#123;opacity:.85;vertical-align:baseline;transition:all .1s ease&#125;.markdown-body a:hover,.markdown-body code:hover,.markdown-body h1:hover,.markdown-body h2:hover,.markdown-body h3:hover,.markdown-body h4:hover,.markdown-body h5:hover,.markdown-body h6:hover,.markdown-body li:hover,.markdown-body p:hover&#123;opacity:1&#125;.markdown-body a&#123;display:inline-block;color:#a862ea;cursor:pointer;text-decoration:none;position:relative&#125;.markdown-body a:after&#123;content:"";position:absolute;width:98%;height:1px;bottom:0;left:0;transform:scaleX(0);background-color:#a862ea;transform-origin:bottom right;transition:transform .3s ease-in-out&#125;.markdown-body a:hover:after&#123;transform:scaleX(1);transform-origin:bottom left&#125;.markdown-body a:active,.markdown-body a:link&#123;color:#a862ea&#125;.markdown-body img&#123;max-width:100%;user-select:none;margin:1em 0;transition:transform .2s ease 0s;background-color:#f8f5ff;box-shadow:0 0 10px #e7daff&#125;.markdown-body img:hover&#123;opacity:1;box-shadow:0 0 20px #e7daff;transform:translateY(-1px)&#125;.markdown-body blockquote&#123;padding:.5em 1em;margin:12px 0;border-top-left-radius:2px;border-bottom-left-radius:2px;border-left:3px solid #a862ea;background-color:#f8f5ff&#125;.markdown-body blockquote>p&#123;margin:0&#125;.markdown-body .math&#123;font-style:italic;margin:12px 0;padding:.5em 1em;background-color:#f8f5ff&#125;.markdown-body .math>p&#123;margin:0&#125;.markdown-body code&#123;padding:2px .4em;overflow-x:auto;color:#a862ea;font-weight:700;word-break:break-word;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;background-color:#f8f5ff&#125;.markdown-body pre&#123;margin:2em 0&#125;.markdown-body pre>code&#123;display:block;padding:1.5em;word-break:normal;font-size:.9em;font-style:normal;font-weight:400;font-family:Operator Mono,Consolas,Monaco,Menlo,monospace;line-height:18px;color:#383838;border-radius:2px;scroll-behavior:smooth;box-shadow:0 0 10px #e7daff&#125;.markdown-body pre>code:hover&#123;box-shadow:0 0 20px #e7daff&#125;.markdown-body pre>code::-webkit-scrollbar&#123;height:6px;background-color:#f8f5ff&#125;.markdown-body pre>code::-webkit-scrollbar-thumb&#123;background-color:#e7daff;border-bottom-left-radius:3px;border-bottom-right-radius:3px&#125;.markdown-body hr&#123;margin:2em 0;border-top:1px solid #a862ea&#125;.markdown-body table&#123;width:100%;font-size:12px;max-width:100%;overflow:auto;border-collapse:collapse&#125;.markdown-body thead&#123;color:#a862ea;background:#f8f5ff&#125;.markdown-body td,.markdown-body th&#123;padding:.5em;border:1px solid #e7daff&#125;.markdown-body tr&#123;background-color:#f8f5ff&#125;@media (max-width:720px)&#123;.markdown-body&#123;font-size:12px&#125;&#125;</style><p>“我报名参加金石计划1期挑战——瓜分10万奖池，这是我的第6篇文章，<a href="https://s.juejin.cn/ds/jooSN7t" title="https://s.juejin.cn/ds/jooSN7t" target="_blank">点击查看活动详情</a>”</p>
<p>一直想着把文案国际化的东西整理输出，写了一些零零碎碎的，正好借这个机会整合一下。</p>
<h1 data-id="heading-0"><strong>一 前言</strong></h1>
<p>应用出海不是一个新鲜的话题，其中要针对国内现有应用出海，对应用本身进行国际化支持改造，是必不可少的环节；而这其中很重要的一步就是对应用的文案进行国际化支持，以支持海外用户无障碍的体验使用。</p>
<p>对文案进行国际化支持并不复杂，其结构一般如下图所示</p>
<p align="center"><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/13b67e18257a4d748ae5d5f08fb74399~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图1-1 文案国际化架构</p>
用户修改应用的语言环境配置，应用语言环境发生变更，则应用需要根据当前语言环境获取展示对应的文案。其最核心要解决的技术问题是
1. 语言环境配置管理
2. 字符串资源管理
<h1 data-id="heading-1"><strong>二 方案分析</strong></h1>
<p>落实到我们项目，业务对于文案国际化关键诉求是：</p>
<ol>
<li>支持显示对应语言环境下的文案（先期支持繁体，后续支持英文）</li>
<li>支持文案在线更新（全量）</li>
</ol>
<p>综合业务诉求与技术核心问题，我们来复盘看看最初的方案选择过程</p>
<h3 data-id="heading-2">语言环境配置管理</h3>
<p>对于用户来说，只要的App的语言环境跟手机语言环境一致，用户使用体验就没有什么影响。移动端应用开发系统框架都提供了直接支持，只需要应用配置好支持的语言环境下的文案资源，并，就能够在用户手机上展示其手机语言环境下的文案展示。</p>
<p>那为什么还需要语言环境配置的管理呢？</p>
<p>其一，应用内容国际化不仅仅是应用端端上文案展示的支持，还存在后端提供的内容国际化的支持，所以需要给到后端相应的语言环境参数</p>
<p>其二，很多国际化的应用会增加一个语言环境配置，即图1中除了系统切换语言环境会有影响外，应用本身也能主动切换影响应用自身的语言环境，同时应用本身的设置通常会包括一个「自动」设置项，用于用户没有设置的时候跟随用户手机系统语言环境。</p>
<p>其三，对于缺省的语言环境设置。一般而言海外应用的缺省语言环境都是英文，但如果是在不同地区多个应用的场景下，设置当地语言作为应用的缺省语言才是最佳选择。</p>
<p>语言环境管理的核心问题就是关于<strong>语言环境参数的定义</strong>，一般提到参数定义的时候，很容易听到的是中文用zh而英文用en或者中文用1而英文用2这样的说法。事实上我们无需重复造轮子，可以参考系统实现，这里以Android的Locale类的说明</p>
<blockquote>
<p>The Locale class implements <strong>IETF BCP 47</strong> which is composed of <strong>RFC 4647</strong> "Matching of Language Tags"  and <strong>RFC 5646</strong> "Tags for Identifying Languages"  with support for the LDML (UTS#35, "Unicode Locale Data Markup Language") BCP 47-compatible extensions for locale data exchange.</p>
</blockquote>
<p>可以看到，对于语言环境的定义，已经有了现成的国际标准，直接使用就行。对于语言环境标准里面没有「自动」业务诉求，可以通过代理模式的思路设计处理解决。</p>
<p>语言环境管理的另一关键问题是<strong>语言环境变更通知</strong>，需要通知到整个应用发生了语言环境的变更，看起来直接广播通知即可解决。但实际情况存在这样的情况，语言环境的变更之间是存在依赖关系的，比如配置系统的语言环境变更要优先通知。因此整个语言环境的变更通知需要支持优先级控制，且高优先级的通知存在阻塞操作的可能。</p>
<h3 data-id="heading-3">字符串资源管理</h3>
<ul>
<li>提供统一的字符资源获取接口，即提供类似如下的资源获取即可</li>
</ul>
<pre><code class="hljs language-arduino copyable" lang="arduino"><span class="hljs-type">String</span> getString（T resId）
<span class="hljs-type">String</span> getString（Locale locale，T resId）
<span class="copy-code-btn">复制代码</span></code></pre>
<p>这里T代表resId的类型，根据候问提到的字符串资源获取方案，此处最初使用了String作为resId的类型标记，后续迭代方案中增加支持回了int类型</p>
<ul>
<li>获取对应locale的字符资源，需要支持在线更新</li>
</ul>
<p>作为Android端开发，第一反应肯定是使用资源包的方式提供，但是存在以下限制需要考虑</p>
<p>1）前期开发支持成本。公司当下并不支持资源包生成配置管理发布，整个前期的技术成本就不限于移动端了，同时注意iOS端也需要使用自己的下发方案。</p>
<p>2）持续维护成本。后期的持续使用过程中，产品运营同学怎么能快速配置发布，测试怎么验证变更。</p>
<p>结合上述限制，灵活的使用了当前应用的配置系统，使用json的格式来描述字符串资源进行提供，双端即可实现共同的资源更新管理。</p>
<h1 data-id="heading-4"><strong>三 实施</strong></h1>
<p>方案确定后，具体到开发实施过程中来说，首先遇到的就是实施的体力活，清洗替换项目现有的文案资源，主要是中文字符串资源。</p>
<h3 data-id="heading-5">洗</h3>
<p>1）字符串来源</p>
<p align="center"><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/5fa3ab56035343fe8c4ab02c27f87b54~tplv-k3u1fbpfcp-zoom-in-crop-mark:4536:0:0:0.awebp?" alt="image.png" width="50%" loading="lazy" referrerpolicy="no-referrer"></p>
<p align="center">图3-1 Android字符串来源</p>
2）利用sed + awk脚本，将符合字符串来源的文案资源洗出。然而发现文案资源规模太大，考虑到后续工作量成本，于是进行了一个比较大胆的操作，对项目中无用的代码布局等资源进行删除操作处理。对比删除前后的洗出字符串，差不多减少了50%以上的文案，这一操作也有效的降低翻译成本。
<p>3）注意日志等调用中的文案无需处理</p>
<h3 data-id="heading-6">换</h3>
<p>1）提供基础组件。自定义了一系列的支持国际化文案获取的TextView。通过查找替换脚本，可以快速有效的替换布局文件中使用国际化文案的字符串</p>
<p>2）反向替换。将res/string中的id到string的资源，在使用点用string替换对应的id，然后通过string本身，再整体使用洗出来的数据进行映射，映射回我们自定的key上去。</p>
<h3 data-id="heading-7">问题处理</h3>
<ul>
<li></li>
</ul>
<p>下面列举了一些文案处理过程中遇到的问题点</p>
<p>1）文案相关图片资源。存在百张以上图片上包含了文案，考虑到需要重新实现文案背景分离的成本，此处直接通过设计作图替换；但是带来了新的问题是图片资源需要支持国际化资源获取，国际化图片资源需要跟现有的皮肤主题框架的使用兼容</p>
<p>2）微件（Widget），不支持使用自定义ui组件，需要注意此处只能对数据进行替换。</p>
<p>3）依赖关系，原有文案遍布整个项目，导致项目依赖存在循环引用风险，因此新增了国际化模块作为根本，同时剥离了utils库中的文案使用等，以解决依赖风险。</p>
<p>4）三方库，存在使用等三方库中写死文案，通过外部传入，包装，乃至无法处理等躺平接受无法支持等努力进行解决。</p>
<p>5）接口返回，需要给到不同接口放根据不同接口使用时候到语言环境参数。</p>
<p>6）ui缓存，惊了个大呆的是存在缓存dialog这样子的操作，导致替换不生效，解决缓存。</p>
<p>7）不规范的格式导致的问题，比如R.string.XXX能被格式化成R.\nstring.\nxxx等代码格式问题导致的替换处理失败</p>
<h1 data-id="heading-8"><strong>四 演进</strong></h1>
<p>跌跌撞撞的，在以上处理完后就第一个版本的文案国际化方案实施得到落实，后续又持续迭代了两个版本</p>
<h3 data-id="heading-9">v2版本：增量更新支持/缺省语言环境配置分包支持</h3>
<p>考虑到应用文案改动的概率基本接近于0，实施全量更新实质是对配置资源的浪费，增加了不必要的流量成本，而本地也会保存最新配置，因此从全量更新变更为了增量更新，增加模式选择控制，事实上对于整个获取框架来说并无影响，都是先检查远端配置是否有对应key的内容，没有再从本地获取。</p>
<h3 data-id="heading-10">v3版本：开发友好</h3>
<p>原来的的使用string作为key的获取文案资源方案，由于双端一次性导致key的平衡结果是使用了字符串，但是为了快速支持使用的是随机字符串，通过key无法方便的获取其代表的字符串，因此v1版本时候通过在获取默认字符串位置放置中文简体文案解决。后续修改为通过Android系统本身的id获取方案，IDE自动转化，有效的降低使用难度体验。具体来说关键技术点为</p>
<ul>
<li>资源的名称跟id转换，解决配置的key是String，而系统提供的是int，用于检测是否存在远端更新替换</li>
<li>切换locale获取对应的字符串内容，注意存在系统版本的兼容</li>
</ul>
<h1 data-id="heading-11"><strong>五 总结</strong></h1>
<p>总结来说就是一个规范的项目将大大降低项目的持续开发维护成本。同时方案的实施也要与项目资源相适应才能有效的开展落实。所以前期的准备估算工作很重要，对于项目的熟悉程度不足的时候不要做风险决定。不过一旦担当了，那就要踏踏实实的去落实解决，尽力达成目标，即</p>
<ul>
<li>使用标准规范定义通用参数</li>
<li>代码风格规范</li>
<li>考虑研发成本限制，循序渐进</li>
<li>熟悉项目</li>
</ul>
<h1 data-id="heading-12">参考</h1>
<ol>
<li><a href="https://link.juejin.cn/?target=https%3A%2F%2Fdeveloper.android.google.cn%2Fdevelop%2Fui%2Fviews%2Fappwidgets%2Foverview%3Fhl%3Dzh-cn" target="_blank" rel="nofollow noopener noreferrer" title="https://developer.android.google.cn/develop/ui/views/appwidgets/overview?hl=zh-cn" ref="nofollow noopener noreferrer">App widgets overview</a></li>
</ol></div>  
</div>
            