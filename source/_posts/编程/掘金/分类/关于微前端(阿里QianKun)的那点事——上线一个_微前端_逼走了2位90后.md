
---
title: '关于微前端(阿里QianKun)的那点事——上线一个_微前端_逼走了2位90后'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889589684e494d6b877d88cd0ea855da~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 16:23:45 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889589684e494d6b877d88cd0ea855da~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>「本文已参与好文召集令活动，点击查看：<a href="https://juejin.cn/post/6978685539985653767" target="_blank">后端、大前端双赛道投稿，2万元奖池等你挑战！</a>」</p>
<blockquote>
<ul>
<li>📢欢迎点赞 ：👍 收藏 ⭐留言 📝 如有错误敬请指正，赐人玫瑰，手留余香！</li>
<li>📢本文作者：由webmote 原创，首发于 C🙉</li>
<li>📢作者格言： 生活在于折腾，当你不折腾生活时，生活就开始折腾你，让我们一起加油！💪💪💪</li>
</ul>
</blockquote>
<h1 data-id="heading-0">🎏 序言</h1>
<p>作为一个团队领导者，需要经常帮助组员解决各类阻塞问题。🎎🎎🎎</p>
<p>而我一直从事后端的开发，导致对前端的知识储备并没有那么丰富（实际很简陋）。</p>
<p>鉴于当下流行的开发模式几乎都是前后端分离的，为了组建好团队，前端、后端几乎1比1配置好像有些不太对，因此稍微倾斜了下后端，按80%配置前端，这个比例到底是不是合适，估计每个人都有自己的见解，可以留言谈谈你们团队的人员配比问题。</p>
<p>我们的新的产品，后端采用微服务，前端采用微前端，感觉是绝配啊。没想到，悲剧就此拉开序幕.....</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/889589684e494d6b877d88cd0ea855da~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-1">🎏 01.你好像不会哎...</h1>
<p>为了组建团队，需要进行多轮次的面试，遴选人才从来不是一个轻松的活。</p>
<p>揣着一颗忐忑不安的心，在备足了前端的知识后，开始上岗面试了，碰到我这种半瓶子晃荡的面试官，诸位前端大佬们是不是很轻松的吊打面试官？</p>
<p>谈谈我的面试方式</p>
<p>我的一般步骤是：</p>
<ul>
<li>🍄进入正题前，和他们聊聊经历、离职原因以及之前的开发团队情况，聊完觉得还合适的，就再深入聊聊技术。</li>
<li>🍄一般会问下vue的生命周期、vue的路由分类、父子组件通信方式以及对象的深度拷贝，甚至会让他写个递归函数，到此基本结束。</li>
</ul>
<p>一般在聊对象深拷贝的时候，好多前端工程师就冒出来一句：你好像不会哎，你不了解前端吧。</p>
<pre><code class="copyable">  哎呀，妈呀！这句话简直是晴天霹雳，震得老夫虎躯一阵摇晃！
<span class="copy-code-btn">复制代码</span></code></pre>
<p>看来我恶补的vue知识、typescript基础以及当时上手的angular项目都是白来的了，好吧，我只好坦白，我不是很懂。</p>
<p>好像我终于找到了真正的前端工程师，你就是我想要的人才！</p>
<p>来吧，come on，baby!</p>
<p>这就是我被吊打的整个过程。🔥🔥🔥</p>
<h1 data-id="heading-2">🎏 02.看起来不错的90后前端</h1>
<p>面试的一位前端90后，聊的还算愉快，会的也多（⚡吊打后的真实反应⚡），看项目经验也蛮不错，我希望他来做前端组长。</p>
<p>毕竟对于疏于前端知识的我来说，没必要在不熟悉的领域花费太多时间。</p>
<p>让能干的人，把事情干好就行了。🤔🤔🤔</p>
<p><strong>工资我还希望能再给他多点</strong>，毕竟找个能干的人不容易，稳定的团队才能够持续发展。</p>
<p><strong>也许灾难的起源就在于不了解</strong>，对前端的知识匮乏，导致了后续事件的发酵。</p>
<p><strong>微前端</strong>的概念应该有好几年了，之前也和以前的同事聊过，都觉得是不错的理念。恰好我看到有介绍阿里<strong>QianKun</strong>引擎的文章，讲的非常详细，我就转发给了这位90后小伙子。并多次给他说我们需要微前端架构搭设我们的项目，采用阿里成熟的引擎，至少方向不会错。</p>
<p><em>不知道我的理解对不对：</em></p>
<blockquote>
<p>微前端在我的理解是基于目前的框架，代替了iframe老式组织形式的变种而已。</p>
</blockquote>
<p>如果没有淘汰iframe，那么使用iframe做微前端，简直简单的要死。 而微前端引擎就是采用新的技术替代iframe，因此需要做到子应用的加载，甚至动态加载，并且需要解决掉CSS、JS的冲突，隔离开其范围。</p>
<p>任务已经布置了，就耐心等待结果吧，一切就交给“<strong>前端组长</strong>”吧！😍😍😍</p>
<h1 data-id="heading-3">🎏 03.目不暇接的DEMO</h1>
<p><strong>团队的沟通</strong>永远是个问题，而日本人并不这么认为，他们有一套自己的方法。</p>
<p><strong>一个问题，要想布置的很清晰，需要按五步法来进行。</strong></p>
<ol>
<li>要有一个能胜任的人  🕺</li>
<li>要有明确的完成时间  ⏱️</li>
<li>要有明确的完成标准  🚩</li>
<li>布置完任务，让员工复述一遍🗣️</li>
<li>做好汇报要求，检查进展✅</li>
</ol>
<p>而在此过程中，我并没有按照上述步骤实施，而<strong>我以为</strong>和<strong>他以为</strong>可能并未对齐。</p>
<p>当然我只是简单的跟踪下任务进度和看下最终结果，里面的代码我也没有去把控。</p>
<p>大概几天后，我亲爱的90后前端组长（手下有2为前端成员），就拿出来3个DEMO，说都是别人基于qiankun或是single-spa做的微前端，基座和子应用都有，支持vue、angule、react等等。</p>
<p>我感觉随便一个都满足我的需求啊，这下我就更放心了。
“你来定一个”，反正我们也不需要其他技术栈，只要支持vue就可以了。</p>
<p>另外一个前端工程师去做子应用，配合基座完成子应用的改造。</p>
<p>分工感觉很明晰了，这个迭代的目标也应该没问题了吧？每天的晨会，都有进展，就不提了。</p>
<p>🏃🏃🏃又过了大约1-2周，当我再去了解的时候，前端组长说基座和子应用通信有些问题，我就大致看了下qiankun的介绍文档，并把文档贴到群里。
<img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/e5a31a28b32e48c1848975d693605bda~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>我感觉我已经看懂了，采用引擎提供的api，就可以传递token过去，然后我决定和他当面沟通下。
对话如下：</p>
<blockquote>
<p>我：咱们这个通讯采用我发的那篇文章介绍就可以，你看看。
他：嗯嗯，这个很简单，采用localstorage就可以。
我：不行吧，子应用可能部署在不同的域下，那怎么可能呢？
他：这样啊，那我们就采用那个api，我再改改，改动比较大。
我：你用的是qiankun 几？
他：别人集成的，不知道啊。
我：是不是版本太低，现在好像是2点几。
他：这个项目看不了使用的是啥版本。
我：看看包里有没，我再看看官方文档去。
............. 我看文档后 ，发现只需要安装qiankun包即可。
我：yarn add qiankun
他：我这个项目好像不是qiankuan的，我再看看别的demo......</p>
</blockquote>
<p>此时，另外一位前端告诉我，他已经按照组长的吩咐，分别在3个demo上改了3版登录了，并且用的都不是qiankun...</p>
<p><strong>我的娘啊，发生了啥！</strong></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/21502ec367c249b3b93089ba2395768b~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h1 data-id="heading-4">🎏 04. 闪人了</h1>
<p>星星之火，已经燎原！🔥🔥🔥</p>
<p>前面的错误耽搁了我们的选型时间，不过知错就改，赶快掉头仍来得及。</p>
<p>事情来了，稳住，别乱！🧺</p>
<p>我紧急通知前端组长，尽快采用qiankun包，构造项目，搭建基座。</p>
<p>刚好公司又来了一位前端，是个老手，这里就称呼他老A吧，让他和前端组长一块搞。</p>
<p>我自己也忙着查看官方文档，试图协助他们搞定基座容器项目，毕竟<strong>迭代任务需要按时完成</strong>。</p>
<p>花费了几个小时，大致原理我看了一遍，觉得集成起来应该很简单，没有特别复杂的地方，当然作为技术经理，对其中的小坑还是有一定预知的。</p>
<p><strong>下班时间到了</strong>，和他们一起沟通了下，哎，<strong>下班前做事情</strong>真不是我的初衷。</p>
<blockquote>
<p>老A说，没问题，特简单，交给我搞吧，明天搞定。</p>
</blockquote>
<blockquote>
<p>前端组长说：搞不定了，让我去做子应用吧。</p>
</blockquote>
<blockquote>
<p>@@@我就和他单独聊了下前因后果，应该没有特别重的话，只是告诉他应该采用qiankun，而不应该采用其他的引擎，除非他有把握做的更好。这次就这样吧，让老A去搞基座，我们去做子应用的相关任务，并给他分了几个任务。</p>
</blockquote>
<p>没想到在下班路上收到他的微信。</p>
<blockquote>
<p>经理我想提离职，状态不行，平静一段时间再找工作</p>
</blockquote>
<blockquote>
<p>没适应过来</p>
</blockquote>
<blockquote>
<p>本来一号想说</p>
</blockquote>
<blockquote>
<p>状态不行，怕耽误进度</p>
</blockquote>
<p>我试图挽留，毕竟仅仅遇到一个小坎坷呗，挺过去就没什么了。结果他只说了句：<strong>哎，状态没调整过来，去深圳我同学那调整一段时间，提升下技术。</strong></p>
<p>好似一片雪花从头上划过，我看好的，依赖的，没有检验就依赖的前端组长，就这样闪人了。
一个月，留下了 7个DEMO项目。</p>
<blockquote>
<p>难道这就是，传说中的这个领导不听我的....</p>
</blockquote>
<h1 data-id="heading-5">🎏 05. 救火还需队长</h1>
<p>除了面临前端组长留下的烂摊子以外，我也备受组建团队的打击。</p>
<p>我忽然明白了一个人的突然离职，对他的上级来说，<strong>也是一种额外的重击</strong>，当然，最终我又想通了，没啥大不了的，总结下教训就是了，没必要上纲上线。</p>
<p>第二天仍然是忙乱的一天，我一直跟踪着基座项目的进展，消息忽好忽坏。</p>
<p>下班的时候，前端老A告诉我，里面有许多问题搞不定，可能用不了，他下班了，明天再看。</p>
<p>虽然下班了，但我真的不能任事态发展下去了，我决心自己来试一下，看看到底卡在哪里了。</p>
<p><strong>加班不分时间</strong>，好像做了领导就有了这觉悟！</p>
<p>我克隆下qiankun的官方Demo1、我发的那篇文章的Demo2，然后对比教程，一步步建立一个新的vue基座项目。</p>
<p>不会的就百度、谷歌。</p>
<ol>
<li>建立新的vue项目:宇宙飞船</li>
</ol>
<p><code>vue create portal-spaceShip  </code></p>
<ol start="2">
<li>增加element-ui</li>
</ol>
<p><code>yarn install element-ui</code></p>
<ol start="3">
<li>增加qiankun</li>
</ol>
<p><code>yarn add qiankun</code></p>
<ol start="4">
<li>把demo2的ts程序翻译为js写到项目内</li>
<li>启动</li>
</ol>
<p>✨好像成功了，我怀疑我是不是没进入新的状态，这么顺利吗？</p>
<p>✨把demo1的子应用启动一个，我的神啊，就这么快吗，没问题啊。</p>
<p>❤️好像有信心了：增加登录窗口、增加链接，没什么难点啊，登录ok了。</p>
<p>应该好了70%吧,我心里想。</p>
<p>好像还有点小问题，加载的子应用并没渲染到指定的容器内，而是顶在了顶层容器上。一番折腾，我终于发现问题的根源。</p>
<h3 data-id="heading-6">5.1 阿里乾坤的坑1</h3>
<p>子应用加载会加载到顶层，是因为子应用和基座应用都使用了相同的id，把基座的index.html内的id修改为不同的id即可。</p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/cce54bf3a7934070a80af202bc08ecbf~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-7">5.2 坑2 动态注册微服务</h3>
<p>引擎注册由于生命周期缘故，需要在vue的周期前后启动，一般放在main.js，注册api  registerMicroApps也在此时调用。但由于还没登录，因此无法注册设定的服务。经过大量查询issue，发现其已经支持动态添加子应用。只需再次调用 <strong>registerMicroApps</strong>即可。</p>
<p>你可以在app.vue内合适的地方调用，即可渲染增加新的微服务。</p>
<h3 data-id="heading-8">5.3 坑3 子应用返回主应用</h3>
<p>这个应该不能算是引擎的坑，应该是启用了根目录导致的，不能往上层弹出路由，仅需要使用即可。</p>
<pre><code class="hljs language-shell copyable" lang="shell">      //window.location.href = "/";
      window.history.pushState(null,'','/login');
