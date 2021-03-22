
---
title: 'uni-app跨端开发H5、小程序、IOS、Android（二）：开发工具HBuilderX使用技巧'
categories: 
    - 编程
    - 掘金 - 分类
author: 掘金 - 分类
comments: false
date: Sun, 21 Mar 2021 22:32:42 GMT
thumbnail: 'https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064624c90ebe4f14adbde92d835218e3~tplv-k3u1fbpfcp-watermark.image'
---

<div>   
<div class="markdown-body"><style>.markdown-body&#123;word-break:break-word;line-height:1.75;font-weight:400;font-size:15px;overflow-x:hidden;color:#333&#125;.markdown-body h1,.markdown-body h2,.markdown-body h3,.markdown-body h4,.markdown-body h5,.markdown-body h6&#123;line-height:1.5;margin-top:35px;margin-bottom:10px;padding-bottom:5px&#125;.markdown-body h1&#123;font-size:30px;margin-bottom:5px&#125;.markdown-body h2&#123;padding-bottom:12px;font-size:24px;border-bottom:1px solid #ececec&#125;.markdown-body h3&#123;font-size:18px;padding-bottom:0&#125;.markdown-body h4&#123;font-size:16px&#125;.markdown-body h5&#123;font-size:15px&#125;.markdown-body h6&#123;margin-top:5px&#125;.markdown-body p&#123;line-height:inherit;margin-top:22px;margin-bottom:22px&#125;.markdown-body img&#123;max-width:100%&#125;.markdown-body hr&#123;border:none;border-top:1px solid #ddd;margin-top:32px;margin-bottom:32px&#125;.markdown-body code&#123;word-break:break-word;border-radius:2px;overflow-x:auto;background-color:#fff5f5;color:#ff502c;font-size:.87em;padding:.065em .4em&#125;.markdown-body code,.markdown-body pre&#123;font-family:Menlo,Monaco,Consolas,Courier New,monospace&#125;.markdown-body pre&#123;overflow:auto;position:relative;line-height:1.75&#125;.markdown-body pre>code&#123;font-size:12px;padding:15px 12px;margin:0;word-break:normal;display:block;overflow-x:auto;color:#333;background:#f8f8f8&#125;.markdown-body a&#123;text-decoration:none;color:#0269c8;border-bottom:1px solid #d1e9ff&#125;.markdown-body a:active,.markdown-body a:hover&#123;color:#275b8c&#125;.markdown-body table&#123;display:inline-block!important;font-size:12px;width:auto;max-width:100%;overflow:auto;border:1px solid #f6f6f6&#125;.markdown-body thead&#123;background:#f6f6f6;color:#000;text-align:left&#125;.markdown-body tr:nth-child(2n)&#123;background-color:#fcfcfc&#125;.markdown-body td,.markdown-body th&#123;padding:12px 7px;line-height:24px&#125;.markdown-body td&#123;min-width:120px&#125;.markdown-body blockquote&#123;color:#666;padding:1px 23px;margin:22px 0;border-left:4px solid #cbcbcb;background-color:#f8f8f8&#125;.markdown-body blockquote:after&#123;display:block;content:""&#125;.markdown-body blockquote>p&#123;margin:10px 0&#125;.markdown-body ol,.markdown-body ul&#123;padding-left:28px&#125;.markdown-body ol li,.markdown-body ul li&#123;margin-bottom:0;list-style:inherit&#125;.markdown-body ol li .task-list-item,.markdown-body ul li .task-list-item&#123;list-style:none&#125;.markdown-body ol li .task-list-item ol,.markdown-body ol li .task-list-item ul,.markdown-body ul li .task-list-item ol,.markdown-body ul li .task-list-item ul&#123;margin-top:0&#125;.markdown-body ol ol,.markdown-body ol ul,.markdown-body ul ol,.markdown-body ul ul&#123;margin-top:3px&#125;.markdown-body ol li&#123;padding-left:6px&#125;.markdown-body .contains-task-list&#123;padding-left:0&#125;.markdown-body .task-list-item&#123;list-style:none&#125;@media (max-width:720px)&#123;.markdown-body h1&#123;font-size:24px&#125;.markdown-body h2&#123;font-size:20px&#125;.markdown-body h3&#123;font-size:18px&#125;&#125;</style><p>​大家好，我是黑马腾云。</p>
<p><strong>这是一个原创系列连载文章，基于企业真实项目案例分享经验，带你快速入门uni-app开发！欢迎点击头像关注，避免迷路！</strong></p>
<p>​前几天，不少读者私信咨询前文中项目案例的种种实现细节，本文先揭晓使用的开发工具。</p>
<p>​特别说明：系列文章定位是帮助初学者从入门到实战，适合零基础或基础较差uni-apper。为了节约时间，高手勿进，可关注后续的实战部分。</p>
<h3 data-id="heading-0">一、项目演示</h3>
<p>​前文提到的项目是真实上线的商业项目，如果还没体验的可以找前一篇文章的入口进入体验。</p>
<p>贴心的小编也为你录好了屏，方便各位看官儿查看。</p>
<h4 data-id="heading-1">1、商城项目APP</h4>
<h4 data-id="heading-2">2、外卖项目小程序</h4>
<p>ps：不支持视频上传，那就先上传了。</p>
<p>​以上项目都包含APP（IOS、Android）、小程序和H5。</p>
<p>​看到这个演示，相信大家脑海里一定有不同的实现方式。那么，你想到了哪些实现方式呢？</p>
<p>​我们考虑的实现方案有很多，对比分析后，最终选择uni-app多端开发（至于原因前文有提到）。</p>
<p>​采取不同的开放方案，对应的开发环境和工具也有所不同。既然选择了 uni-app 开发，工具自然是采用官方的HBuilderX。</p>
<p>​下边来看看它和其它前端开发工具的一些对比</p>
<h3 data-id="heading-3">二、前端工具对比选择</h3>
<h4 data-id="heading-4">1、VSCode</h4>
<p>​微软发布的免费跨平台编辑器，使用的人也是非常多。</p>
<p>​VSCode 全称 Visual Studio Code，现代化轻量级的代码编辑器，支持几乎所有主流的开发语言的语法高亮、智能代码补全、自定义热键、括号匹配、代码片段、代码对比 Diff、Git 等特性，支持插件扩展，并针对网页开发和云端应用开发做了优化。软件跨平台支持 Win、Mac 以及 Linux，运行流畅。</p>
<h4 data-id="heading-5">2、HBuilderX</h4>
<p>​HBuilderX（简称：HX）是轻量编辑器和强大IDE的完美结合体，是HBuilder的升级版。敏捷的性能，清爽的界面，强大的功能。</p>
<p>​国产编辑器，且拥有世界级语法分析引擎，与uni-app出自同一家公司，有很多本地化的天然支持优势。</p>
<p>​HBuilder最大的优势就是速度比较快，强大的代码提示和代码输入，大大增加了开发者的开发效率。</p>
<h4 data-id="heading-6">3、webStorm</h4>
<p>​对js支持非常好，用的人也非常多（虽然收费，但相信聪明的你一定有办法，懂得）。</p>
<h4 data-id="heading-7">4、Sublime Text</h4>
<p>​一款代码编辑器，拥有漂亮的用户页面和实用功能，以及多功能插件。功能很多，包括多选择和多窗口和python api等功能。</p>
<h4 data-id="heading-8">5、Bracket</h4>
<p>​免费、开源且跨平台的 HTML/CSS/JavaScript 前端WEB集成开发环境IDE。由 Adobe 创建和维护，根据 MIT 许可证发布，支持 Windows、Linux 以及 OS X 平台。</p>
<p>​当然除了这些，还有一些其它的工具（DreamWeaver等等）也非常优秀。工具本质都是为开发服务的，因此选择适合的即可。</p>
<p>​接下来演示如何利用HBuilderX来创建一个uni-app项目：</p>
<h3 data-id="heading-9">三、HBuilderX创建项目</h3>
<h4 data-id="heading-10">1、下载安装</h4>
<p>​直接去官网下载安装即可，截至写文时最新版本为：3.0.7，本系列开发也是采用此版本。</p>
<blockquote>
<p>注意：官方版本更新比较快，如果你的版本不一致，可能软件界面和功能有些区别。</p>
<p>此系列文章我的开发环境为windows，如果你用的mac环境，快捷键和界面也有一定区别。</p>
</blockquote>
<p>​安装过程就不再赘述，按提示一路点击下一步即可。</p>
<p>​如果网速较慢或不方便下载，也可以私信我发你。</p>
<h4 data-id="heading-11">2、创建项目</h4>
<p>HBuilderX可以创建多种类型的项目，此处以创建基于HTML的Web项目为例，演示项目创建过程。</p>
<ul>
<li>新建项目</li>
</ul>
<p><img alt="n1.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/064624c90ebe4f14adbde92d835218e3~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>通过菜单栏：文件-新建-项目，或者直接主界面点击“新建项目”都会弹出如下：“新建项目”界面</p>
<p><img alt="n2.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fdc9471a4afe4a31b1422769513ef4d2~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>如上选择“普通项目”，输入项目名称，选择存储位置，点击“创建”，就会成功创建项目。</p>
<ul>
<li>新建文件</li>
</ul>
<p>在创建的“test”项目上右键-新建-html文件，就可以为项目添加文件</p>
<p><img alt="n3.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/db02bc906e61447fbe373631c5ca91f0~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>输入文件名称：getstart.html</p>
<p><img alt="n4.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/07e3daaff2394f25a45232b9bcae592c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>文件创建成功后，预览文件</p>
<p><img alt="n5.jpg" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7215766b7251460ea77c2b270c17bd7c~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>在文件中输入内容并保存，点击右上角的“预览”按钮，就可以实时预览修改的内容。</p>
<p>创建项目和添加文件的过程，和其它编辑器或IDE并没有太大的区别。</p>
<h4 data-id="heading-12">3、软件界面</h4>
<p><img alt="n6.jpg" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71d82c68e7854e59b0d2809250e9839d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>主界面如上图，界面比较简洁，右下角还可以选择文件的编码。</p>
<h4 data-id="heading-13">4、打开、关闭项目</h4>
<ul>
<li>打开项目</li>
</ul>
<p>菜单：文件-打开目录，弹出框中选择对应项目所在的文件夹即可。</p>
<ul>
<li>关闭项目</li>
</ul>
<p>在项目上右键-移除项目或关闭项目。</p>
<p><img alt="n7.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b2f5828092d345189ef384deaee2187f~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>移除项目会从本地电脑删除。</p>
<p>关闭项目仅仅是不会展示在项目区，会展示在“已关闭项目”区，右击已关闭的项目，可以再次打开。</p>
<p>基于以上的Web项目，我们来演示一下HBuilderX的骚操作。</p>
<h3 data-id="heading-14">四、HBuilderX初体验</h3>
<p>以下操作，强烈建议对照着打开HBuilderX亲自操作一遍，才能达到事半功倍的效果。</p>
<h4 data-id="heading-15">1、强大的代码块</h4>
<p>使用代码块，可以减少重复代码工作量。</p>
<p>打开刚才的getstart.html文件，删除里边的内容，在英文状态输入h字符</p>
<p><img alt="n8.jpg" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/447bf5fe09984516b2fbc0d09d856a76~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>根据提示，alt+前边的数字可以快速插入对应的代码块。</p>
<p>alt+9，快速输入html代码块。</p>
<p><img alt="n9.jpg" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/1d6a9ec636f641d49ef1e0fcb9de400e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>怎么样？只需要一个键就能把html的基础结构写好，你还在一个个字符挨着敲吗？</p>
<h4 data-id="heading-16">2、强大的快捷键</h4>
<p>熟练使用快捷键，码字就像飞一般的感觉。不信你看！！！</p>
<p><img alt="n10.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/fe8b81eb8e3f4b869a8213aa38b34488~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>一定要跟着敲噢！步骤如下：</p>
<ul>
<li>
<p>接着上边的例子，新建html文件后，当前光标处于title标签内，此时我们给HTML设置title:hellohbuilder,完成后使用Ctrl+回车在当前的下一行插入空行,并将光标移动到下一行。</p>
</li>
<li>
<p>使用sc代码块生成一个script块来编写js代码(输入sc,回车)</p>
</li>
<li>
<p>使用funn代码块编写一个JS方法helloworld(输入funn,回车)。此时生成的方法的方法名是选中状态,我们只需要直接输入新的方法名helloworld即可，敲击回车光标会直接跳转至函数体中。</p>
</li>
<li>
<p>按向下、向下,Ctrl+回车,输入style回车,生成css代码区域。定义一个Css类classA：输入.classA&#123; 然后回车，输入font 选择对应的字体后回车即可。</p>
</li>
<li>
<p>向下键跳转至下一个编辑区域</p>
</li>
<li>
<p>输入<div 回车，输入i回车，输入d1，空格，c回车，回车。</p>
</li>
<li>
<p>ctrl+回车，添加空行</p>
</li>
<li>
<p>divc回车，回车，输入hellworld。</p>
</li>
</ul>
<p>全程不用鼠标，感觉就像在linux上敲命令。</p>
<p>当然，初次使用肯定记不住这么多，多敲几遍就形成条件反射了，实在记不住，可以查看对应的菜单。菜单上都有快捷键的提示。</p>
<h4 data-id="heading-17">3、强大的js解析引擎提示</h4>
<p>js提示html的id</p>
<p><img alt="n11.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/efe45e8b6b594273a1f15d8b1cdd9b72~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>js提示html的tagname</p>
<p><img alt="n12.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b270d1c520a74bef9afa4144ad23b71d~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>js提示css类名</p>
<p><img alt="n13.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3bbf563ee5934d399387696429773886~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-18">4、跳转到class、id、js方法定义处</h4>
<p>只需要“alt+左键点击”引用的方法名、ID、CSS类、文件(链接、图片),均可跳转到引用的地方,跨文件的引用也可以。</p>
<p><img alt="n14.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9ef81feffd2c4579a0221e19b20a737b~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>演示完毕，接下来再看看具体的一些技巧</p>
<h3 data-id="heading-19">五、HBuilderX高效率技巧</h3>
<h4 data-id="heading-20">1、文件保存</h4>
<p>HX默认30秒保存一次文件。</p>
<p>不管是关闭hx，还是断电、崩溃，临时文件始终会自动保存，不用担心丢失。</p>
<p>默认的自动保存不会触发编译，只有手动保存（ctrl+s）时才会。</p>
<p>前端预编译型语言越来越多，每次保存都触发编译比较消耗资源，有了hx，可以专注写代码而不需要隔一会按一下ctrl+s，需要编译时再保存。</p>
<h4 data-id="heading-21">2、语法提示</h4>
<p>世界级语法分析引擎一直是HBuilder系列产品最大特点。</p>
<p>前端框架众多，框架的语法提示需要加载单独的语法提示库，框架语法提示库是在页面的右下角选择。</p>
<p><img alt="n17.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/497e5e447e364d5eb4f72ce0fa0abad9~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>框架语法库是挂在项目下的，一个项目加载了一个框架语法库后，这个项目下所有js文件或HTML文件都会在代码助手提示这个框架的语法。</p>
<p>但如果一个文件是单独从硬盘打开，没有整项目拖入hx，那么此时无法加载框架语法库。</p>
<h4 data-id="heading-22">3、代码助手</h4>
<p>hx的代码助手，可以按alt+数字选择直接选择某个项目，类似中文输入法数字选词</p>
<p><img alt="n18.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/847df438c94f43d0aee7e8515d2de744~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-23">4、语法帮助</h4>
<p>标放到某api处，按下F1，就可跳转到这个api的官方手册。目前支持vue、uni-app、5+等api</p>
<p><img alt="n15.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b482c449a3a34742b3d512d299622245~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-24">5、多光标批处理</h4>
<p>hx支持多光标，按 ctrl+鼠标左键 就可增加一个光标，ctrl+鼠标右键 可取消一个光标或选区。</p>
<p><img alt="n16.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/19e9c018c29145a2998994d9bead3819~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>还可以选择相同词，ctrl+e 可选中相同的词做批处理。</p>
<p><img alt="n19.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/d0d9943d73da4bbf85c2aaa80b805901~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-25">6、列选择</h4>
<p>hx的列选择，是alt+鼠标拖选</p>
<p><img alt="n20.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2cf6e49d98f14a449d585391498ec899~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-26">7、选择编码</h4>
<p>当打开一个不认识的文档时，即hx的无法高亮着色，可以在右下角选择使用其他编辑器打开。</p>
<p>当打开一个文件编码错乱，产生乱码时，也可以在右下角选择编码重新打开。</p>
<p><img alt="n21.gif" class="lazyload" src="https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/87b3c8dfca8c41978192be673030489e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-27">8、转到定义</h4>
<p>快捷键是Alt+d，鼠标操作是alt+左键单击</p>
<p><img alt="n22.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/3c64c18658e7475392f4af9c28ab4262~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>HBuilderX还有一个特色是转到定义到分栏，ctrl+alt+左键，可以把一个定义处的代码打开在另一侧，方便共同查看</p>
<p><img alt="n23.gif" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/2ee7cf2078904b1c9226fe694c0c7445~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>支持切换【Ctrl+鼠标左键】或【Alt+鼠标左键】进行转到定义 （菜单【选择】，最后一个菜单）</p>
<p><img alt="n24.png" class="lazyload" src="https://p1-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/aaccffddf66f460494b8e1c1f8b86ec5~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>当然，快捷键可以进行个性化设置，可以修改，因此自己根据个人习惯设置即可，不一定和我的一样。</p>
<h4 data-id="heading-28">9、返回上一次光标位置</h4>
<p>在HBuilderX中，Alt+Left或点击工具栏上的<, 即可回到上一个光标位置。</p>
<h4 data-id="heading-29">10、快速打开文件</h4>
<p>在顶部工具栏直接搜索工程下的文件名并打开，或者使用快捷键ctrl+p。</p>
<p><img alt="n25.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/71070c76335849c0a84f280c3c3e1e6e~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>比较常用的文件，可以在工具栏里添加到收藏夹。</p>
<p><img alt="n26.gif" class="lazyload" src="https://p9-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/b1f4049091b048cc940fce1f357c223a~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<h4 data-id="heading-30">11、目录内搜索</h4>
<p>项目管理器点右键，选：查找字符串(当前目录)，可在该目录下所有文件中搜索字符串</p>
<p><img alt="n27.gif" class="lazyload" src="https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/9758875e3f33449c8a7a28602e4d7980~tplv-k3u1fbpfcp-watermark.image" data-width="800" data-height="600" referrerpolicy="no-referrer"></p>
<p>以上快捷功能熟悉后，日常开发就可以大大提高效率。</p>
<p>还有一些功能：</p>
<p>​比如语法校验插件、svn/git项目管理插件、预编译器（less/sass）等，篇幅所限就不展开了，以后有时间再继续写。</p>
<p>另外如果有兴趣，以后高级篇讲讲HbuilderX插件的开发，随心所欲定制扩展你的编辑器功能。</p>
<p>下一篇文章，我们讨论下uni-app的MVVM框架思想。</p>
<p>讨论时间：</p>
<p>​你认为哪个开发工具最牛X？</p>
<p>​600万开发者的选择，HBuilderX凭啥？</p>
<p>​咱们留言区见！</p>
<p><strong>作者介绍：</strong></p>
<p><strong>黑马腾云，码农、创业者、终身学习者！</strong></p>
<p><strong>乐于分享技术、创业、人生思考。关注我，一起为人生喝彩！</strong></p></div> <div class="image-viewer-box" data-v-78c9b824><!----></div>  
</div>
            