
---
title: 'COCOS 微信小游戏开发完整记录和坑'
categories: 
 - 编程
 - 掘金
 - 分类
headimg: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91282c82da41769792a79c2bcd679a~tplv-k3u1fbpfcp-watermark.image'
author: 掘金
comments: false
date: Mon, 05 Jul 2021 02:23:09 GMT
thumbnail: 'https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91282c82da41769792a79c2bcd679a~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><h1 data-id="heading-0">COCOS微信小游戏开发完整记录 -> 结尾有惊喜</h1>
<h2 data-id="heading-1">背景</h2>
<p>因为我个人喜欢游戏，一直想做一小游戏，但是一直拖着，没时间做，现在终于在周末空闲时间做了一个微信小游戏。</p>
<p>第一次写技术文章，篇幅可能较长，但是自我感觉干货满满，如果有不好的地方希望小伙伴们多多提出意见，<strong>内含游戏核心数值设计的全过程。</strong></p>
<p>如果你正准备做游戏开发，或者不知道怎么下手，希望本文能为你带来一定的收获</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/bf91282c82da41769792a79c2bcd679a~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p><em>废话不多说，先上图看看效果，如果想先体验，可直接拖到底部</em></p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2224a4b5fd074c778e07beb579c3bfd5~tplv-k3u1fbpfcp-watermark.image" alt="1411623937312_.pic.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/a6520816fc8b4689ae634f01420ccbe7~tplv-k3u1fbpfcp-watermark.image" alt="1421623937312_.pic.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-2">目录</h2>
<ul>
<li>游戏玩法介绍</li>
<li><strong>数值设计（砖块血量，玩家攻击，攻速等关系）</strong></li>
<li>开发过程</li>
<li>采坑记录</li>
<li>微信部署相关问题</li>
<li>微信广告接入</li>
</ul>
<blockquote>
<p>注意：本文不涉及太多具体代码以及全部代码，会列出一个新手在 Cocos 开发一款完整游戏的思想，避免大家采坑，但是会有一些核心的数值或者关键代码提供参考学习，纯干货。</p>
</blockquote>
<h3 data-id="heading-3">1 游戏基本玩法介绍</h3>
<p>当时最初的设计是一款轻量级的射击爽游，自动发射子弹，通过手指触摸移动来改变角色的移动，吃不同的 Buff 可以叠加对应的能力，通过打击砖块获得更高分数。</p>
<p><em><strong>以下是目前支持的一些功能</strong></em></p>
<ul>
<li>自动发射子弹，双列，三列，四列子弹</li>
<li>飞机移动与砖块碰撞</li>
<li>子弹碰撞</li>
<li>完整排行榜实现</li>
<li>完整游戏流程，开始，游戏中，游戏结束</li>
<li>砖块血量数值算法</li>
<li>Buff 叠加，攻击，攻速，炮筒数量，无敌 Buff</li>
</ul>
<h3 data-id="heading-4">2 数值设计</h3>
<p>如果条件允许数值设计其实也是专门的数值策划的工作，但是...  我也做了，为了想要得到玩家在不同时间段攻击应该是多少，我做了一个 Excel 来推算玩家攻击的数值，后作为实际开发怪物生命的设置。先上一张我的数值设计的样子（实际上 Excel 推算了 100 行的数值左右，图太长，所以我只截取了前面一部分）。</p>
<blockquote>
<p>数值设计我觉得算是整个游戏的一个核心，是游戏平衡，可玩性的核心，这一部分我花了一部分时间来思考，整个游戏设计是只有攻击和生命，没有护甲，所以对于计算来说用了比较简单的 <strong>减法公式</strong></p>
</blockquote>
<p>公式1：攻击 = 消耗</p>
<p>公式2：生命 - 消耗 = 结果</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6cfdd1a197984e09ad3602783168cd9f~tplv-k3u1fbpfcp-watermark.image" alt="QQ20210705-164023.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>数值组成字段 Tab 说明</p>
<ul>
<li>怪物波数：砖块是一波一波的下落（一波砖块为一排）</li>
<li>打击时间：平均打死一个怪物的时间</li>
<li>成长率：打击的时间成长率（控制打击的时间因素）</li>
<li>怪物血量：砖块的生命值</li>
<li>血量成长：控制怪物血量的成长因素</li>
<li>玩家攻击：最终得出不同波数怪物玩家攻击数值应该是多少</li>
</ul>
<h4 data-id="heading-5">数值设计过程</h4>
<blockquote>
<p>对于 Excel 的操作我就不做介绍了，各位大佬自行百度。应该各种教程特别多</p>
</blockquote>
<p>1：我的想法就是 最初玩家一秒能打死一个砖块（因为初始的攻击速度在 0.5 秒一发子弹，子弹移动到怪物身上大约0.5 秒左右），于是就有了第二列第一行 打击时间为 1s</p>
<blockquote>
<p>得出第一个初始值：打击时间 1s</p>
</blockquote>
<p>2：然后就是每波怪，玩家的打击时间应该增加多少呢？因为这是一个怪物无限往下掉，打击时间肯定不能太久，否则打不死就 GG 了，所以我设定了一个成长率为 0.01，通过数值验证比较合适，到第30波的时候也就 1.3s，</p>
<blockquote>
<p>得到第二个初始值以及计算公式：打击时间成长率 0.01，打击时间的计算公式为： =B2+B2*C2 【注意：这个值需要多次尝试，根据自己的需求来得到最终的结果】</p>
</blockquote>
<p><img src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/172db777f4b741eeb2fa3c9553fde716~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>3：然后就是怪物的血量应该是多少，一开始肯定不能设计得太多，如果设计得太多，并且要在 1 秒内打死 那么攻击肯定也特别高，而我的想法就是攻击需要根据吃 Buff 来进行叠加。</p>
<blockquote>
<p>得出第三个初始值：怪物初始血量为 2</p>
</blockquote>
<p>4：同样的血量肯定有成长因素，所以这里就出现了一个血量成长率，这里我最开始从 1 的倍率一直到 0.2 倍率都试了，发现 0.55 比较合适成长不低不高，算是比较满意的状态</p>
<blockquote>
<p>得到第四个初始值以及实际血量计算公式：血量成长率 0.55， 血量成长的计算公式为： =A3<em>A3</em>E2+D2*E2，血量增加除了和成长有关，还得和砖块的波数成比例，波数越高怪物血量随之约高。</p>
</blockquote>
<blockquote>
<p>怪物波数的平方*血量成长 + 上一波砖块血量 * 血量成长，【最开始我只想了 血量 * 成长，发现比较低，在50波以上的时候数值还是太低了，所以我增加了一个怪物波数的条件】</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/799482ee9b1b4291895a4c1285c8622d~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>5：最后一个 玩家攻击就相对比较简单了，砖块血量 / 打击时间 = 玩家攻击</p>
<blockquote>
<p>得出玩家攻击数值：初始值设定的 2 (因为怪物设定的初始血量为 2，因为一发打死一个小朋友)
玩家实际攻击 = 砖块血量 / 打击时间</p>
</blockquote>
<p><img src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/f32f8a4bf89946d897e5ad4dfdfdcb57~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<p>至此整个游戏核心的数值就设计完毕，但是漏了一点，因为这是一个类似射击类的游戏，子弹不止一发，所以后面需要 <strong>将子弹速度、炮筒数量加进去一起计算</strong>。</p>
<p>以下是砖块血量计算的完整代码</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/731f582281064aaa9b5f1c8b85f7f198~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<blockquote>
<p>第一行 hp 变量最终值乘以了 0.65，因为 Buff 的随机性导致攻击可能不能和数值表设计的完全一致，所以这里做了一个优化。</p>
</blockquote>
<blockquote>
<p>当炮筒达到满状态并且攻速达到满状态的时候（满攻速是 2 帧（≈0.03s）一发，算上满炮筒 大概是 0.03s 3 or 4发子弹），当时发现攻击过于高了，所以在玩家达到不同状态的时候给 HP 增加了一定的数值修正。</p>
</blockquote>
<blockquote>
<p>攻速 Buff 每次减少 3 帧（也就是攻速会提升 0.045s 左右），上限为 2 帧。</p>
</blockquote>
<blockquote>
<p>攻击 Buff 每次增加 3 点攻击力，无上限，出现的概率比攻速要大</p>
</blockquote>
<h3 data-id="heading-6">3 开发过程</h3>
<p>游戏核心数值搞定了，开发其实就是比较轻松的了，无非查查API，想想游戏怎么做。</p>
<p>这里我列一下我做整个游戏的一个步骤</p>
<p>1：想好整个游戏的具体玩法，如何操作，如果胜利和死亡，核心玩法是什么。一步一步的完成整个游戏。</p>
<p>2：第一步，完成玩家的操作，拖拽移动</p>
<p>3：第二步，完成玩家的发射等功能、子弹管理（速度、子弹状态、炮筒数量等等）。</p>
<p>4：第三步：开始制作砖块，设定好砖块的位置，按照固定的速度往下掉。</p>
<p>5：第四步：处理子弹和砖块的碰撞【这里自喷一下，最开始我居然用的 Cocos 提供的物理引擎来进行碰撞检测等操作，后发现当子弹特别多的时候，就有点卡了，于是我查了一下，找到了普通的 2d 碰撞检测】。</p>
<p>6：第五步：制作各种界面，如开始界面，结束界面等。</p>
<blockquote>
<p>哦对了，游戏涉及到的数据存储，我是用的 Node 来写的后端，因为作为前端开发，只会 Node 哈哈哈</p>
</blockquote>
<h3 data-id="heading-7">4 采坑记录</h3>
<ul>
<li>坑1 ：UI 同学给了我一版新的 UI 图，我换上之后发现在 IOS 平台（微信小游戏）无法加载这个图（因为这个图不起眼，我就没有注意），安卓所有平台 小游戏 无法打开小程序，各种百度，以及微信开放社区都无法查阅相关信息， 偶然间我看到有人说，小游戏的图片尺寸不能超过 2048， 于是我检测了一下我的图片，确实哪一张图超过了2048，于是我试了一下，结果我特 &……*&%%￥&， 搞了我几天的问题，竟然是这 。。。</li>
</ul>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/29aa5910e9044c4aa982b472f0f26cf3~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<ul>
<li>
<p>坑2 ：精灵图，对于 Cocos 建议不用自己去合并精灵图，麻烦，而且不易扩展，每次新增一个图都要重新生成。可以使用官方提供的 自动合并精灵图，会根据我们的引用自动生成精灵图，特别好用</p>
</li>
<li>
<p>坑3 ：我在引入友盟统计的时候，发现导入进来各种问题，微信授权也没有，然后我发现不知是我操作问题，还是 SDK 代码的问题，于是我自己吧友盟的 min.js 文件格式化之后 一通改动。</p>
</li>
</ul>
<p>额其他的暂时没想到了，如果想到了，我在在补上。</p>
<h3 data-id="heading-8">5 微信部署相关问题</h3>
<p>1：微信部署其实很简单，微信小游戏现在不需要软著了，但是貌似隔壁抖音必须要软著</p>
<p>2：目前提审的时候 基本上都是一次过，只要不涉及什么违法违纪什么的，基本上都没问题。</p>
<p>3：值得一提的是，微信小程序做版本兼容一直是个很头疼的问题，这个得想好</p>
<blockquote>
<p>Cocos 提供了全局参数 CC_DEBUG 为true表示开发环境</p>
</blockquote>
<blockquote>
<p>小程序提供了 __wxConfig.envVersion 属性用来区分小程序的状态 develop = 开发版 ，trial = 体验版， release = 正式版</p>
</blockquote>
<h3 data-id="heading-9">6 微信广告接入</h3>
<p>1： 这个也很简单，但是前提是 需要满足 1000 独立 UV ,这个比较麻烦，但是没有什么是难道我们强大的国家（<strong>伟大、光荣、正确的中国共产党万岁！伟大、光荣、英雄的中国人民万岁！</strong>）</p>
<p>2：然后有个小问题就是，微信 Banner 广告如何正确的定位在底部，因为微信是按照他自己的位置和像素进行计算，而且只支持top属性，所以很坑爹，也就是说和 Cocos 的尺寸并不兼容，这里我说一下我的解决方案。</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-comment">// 定位 Left 的计算方式</span>
Left = (屏幕宽 - 设定的 Banner 宽) / <span class="hljs-number">2</span>;