<span class="copy-code-btn">复制代码</span></code></pre>
<h3 data-id="heading-9">5.4 核心点 子应用无需qiankun包</h3>
<p>最核心的一点是，子应用不需要关注<strong>qiankun框架</strong>，无需引用其包，只需按照标准实现导出接口即可。</p>
<p>一切妥妥的，并没有那么难。</p>
<h1 data-id="heading-10">🎏 06. 绝杀技：有事不来了</h1>
<p>当然晚上加班并没有搞完所有的，几个坑也是在加班后第二天解决的。</p>
<p>因为老A第二天没来，问起来，说是请假了，哎，这个假批还是不批...</p>
<p>其实既然已经开始搞了，那就搞得风生水起，当然也无需在意这些细节。</p>
<p>“不来就不来吧，没什么大不了。”  我只能自己安慰自己。</p>
<blockquote>
<p>职场生存技能：如果搞不定手头的紧急事情，就请假吧，拖到你的上级两眼冒金星✨✨✨，事情自然有进展！</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2f63e59de338481fa931f4bf10a792d8~tplv-k3u1fbpfcp-zoom-1.image" alt="在这里插入图片描述" loading="lazy" referrerpolicy="no-referrer"></p>
<p>看起来，有必要加强前端知识了~~~</p>
<p>看起来，我带队伍的能力有待提高 ~~~</p>
<h1 data-id="heading-11">🎏 07. 结语</h1>
<p>关于此事情，我和老板详谈了下，要点记录如下。</p>
<p>当然是他得看法和建议，值得反思，其实也有点打击我的积极性，因为我没有得到他的支持。</p>
<ul>
<li>识人问题，没搞清楚，就让人担大任</li>
<li>放权问题，检验与任务布置不清晰</li>
<li>职级差别，心离得太远，很难听到实话</li>
<li>沟通占用时间过长，每个人都需要和我沟通</li>
<li>后台框架固有问题，某某的槽点</li>
<li>情商问题，情商不高🤕🤕🤕</li>
<li>需要考虑轮流组长，设定中间人，来承担任务</li>
</ul>
<p>🤕🤕🤕玻璃心的我也受到1万点伤害，不过我需要挺过去，看到得朋友希望能帮我分析分析！</p>
<p>谢谢，谢谢大家了。</p>
<p>这也是一场难得得经历，记录下来，以后也是一串特别得足迹！</p>
<p>年少不识前端香，🕺🕺🕺 错把后端当个宝！</p>
<p>例行小结，理性看待！</p>
<p>结的是啥啊，结的是我想你点赞而不可得的寂寞。😳😳😳</p>
<p>👓都看到这了，还在乎点个赞吗？</p>
<p>👓都点赞了，还在乎一个收藏吗？</p>
<p>👓都收藏了，还在乎一个评论吗？</p>
<blockquote>
<p><strong>还有系列前端文章，客官，你不瞧瞧？</strong></p>
</blockquote>
<p>👉<a href="https://juejin.cn/post/6980530046553292831" target="_blank">前端项目，看我在这里管理全局后台初始化的数据，就问你飒不飒？</a></p>
<p>👉<a href="https://blog.csdn.net/codeex/article/details/115674542" target="_blank" rel="nofollow noopener noreferrer">Vue中路由到一个公共组件，然后根据路径中是否存在文件动态加载组件</a></p>
<p>👉<a href="https://blog.csdn.net/codeex/article/details/117462163" target="_blank" rel="nofollow noopener noreferrer">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之一缘起</a></p>
<p>👉<a href="https://blog.csdn.net/codeex/article/details/117552675" target="_blank" rel="nofollow noopener noreferrer">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之二接口</a></p>
<p>👉<a href="https://blog.csdn.net/codeex/article/details/117756676" target="_blank" rel="nofollow noopener noreferrer">解放前端工程师——手把手教你开发自己的自定义列表和自定义表单系列之三表格</a></p></div>  
</div>
            