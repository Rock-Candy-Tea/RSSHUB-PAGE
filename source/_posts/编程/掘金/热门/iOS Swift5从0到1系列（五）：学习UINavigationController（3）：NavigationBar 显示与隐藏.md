
---
title: 'iOS Swift5从0到1系列（五）：学习UINavigationController（3）：NavigationBar 显示与隐藏'
categories: 
 - 编程
 - 掘金
 - 热门
headimg: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1213f23e34254b06a99c20bc1e721e1a~tplv-k3u1fbpfcp-zoom-1.image'
author: 掘金
comments: false
date: Wed, 10 Mar 2021 08:12:01 GMT
thumbnail: 'https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1213f23e34254b06a99c20bc1e721e1a~tplv-k3u1fbpfcp-zoom-1.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><blockquote>
<h2 data-id="heading-0">UINavigationController 小系列 <a href="https://github.com/qingye/ios-swift5-demo" target="_blank" rel="nofollow noopener noreferrer">【源码 Github 传送门】</a>：</h2>
<p><a href="https://juejin.cn/post/6937492008160198663" target="_blank">学习UINavigationController（1）：基础</a></p>
<p><a href="https://juejin.cn/post/6937878071370334215/" target="_blank">学习UINavigationController（2）：底部TabBar的显示与隐藏</a></p>
<p><a href="https://juejin.cn/post/6938056448056229896/" target="_blank">学习UINavigationController（3）：NavigationBar 显示与隐藏</a></p>
<p><a href="https://juejin.cn/post/6938429340275179557/" target="_blank">学习UINavigationController（4）：自定义导航栏+完美过渡+统一返回按钮</a></p>
</blockquote>
<h2 data-id="heading-1">一、前言</h2>
<p>上篇，我们分析了如何正确的通过继承 UINavigationBar 并重写 pushViewController 来正确的设置 tabBar 的显示与隐藏，本篇，将如题所述那样，控制顶部导航栏的显示与隐藏。</p>
<p>导航栏的显示与隐藏，一般用于的场景：</p>
<ul>
<li>类似天猫、京东APP首页，默认隐藏导航栏，滚动时，通过过渡动画来显示自定义导航栏；</li>
<li>Hybrid时，即WKWebView全屏展示H5时，隐藏原生导航栏，由H5来自主导航栏；</li>
<li>查看图片 / 视频时，进入与退出全屏时控制导航栏的显示与隐藏；</li>
<li>..... 等等，还有很多 case，就不一一列举；</li>
</ul>
<p>列举以上的场景，并不是让大家去做产品经理（虽然，有本书叫作：人人都是产品经理；无论是开发还是测试，都应该站在用户的角度去思考，如何更好更合理的设计出一款APP），而是我们在某些场景下，页面的切换（push & pop）需要保持页面导航栏前后一致性。</p>
<h2 data-id="heading-2">二、页面导航栏前后一致性</h2>
<p>本小节会深入分析 UINavigationController 的原理，新人需要好好学习，因为控制不当，容易造成前后不一致（我在上篇前言中，贴了一张 gif 图，首页的导航栏背景色开始是白色，push 到下一个页面，导航栏背景是蓝色，然后 pop 回来，首页的导航栏还是蓝色，并没有恢复为白色）；同样，多年开发的老同学，也需要『温顾而知新』。</p>
<ul>
<li>
<p>UINavigationController 在之前就分析过：</p>
<ul>
<li>栈式管理 ViewController；</li>
<li>栈式管理 navigationItem；</li>
<li>push & pop 时，UINavigationController会 sync，即同步；</li>
</ul>
</li>
<li>
<p>除此，还有几点我没有提到，而是特意保留到了本章来讲：</p>
<ol>
<li>UINavigationController 具有传递性（其实就是 sync）；</li>
<li>每个 UINavigationController 是单独管理自己的栈的；</li>
</ol>
</li>
<li>
<p>针对上面两点，我来一一解释：</p>
<ol>
<li>所谓传递性，其实是 navigationBar （类型：UINavigationBar，依附于当前的 navigationController 实例），它是一个针对当前 UINavigationController 实例的统一设定，所以一旦某处作了修改，将会适用于该 UINavigationController 栈中所有的 VC，但你可以通过 UINavigationItem 来为其定制左右按钮，至于修改背景色，额，只能自定义导航栏，除此无它法，<span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mtext>所以，千万不要随意去修改</mtext></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123;所以，千万不要随意去修改&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.68333em;vertical-align:0em;"></span><span class="mord" style="color:red;"><span class="mord cjk_fallback" style="color:red;">所</span><span class="mord cjk_fallback" style="color:red;">以</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">千</span><span class="mord cjk_fallback" style="color:red;">万</span><span class="mord cjk_fallback" style="color:red;">不</span><span class="mord cjk_fallback" style="color:red;">要</span><span class="mord cjk_fallback" style="color:red;">随</span><span class="mord cjk_fallback" style="color:red;">意</span><span class="mord cjk_fallback" style="color:red;">去</span><span class="mord cjk_fallback" style="color:red;">修</span><span class="mord cjk_fallback" style="color:red;">改</span></span></span></span></span></span> <span class="math math-inline"><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mstyle mathcolor="red"><mrow><mi>n</mi><mi>a</mi><mi>v</mi><mi>i</mi><mi>g</mi><mi>a</mi><mi>t</mi><mi>i</mi><mi>o</mi><mi>n</mi><mi>B</mi><mi>a</mi><mi>r</mi><mtext>的属性，极度危险！！！</mtext></mrow></mstyle></mrow><annotation encoding="application/x-tex">\color&#123;red&#125;&#123; navigationBar 的属性，极度危险！！！&#125;</annotation></semantics></math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut" style="height:0.8777699999999999em;vertical-align:-0.19444em;"></span><span class="mord" style="color:red;"><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="color:red;">a</span><span class="mord mathnormal" style="margin-right:0.03588em;color:red;">v</span><span class="mord mathnormal" style="color:red;">i</span><span class="mord mathnormal" style="margin-right:0.03588em;color:red;">g</span><span class="mord mathnormal" style="color:red;">a</span><span class="mord mathnormal" style="color:red;">t</span><span class="mord mathnormal" style="color:red;">i</span><span class="mord mathnormal" style="color:red;">o</span><span class="mord mathnormal" style="color:red;">n</span><span class="mord mathnormal" style="margin-right:0.05017em;color:red;">B</span><span class="mord mathnormal" style="color:red;">a</span><span class="mord mathnormal" style="margin-right:0.02778em;color:red;">r</span><span class="mord cjk_fallback" style="color:red;">的</span><span class="mord cjk_fallback" style="color:red;">属</span><span class="mord cjk_fallback" style="color:red;">性</span><span class="mord cjk_fallback" style="color:red;">，</span><span class="mord cjk_fallback" style="color:red;">极</span><span class="mord cjk_fallback" style="color:red;">度</span><span class="mord cjk_fallback" style="color:red;">危</span><span class="mord cjk_fallback" style="color:red;">险</span><span class="mord cjk_fallback" style="color:red;">！</span><span class="mord cjk_fallback" style="color:red;">！</span><span class="mord cjk_fallback" style="color:red;">！</span></span></span></span></span></span>；</li>
<li>我们在 UITabBarController 中，嵌套了 N 个 UINavigationController(ViewController)，因此，这 N 个 UINavigationController 对象的 VC 栈是独立的管理的，不会相互使用；</li>
</ol>
</li>
</ul>
<p>另外，针对有多个 UINavigationController (即会生成多个对应的 navigationBar)，可以使用 UINavigationBar 的 UIAppearance 进行全局统一设置，因为 appearance 是单例。</p>
<h2 data-id="heading-3">三、统一处理（了解就行）</h2>
<p>UINavigationBar 中有个属性 isHidden，为 true 就隐藏，false 就显示，但是上篇我也说了，操作 navigationBar 是极度危险的，会对当前栈中所有的 UIViewController 都适用，所以，如果我们 previousVC 是隐藏，push 后下一个是显示，再 pop 时，previousVC 的导航栏就显示了，因此，我们需要统一处理，虽然这种方式能够达到显示与隐藏的效果，但是用户体验非常不好。</p>
<h3 data-id="heading-4">3.1、进入与退出时设置 isHidden</h3>
<p>先上图如下：</p>
<p><img alt="show-hide-navigation-bar-bad!.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1213f23e34254b06a99c20bc1e721e1a~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>上图我们可以看到两处非常生硬的导航栏处理：</p>
<ul>
<li>push 下一页时，还没完全进入，下一面的导航栏就已经显示了；</li>
<li>pop 回上一页时，刚开始动画，导航栏就隐藏了；</li>
</ul>
<p>先给出这种统一处理的代码：</p>
<ul>
<li>修改 BaseViewController：</li>
</ul>
<p><img alt="base-vc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b4bf37bd73004b99aba2ec9c0654f25e~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>修改一级页面 HomeViewController：</li>
</ul>
<p><img alt="home-vc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d97f9fc63b0b4d6590b4786e4516cc1d~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>修改二级页面 ViewController：</li>
</ul>
<p><img alt="vc.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/89bc38acc6f24dbbac9ef37b353eb0cc~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<ul>
<li>修改 CustomNavigationController：</li>
</ul>
<p><img alt="custom-nc-pop.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/506aaa9901c04be5a61aeba930aee6ad~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h3 data-id="heading-5">3.2、退出后再处理导航栏</h3>
<p>同样先上图如下：</p>
<p><img alt="show-hide-navigation-bar-less-bad!.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7cb89b3a71a04bf289d10b2fe628881b~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>虽然用户体验还是非常的差，但稍微好一点点在于：导航栏在 pop 完全完成后才消失。当然，也不能说这种方式就比上一种要好，各有侧重点吧。</p>
<p>基于上面 3.1 的代码，我们只需要稍微修改一下 CustomNavigationController，实现一个 CustomNavigationControllerDelegate 即可：</p>
<p><img alt="custom-nc-delegate.png" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/17dd5bb2036c46abbbbe3c3cfdebd8fd~tplv-k3u1fbpfcp-zoom-1.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>那有没有比这两种方式更好的处理呢？当然是有的，下一篇，我将分享，如何通过自定义导航栏完成以下事：</p>
<ol>
<li>ViewController 控制各自的导航栏；</li>
<li>push & pop 相互不会影响；</li>
<li>基于以上两点，即便颜色、背景不一样，都能较为完美的过渡；</li>
</ol>
<p>敬请期待，谢谢！</p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            