<span class="hljs-comment">// 定位 Top 的计算方式，这里的 20 是自己设定的距离底部的距离，Banner的高度需要通过 onResize事件来动态获取</span>
Top = 屏幕高 - Banner 高 - <span class="hljs-number">20</span>;
<span class="copy-code-btn">复制代码</span></code></pre>
<p>以下是详细的相关代码</p>
<pre><code class="hljs language-js copyable" lang="js"><span class="hljs-keyword">const</span> getWxSystemInfo = <span class="hljs-function">() =></span> &#123;
    <span class="hljs-keyword">return</span> <span class="hljs-keyword">new</span> <span class="hljs-built_in">Promise</span>(<span class="hljs-function"><span class="hljs-params">resolve</span> =></span> &#123;
        wxFn().getSystemInfo(&#123;
            <span class="hljs-attr">success</span>: <span class="hljs-function"><span class="hljs-params">res</span> =></span> &#123;
                resolve(res);
            &#125;
        &#125;)
    &#125;)
&#125;


<span class="hljs-comment">/**
* 下面的内容在一个函数体内，我单独复制出来的
**/</span>
<span class="hljs-keyword">const</span> wxInfo: any = <span class="hljs-keyword">await</span> getWxSystemInfo();
        
<span class="hljs-comment">// 首页banner</span>
<span class="hljs-built_in">this</span>.homeBannerAd = wxFn().createBannerAd(&#123;
    <span class="hljs-attr">adUnitId</span>: <span class="hljs-string">'adUnitId'</span>,
    <span class="hljs-attr">adIntervals</span>: <span class="hljs-number">30</span>,
    <span class="hljs-attr">style</span>: &#123;
        <span class="hljs-attr">left</span>: <span class="hljs-number">20</span>,
        <span class="hljs-comment">// 初始化的时候 随便设</span>
        <span class="hljs-attr">top</span>: <span class="hljs-number">0</span>, 
        <span class="hljs-attr">width</span>: wxInfo.screenWidth - <span class="hljs-number">40</span>
    &#125;
&#125;);
<span class="hljs-built_in">this</span>.homeBannerAd?.onResize(<span class="hljs-function">(<span class="hljs-params">res</span>) =></span> &#123;
    <span class="hljs-built_in">this</span>.homeBannerAd.style.top = wxInfo.screenHeight - res.height - <span class="hljs-number">20</span>;
&#125;);
<span class="copy-code-btn">复制代码</span></code></pre>
<p>终于，写完了，，</p>
<p><img src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/6112a5ec2eec40caa8d3192779cba470~tplv-k3u1fbpfcp-watermark.image" alt="image.png" loading="lazy" referrerpolicy="no-referrer"></p>
<h2 data-id="heading-10">惊喜</h2>
<p>现在这个游戏第一期排名送现金红包活动，大家可以去体验玩玩，顺便赚钱钱 😄 😄 😄</p>
<p>以下是体验地址，欢迎大家体验</p>
<p><img src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d5487ebfa17d455fb961ffd0d7ac8bec~tplv-k3u1fbpfcp-watermark.image" alt="gh_7189d0e0ae6d_258.jpg" loading="lazy" referrerpolicy="no-referrer"></p>
<p>如果大家有什么问题，或者不清楚的欢迎留言讨论！！！</p>
<p>最后感谢 UI 大佬提供的资源素材</p>
<p>他的虎课网：<a href="https://huke88.com/person/opus/126352.html" target="_blank" rel="nofollow noopener noreferrer">huke88.com/person/opus…</a></p>
<p>他的站酷：<a href="https://zhujiu.zcool.com.cn/" target="_blank" rel="nofollow noopener noreferrer">zhujiu.zcool.com.cn/</a></p></div>  
</div>
            